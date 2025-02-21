"""Base Matcher class."""

import logging
import pickle
import warnings
import copy
from typing import Union, Iterable, List

import numpy as np
import pandas as pd

try:
    from tqdm.auto import tqdm
except:
    try:
        from tqdm import tqdm
    except:
        raise Exception("Can't import tqdm")

from .algorithms.faiss_matcher import FaissMatcher
from .algorithms.no_replacement_matching import MatcherNoReplacement
from .selectors.feature_selector import FeatureSelector
from .selectors.spearman_filter import SpearmanFilter
from .selectors.outliers_filter import OutliersFilter
from .selectors.base_filtration import const_filtration, nan_filtration
from .selectors.selector_primal_methods import (
    pd_lgbm_feature_selector,
    pd_catboost_feature_selector,
    pd_ridgecv_feature_selector,
)
from .utils.validators import emissions
from .utils.validators import random_feature
from .utils.validators import permutation_test
from .utils.validators import subset_refuter
from .utils.validators import test_significance

REPORT_FEAT_SELECT_DIR = "report_feature_selector"
REPORT_PROP_MATCHER_DIR = "report_matcher"
NAME_REPORT = "lama_interactive_report.html"
N_THREADS = 1
N_FOLDS = 4
RANDOM_STATE = 123
TEST_SIZE = 0.2
TIMEOUT = 600
VERBOSE = 2
DEFAULT_FEATURE_SELECT_ALGO = "catboost"
FEATURE_SELECT_ALGO = {
    "lgbm": pd_lgbm_feature_selector,
    "catboost": pd_catboost_feature_selector,
    "ridgecv": pd_ridgecv_feature_selector,
}
PROP_SCORES_COLUMN = "prop_scores"
GENERATE_REPORT = True
SAME_TARGET_THRESHOLD = 0.7
OUT_INTER_COEFF = 1.5
OUT_MODE_PERCENT = True
OUT_MIN_PERCENT = 0.02
OUT_MAX_PERCENT = 0.98
RARE_CAT_SCENARIO_LIST = ["raise", "drop", "genetic"]

logger = logging.getLogger("hypex")
console_out = logging.StreamHandler()
logging.basicConfig(
    handlers=(console_out,),
    format="[%(asctime)s | %(name)s | %(levelname)s]: %(message)s",
    datefmt="%d.%m.%Y %H:%M:%S",
    level=logging.INFO,
)


class Matcher:
    """Class for compile full pipeline of Matching in Causal Inference task.

    Matcher steps:
        - Read, analyze data
        - Feature selection via LightAutoML
        - Converting a dataset with features to another space via Cholesky decomposition
          In the new space, the distance L2 becomes equivalent to the Mahalanobis distance.
          This allows us to use faiss to search for nearest objects, which can search only by L2 metric,
          but without violating the methodology of matching,
          for which it is important to count by the Mahalanobis distance
        - Finding the nearest neighbors for each unit (with duplicates) using faiss.
          For each of the control group, neighbors from the target group are matched and vice versa.
        - Calculation bias
        - Creating matched df (Wide df with pairs)
        - Calculation metrics: ATE, ATT, ATC, p-value,  and сonfidence intervals
        - Calculation quality: PS-test, KS test, SMD test
        - Returns metrics as dataframe, quality results as dict of df's and df_matched
        - After receiving the result, the result should be validated using :func:`~hypex.matcher.Matcher.validate_result`

    Example:
        Common usecase - base pipeline for matching

        >>> # Base info
        >>> data = create_test_data()
        >>> treatment = "treatment" # Column name with info about 'treatment' 0 or 1
        >>> target = "target" # Column name with target
        >>>
        >>> # Optional
        >>> info_col = ["user_id", 'address'] # Columns that will not participate in the match and are informative.
        >>> group_col = "CatCol" # Column name for strict comparison (for a categorical feature)
        >>>
        >>> # Matching
        >>> model = Matcher(data, outcome=target, treatment=treatment, info_col=info_col, group_col=group_col)
        >>> features = model.feature_select() # Feature selection
        >>> results, quality, df_matched = model.estimate(features=['some_features', 'some_features_2']) # Performs matching
        >>>
        >>> model.validate_result()
    """

    def __init__(
            self,
            input_data: pd.DataFrame,
            treatment: str,
            outcome: Union[str, list] = None,
            outcome_type: str = "numeric",
            group_col: Union[str, List[str]] = None,
            info_col: list = None,
            weights: dict = None,
            base_filtration: bool = False,
            rare_categories_scenario: str = "raise",
            generate_report: bool = GENERATE_REPORT,
            report_feat_select_dir: str = REPORT_FEAT_SELECT_DIR,
            timeout: int = TIMEOUT,
            n_threads: int = N_THREADS,
            n_folds: int = N_FOLDS,
            verbose: bool = VERBOSE,
            use_algos: list = None,
            same_target_threshold: float = SAME_TARGET_THRESHOLD,
            interquartile_coeff: float = OUT_INTER_COEFF,
            drop_outliers_by_percentile: bool = OUT_MODE_PERCENT,
            min_percentile: float = OUT_MIN_PERCENT,
            max_percentile: float = OUT_MAX_PERCENT,
            n_neighbors: int = 1,
            silent: bool = True,
            pbar: bool = True,
            max_categories: int = 100,
            fill_gaps: bool = False,
            algo: str = 'fast'
    ):
        """Initialize the Matcher object.

        Args:
            input_data:
                Input dataframe
            outcome:
                Target column
            treatment:
                Column determine control and test groups
            outcome_type:
                Values type of target column. Defaults to "numeric"
            group_col:
                Column for grouping. Defaults to None.
            info_col:
                Columns with id, date or metadata, not taking part in calculations. Defaults to None
            weights:
                weights for numeric columns in order to increase matching quality by weighted feature.
                By default, is None (all features have the same weight equal to 1). Example: {'feature_1': 10}
            base_filtration:
                To use or not base filtration of features in order to remove all constant or almost all constant, bool.
                Default is False.
            rare_categories_scenario:
                /
            generate_report:
                Flag to create report. Defaults to True
            report_feat_select_dir:
                Folder for report files. Defaults to "report_feature_selector"
            timeout:
                Limit work time of code LAMA. Defaults to 600
            n_threads:
                Maximum number of threads. Defaults to 1
            n_folds:
                Number of folds for cross-validation. Defaults to 4
            verbose:
                Flag to show process stages. Defaults to 2
            use_algos:
                List of names of algorithms for feature selection. Defaults to catboost
            same_target_threshold:
                Threshold for correlation coefficient filter (Spearman). Default to 0.7
            interquartile_coeff:
                Percent for drop outliers. Default to 1.5
            drop_outliers_by_percentile:
                Flag to drop outliers by custom percentiles. Defaults to True
            min_percentile:
                Minimum percentile to drop outliers. Defaults to 0.02
            max_percentile:
                Maximum percentile to drop outliers. Defaults to 0.98
            n_neighbors:
                Number of neighbors to match (in fact you may see more then n matches as every match may have more then
                one neighbor with the same distance). Default value is 1.
            silent:
                Write logs in debug mode
            pbar:
                Display progress bar while get index
            max_categories:
                The maximum number of categories. Default to 100.
            fill_gaps:
                Determines whether to automatically fill NaN values in categorical columns used for grouping.
            algo:
                Detect algo for Matching. Bootstrap (high quality but less speed) or quick (less quality but more speed)
        ..warnings::
            Multitarget involves studying the impact on multiple targets.
            The algorithm is implemented as a repetition of the same matching on the same feature space and samples, but with
            different targets. To ensure the algorithm's correct operation, it's necessary to guarantee the independence of the
            targets from each other.
            The best solution would be to conduct several independent experiments, each with its own set of features for each
            target.
        """
        self.short_features_df = None
        self.detailed_features_df = None
        use_algos = DEFAULT_FEATURE_SELECT_ALGO if use_algos is None else use_algos
        self.feature_selection_method = FEATURE_SELECT_ALGO.get(use_algos, None)
        if self.feature_selection_method is None:
            raise Exception(
                f"Unknown input algorithm used on feature_selector: {use_algos}"
            )

        self.input_data = input_data.copy()

        # transform group_col to list
        if group_col is not None and isinstance(group_col, str):
            group_col = [group_col]
        elif group_col is not None and isinstance(group_col, list):
            group_col = group_col
        else:
            group_col = []

        # check group_col onto null-values
        null_contained_group_cols = self.input_data.loc[:, group_col].pipe(pd.isnull).any(axis=0)
        null_contained_group_cols = null_contained_group_cols[null_contained_group_cols].index
        if null_contained_group_cols.shape[0] != 0 and fill_gaps == False:
            raise ValueError(
                f"Next group columns contain NULLs: {null_contained_group_cols}. Process these columns or set 'fill_gaps = True'."
            )

        if fill_gaps == True:
            for column in group_col:
                self.input_data[column] = self.input_data[column].fillna(f'unknown_{column}')

        # join group_cols
        self.group_col = group_col if group_col == [] else ['|'.join(group_col)]
        if len(group_col) > 1:
            self.input_data[self.group_col[0]] = (
                self.input_data
                .loc[:, group_col]
                .apply(lambda x: '|'.join(x.values.tolist()), axis=1)
            )
            self.input_data.drop(columns=group_col, inplace=True)
        # self.group_col = None if group_col == [] else group_col
        del input_data

        if outcome is None:
            outcome = list()
        self.outcomes = outcome if type(outcome) == list else [outcome]
        self.treatment = treatment
        self.info_col = info_col
        self.outcome_type = outcome_type
        self.weights = weights
        self.generate_report = generate_report
        self.report_feat_select_dir = report_feat_select_dir
        self.timeout = timeout
        self.n_threads = n_threads
        self.n_folds = n_folds
        self.verbose = verbose
        self.use_algos = use_algos
        self.same_target_threshold = same_target_threshold
        self.interquartile_coeff = interquartile_coeff
        self.mode_percentile = drop_outliers_by_percentile
        self.min_percentile = min_percentile
        self.max_percentile = max_percentile
        self.base_filtration = base_filtration
        self.rare_categories_scenario = rare_categories_scenario
        self.features_importance = None
        self.matcher = None
        self.val_dict = None
        self.pval_dict = None
        self.new_treatment = None
        self.validate = None
        self.dropped_features = []
        self.n_neighbors = n_neighbors
        self.silent = silent
        self.pbar = pbar
        self.max_categories = max_categories
        self.algo = algo
        self._preprocessing_data()

    def _convert_categorical_to_dummy(self):
        """Converts categorical variables to dummy variables.

        Returns:
            Data with categorical variables converted to dummy variables.
        """
        info_col = self.info_col if self.info_col is not None else []

        columns_to_drop = info_col + self.group_col
        if columns_to_drop is not None:
            data = self.input_data.drop(columns=columns_to_drop)
        else:
            data = self.input_data

        col_cut = [x for x in data.select_dtypes(include=['category', 'object']).columns if
                   len(data[x].unique()) > self.max_categories]
        if col_cut is not None and col_cut != []:
            logger.error("There are too many categories!")
            raise NameError(
                f"There are too many categories in columns {data[col_cut].dtypes.index}! Check your data or change the parameter 'max_cut' describing the maximum number of categories."
            )
        dummy_data = pd.get_dummies(data, drop_first=True, dtype=np.uint8)
        return dummy_data

    def _preprocessing_data(self):
        """Converts categorical features into dummy variables."""
        if isinstance(self.outcomes, list) and len(self.outcomes) > 1:
            warnings.warn(
                "To ensure the multitarget's correct operation, it's necessary to guarantee the independence of the targets from each other."
            )
            raise NotImplementedError(
                "We are working on it"
            )
        info_col = self.info_col if self.info_col is not None else []
        if self.group_col is not None:
            self.input_data = self.validate_group_col(
                self.input_data,
                self.group_col,
                self.treatment,
                self.outcomes,
                1,
                self.rare_categories_scenario
            )
        columns_to_drop = info_col + self.group_col + self.outcomes + [self.treatment]

        if self.base_filtration:
            filtered_features = nan_filtration(
                self.input_data.drop(columns=columns_to_drop)
            )
            self.dropped_features = [
                f
                for f in self.input_data.columns
                if f not in filtered_features + columns_to_drop
            ]
            self.input_data = self.input_data[filtered_features + columns_to_drop]

        nan_counts = self.input_data.isna().sum().sum()
        if nan_counts != 0:
            self._log(
                f"Number of NaN values filled with zeros: {nan_counts}", silent=False
            )
            if pd.__version__ < '2.2.0':
                self.input_data = self.input_data.fillna(0, downcast=False)
            else:
                self.input_data = self.input_data.fillna(0)

        if self.group_col is not None:
            group_col = self.input_data[
                [self.group_col] if isinstance(self.group_col, str) else self.group_col
            ]
        if self.info_col is not None:
            info_col = self.input_data[self.info_col]

        self.input_data = self._convert_categorical_to_dummy()
        if self.group_col is not None:
            self.input_data = pd.concat([self.input_data, group_col], axis=1)

        if self.info_col is not None:
            self.input_data = pd.concat([self.input_data, info_col], axis=1)

        if self.base_filtration:
            filtered_features = const_filtration(
                self.input_data.drop(columns=columns_to_drop)
            )
            self.dropped_features = np.concatenate(
                (
                    self.dropped_features,
                    [
                        f
                        for f in self.input_data.columns
                        if f not in filtered_features + columns_to_drop
                    ],
                )
            )
            self.input_data = self.input_data[filtered_features + columns_to_drop]
        self._log("Categorical features turned into dummy")

    def validate_group_col(
            self,
            df: pd.DataFrame,
            group_col: List[str],
            treat_col: str,
            target_col: str,
            frequency_th: int = 1,
            rare_categories_scenario: str = "raise",
    ) -> pd.DataFrame:
        """
        Validates the distribution of control and test group instances within each category of a specified grouping column(s) in a DataFrame. It handles rare categories (categories with instances below a specified threshold) according to the defined scenario ('raise', 'drop', or 'genetic').

        Args:
            df: The DataFrame containing the data to be validated.
            group_col: The name of the column used for grouping data.
            treat_col: The name of the column indicating treatment groups.
            target_col: The name of the column containing target values.
            frequency_th: The minimum number of instances required for a category not to be considered rare. Default is 1.
            rare_categories_scenario: Defines the action to take when rare categories are found. Options are 'raise' (default), 'drop', or 'genetic'. 'raise' will cause an error; 'drop' will remove rare categories; 'genetic' will apply a genetic stratification method to handle rare categories.

        Returns:
            A DataFrame that has been processed based on the specified 'rare_categories_scenario'. If 'drop' is used, rare categories are removed. If 'genetic' is used, the DataFrame is modified accordingly.

        Raises:
            KeyError: If an invalid 'rare_categories_scenario' is provided.
            ValueError: If 'raise' is specified for 'rare_categories_scenario' and rare categories are found.

        Example:
            >>> df_validated = validate_group_col(df, 'Group', 'Treatment', 'Outcome', 1, 'drop')
            This will drop any groups in 'Group' column that have less than or equal to one instance in
            either treatment group
        """
        if rare_categories_scenario not in RARE_CAT_SCENARIO_LIST:
            raise KeyError(
                f"""Wrong rare_categories_scenario value: {rare_categories_scenario}
            It should be one of {RARE_CAT_SCENARIO_LIST}"""
            )

        if group_col:
            rare_categories = self.get_rare_categories(
                df, group_col, treat_col, frequency_th=frequency_th
            )
            if len(rare_categories) > 0:
                if rare_categories_scenario == "raise":
                    raise ValueError(
                        f"""Next columns have low frequency: {rare_categories}.
                    Try to change rare_categories_scenario for one of {RARE_CAT_SCENARIO_LIST} for auto process."""
                    )
                elif rare_categories_scenario == "drop":
                    df = df.loc[~df[group_col[0]].isin(rare_categories)]
                elif rare_categories_scenario == "genetic":
                    new_group_col = self.genetic_stratification(
                        df, group_col[0], treat_col, target_col
                    )
                    df[group_col[0]] = new_group_col
        return df.reset_index(drop=True)

    @staticmethod
    def get_rare_categories(
            df: pd.DataFrame,
            group_col: str,
            treat_col: str,
            frequency_th: int = 1,
    ) -> List[str]:
        """
        Identifies and returns a list of categories within specified grouping columns that
        occur less than or equal to a specified frequency threshold within each treatment
        group. This can be useful for filtering out rare categories in treatment/control
        groups to ensure sufficient sample sizes for analysis.

        Args:
            df: The dataframe containing the data to be analyzed.
            group_col: The column used for grouping the data.
            treat_col: The column specifying the treatment group. This column
                is used to separate the data into different treatment groups.
            frequency_th: The frequency threshold. Categories within
                each treatment group that occur less than or equal to this number
                will be considered rare. Default is 1, which selects categories that
                occur only once within each treatment group.

        Returns:
            A list of the rare categories within the specified grouping columns.
                If there are no rare categories, an empty list is returned.

        Example:
            >>> df = pd.DataFrame({
                    'Group': ['A', 'A', 'B', 'B', 'C'],
                    'Treatment': [0, 1, 1, 1, 0],
                    'Data': [5, 6, 7, 8, 9]
                })
            >>> get_rare_categories(df, 'Group', 'Treatment', 1)
            ['C']
        """
        if isinstance(group_col, list) and len(group_col) == 1:
            group_col = group_col[0]
        else:
            raise ValueError(f'Wrong group_col format: {group_col}')
        frequencies = df \
            .groupby(by=[group_col, treat_col]) \
            .size() \
            .groupby(group_col) \
            .agg(lambda x: (len(x) == 2) * x.min())
        rare_categories = (
            frequencies[frequencies < frequency_th].reset_index().loc[:, group_col]
        ).tolist()
        # rare_categories = (
        #     rare_categories.unique().tolist() if rare_categories.size > 0 else []
        # )

        return rare_categories

    @staticmethod
    def genetic_stratification(
            df: pd.DataFrame,
            group_col: Union[str, List[str]],
            treat_col: str,
            target_col: str,
            frequency_th: int = 1,
    ) -> List[str]:
        """
        Generates a new_group_col using a genetic algorithm.
        """
        raise NotImplementedError

    def _apply_filter(self, filter_class, *filter_args):
        """Applies a filter to the input data.

        Args:
            filter_class:
                The class of the filter to apply.
            *filter_args:
                Arguments to pass to the filter class.
        """
        filter_instance = filter_class(*filter_args)
        self.input_data = filter_instance.perform_filter(self.input_data)

    def _spearman_filter(self):
        """Applies a filter by dropping columns correlated with the outcome column.

        This method uses the Spearman filter to eliminate features from the dataset
        that are highly correlated with the outcome columns, based on a pre-set threshold
        """
        self._log(
            "Applying filter by spearman test - drop columns correlated with outcome"
        )
        self._apply_filter(
            SpearmanFilter, self.outcomes[0], self.treatment, self.same_target_threshold
        )

    def outliers_filter(self):
        """Removes outlier values from the dataset.

        This method employs an OutliersFilter. If `drop_outliers_by_percentile` is True,
        it retains only the values between the min and max percentiles
        If `drop_outliers_by_percentile` is False, it retains only the values between 2nd and 98th percentiles
        """
        self._log(
            f"Applying filter of outliers\n"
            f"interquartile_coeff={self.interquartile_coeff}\n"
            f"mode_percentile={self.mode_percentile}\n"
            f"min_percentile={self.min_percentile}\n"
            f"max_percentile={self.max_percentile}"
        )

        self._apply_filter(
            OutliersFilter,
            self.interquartile_coeff,
            self.mode_percentile,
            self.min_percentile,
            self.max_percentile,
        )

    def match_no_rep(
            self, threshold: float = 0.1, approximate_match: bool = False
    ) -> pd.DataFrame:
        """Matching groups with no replacement.

        It's done by optimizing the linear sum of
        distances between pairs of treatment and control samples.

        Args:
            threshold: caliper for minimum deviation between test and control groups. in case weights is not None.
            approximate_match: use or not approximate matching

        Returns:
              Matched dataframe with no replacements.
        """
        a = self.input_data[self.treatment]
        X = self.input_data.drop(columns=self.treatment)

        if self.info_col is not None:
            X = X.drop(columns=self.info_col)

        index_matched = MatcherNoReplacement(
            X, a, self.weights, approximate_match
        ).match()

        filtered_matches_tr = (
            index_matched.loc[1]
            .iloc[self.input_data[a == 1].index]
            .matches[index_matched.loc[1]
            .iloc[self.input_data[a == 1].index]
            .matches.apply(lambda x: x != [])]
        )
        filtered_matches_ntr = (
            index_matched.loc[0]
            .iloc[self.input_data[a == 0].index]
            .matches[index_matched.loc[1]
            .iloc[self.input_data[a == 0].index]
            .matches.apply(lambda x: x != [])]
        )

        filtered_matches = pd.concat([filtered_matches_tr, filtered_matches_ntr]).sort_index()

        matched_data = self.input_data.loc[filtered_matches.index.to_list()]

        filtered_matches = filtered_matches.apply(lambda x: int(x[0]))
        filtered_matches_df = filtered_matches.to_frame().reset_index()
        df_matched = matched_data.merge(
            filtered_matches_df, left_index=True, right_on='index', how="left"
        ).merge(
            filtered_matches_df, left_index=True, right_on='matches', how='left'
        ).fillna(0)

        df_matched['index_matched'] = df_matched['matches_x']
        df_matched = df_matched.drop(columns=['index_x', 'matches_x', 'index_y', 'matches_y'])
        df_matched['index_matched'] = df_matched['index_matched'].astype(int)

        input_data_matched = self.input_data.add_suffix('_matched')

        df_matched = df_matched.merge(
            input_data_matched, left_on='index_matched', right_index=True, how='left'
        )

        df_matched = df_matched.set_index("matches").reset_index().drop(columns=['index_matched', 'matches'])

        return df_matched

    def feature_select(self) -> pd.DataFrame:
        """Calculates the importance of each feature.

        This use one of FeatureSelector methods to rank the importance of each feature in the dataset
        The features are then sorted by their importance with the most important feature first

        Returns:
            The feature importance, sorted in descending order
        """
        self._log("Counting feature importance")

        feat_select = FeatureSelector(
            outcome=self.outcomes,
            treatment=self.treatment,
            feature_selection_method=self.feature_selection_method,
        )
        df = (
            self.input_data
            if self.group_col is None
            else self.input_data.drop(columns=self.group_col)
        )

        if self.info_col is not None:
            df = df.drop(columns=self.info_col)

        self.detailed_features_df = feat_select.perform_selection(df=df)
        self.short_features_df = self.detailed_features_df.loc[:, ["rank"]]

        return self.short_features_df

    def _create_faiss_matcher(self, df=None, validation=None, refuter=None):
        """Creates a FaissMatcher object.

        Args:
            df:
                The dataframe to use. If None, uses self.input_data.
            validation:
                Whether to use the matcher for validation. If None, determines based on whether
        """
        if df is None:
            df = self.input_data
        self.matcher = FaissMatcher(
            df,
            self.outcomes,
            self.treatment,
            info_col=self.info_col,
            weights=self.weights,
            features=self.features_importance,
            group_col=self.group_col,
            validation=validation,
            refuter=refuter,
            n_neighbors=self.n_neighbors,
            pbar=False if validation else self.pbar,
            algo=self.algo
        )

    def _perform_validation(self):
        """Performs validation using the FaissMatcher."""
        if self.group_col in [None, []]:
            sim = self.matcher.match()
        else:
            sim = self.matcher.group_match()
        for key in self.val_dict.keys():
            self.val_dict[key].append(sim[key][0])

    def _log(self, message, silent=None):
        """Logs a message at the appropriate level.

        Args:
            message:
                The message to log.
            silent:
                If silent, logs will be only info
        """
        if silent is None:
            silent = self.silent
        if silent:
            logger.debug(message)
        else:
            logger.info(message)

    def _matching(self) -> tuple:
        """Performs matching considering the presence of groups.

        Returns:
            Results of matching and matching quality metrics
        """
        self._create_faiss_matcher()
        self._log("Applying matching")

        self.results, df_matched = self.matcher.match()

        self.quality_result = self.matcher.matching_quality(df_matched)

        return self.results, self.quality_result, df_matched

    def validate_result(
            self,
            refuter: str = "permutation_test",
            effect_type: str = "att",
            n_sim: int = 500,
            fraction: float = 0.8,
            low: float = 1.0,
            high: float = 99.0
    ) -> dict:
        """Validates estimated ATE (Average Treatment Effect).

        Validates estimated effect:
                                    1) by replacing real treatment with random placebo treatment.
                                     Estimated effect must be droped to zero, p-val < 0.05;
                                    2) by adding random feature (`random_feature`). Estimated effect shouldn't change
                                    significantly, p-val < 0.05;
                                    3) estimates effect on subset of data (default fraction is 0.8). Estimated effect
                                    shouldn't change significantly, p-val < 0.05.

        Args:
            refuter:
                Refuter type (`permutation_test`, `random_feature`, `subset_refuter`, `emissions`)
            effect_type:
                Which effect to validate (`ate`, `att`, `atc`)
            n_sim:
                Number of simulations
            fraction:
                Subset fraction for subset refuter only
            low:
                The lower percentile value for removing outliers (default = 1)
            high:
                The upper percentile value for removing outliers (default = 99)

        Returns:
            Dictionary of outcome_name (mean_effect on validation, p-value)
            or dataframe with effects after outliers are removed

        ..warnings::
            Random Treatment algorithm randomly shuffles the actual treatment.
            It is expected that the treatment's effect on the target will be close to 0.
            Random Feature adds a feature with random values.
            It is expected that adding a random feature will maintain the same impact of the treatment on the target.

            These methods are not sufficiently accurate markers of a successful experiment.
        """
        if refuter != "permutation_test":
            raise NotImplementedError(
                "We have found that old validation is not mathematically correct. So now we are working on new method. Please use permutation_test."
            )
        if self.silent:
            logger.debug("Applying validation of result")
        else:
            logger.info("Applying validation of result")

        self.val_dict = {k: [] for k in self.outcomes}
        self.pval_dict = dict()

        effect_dict = {"ate": 0, "atc": 1, "att": 2}

        assert effect_type in effect_dict.keys()

        if refuter == "emissions":

            self._create_faiss_matcher(self.input_data, validation=True, refuter="emissions")
            if self.group_col == []:
                results = self.matcher.match()
            else:
                results = self.matcher.group_match()
            ATE, ATC, ATT = results['effect_size']

            df_full_test, count_test, percent_test = emissions(self.input_data, 1, self.outcomes[0], low, high)
            self._create_faiss_matcher(df_full_test, validation=True, refuter="emissions")
            if self.group_col == []:
                results_test = self.matcher.match()
            else:
                results_test = self.matcher.group_match()
            ATE_test, ATC_test, ATT_test = results_test['effect_size']

            df_full_control, count_control, percent_control = emissions(self.input_data, 0, self.outcomes[0], low, high)
            self._create_faiss_matcher(df_full_control, validation=True, refuter="emissions")
            if self.group_col == []:
                results_control = self.matcher.match()
            else:
                results_control = self.matcher.group_match()
            ATE_control, ATC_control, ATT_control = results_control['effect_size']

            dict_metrics = {'ATE': [ATE, ATE_test, ATE_control],
                            'ATC': [ATC, ATC_test, ATC_control],
                            'ATT': [ATT, ATT_test, ATT_control]
                            }
            rslt_emissions = pd.DataFrame(dict_metrics, index=['Data with outliers',
                                                               f'Metric for deleting {count_test} rows ({percent_test}%) from the test',
                                                               f'Metric for deleting {count_control} rows ({percent_control}%) from the control'])
            return rslt_emissions

        else:

            for i in tqdm(range(n_sim)):
                if refuter in ["permutation_test", "random_feature"]:
                    if refuter == "permutation_test":
                        self.input_data, orig_treatment, self.validate = permutation_test(self.input_data,
                                                                                          self.treatment)
                    elif refuter == "random_feature":
                        self.input_data, self.validate = random_feature(self.input_data)
                        if self.features_importance is not None and i == 0:
                            self.features_importance.append("random_feature")

                    self.matcher = FaissMatcher(
                        self.input_data,
                        self.outcomes,
                        self.treatment,
                        info_col=self.info_col,
                        features=self.features_importance,
                        group_col=self.group_col,
                        validation=self.validate,
                        n_neighbors=self.n_neighbors,
                        pbar=False,
                    )
                elif refuter == "subset_refuter":
                    df, self.validate = subset_refuter(self.input_data, self.treatment, fraction)
                    self.matcher = FaissMatcher(
                        df,
                        self.outcomes,
                        self.treatment,
                        info_col=self.info_col,
                        features=self.features_importance,
                        group_col=self.group_col,
                        validation=self.validate,
                        n_neighbors=self.n_neighbors,
                        pbar=False,
                    )
                else:
                    logger.error("Incorrect refuter name")
                    raise NameError(
                        "Incorrect refuter name! Available refuters: `random_feature`, `permutation_test`, `subset_refuter`"
                    )

                if self.group_col == []:
                    sim = self.matcher.match()
                else:
                    sim = self.matcher.group_match()

                for key in self.val_dict.keys():
                    self.val_dict[key].append(sim[key][0])

        for outcome in self.outcomes:
            self.pval_dict.update({outcome: [np.mean(self.val_dict[outcome])]})
            self.pval_dict[outcome].append(
                test_significance(
                    self.results.query("outcome==@outcome").loc[effect_type.upper()][
                        "effect_size"
                    ],
                    self.val_dict[outcome],
                )
            )
        if refuter == "permutation_test":
            self.input_data[self.treatment] = orig_treatment
        elif refuter == "random_feature":
            self.input_data = self.input_data.drop(columns="random_feature")
            if self.features_importance is not None:
                self.features_importance.remove("random_feature")

        return self.pval_dict

    def estimate(self, features: Iterable = None) -> tuple:
        """Performs matching via Mahalanobis distance.

        Args:
            features:
                List or feature_importances from LAMA of features for matching

        Returns:
            Results of matching and matching quality metrics
        """
        if features is not None:
            features = list(features)
            self.features_importance = features
            if self.group_col is not None and self.group_col not in features:
                features.extend(self.group_col)
        return self._matching()

    def save(self, filename):
        """Save the object to a file using pickle.

        This method serializes the object and writes it to a file

        Args:
            filename:
                The name of the file to write to.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, filename):
        """Load an object from a file.

        This method reads a file and deserializes the object from it

        Args:
            filename:
                The name of the file to read from.

        Returns:
                The deserialized object
        """
        with open(filename, "rb") as f:
            return pickle.load(f)
