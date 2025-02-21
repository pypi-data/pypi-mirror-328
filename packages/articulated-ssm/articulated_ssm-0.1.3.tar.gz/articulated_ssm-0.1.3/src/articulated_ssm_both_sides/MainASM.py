# Main articulated SSM model fitting script
# 25/01/2023

import os
import numpy as np

from articulated_ssm_both_sides.FitASM_2 import FitASM
from articulated_ssm_both_sides.LandmarkHandler import LandmarkHandler
from articulated_ssm_both_sides.SegmentationHandler import SegmentationHandler
from articulated_ssm_both_sides.LowerLimb import LowerLimb
from articulated_ssm_both_sides.PLSR import plsr


# TODO: Remove all input files.
#   All outputs should go in an (untracked) output directory.
#   Return the output directory so caller can find mesh files...?

# TODO: JUST keep the remaining values in the dictionary for now and pass in ONLY the TRC data.
#   Then it will be working, and we can sort the rest out later.
# TODO: Actually, I'm not sure if segmentation is supposed to be an additional or alternative step.
#   - 'seg' or 'lm', we don't need two checks...?
#   - Is 'PLSR' in addition to one of the fit methods above?
#   - Put 'seg' and 'PLSR' in their own functions, since they aren't ever used we don't currently need those `if` checks.
general_fit_settings = {
    'segm_fit': False,                          # Fit using segmentation data
    'lm_fit': True,                             # Fit using landmark coordinates
    # TODO: Keep these as a setting.
    'include_patella': False,                   # Include patella
    'patella_shift': np.array([50, 50, -10]),
    # TODO: Maybe keep these as setting for now but consider making available later.
    'pc_modes': [[0], [0, 1, 2, 3]],            # , [[0,1],[0, 1, 2, 3, 4]],    # PC modes to fit (multi fit: [[],[]])
    'mweight': [1, 0.0001],                     # [1, 0.01],                    # Mahalanobis weight (multi fit: [float, float])
    'min_args': {'method': 'Powell'},           # {'method': 'BFGS','jac': False,'bounds': None, 'tol': 1e-6,'options': {'eps': 1e-5}},
    # TODO: Modifiable knee values for advanced users.
    'knee_gap': 5,                              # Minimal gap between femur and tibia knee nodes
    'knee_fixed': False,                        # Fix the knee in initial position (0)
    'allow_knee_adduction_dof': True,           # Allow rotation in VV when placing tibia-fibula
    'allow_knee_adduction_correction': True,    # Allow VV rotation to obtain minimal knee gap
    # TODO: Does this really need to be a setting?
    'x0': None,                                 # Initial parameters for the 1st fit
    'init_pc_weights': None,                    # Initial weights for each mode in the first fit.
    # TODO: Advanced users.
    'correct_markers': True,                    # if motion capture markers are used for prediction: True
    # TODO: Keep this hard coded.
    #   Is this in addition to seg/landmark...?
    'PLSR': False,                              # if a partial least squares regression is used to provide an initial guess to shape model
    }


def run_asm(marker_data, output_directory):
    """
    Main entry point for ASM fitting process. Takes a dictionary containing the landmark positions
    defining a single TRC frame.

    :param marker_data: A dictionary containing the landmark positions defining a single TRC frame.
    :param output_directory: The path to the directory where the mesh files should be saved.
    """

    # Generate and load lower limb model.
    lower_limb_model = LowerLimb(general_fit_settings)
    lower_limb_model.ll_l.load_bones_and_model()
    lower_limb_model.ll_r.load_bones_and_model()

    # Load landmark coordinates data to fit to.
    fit_data = landmark_fit(lower_limb_model, marker_data)

    asm_fitter_l = FitASM(lower_limb_model, general_fit_settings, fit_data, output_directory, 'left')
    asm_fitter_r = FitASM(lower_limb_model, general_fit_settings, fit_data, output_directory, 'right')

    write_fit_metrics(asm_fitter_l, asm_fitter_r, output_directory)


def landmark_fit(lower_limb_model, marker_data):
    landmark_names_to_fit = ['ASIS', 'PSIS', 'SAC', 'LEC', 'MEC', 'malleolus_med', 'malleolus_lat']

    fit_data = {}
    for side in ['left', 'right']:
        fit_data[f'landmark_handler_{side[0]}'] = LandmarkHandler(
            marker_data, landmark_names_to_fit, lower_limb_model, general_fit_settings['correct_markers'], side
        )

    return fit_data


def segmentation_fit(segmentations_directory):
    segmentation_handler = SegmentationHandler(segmentations_directory, general_fit_settings)
    fit_data = {'segmentation_handler': segmentation_handler}

    return fit_data


def plsr_fit(anthro_data_path, case_data):
    """
    `case_data` should be a numpy array containing the values: 'height', ASIS width, femur length, tibia length.
    """
    pred_weights, pred_sd = plsr(case_data, anthro_data_path, general_fit_settings)
    if isinstance(general_fit_settings['pc_modes'][0], (list, tuple, np.ndarray)):
        general_fit_settings['init_pc_weights'] = pred_sd[:(len(general_fit_settings['pc_modes'][-1]))]
    else:
        general_fit_settings['init_pc_weights'] = pred_sd[:(len(general_fit_settings['pc_modes']))]
        print(general_fit_settings['init_pc_weights'])


def write_fit_metrics(asm_fitter_l, asm_fitter_r, output_directory):
    metrics_path = os.path.join(output_directory, "asm_fit_metrics.txt")
    with open(metrics_path, "w") as metrics_file:
        metrics_file.write("MAE, RMSE, m_weight\n")
        metrics_file.write(f"{asm_fitter_l.mae_lm}, {asm_fitter_l.rmse_lm}, {asm_fitter_l.opt_mweight}\n")
        metrics_file.write(f"{asm_fitter_r.mae_lm}, {asm_fitter_r.rmse_lm}, {asm_fitter_r.opt_mweight}\n")
