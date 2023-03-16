import os
import PySimpleGUI as sg
import mpv
import anime4k
from localization import strings as loc

sg.theme('DarkBlue9')
icon = f'{os.path.dirname(__file__) + os.sep}favicon.ico'
formats = ('mp4', 'mkv', 'webm', 'avi', 'mov', 'wmv', '3gp', 'mp4a', 'mp3', 'flac', 'ogg', 'aac', 'opus', 'wav')
version = '0.2.2 Alpha'


def list_files():
    return [os.path.join(folder, f) for f in os.listdir(folder) if (f.split('.')[-1].lower() in formats)]


def list_filenames():
    filenames = [f for f in os.listdir(folder) if (f.split('.')[-1].lower() in formats)]
    return [f'{i + 1}) ' + filenames[i] for i in range(len(filenames))]


folder = ''
filename = ''
files = []
filenames_only = []
filenum = -1
modes = []
tabs = []

for quality in anime4k.qualities:
    modes += [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]
for quality in anime4k.qualities:
    tabs += [f'{loc["Quality"]} {quality}', [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]]
tabs += [f'{loc["Quality"]} UHQ', [f'{loc["Mode"]} {mode}' for mode in list(anime4k.presets.keys())[9:]]]

menu = [
    [loc['File'], [loc['Open file'], loc['Open URL'], loc['Open folder'], '---', loc['Exit']]],
    [loc['Playback'], [loc['Play | Pause'], '---', loc['Fullscreen']]],
    [loc['Increasing image quality'], [loc['Disable'], '---'] + tabs],
    [loc['Other'], [loc['Reference'], loc['Activate SVP'], loc['Create config for Android'], loc['About']]]
]

panel = [
    [
        sg.Slider(orientation='h', key='-TIME-', enable_events=True, expand_x=True, range=(0, 0),
                  disable_number_display=True)
    ],
    [
        sg.Text('00:00 / 00:00', key='-MEDIA_TIME-'),
        sg.Button('<<', size=(5, 1)),
        sg.Button('ИГРАТЬ', key='-PLAY-', size=(8, 1)),
        sg.Button('>>', size=(5, 1)),
        sg.Image(expand_x=True, pad=(0, 0)),
        sg.Button('ПОЛН', key='-FS-', size=(8, 1)),
        sg.Button('МЕНЮ', key='-MENU-', size=(8, 1)),
        sg.Slider(orientation='h', key='-VOLUME-', default_value=100, enable_events=True, range=(0, 100), size=(12, 16),
                  pad=((5, 5), (0, 8)))
    ]
]

col = [
    [
        sg.Image(key='-LEFT_PAD-', pad=(0, 0), size=(4, 0)),
        sg.Image(key='-VID_OUT-', expand_x=True, expand_y=True, pad=(0, 0)),
        sg.Image(key='-RIGHT_PAD-', pad=(0, 0), size=(4, 0))
    ],
    [
        sg.Frame('', key='-PANEL-', layout=panel, expand_x=True)
    ]
]

col_files = [
    [
        sg.Frame('Информация', key='-INFO-', layout=[[sg.Text('', key='-MEDIA_INFO-')]],
                 expand_x=True)
    ],
    [
        sg.Listbox(values=filenames_only, size=(50, 1000), key='-FILELIST-', enable_events=True, horizontal_scroll=True,
                   font='Consolas 10')
    ]
]

layout = [
    [
        sg.Menu(menu, key='-MENUBAR-', font='Consolas 10'),
        sg.Col(col, expand_x=True, expand_y=True, pad=(0, 0)),
        sg.Col(col_files, key='-LIST-', visible=False)
    ]
]

window = sg.Window('Anime Player', layout, icon=icon, resizable=True, finalize=True, font='Consolas 11',
                   size=(980, 540), margins=(0, 0), return_keyboard_events=True)
window['-FILELIST-'].Widget.bind('<KeyPress>', 'break')

player: mpv.MPV = mpv.MPV(wid=window['-VID_OUT-'].Widget.winfo_id(), keep_open=True, profile='gpu-hq', scale='spline64',
                          cscale='spline64')

while True:
    event, values = window.read(timeout=100)
    # --------------------- Кнопки ---------------------
    if event in (None, sg.WIN_CLOSED, loc['Exit']):
        break
    elif event == '-VOLUME-':
        player.volume = values['-VOLUME-']
    elif event == '-TIME-' and player.duration is not None:
        player.time_pos = values['-TIME-']
        window['-MEDIA_TIME-'].update(value="{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(int(player.time_pos), 60),
                                                                                   *divmod(int(player.duration), 60)))
    elif event in '>>' and filenum < len(files) - 1:
        filenum += 1
        filename = files[filenum]
        window['-FILELIST-'].update(set_to_index=filenum, scroll_to_index=filenum)
        player.play(filename)
    elif event in '<<':
        if filenum > 0:
            filenum -= 1
            filename = files[filenum]
            window['-FILELIST-'].update(set_to_index=filenum, scroll_to_index=filenum)
            player.play(filename)
        else:
            filenum = 0
            window['-FILELIST-'].update(set_to_index=filenum, scroll_to_index=filenum)
    elif event in ('-PLAY-', loc['Play | Pause'], ' '):
        if filename != '':
            if player.duration is None:
                player.play(filename)
                player.pause = False
                window['-PLAY-'].update('ПАУЗА')
            elif not player.pause:
                player.pause = True
                window['-PLAY-'].update('ИГРАТЬ')
            else:
                player.pause = False
                window['-PLAY-'].update('ПАУЗА')
    elif event in ('-FS-', loc['Fullscreen'], 'F11:122'):
        # Взял window['-LEFT_PAD-'].visible как значение по которому ориентируюсь включен ли полноэкранный режим
        if window['-LEFT_PAD-'].visible:
            window.TKroot.attributes("-fullscreen", True)
            window['-VID_OUT-'].set_size(window.size)
            window['-MENUBAR-'].update(visible=False)
            window['-LEFT_PAD-'].update(visible=False)
            window['-RIGHT_PAD-'].update(visible=False)
        else:
            window.TKroot.attributes("-fullscreen", False)
            window['-VID_OUT-'].set_size((0, 0))
            window['-PANEL-'].update(visible=True)
            window['-MENUBAR-'].update(visible=True)
            window['-LEFT_PAD-'].set_size((4, 0))
            window['-RIGHT_PAD-'].set_size((4, 0))
            window['-VID_OUT-'].update(visible=False)
            window['-LEFT_PAD-'].update(visible=True)
            window['-VID_OUT-'].update(visible=True)
            window['-RIGHT_PAD-'].update(visible=True)
        # if player.duration is not None:
        #     player.wid = -1
        #     player.vo = 'null'
        #     player.fullscreen = True
        #     player.vo = ''
        #     player.wait_for_property('fullscreen', lambda val: not val)
        #     player.fullscreen = True
        #     if player.pause and window['-PLAY-'] != 'ИГРАТЬ':
        #         window['-PLAY-'].update('ИГРАТЬ')
        #     elif not player.pause and window['-PLAY-'] != 'ПАУЗА':
        #         window['-PLAY-'].update('ПАУЗА')
        #     player.wid = window['-VID_OUT-'].Widget.winfo_id()
        #     player.vo = 'null'
        #     player.vo = ''
    elif event == '-MENU-':
        if not window['-LIST-'].visible:
            window['-LIST-'].update(visible=True)
        else:
            window['-LIST-'].update(visible=False)
    elif event == loc['Activate SVP']:
        if player.input_ipc_server != 'mpvpipe':
            player.input_ipc_server = 'mpvpipe'
            player.hwdec = 'auto-copy'
            player.hwdec_codecs = 'all'
            player.hr_seek_framedrop = False
    elif event == '-FILELIST-':
        if len(filenames_only) >= 1:
            if len(filenames_only) > 1 or len(values['-FILELIST-'][0]) > 1 and values['-FILELIST-'][0][1] == ')':
                filename_temp = os.path.join(folder, values['-FILELIST-'][0].split(' ', 1)[-1])
                if filename != filename_temp or filenum < 0:
                    filename = filename_temp
                    filenum = files.index(filename)
                    player.play(filename)
    # ------------------ Клавиатура ------------------
    elif event == 'Right:39' and player.time_pos is not None:
        player.time_pos += 5
    elif event == 'Left:37' and player.time_pos is not None:
        if player.time_pos > 5:
            player.time_pos -= 5
        else:
            player.time_pos = 0
    elif event == 'Up:38':
        if player.volume > 95:
            player.volume = 100
        else:
            player.volume += 5
        window['-VOLUME-'].update(value=player.volume)
    elif event == 'Down:40':
        if player.volume < 5:
            player.volume = 0
        else:
            player.volume -= 5
        window['-VOLUME-'].update(value=player.volume)
    # ----------------- Верхнее меню -----------------
    elif event == loc['Open file']:
        file = sg.popup_get_file('Выберите файл', no_window=True, icon=icon,
                                 file_types=(('Все поддерживаемые файлы', ' '.join(['.' + f for f in formats])),))
        if file != '' and file is not None:
            file = file.replace('/', os.sep)
            player.pause = True
            player.stop()
            window['-PLAY-'].update('ИГРАТЬ')
            folder = file.rsplit(os.sep, 1)[0]
            files = [file]
            filenames_only = [file.split(os.sep)[-1]]
            filenum = 0
            filename = file.rsplit(os.sep, 1)[-1]
            window['-FILELIST-'].update(values=filenames_only)
            window['-LIST-'].update(visible=False)
            player.play(file)
            window.refresh()
    elif event == loc['Open URL']:
        link = sg.popup_get_text('Введите URL-адрес', title='Ввод ссылки', icon=icon, font='Consolas', size=(30, 40))
        if link != '' and link is not None:
            player.pause = True
            player.stop()
            window['-PLAY-'].update('ИГРАТЬ')
            folder = 'Ссылка'
            files = [link]
            filenames_only = []
            filenum = 0
            filename = link
            window['-FILELIST-'].update(values=files)
            window['-LIST-'].update(visible=False)
            player.play(link)
            window.refresh()
    elif event == loc['Open folder']:
        new_folder = sg.popup_get_folder(
            'Выберите папку с медиа', title='Выбор папки', icon=icon, font='Consolas', history=True, size=(30, 40))
        if new_folder != '' and new_folder is not None:
            new_folder = new_folder.replace('/', os.sep)
            player.pause = True
            player.stop()
            window['-PLAY-'].update('ИГРАТЬ')
            folder = new_folder
            files = list_files()
            filenames_only = list_filenames()
            filenum = -1
            if len(files) != 0:
                filename = files[0]
            else:
                filename = ''
            window['-FILELIST-'].update(values=filenames_only)
            window['-LIST-'].update(visible=True)
            window.refresh()
    elif event == loc['Disable']:
        player.glsl_shaders = ''
    elif event in [f'{loc["Mode"]} {mode}' for mode in anime4k.presets.keys()]:
        player.glsl_shaders = anime4k.to_string(anime4k.presets[event.split(' ', 1)[-1]])
    elif event in modes:
        quality = event.replace(')', '').split('(')[1]
        mode = event.split(' ')[1]
        player.glsl_shaders = anime4k.to_string(anime4k.create_preset(quality, mode))
    elif event == loc['Reference']:
        with open(f'{os.path.dirname(__file__) + os.sep}doc{os.sep}GLSL_Instructions_Advanced_ru.txt', 'r',
                  encoding='utf-8') as file:
            reference = file.read()
        sg.popup_scrolled(reference, size=(180, 0), title=loc['Reference'], icon=icon, font='Consolas')
    elif event == loc['Create config for Android']:
        config_layout = [
            [sg.Text(
                'Этот конфиг вы можете использовать для использования алгоритма Anime4K в видеоплеере mpv на андроид')],
            [sg.Text('Введите путь до шейдеров')],
            [sg.Input('/storage/emulated/0/mpv/shaders/')],
            [sg.Text('Выберите конфигурацию алгоритма')],
            [sg.Combo(modes, readonly=True)],
            [sg.OK(size=(6, 1)), sg.Button('Все', size=(6, 1))]
        ]
        config_windows = sg.Window(loc['Create config for Android'], config_layout, icon=icon, resizable=True,
                                   size=(500, 180), modal=True)
        while True:
            event, values = config_windows.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'OK' and values[1] != '':
                quality = values[1].replace(')', '').split('(')[1]
                mode = values[1].split(' ')[1]
                sg.popup_scrolled(
                    f'# {values[1]}\n' + anime4k.android_config(anime4k.create_preset(quality, mode), values[0]),
                    title=values[1], icon=icon)
            elif event == 'Все':
                mods = []
                for mod in modes:
                    quality = mod.replace(')', '').split('(')[1]
                    mode = mod.split(' ')[1]
                    mods.append(
                        f'# {mod}\n' + '# ' + anime4k.android_config(anime4k.create_preset(quality, mode), values[0]))
                sg.popup_scrolled('\n\n'.join(mods), title='Все', icon=icon)
        config_windows.close()
    elif event == loc['About']:
        sg.popup(f'Anime Player v{version}\n\n{loc["About program"]}\n\nCopyright © 2023 MazurDev', title=loc['About'],
                 icon=icon)

    duration = player.duration
    time_pos = player.time_pos
    codec = player.video_format if player.video_format is not None else player.audio_codec_name
    fps = round(player.estimated_vf_fps, 1) if player.estimated_vf_fps is not None else None
    str_resolution = f'{player.width}x{player.height}' if player.width is not None else ''
    str_fps = f'{fps} FPS' if fps is not None else '0.0 FPS' if str_resolution != '' else ''
    str_codec = f'{codec}' if codec is not None else ''
    str_frame_drop = f'Потеряно кадров:  {player.frame_drop_count}' if player.frame_drop_count is not None else ''

    # Обновление имени файла
    window['-INFO-'].update(value=folder)
    # Обновление информации о разрешении, FPS, кодеке и потерянных кадрах
    window['-MEDIA_INFO-'].update(
        '|'.join([string for string in [str_resolution, str_fps, str_codec, str_frame_drop] if string != '']))
    # Обновление кнопки ИГРАТЬ
    if duration is not None and player.pause and window['-PLAY-'] != 'ИГРАТЬ':
        window['-PLAY-'].update('ИГРАТЬ')
    # Обновление ползунка прокрутки и времени
    if duration is not None and time_pos is not None:
        window['-MEDIA_TIME-'].update(value="{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(int(time_pos), 60),
                                                                                   *divmod(int(duration), 60)))
        window['-TIME-'].update(range=(0, duration), value=time_pos)
    else:
        window['-TIME-'].update(range=(0, 0), value=0)
        window['-MEDIA_TIME-'].update(value='00:00 / 00:00')

    if not window['-LEFT_PAD-'].visible:
        if window.mouse_location()[1] < 300:
            window['-MENUBAR-'].update(visible=True)
        else:
            window['-MENUBAR-'].update(visible=False)
        if window.mouse_location()[1] > window.size[1] - 120 and window['-VID_OUT-'].get_size()[0] > window.size[0] - 1:
            window['-VID_OUT-'].set_size((window.size[0], 0))
        elif window.mouse_location()[0] > window.size[0] - 450:
            window['-VID_OUT-'].set_size((0, window.size[1]))
        else:
            window['-VID_OUT-'].set_size(window.size)

window.close()
