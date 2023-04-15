import os

standard_presets = {
    'A (Fast)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_M.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_S.glsl'
    ),
    'B (Fast)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_M.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_S.glsl'
    ),
    'C (Fast)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_M.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_S.glsl'
    ),
    'A (HQ)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_VL.glsl', 'Anime4K_Upscale_CNN_x2_VL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ),
    'B (HQ)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_VL.glsl', 'Anime4K_Upscale_CNN_x2_VL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ),
    'C (HQ)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_VL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ),
    'A+A (HQ)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_VL.glsl', 'Anime4K_Upscale_CNN_x2_VL.glsl',
        'Anime4K_Restore_CNN_M.glsl', 'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
        'Anime4K_Upscale_CNN_x2_M.glsl'
    ),
    'B+B (HQ)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_VL.glsl', 'Anime4K_Upscale_CNN_x2_VL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_CNN_Soft_M.glsl',
        'Anime4K_Upscale_CNN_x2_M.glsl'
    ),
    'C+A (HQ)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_VL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_CNN_M.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    )
}

ultra_hq_presets = {
    'A': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ),
    'B': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ),
    'C': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ),
    'A+A': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl',
        'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
        'Anime4K_Upscale_CNN_x2_UL.glsl'
    ),
    'B+B': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl',
        'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_CNN_Soft_UL.glsl',
        'Anime4K_Upscale_CNN_x2_UL.glsl'
    ),
    'C+A': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_CNN_x2_UL.glsl'
    ),
    'A (Death)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_GAN_x4_UUL.glsl',
        'Anime4K_Restore_CNN_Soft_M.glsl', 'Anime4K_Upscale_CNN_x2_M.glsl'
    ),
    'C+A (Death)': (
        'Anime4K_Clamp_Highlights.glsl', 'Anime4K_Upscale_Denoise_CNN_x2_UL.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
        'Anime4K_AutoDownscalePre_x4.glsl', 'Anime4K_Restore_GAN_UUL.glsl', 'Anime4K_Upscale_GAN_x4_UUL.glsl',
        'Anime4K_Restore_CNN_Soft_M.glsl'
    )
}

qualities = ('S', 'M', 'L', 'VL', 'UL')
modes = ('A', 'B', 'C', 'A+A', 'B+B', 'C+A')
sec_qualities = {'S': 'S', 'M': 'S', 'L': 'M', 'VL': 'M', 'UL': 'L'}
current_preset = ''


def create_preset(quality, mode):
    created_presets = {
        'A': (
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
            'Anime4K_AutoDownscalePre_x4.glsl', f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ),
        'B': (
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_Soft_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
            'Anime4K_AutoDownscalePre_x4.glsl', f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ),
        'C': (
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Upscale_Denoise_CNN_x2_{quality}.glsl',
            'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ),
        'A+A': (
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', f'Anime4K_Restore_CNN_{sec_qualities[quality]}.glsl',
            'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ),
        'B+B': (
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Restore_CNN_Soft_{quality}.glsl',
            f'Anime4K_Upscale_CNN_x2_{quality}.glsl', 'Anime4K_AutoDownscalePre_x2.glsl',
            'Anime4K_AutoDownscalePre_x4.glsl', f'Anime4K_Restore_CNN_Soft_{sec_qualities[quality]}.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        ),
        'C+A': (
            'Anime4K_Clamp_Highlights.glsl', f'Anime4K_Upscale_Denoise_CNN_x2_{quality}.glsl',
            'Anime4K_AutoDownscalePre_x2.glsl', 'Anime4K_AutoDownscalePre_x4.glsl',
            f'Anime4K_Restore_CNN_{sec_qualities[quality]}.glsl',
            f'Anime4K_Upscale_CNN_x2_{sec_qualities[quality]}.glsl'
        )
    }
    return created_presets[mode]


def to_string(preset, preset_name=''):
    global current_preset
    preset = (os.path.dirname(__file__) + os.sep + 'shaders' + os.sep + shader for shader in preset)
    current_preset = preset_name
    if os.name == 'nt':
        sep = ';'
    else:
        sep = ':'
    return sep.join(preset)


def android_config(preset, path='/storage/emulated/0/mpv/shaders/'):
    if len(path) != 0 and path[-1] == '/':
        path = path[0:-1]
    preset = (path + '/' + shader for shader in preset)
    return 'glsl-shaders=' + ':'.join(preset)
