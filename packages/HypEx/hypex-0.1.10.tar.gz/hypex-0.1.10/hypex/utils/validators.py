"""Validators."""

from typing import List

import numpy as np
import pandas as pd
from scipy import stats as st

def permutation_test(df: pd.DataFrame, treatment: str):
    """Replaces real treatment with a random placebo treatment.

    Args:
        df:
            The initial dataframe
        treatment:
            The columns name representing the treatment

    Returns:
        The modified dataframe with the original treatment replaced
        The original treatment series
        A validation flag
    """
    prop1 = df[treatment].sum() / df.shape[0]
    prop0 = 1 - prop1
    new_treatment = np.random.choice([0, 1], size=df.shape[0], p=[prop0, prop1])
    validate = 1
    orig_treatment = df[treatment]
    df = df.drop(columns=treatment)
    df[treatment] = new_treatment
    return df, orig_treatment, validate


def random_feature(df: pd.DataFrame):
    """Adds a random feature to the initial dataset.

    Args:
        df:
            The initial dataframe

    Returns:
        The modified dataframe with an additional random feature
        A validation flag
    """
    feature = np.random.normal(0, 1, size=len(df))
    validate = 1
    df["random_feature"] = feature
    return df, validate


def subset_refuter(df: pd.DataFrame, treatment: str, fraction: float = 0.8):
    """Returns a subset of data with given fraction (default 0.8).

    Args:
        df:
            The initial dataframe
        treatment:
            The column name representing the treatment
        fraction:
            The fraction of the dataset to divide random matching

    Returns:
        The subset of the dataframe
        A validation flag
    """
    df = df.groupby(treatment, group_keys=False).apply(
        lambda x: x.sample(frac=fraction)
    )
    validate = 1
    return df, validate


def test_significance(estimate: float, simulations: List) -> float:
    """Performs a significance test for a normal distribution.

    Args:
        estimate:
            The estimated effect
        simulations:
            A list of estimated effects from each simulation

    Returns:
        The p-value of the test
    """
    mean_refute_value = np.mean(simulations)
    std_dev_refute_values = np.std(simulations)
    z_score = (estimate - mean_refute_value) / std_dev_refute_values

    if z_score > 0:  # Right Tail
        p_value = 1 - st.norm.cdf(z_score)
    else:  # Left Tail
        p_value = st.norm.cdf(z_score)

    return p_value


def emissions(df: pd.DataFrame, treatment: str, is_treated: int, outcome: str, low: float, high: float) -> tuple:
    """
    Removes outliers in the target beyond the 1st and 99th percentiles.

    Args:
        df: The initial dataframe.
        treatment: Column name representing the treatment.
        is_treated: Value indicating whether a row is treated or not.
        outcome: Column name with the target.
        low: Lower threshold for removing emissions.
        high: Upper threshold for removing emissions.

    Returns:
        A tuple containing:
            - A dataframe that does not contain outliers in the target.
            - The number of emissions removed.
            - The percentage of emissions removed.
    """
    df_treat = df.loc[df[treatment] == is_treated].copy()
    Q3, Q1 = np.nanpercentile(df_treat[outcome], [high, low])
    df_new = df_treat.loc[df_treat[outcome].between(Q1, Q3)]

    count = df_treat.shape[0] - df_new.shape[0]
    percent = round(count * 100 / df_treat.shape[0], 1)
    frames = [df_new, df[df[treatment] != is_treated]]
    df_full = pd.concat(frames, axis=0)
    return df_full, count, percent
