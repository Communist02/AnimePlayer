import os
import PySimpleGUI as sg
import mpv
import anime4k
import localization
import sys
import icons
import fonts

icon = f'{os.path.dirname(__file__) + os.sep}favicon.ico'
formats = ('mp4', 'mkv', 'webm', 'avi', 'mov', 'wmv', '3gp', 'm4a', 'mp3', 'flac', 'ogg', 'aac', 'opus', 'wav')
version = '0.3.1 Alpha'
font = 'Balsamiq Sans Regular'
light = {
    'BACKGROUND': '#f5f1eb',
    'TEXT': '#575656',
    'INPUT': '#ebe3d7',
    'TEXT_INPUT': '#575656',
    'SCROLL': '#ebe3d7',
    'BUTTON': ('#ebe3d7', '#575656'),
    'PROGRESS': ('#ebe3d7', '#beab98'),
    'BORDER': 1,
    'SLIDER_DEPTH': 1,
    'PROGRESS_DEPTH': 1
}
dark = {
    'BACKGROUND': '#1b1c1e',
    'TEXT': '#e3e3e3',
    'INPUT': '#202328',
    'TEXT_INPUT': '#c4c7c5',
    'SCROLL': '#28292a',
    'BUTTON': ('#c2e7ff', '#42474d'),
    'PROGRESS': ('#505f69', '#32414b'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}
sg.theme_add_new('light', light)
sg.theme_add_new('dark', dark)
fonts.load_font(f'{os.path.dirname(__file__) + os.sep}fonts{os.sep}BalsamiqSans-Regular.ttf')
sg.set_options(font=(font, 10), icon=icon)
sg.user_settings_filename(filename='AnimePlayer.json')
if sg.user_settings_get_entry('darkTheme') is not None and sg.user_settings_get_entry('darkTheme'):
    sg.theme('dark')
    icons.set_grey_color()
else:
    sg.theme('light')
    icons.set_grey_color()
localization.set_locale(sg.user_settings_get_entry('language'))
loc = localization.strings


modes = []
for quality in anime4k.qualities:
    modes += [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]
tabs = []
for quality in anime4k.qualities:
    tabs += [f'{loc["Quality"]} {quality}',
             [f'{loc["Mode"]} {mode}' + f'::{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]]
tabs += [f'{loc["Quality"]} HQ', [f'{loc["Mode"]} {mode}' for mode in list(anime4k.ultra_hq_presets.keys())]]

menu = [
    [
        loc['File'],
        [loc['Open file'] + '::-OPEN_FILE-', loc['Open URL'] + '::-OPEN_URL-', loc['Open folder'] + '::-OPEN_FOLDER-',
         loc['Close'] + '::-CLOSE-', '---', loc['Settings'] + '::-SETTINGS-', '---', loc['Exit'] + '::-EXIT-']
    ],
    [
        loc['Playback'], [loc['Play | Pause'] + '::-TAB_PLAY-', '---', loc['Fullscreen'] + '::-TAB_FS-']
    ],
    [
        loc['Increasing image quality'], [loc['Disable'] + '::-DISABLE-', '---'] + tabs
    ],
    [
        loc['Other'], [loc['Reference'] + '::-REFERENCE-', loc['Activate SVP'] + '::-SVP-',
                       loc['Create config for Android'] + '::-ANDROID_CONFIG-', loc['About'] + '::-ABOUT-']
    ]
]

right_click_menu = [
    '&Right',
    [
        loc['Open file'] + '::-OPEN_FILE-', loc['Open URL'] + '::-OPEN_URL-', loc['Open folder'] + '::-OPEN_FOLDER-',
        loc['Close'] + '::-CLOSE-',
        '---',
        loc['Settings'] + '::-SETTINGS-',
        '---',
        loc['Play | Pause'] + '::-TAB_PLAY-', loc['Fullscreen'] + '::-TAB_FS-',
        '---',
        loc['Increasing image quality'], [loc['Disable'] + '::-DISABLE-', '---'] + tabs,
        loc['Other'], [loc['Reference'] + '::-REFERENCE-', loc['Activate SVP'] + '::-SVP-',
                       loc['Create config for Android'] + '::-ANDROID_CONFIG-', loc['About'] + '::-ABOUT-'],
        '---',
        loc['Exit'] + '::-EXIT-'
    ]
]

panel = [
    [
        sg.Text('00:00', key='-CURRENT_TIME-', size=(5, 0)),
        sg.Slider(orientation='h', key='-TIME-', enable_events=True, expand_x=True, range=(0, 0),
                  disable_number_display=True, background_color=sg.theme_button_color()[1], relief=sg.RELIEF_GROOVE),
        sg.Text('00:00', key='-ALL_TIME-', size=(5, 0)),
    ],
    [
        sg.Col([], expand_x=True, pad=(0, 0)),
        sg.Col([[
            sg.Button(key='-FS-', image_data=icons.fullscreen, button_color=sg.theme_background_color(),
                      border_width=0, tooltip=loc['Fullscreen']),
            sg.Button(key='-MENU-', image_data=icons.menu, button_color=sg.theme_background_color(), border_width=0,
                      tooltip=loc['Menu']),
            sg.Button(key='-PREV-', image_data=icons.prev, button_color=sg.theme_background_color(), border_width=0,
                      tooltip=loc['Previous file']),
            sg.Button(key='-PLAY-', image_data=icons.play, button_color=sg.theme_background_color(), border_width=0,
                      tooltip=loc['Play']),
            sg.Button(key='-NEXT-', image_data=icons.next, button_color=sg.theme_background_color(), border_width=0,
                      tooltip=loc['Next file']),
            sg.Slider(orientation='h', key='-VOLUME-', default_value=100, enable_events=True, range=(0, 100),
                      size=(12, 16), pad=((5, 5), (0, 8)), tooltip=loc['Sound level'])
        ]], expand_x=True, pad=(0, 0)),
    ]
]

col = [
    [
        sg.Image(key='-LEFT_PAD-', pad=(2, 0)),
        sg.Image(f'{os.path.dirname(__file__) + os.sep}image{os.sep}play-button.png', key='-VID_OUT-', subsample=3,
                 right_click_menu=right_click_menu, expand_x=True, expand_y=True, pad=(0, 0)),
        sg.Image(key='-RIGHT_PAD-', pad=(2, 0))
    ],
    [
        sg.Frame('', key='-PANEL-', layout=panel, expand_x=True)
    ]
]

col_files = [
    [
        sg.Frame(loc['Information'], key='-INFO-', layout=[[sg.Text('', key='-MEDIA_INFO-')]], expand_x=True)
    ],
    [
        sg.Listbox(values=[], size=(50, 1000), key='-FILELIST-', enable_events=True, horizontal_scroll=True,
                   font=(font, 10), expand_x=True)
    ]
]

layout = [
    [
        sg.Menu(menu, key='-MENUBAR-', font=(font, 10)),
        sg.Col(col, expand_x=True, expand_y=True, pad=(0, 0)),
        sg.Col(col_files, key='-LIST-', visible=False)
    ]
]

window = sg.Window('Anime Player', layout, resizable=True, finalize=True, size=(980, 540), margins=(0, 0),
                   return_keyboard_events=True, enable_close_attempted_event=True)
window['-FILELIST-'].Widget.bind('<KeyPress>', 'break')
window['-VID_OUT-'].bind('<Double-Button-1>', '+-double_click-')

player: mpv.MPV = mpv.MPV(wid=window['-VID_OUT-'].Widget.winfo_id(), keep_open=True, profile='gpu-hq', scale='spline64',
                          cscale='spline64')


class Player:
    folder = ''
    filename = ''
    files = []
    filenames_only = []
    filenum = -1

    @classmethod
    def list_files(cls):
        return [os.path.join(cls.folder, f) for f in os.listdir(cls.folder) if (f.split('.')[-1].lower() in formats)]

    @classmethod
    def list_filenames(cls):
        filenames = [f for f in os.listdir(cls.folder) if (f.split('.')[-1].lower() in formats)]
        return [f'{i + 1}) ' + filenames[i] for i in range(len(filenames))]

    @classmethod
    def play(cls):
        if cls.filename != '':
            if player.duration is None:
                player.play(cls.filename)
                player.pause = False
                window['-PLAY-'].update(image_data=icons.pause)
            elif not player.pause:
                player.pause = True
                window['-PLAY-'].update(image_data=icons.play)
            else:
                player.pause = False
                window['-PLAY-'].update(image_data=icons.pause)

    @classmethod
    def next(cls):
        print(1)
        if cls.filenum < len(cls.files) - 1:
            cls.filenum += 1
            cls.filename = cls.files[cls.filenum]
            window['-FILELIST-'].update(set_to_index=cls.filenum, scroll_to_index=cls.filenum)
            player.play(cls.filename)

    @classmethod
    def prev(cls):
        if cls.filenum > 0:
            cls.filenum -= 1
            cls.filename = cls.files[cls.filenum]
            window['-FILELIST-'].update(set_to_index=cls.filenum, scroll_to_index=cls.filenum)
            player.play(cls.filename)
        else:
            cls.filenum = 0
            window['-FILELIST-'].update(set_to_index=cls.filenum, scroll_to_index=cls.filenum)

    @classmethod
    def open_file(cls, file, pause=False):
        file = file.replace('/', os.sep)
        player.stop()
        player.pause = pause
        if pause:
            window['-PLAY-'].update(image_data=icons.play)
        else:
            window['-PLAY-'].update(image_data=icons.pause)
        cls.folder = file.rsplit(os.sep, 1)[0]
        cls.files = [file]
        cls.filenames_only = [file.split(os.sep)[-1]]
        cls.filenum = 0
        cls.filename = file.rsplit(os.sep, 1)[-1]
        window['-FILELIST-'].update(values=cls.filenames_only)
        window['-INFO-'].update(value=cls.folder)
        player.play(file)
        sg.user_settings_set_entry('opened', ['file', file])

    @classmethod
    def open_url(cls, link, pause=False):
        player.stop()
        player.pause = pause
        if pause:
            window['-PLAY-'].update(image_data=icons.play)
        else:
            window['-PLAY-'].update(image_data=icons.pause)
        cls.folder = 'Ссылка'
        cls.files = [link]
        cls.filenames_only = []
        cls.filenum = 0
        cls.filename = link
        window['-FILELIST-'].update(values=cls.files)
        window['-INFO-'].update(value=cls.folder)
        player.play(link)
        sg.user_settings_set_entry('opened', ['url', link])

    @classmethod
    def open_folder(cls, folder, pause=True):
        cls.folder = folder.replace('/', os.sep)
        player.stop()
        player.pause = pause
        if pause:
            window['-PLAY-'].update(image_data=icons.play)
        else:
            window['-PLAY-'].update(image_data=icons.pause)
        cls.files = cls.list_files()
        cls.filenames_only = cls.list_filenames()
        cls.filenum = -1
        if len(cls.files) != 0:
            cls.filename = cls.files[0]
        else:
            cls.filename = ''
        window['-FILELIST-'].update(values=cls.filenames_only)
        window['-LIST-'].update(visible=True)
        window['-INFO-'].update(value=cls.folder)
        sg.user_settings_set_entry('opened', ['folder', folder])

    @classmethod
    def close(cls):
        player.stop()
        player.pause = False
        window['-PLAY-'].update(image_data=icons.play)
        cls.folder = ''
        cls.filename = ''
        cls.files = []
        cls.filenames_only = []
        cls.filenum = -1
        window['-FILELIST-'].update(values=cls.filenames_only)
        window['-INFO-'].update(value=cls.folder)
        sg.user_settings_set_entry('opened', ['', ''])

    @classmethod
    def update_filelist(cls):
        if len(cls.filenames_only) >= 1:
            if len(cls.filenames_only) > 1 or len(values['-FILELIST-'][0]) > 1 and values['-FILELIST-'][0][1] == ')':
                filename_temp = os.path.join(cls.folder, values['-FILELIST-'][0].split(' ', 1)[-1])
                if cls.filename != filename_temp or cls.filenum < 0:
                    cls.filename = filename_temp
                    cls.filenum = cls.files.index(cls.filename)
                    player.play(cls.filename)

    @staticmethod
    def fullscreen():
        # Взял window['-LEFT_PAD-'].visible как значение по которому ориентируюсь включен ли полноэкранный режим
        if window['-LEFT_PAD-'].visible:
            window.TKroot.attributes('-fullscreen', True)
            window['-VID_OUT-'].set_size(window.size)
            window['-MENUBAR-'].update(visible=False)
            window['-LEFT_PAD-'].update(visible=False)
            window['-RIGHT_PAD-'].update(visible=False)
        else:
            window.TKroot.attributes('-fullscreen', False)
            window['-VID_OUT-'].set_size((0, 0))
            window['-PANEL-'].update(visible=True)
            window['-MENUBAR-'].update(visible=True)
            window['-VID_OUT-'].update(visible=False)
            window['-LEFT_PAD-'].update(visible=True)
            window['-VID_OUT-'].update(visible=True)
            window['-RIGHT_PAD-'].update(visible=True)

    @staticmethod
    def new_position(position, slider_update=False):
        if player.duration is not None:
            player.time_pos = position
            window['-CURRENT_TIME-'].update(value='{:02d}:{:02d}'.format(*divmod(int(player.time_pos), 60)))
            window['-ALL_TIME-'].update(value='{:02d}:{:02d}'.format(*divmod(int(player.duration), 60)))
            if slider_update:
                window['-TIME-'].update(range=(0, player.duration), value=player.time_pos)

    @staticmethod
    def volume_update():
        player.volume = values['-VOLUME-']
        sg.user_settings_set_entry('volume', values['-VOLUME-'])

    @classmethod
    def save_parameters(cls):
        file = cls.filename
        position = player.time_pos
        sg.user_settings_set_entry('file', file)
        if position is not None and position >= 10:
            sg.user_settings_set_entry('position', position)
        else:
            sg.user_settings_set_entry('position', None)

    @classmethod
    def position_recovery(cls, position):
        if position is not None:
            try:
                player.wait_for_property('duration', lambda val: val is not None, timeout=3)
            except TimeoutError:
                pass
            else:
                cls.new_position(position, slider_update=True)

    @classmethod
    def configuration(cls, open_prev=True):
        volume = sg.user_settings_get_entry('volume')
        opened = sg.user_settings_get_entry('opened')
        file = sg.user_settings_get_entry('file')
        position = sg.user_settings_get_entry('position')
        open_last = sg.user_settings_get_entry('openLastFile')
        if volume is not None:
            player.volume = volume
            window['-VOLUME-'].update(value=volume)
        if opened is not None and open_prev and (open_last is None or open_last):
            match opened[0]:
                case 'file':
                    if os.path.exists(opened[1]):
                        cls.open_file(opened[1], pause=True)
                        cls.position_recovery(position)
                case 'url':
                    cls.open_url(opened[1], pause=True)
                    cls.position_recovery(position)
                case 'folder':
                    if os.path.exists(opened[1]):
                        cls.open_folder(opened[1], pause=True)
                        if file is not None and os.path.exists(file):
                            cls.filename = file
                            cls.filenum = cls.files.index(cls.filename)
                            player.play(cls.filename)
                            cls.position_recovery(position)

    @classmethod
    def start_player(cls, args):
        if len(args) > 1:
            cls.configuration(open_prev=False)
            if os.path.isfile(args[1]):
                file = sg.user_settings_get_entry('opened')[1]
                position = sg.user_settings_get_entry('position')
                cls.open_file(args[1])
                if file is not None and file == args[1] and position is not None:
                    cls.position_recovery(position)
            elif os.path.isdir(args[1]):
                cls.open_folder(args[1])
        else:
            cls.configuration(open_prev=True)


Player.start_player(sys.argv)

while True:
    event, values = window.read(timeout=100)
    if event is None:
        break
    else:
        event = event.split('::', 1)[-1]
    # --------------------- Кнопки ---------------------
    match event:
        case '__TIMEOUT__':
            pass
        case (sg.WIN_CLOSED | '-EXIT-' | sg.WINDOW_CLOSE_ATTEMPTED_EVENT):
            Player.save_parameters()
            break
        case '-VOLUME-':
            Player.volume_update()
        case '-TIME-':
            Player.new_position(values['-TIME-'])
        case '-NEXT-':
            Player.next()
        case '-PREV-':
            Player.prev()
        case ('-PLAY-' | '-TAB_PLAY-' | ' '):
            Player.play()
        case ('-FS-' | '-TAB_FS-' | 'F11:122' | '-VID_OUT-+-double_click-'):
            Player.fullscreen()
        case '-MENU-':
            if not window['-LIST-'].visible:
                window['-LIST-'].update(visible=True)
            else:
                window['-LIST-'].update(visible=False)
        case '-SVP-':
            if player.input_ipc_server != 'mpvpipe':
                player.input_ipc_server = 'mpvpipe'
                player.hwdec = 'auto-copy'
                player.hwdec_codecs = 'all'
                player.hr_seek_framedrop = False
        case '-FILELIST-':
            Player.update_filelist()
        # ------------------ Клавиатура ------------------
        case 'Right:39':
            if player.time_pos is not None:
                player.time_pos += 5
        case 'Left:37':
            if player.time_pos is not None:
                if player.time_pos > 5:
                    player.time_pos -= 5
                else:
                    player.time_pos = 0
        case 'Up:38':
            if player.volume > 95:
                player.volume = 100
            else:
                player.volume += 5
            window['-VOLUME-'].update(value=player.volume)
        case 'Down:40':
            if player.volume < 5:
                player.volume = 0
            else:
                player.volume -= 5
            window['-VOLUME-'].update(value=player.volume)
        case 'Escape:27':
            if not window['-LEFT_PAD-'].visible:
                Player.fullscreen()
        # ----------------- Верхнее меню -----------------
        case '-OPEN_FILE-':
            new_file = sg.popup_get_file('Выберите файл', no_window=True, file_types=(
                ('Все поддерживаемые файлы', ' '.join(['.' + f for f in formats])),))
            if new_file != '' and new_file is not None:
                Player.open_file(new_file)
        case '-OPEN_URL-':
            new_link = sg.popup_get_text('Введите URL-адрес', title='Ввод ссылки', size=(30, 40))
            if new_link != '' and new_link is not None:
                Player.open_url(new_link)
        case '-OPEN_FOLDER-':
            new_folder = sg.popup_get_folder('Выберите папку с медиа', title='Выбор папки', history=True, size=(30, 40))
            if new_folder != '' and new_folder is not None:
                Player.open_folder(new_folder)
        case '-CLOSE-':
            Player.close()
        case '-DISABLE-':
            anime4k.current_preset = ''
            player.glsl_shaders = ''
        case '-ABOUT-':
            sg.popup(f'Anime Player v{version}\n\n{loc["About program"]}\n\nCopyright © 2023 MazurDev',
                     title=loc['About'])
        case '-REFERENCE-':
            with open(f'{os.path.dirname(__file__) + os.sep}doc{os.sep}GLSL_Instructions_Advanced_ru.txt', 'r',
                      encoding='utf-8') as ref_data:
                reference = ref_data.read()
                sg.popup_scrolled(reference, size=(180, 0), title=loc['Reference'], font=('Consolas', 11))
        case '-ANDROID_CONFIG-':
            config_layout = [
                [sg.Text(
                    'Этот конфиг вы можете использовать для использования алгоритма Anime4K в видеоплеере mpv на андроид')],
                [sg.Text('Введите путь до шейдеров')],
                [sg.Input('/storage/emulated/0/mpv/shaders/')],
                [sg.Text('Выберите конфигурацию алгоритма')],
                [sg.Combo(modes, readonly=True)],
                [sg.OK(size=(6, 1)), sg.Button('Все', size=(6, 1))]
            ]
            config_windows = sg.Window(loc['Create config for Android'], config_layout, resizable=True, size=(500, 200),
                                       modal=True)
            while True:
                event, values = config_windows.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == 'OK' and values[1] != '':
                    quality = values[1].replace(')', '').split('(')[1]
                    mode = values[1].split(' ')[1]
                    sg.popup_scrolled(
                        f'# {values[1]}\n' + anime4k.android_config(anime4k.create_preset(quality, mode), values[0]),
                        title=values[1])
                elif event == 'Все':
                    mods = []
                    for mod in modes:
                        quality = mod.replace(')', '').split('(')[1]
                        mode = mod.split(' ')[1]
                        mods.append(
                            f'# {mod}\n' + '# ' + anime4k.android_config(anime4k.create_preset(quality, mode),
                                                                         values[0]))
                    sg.popup_scrolled('\n\n'.join(mods), title='Все')
            config_windows.close()
        case '-SETTINGS-':
            open_last_file = sg.user_settings_get_entry('openLastFile') is None or sg.user_settings_get_entry(
                'openLastFile')
            match sg.user_settings_get_entry('language'):
                case 'Русский':
                    lang = 'Русский'
                case 'English':
                    lang = 'English'
                case _:
                    lang = 'Auto'
            settings_layout = [
                [sg.Text('Выбор языка (требуется перезагрузка)'),
                 sg.Combo(['Auto', 'Русский', 'English'], readonly=True, default_value=lang, key='-LANGUAGE-')],
                [sg.Checkbox('При запуске открывать последний открытый файл', key='-OPEN_LAST_FILE-',
                             default=open_last_file)],
                # [sg.Checkbox('Устанавливать позицию последнего открытого файла')],
                [sg.Checkbox('Темная тема (требуется перезагрузка)', key='-DARK_THEME-',
                             default=sg.user_settings_get_entry('darkTheme'))],
                [sg.OK(size=(6, 1)), sg.Button('Отмена', size=(6, 1))]
            ]
            settings_windows = sg.Window(loc['Settings'], settings_layout, modal=True)
            while True:
                event, values = settings_windows.read()
                if event == sg.WINDOW_CLOSED or event == 'Отмена':
                    break
                elif event == 'OK':
                    sg.user_settings_set_entry('language', values['-LANGUAGE-'])
                    sg.user_settings_set_entry('openLastFile', values['-OPEN_LAST_FILE-'])
                    sg.user_settings_set_entry('darkTheme', values['-DARK_THEME-'])
                    break
            settings_windows.close()
        case _:
            if event in [f'{loc["Mode"]} {mode}' for mode in anime4k.ultra_hq_presets.keys()]:
                player.glsl_shaders = anime4k.to_string(anime4k.ultra_hq_presets[event.split(' ', 1)[-1]],
                                                        event + ' (HQ)')
            elif event in modes:
                quality = event.replace(')', '').split('(')[1]
                mode = event.split(' ')[1]
                player.glsl_shaders = anime4k.to_string(anime4k.create_preset(quality, mode), event)

    duration = player.duration
    time_pos = player.time_pos
    codec = player.video_format if player.video_format is not None else player.audio_codec_name
    fps = round(player.estimated_vf_fps, 1) if player.estimated_vf_fps is not None else None
    str_resolution = f'{player.width}x{player.height}' if player.width is not None else ''
    str_fps = f'{fps} FPS' if fps is not None else '0.0 FPS' if str_resolution != '' else ''
    str_codec = f'{codec.upper()}' if codec is not None else ''
    str_frame_drop = f'{loc["Frames lost"]}: {player.frame_drop_count}' if player.frame_drop_count is not None else ''

    # Обновление информации о разрешении, FPS, кодеке и потерянных кадрах
    window['-MEDIA_INFO-'].update(' | '.join(
        [string for string in [anime4k.current_preset, str_codec, str_resolution, str_fps, str_frame_drop] if
         string != '']
    ))
    # Обновление кнопки ИГРАТЬ
    if duration is not None and player.pause:
        window['-PLAY-'].update(image_data=icons.play)
    # Обновление ползунка прокрутки и времени
    if duration is not None and time_pos is not None:
        window['-CURRENT_TIME-'].update(value='{:02d}:{:02d}'.format(*divmod(int(time_pos), 60)))
        window['-ALL_TIME-'].update(value='{:02d}:{:02d}'.format(*divmod(int(duration), 60)))
        window['-TIME-'].update(range=(0, duration), value=time_pos)
    else:
        window['-TIME-'].update(range=(0, 0), value=0)
        window['-CURRENT_TIME-'].update(value='00:00')
        window['-ALL_TIME-'].update(value='00:00')

    if not window['-LEFT_PAD-'].visible:
        # if window.mouse_location()[1] < 300:
        #     window['-MENUBAR-'].update(visible=True)
        # else:
        #     window['-MENUBAR-'].update(visible=False)
        if window.mouse_location()[1] > window.size[1] - 120 and window['-VID_OUT-'].get_size()[0] > window.size[0] - 1:
            window['-VID_OUT-'].set_size((window.size[0], 0))
        elif window.mouse_location()[0] > window.size[0] - 450:
            window['-VID_OUT-'].set_size((0, window.size[1]))
        else:
            window['-VID_OUT-'].set_size(window.size)

window.close()
