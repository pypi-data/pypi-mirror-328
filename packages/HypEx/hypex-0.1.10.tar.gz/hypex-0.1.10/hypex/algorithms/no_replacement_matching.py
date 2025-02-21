"""Here is the realization of Matching without replacement."""
from typing import Tuple

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment
from scipy.spatial import distance

from .faiss_matcher import conditional_covariance


class MatcherNoReplacement:
    """Matching groups with no replacement.

    Realized by optimizing the linear sum of distances between pairs of treatment and
    control samples.
    """

    def __init__(self, X: pd.DataFrame, a: pd.Series, weights: dict = None, approximate_match: bool = False):
        """Initialize matching.

        Args:
            X: features dataframe
            a: series of treatment value
            weights: weights for numeric columns in order to increase matching quality.
            approximate_match: use or not approximate matching
        """
        self.treatment = a
        self.X = X
        self.weights = weights
        self.approximate_match = approximate_match

    def match(self):
        """Function run matching with no replacement.

        Returns:
            Dataframe of matched indexes.
        """
        matches = {}
        cov = conditional_covariance(self.X[self.treatment == 1].values, self.X[self.treatment == 0].values)
        distance_matrix = self._get_distance_matrix(self.X[self.treatment == 1], self.X[self.treatment == 0], cov)
        source_array, neighbor_array_indices, distances = optimally_match_distance_matrix(distance_matrix)
        source_df = self.X[self.treatment == 1].iloc[np.array(source_array)]
        target_df = self.X[self.treatment == 0].iloc[np.array(neighbor_array_indices)]

        matches[1] = self.create_match_df(self.treatment, source_df, target_df, distances)
        matches[0] = self.create_match_df(self.treatment, target_df, source_df, distances)

        match_df = pd.concat(matches, sort=True)
        return match_df

    def create_match_df(
            self, base_series: pd.Series, source_df: pd.DataFrame, target_df: pd.DataFrame, distances: list
    ) -> pd.DataFrame:
        """Function creates matching dataframe.

        Args:
            base_series: series of treatment value.
            source_df: dataframe of sources indexes.
            target_df: dataframe of target indexes.
            distances: matrix of calculated distances.

        Returns:
            Matched dataframe of indexes.
        """
        match_sub_df = pd.DataFrame(
            index=base_series.index,
            columns=[
                "matches",
                "distances",
            ],
            data=base_series.apply(lambda x: pd.Series([[], []])).values,
            dtype="object",
        )

        # matching from source to target: read distances
        match_sub_df.loc[source_df.index] = pd.DataFrame(
            data=dict(
                matches=[[tidx] for tidx in target_df.index],
                distances=distances,
            ),
            index=source_df.index,
        )

        # matching from target to target: fill with zeros
        match_sub_df.loc[target_df.index] = pd.DataFrame(
            data=dict(
                matches=[[tidx] for tidx in target_df.index],
                distances=[[0]] * len(distances),
            ),
            index=target_df.index,
        )
        return match_sub_df

    def _get_metric_dict(self, cov: np.ndarray) -> dict:
        """Function calculates correct feature space and generate metrics dist for cdist calculation.

        Args:
            cov: Matrix of covariations.

        Returns:
            Metric dictionary
        """
        metric_dict = dict(metric="mahalanobis")
        mahalanobis_transform = np.linalg.inv(cov)
        if self.weights is not None:
            features = self.X.columns
            w_list = np.array([self.weights[col] if col in self.weights.keys() else 1 for col in features])
            w_matrix = np.sqrt(np.diag(w_list / w_list.sum()))
            mahalanobis_transform = np.dot(w_matrix, mahalanobis_transform)

        metric_dict["VI"] = mahalanobis_transform
        return metric_dict

    def _get_distance_matrix(self, source_df: pd.DataFrame, target_df: pd.DataFrame, cov: np.ndarray) -> np.ndarray:
        """Create distance matrix for no replacement match.

        Combines metric and source/target data into a
        precalculated distance matrix which can be passed to
        scipy.optimize.linear_sum_assignment.

        Args:
            source_df: source feature dataframe.
            target_df: target feature dataframe.
            cov: matrix of covariations.

        Returns:
            Matrix of distances.
        """
        cdist_args = dict(XA=_ensure_array_columnlike(source_df.values), XB=_ensure_array_columnlike(target_df.values))
        cdist_args.update(self._get_metric_dict(cov))

        if self.approximate_match:
            if len(cdist_args['XB']) < len(cdist_args['XA']):
                covariance_matrix = np.cov(cdist_args['XB'].T)
            else:
                covariance_matrix = np.cov(cdist_args['XA'].T)
            covariance_matrix_reg = covariance_matrix + np.eye(covariance_matrix.shape[0]) * 1e-8

            distance_matrix = np.zeros((cdist_args['XA'].shape[0], cdist_args['XB'].shape[0]))
            for i, x in enumerate(cdist_args['XA']):
                distance_matrix[i] = _m_distance(cdist_args['XB'], x, np.linalg.inv(covariance_matrix_reg))
        else:
            distance_matrix = distance.cdist(**cdist_args)
        return distance_matrix


def optimally_match_distance_matrix(distance_matrix: np.ndarray) -> Tuple[np.ndarray, np.ndarray, list]:
    """Functions finds optimal neighbor with no replacement.

    Args:
        distance_matrix: matrix of distances.

    Returns:
        - indexes of source dataframe.
        - optimal neighbors array for source array.
        - distances of optimal neighbors.
    """
    source_array, neighbor_array_indices = linear_sum_assignment(distance_matrix)
    distances = [[distance_matrix[s_idx, t_idx]] for s_idx, t_idx in zip(source_array, neighbor_array_indices)]
    return source_array, neighbor_array_indices, distances


def _ensure_array_columnlike(target_array: np.ndarray) -> np.ndarray:
    """Function checks if array is column like and reshape it in order it is not.

    Args:
        target_array: checked array.

    Returns:
        column like target array.
    """
    if len(target_array.shape) < 2 or target_array.shape[1] == 1:
        target_array = target_array.reshape(-1, 1)
    return target_array


def _m_distance(X: np.ndarray, Y: np.ndarray, inv_covariance: np.ndarray) -> np.ndarray:
    """Calculation of the approximate Mahalanobis distance.
    Args:
        X: source feature dataframe.
        Y: iterable rows for calculating distance between X and Y.
        inv_covariance: inverted matrix of covariations.

    Returns:
        Mahalanobis distance between X and Y."""

    diff = X - Y
    return np.sqrt(np.sum(np.dot(diff, inv_covariance) * diff, axis=1))
