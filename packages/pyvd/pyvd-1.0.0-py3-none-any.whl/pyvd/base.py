import numpy as np
import pyvd
from collections import namedtuple


def demog_vd_calc(year_vec, year_init, pop_mat):
    """
    Calculate vital dynamics consistent with a population pyramid (# of people specific per age per year).

    Parameters
    ----------
    year_vec : array_like
        Vector of years.
    year_init : float
        Initial year.
    pop_mat : array_like
        Population matrix (age_bin x year).

    Returns
    -------
    vd_tup : named tuple
        Tuple containing the following elements:
        - mort_year : array_like
            Vector of years relative to year_init.
        - mort_mat : array_like
            Matrix of mortality rates by age group.
        - birth_rate : float
            Initial birth rate (births / person / day).
        - br_mult_x : array_like
            Birth rate multiplier x values (days).
        - br_mult_y : array_like
            Birth rate multiplier y values.

    Notes
    -----
    Some outputs (mort_mat) are forced into stair-step format like [x1, x2, x2+eps, x3] and [y1, y1, y2, y2]
    """

    # Calculate vital dynamics
    diff_ratio = (pop_mat[:-1, :-1] - pop_mat[1:, 1:]) / np.where(
        pop_mat[:-1, :-1] != 0, pop_mat[:-1, :-1], np.nan
    )

    t_delta = np.diff(year_vec) if len(year_vec) > 1 else np.array([])
    pow_vec = 365.0 * t_delta
    mortvecs = 1.0 - np.power(
        1.0 - np.nan_to_num(diff_ratio, nan=0.0), 1.0 / np.nan_to_num(pow_vec, nan=1.0)
    )
    mortvecs = np.minimum(mortvecs, pyvd.constants.MAX_DAILY_MORT)
    mortvecs = np.maximum(mortvecs, 0.0)
    tot_pop = np.sum(pop_mat, axis=0)
    tpop_mid = (tot_pop[:-1] + tot_pop[1:]) / 2.0
    pop_corr = np.exp(-mortvecs[0, :] * pow_vec / 2.0)

    brate_vec = np.round(pop_mat[0, 1:] / tpop_mid / t_delta * 1000.0, 1) / pop_corr
    brate_val = np.interp(year_init, year_vec[:-1], brate_vec)
    yrs_off = year_vec[:-1] - year_init
    yrs_dex = yrs_off > 0

    brmultx_01 = np.array([0.0] + (365.0 * yrs_off[yrs_dex]).tolist())
    brmulty_01 = np.array([1.0] + (brate_vec[yrs_dex] / brate_val).tolist())
    brmultx_02 = np.zeros(2 * len(brmultx_01) - 1)
    brmulty_02 = np.zeros(2 * len(brmulty_01) - 1)

    brmultx_02[0::2] = brmultx_01[0:]
    brmulty_02[0::2] = brmulty_01[0:]
    brmultx_02[1::2] = brmultx_01[1:] - 0.5
    brmulty_02[1::2] = brmulty_01[0:-1]

    birth_rate = brate_val / 365.0 / 1000.0
    mort_year = np.zeros(2 * year_vec.shape[0] - 3)

    mort_year[0::2] = year_vec[0:-1]
    mort_year[1::2] = year_vec[1:-1] - 1e-4
    mort_year = mort_year.tolist()

    mort_mat = np.zeros((len(pyvd.constants.MORT_XVAL), len(mort_year)))

    mort_mat[0:-2:2, 0::2] = mortvecs
    mort_mat[1:-2:2, 0::2] = mortvecs
    mort_mat[0:-2:2, 1::2] = mortvecs[:, :-1]
    mort_mat[1:-2:2, 1::2] = mortvecs[:, :-1]
    mort_mat[-2:, :] = pyvd.constants.MAX_DAILY_MORT

    VitalDynamics = namedtuple(
        "VitalDynamics",
        "mort_year mort_mat birth_rate br_mult_x  br_mult_y",
    )
    return VitalDynamics(mort_year, mort_mat, birth_rate, brmultx_02, brmulty_02)


if __name__ == "__main__":
    pop_input = pyvd.make_pop_dat("IND")
    year_vec = pop_input[0, :] - pyvd.constants.BASE_YEAR
    year_init = pyvd.constants.BASE_YEAR - pyvd.constants.BASE_YEAR
    pop_mat = pop_input[1:, :] + 0.1
    pop_init = [
        np.interp(year_init, year_vec, pop_mat[idx, :])
        for idx in range(pop_mat.shape[0])
    ]
    vd_tup = demog_vd_calc(year_vec, year_init, pop_mat, pop_init)
    print(len(vd_tup))
