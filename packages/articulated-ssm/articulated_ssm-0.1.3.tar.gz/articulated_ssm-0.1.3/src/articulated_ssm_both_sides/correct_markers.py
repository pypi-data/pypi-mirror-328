import numpy as np
from copy import deepcopy
from gias3.common import math

CORRECT_FOR_SKIN_PADDING_AND_MARKER_RADIUS = False
SKIN_PADDING = 5
MARKER_RADIUS = 9   # 7mm marker radius + 2mm marker plate


def correct_target_markers(target_markers_per_bone, side):
    """Correct the target marker location using the marker radius and skin padding
    target_markers_per_bone [dict]: Dictionary with the bones, marker_names and coordinates of each target marker per
                                    side:
                                    target_markers_per_bone = {bone: {'left': {markername1: xyz,
                                                                               markername2: xyz},
                                                                      'right': {markername1: xyz,
                                                                                markername2: xyz}}}
    plot [boolean]: True = plot results, False = do not plot results
    """

    original_target_markers_per_bone = deepcopy(target_markers_per_bone)

    oa = (np.asarray(target_markers_per_bone['left']['ASIS']) +
          np.asarray(target_markers_per_bone['right']['ASIS'])) / 2
    op = (np.asarray(target_markers_per_bone['left']['PSIS']) +
          np.asarray(target_markers_per_bone['right']['PSIS'])) / 2

    ap_axis = math.norm(oa - op)

    if side == 'left':
        ml_axis_fem = math.norm(np.asarray(target_markers_per_bone['left']['MEC']) -
                                np.asarray(target_markers_per_bone['left']['LEC']))
        ml_axis_tib = math.norm(np.asarray(target_markers_per_bone['left']['malleolus_med']) -
                                np.asarray(target_markers_per_bone['left']['malleolus_lat']))
        for side in target_markers_per_bone.keys():
            for lm_name in target_markers_per_bone[side].keys():
                if 'ASIS' in lm_name:  # Move marker location posteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif 'PSIS' in lm_name or lm_name == 'SAC':  # Move marker location anteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'MEC':  # Move marker location laterally
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis_fem * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'LEC':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ml_axis_fem * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_med':  # Move marker location laterally
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis_tib * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_lat':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ml_axis_tib * (MARKER_RADIUS + SKIN_PADDING)
                else:
                    print(lm_name)
                    print('Error in skin padding and marker radius correction')
                    input()

    elif side == 'right':
        ml_axis_fem = math.norm(np.asarray(target_markers_per_bone['right']['LEC']) -
                                np.asarray(target_markers_per_bone['right']['MEC']))
        ml_axis_tib = math.norm(np.asarray(target_markers_per_bone['right']['malleolus_lat']) -
                                np.asarray(target_markers_per_bone['right']['malleolus_med']))
        for side in target_markers_per_bone.keys():
            for lm_name in target_markers_per_bone[side]:
                if 'ASIS' in lm_name:  # Move marker location posteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif 'PSIS' in lm_name or lm_name == 'SAC':  # Move marker location anteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'MEC':  # Move marker location laterally
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ml_axis_fem * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'LEC':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis_fem * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_med':  # Move marker location laterally
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ml_axis_tib * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_lat':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis_tib * (MARKER_RADIUS + SKIN_PADDING)
                else:
                    print('Error in skin padding and marker radius correction')

    else:
        for side in target_markers_per_bone.keys():
            if side == 'left' or side == 'right':
                ml_axis_fem = math.norm(np.asarray(target_markers_per_bone[side]['LEC']) -
                                        np.asarray(target_markers_per_bone[side]['MEC']))
                ml_axis_tib = math.norm(np.asarray(target_markers_per_bone[side]['malleolus_lat']) -
                                        np.asarray(target_markers_per_bone[side]['malleolus_med']))
            for lm_name in target_markers_per_bone[side]:
                if lm_name == 'ASIS':  # Move marker location posteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'PSIS' or lm_name == 'SAC':  # Move marker location anteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'MEC':  # Move marker location laterally
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ml_axis_fem * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'LEC':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis_fem * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_med':  # Move marker location laterally
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ml_axis_tib * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_lat':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis_tib * (MARKER_RADIUS + SKIN_PADDING)
                else:
                    print('Error in skin padding and marker radius correction')


def correct_target_markers_no_med(target_markers_per_bone, side_m):
    """Correct the target marker location using the marker radius and skin padding
    target_markers_per_bone [dict]: Dictionary with the bones, marker_names and coordinates of each target marker per
                                    side:
                                    target_markers_per_bone = {bone: {'left': {markername1: xyz,
                                                                               markername2: xyz},
                                                                      'right': {markername1: xyz,
                                                                                markername2: xyz}}}
    plot [boolean]: True = plot results, False = do not plot results
    """

    original_target_markers_per_bone = deepcopy(target_markers_per_bone)

    oa = (np.asarray(target_markers_per_bone['left']['ASIS']) +
          np.asarray(target_markers_per_bone['right']['ASIS'])) / 2
    op = (np.asarray(target_markers_per_bone['left']['PSIS']) +
          np.asarray(target_markers_per_bone['right']['PSIS'])) / 2

    ap_axis = math.norm(op - oa)
    ml_axis = math.norm(
        np.asarray(target_markers_per_bone['left']['ASIS']) - np.asarray(target_markers_per_bone['right']['ASIS']))

    if side_m == 'left':
        for side in target_markers_per_bone.keys():
            for lm_name in target_markers_per_bone[side].keys():
                if lm_name == 'ASIS':  # Move marker location posteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'PSIS' or lm_name == 'SAC':  # Move marker location anteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'LEC':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_lat':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis * (MARKER_RADIUS + SKIN_PADDING)
                else:
                    print(lm_name)
                    print('Error in skin padding and marker radius correction')
                    input()

    elif side_m == 'right':
        for side in target_markers_per_bone.keys():
            for lm_name in target_markers_per_bone[side]:
                if lm_name == 'ASIS':  # Move marker location posteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'PSIS' or lm_name == 'SAC':  # Move marker location anteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'LEC':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_lat':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis * (MARKER_RADIUS + SKIN_PADDING)
                else:
                    print('Error in skin padding and marker radius correction')

    else:
        for side in target_markers_per_bone.keys():
            for lm_name in target_markers_per_bone[side]:
                if lm_name == 'ASIS':  # Move marker location posteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] + \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'PSIS' or lm_name == 'SAC':  # Move marker location anteriorly
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ap_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'LEC':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis * (MARKER_RADIUS + SKIN_PADDING)
                elif lm_name == 'malleolus_lat':  # Move marker location medially
                    target_markers_per_bone[side][lm_name] = \
                        target_markers_per_bone[side][lm_name] - \
                        ml_axis * (MARKER_RADIUS + SKIN_PADDING)
                else:
                    print('Error in skin padding and marker radius correction')
