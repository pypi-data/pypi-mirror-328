from __future__ import annotations

__all__ = [
    "gumbel_extreme_values",
    "moving_average_extreme_values",
    "peak_extreme_values",
]


import math

import numpy as np

from cfdmod.use_cases.pressure.statistics import (
    ExtremeGumbelParamsModel,
    ExtremeMovingAverageParamsModel,
    ExtremePeakParamsModel,
)


def fit_gumbel_model(
    data: np.ndarray, params: ExtremeGumbelParamsModel, sample_duration: float
) -> float:
    """Fits the Gumbel model to predict extreme events

    Args:
        data (np.ndarray): Historic series
        params (ExtremeGumbelParamsModel): Parameters for Gumbel model analysis
        sample_duration (float): Duration of the sample

    Returns:
        float: Gumbel value for data
    """
    N = len(data)
    y = [-math.log(-math.log(i / (N + 1))) for i in range(1, N + 1)]
    A = np.vstack([y, np.ones(len(y))]).T
    a_inv, U_T0 = np.linalg.lstsq(A, data, rcond=None)[0]
    U_T1 = U_T0 + a_inv * math.log(params.event_duration / (sample_duration / N))
    extreme_val = a_inv * params.yR + U_T1  # This is the design value

    return extreme_val


def gumbel_extreme_values(
    params: ExtremeGumbelParamsModel,
    timestep_arr: np.ndarray,
    hist_series: np.ndarray,
) -> tuple[float, float]:
    """Apply extreme values analysis to coefficient historic series

    Args:
        params (ExtremeGumbelParamsModel): Parameters for extreme values calculation
        time_scale_factor (float): Value for converting time scales
        timestep_arr (np.ndarray): Array of simulated timesteps
        hist_series (np.ndarray): Coefficient historic series

    Returns:
        tuple[float, float]: Tuple with (min, max) extreme values
    """
    CST_full_scale = params.full_scale_characteristic_length / params.full_scale_U_H
    time = (timestep_arr - timestep_arr[0]) * (CST_full_scale)

    T0 = time[-1]
    window_size = max(int(params.peak_duration / (time[1] - time[0])), 1)
    smooth_parent_cp = np.convolve(hist_series, np.ones(window_size) / window_size, mode="valid")

    sub_arrays = np.array_split(smooth_parent_cp, params.n_subdivisions)

    cp_max = np.array([np.max(sub_arr) for sub_arr in sub_arrays])
    cp_min = np.array([np.min(sub_arr) for sub_arr in sub_arrays])

    cp_max = np.sort(cp_max)
    cp_min = np.sort(cp_min)[::-1]

    # It may return NaN values if the time series is invalid or has very few points
    max_extreme_val = fit_gumbel_model(cp_max, params=params, sample_duration=T0)
    min_extreme_val = fit_gumbel_model(cp_min, params=params, sample_duration=T0)

    min_extreme_val = 0 if np.isnan(min_extreme_val) else min_extreme_val
    max_extreme_val = 0 if np.isnan(max_extreme_val) else max_extreme_val

    return min_extreme_val, max_extreme_val


def moving_average_extreme_values(
    params: ExtremeMovingAverageParamsModel, hist_series: np.ndarray
) -> tuple[float, float]:
    """Apply extreme values analysis to coefficient historic series using moving average model

    Args:
        params (ExtremeMovingAverageParamsModel): Parameters for extreme values calculation
        hist_series (np.ndarray): Coefficient historic series

    Returns:
        tuple[float, float]: Tuple with (min, max) extreme values
    """
    CST_full_scale = params.full_scale_characteristic_length / params.full_scale_U_H
    window_size = max(1, round(params.window_size_interval / CST_full_scale))

    kernel = np.ones(window_size) / window_size
    smoothed_signal = np.convolve(hist_series, kernel, mode="valid")

    min_extreme_val = smoothed_signal.min()
    max_extreme_val = smoothed_signal.max()

    return min_extreme_val, max_extreme_val


def peak_extreme_values(
    params: ExtremePeakParamsModel, hist_series: np.ndarray
) -> tuple[float, float]:
    """Apply extreme values analysis to coefficient historic series using peak factor model

    Args:
        params (ExtremePeakParamsModel): Parameters for extreme values calculation
        hist_series (np.ndarray): Coefficient historic series

    Returns:
        tuple[float, float]: Tuple with (min, max) extreme values
    """
    average_val = hist_series.mean()
    std_val = hist_series.std()

    min_extreme_val = average_val - params.peak_factor * std_val
    max_extreme_val = average_val + params.peak_factor * std_val

    return min_extreme_val, max_extreme_val
