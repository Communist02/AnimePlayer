import os
import PySimpleGUI as sg
from mpv import MPV
import anime4k
import localization
import sys
import icons
import fonts

name_program = 'Anime Player'
version = '1.0 Release Candidate 3'
loc = localization.strings
formats = ('mp4', 'mkv', 'webm', 'avi', 'mov', 'wmv', '3gp', 'm4a', 'mp3', 'flac', 'ogg', 'aac', 'opus', 'wav')


def make_window(title: str = 'Anime Player', is_pause: bool = True, files_list: list = None, filenum: int = 0, volume: int = 100, is_files_list_visible: bool = False):
    global loc
    icon = f'{os.path.dirname(__file__) + os.sep}favicon.ico'
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
    if files_list is None:
        files_list = []
    sg.user_settings_filename(filename='AnimePlayer.json')
    sg.theme_add_new('light', light)
    sg.theme_add_new('dark', dark)
    fonts.load_font(f'{os.path.dirname(__file__) + os.sep}fonts{os.sep}BalsamiqSans-Regular.ttf')
    sg.set_options(font=(font, 10), icon=icon)
    if sg.user_settings_get_entry('darkTheme', False):
        sg.theme('dark')
    else:
        sg.theme('light')
    volume_plus = sg.user_settings_get_entry('volumePlus', False)
    localization.set_locale(sg.user_settings_get_entry('language'))
    loc = localization.strings
    tabs = []
    for quality in anime4k.qualities:
        tabs += [f'{loc["Quality"]} {quality}', [f'{loc["Mode"]} {mode}' + f'::{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]]
    tabs += [f'{loc["Quality"]} HQ', [f'{loc["Mode"]} {mode}' for mode in list(anime4k.ultra_hq_presets.keys())]]

    menu = [
        [
            loc['File'],
            [loc['Open file'] + '::-OPEN_FILE-', loc['Open URL'] + '::-OPEN_URL-',
             loc['Open folder'] + '::-OPEN_FOLDER-',
             loc['Close'] + '::-CLOSE-', '---', loc['Settings'] + '::-SETTINGS-', '---', loc['Exit'] + '::-EXIT-']
        ],
        [
            loc['Playback'],
            [
                loc['Play | Pause'] + '::-TAB_PLAY-',
                loc['Playback speed'],
                ['x0.25', 'x0.5', 'x0.75', 'x1.0', 'x1.25', 'x1.5', 'x1.75', 'x2.0', 'x2.25', 'x2.5', 'x2.75', 'x3.0'],
                loc['Take a screenshot'] + '::-SCREENSHOT-',
                '---', loc['Fullscreen'] + '::-TAB_FS-'
            ]
        ],
        [
            loc['Increasing image quality'], [loc['Disable'] + '::-DISABLE-', '---'] + tabs
        ],
        [
            loc['Other'], [loc['Reference'] + '::-REFERENCE-', loc['Create config for Android'] + '::-ANDROID_CONFIG-', loc['About'] + '::-ABOUT-']
        ]
    ]

    right_click_menu = [
        '&Right',
        [
            loc['Open file'] + '::-OPEN_FILE-', loc['Open URL'] + '::-OPEN_URL-',
            loc['Open folder'] + '::-OPEN_FOLDER-',
            loc['Close'] + '::-CLOSE-',
            '---',
            loc['Settings'] + '::-SETTINGS-',
            '---',
            loc['Play | Pause'] + '::-TAB_PLAY-',
            loc['Playback speed'],
            ['x0.25', 'x0.5', 'x0.75', 'x1.0', 'x1.25', 'x1.5', 'x1.75', 'x2.0', 'x2.25', 'x2.5', 'x2.75', 'x3.0'],
            loc['Take a screenshot'] + '::-SCREENSHOT-',
            loc['Fullscreen'] + '::-TAB_FS-',
            '---',
            loc['Increasing image quality'], [loc['Disable'] + '::-DISABLE-', '---'] + tabs,
            loc['Other'], [loc['Reference'] + '::-REFERENCE-', loc['Create config for Android'] + '::-ANDROID_CONFIG-', loc['About'] + '::-ABOUT-'],
            '---',
            loc['Exit'] + '::-EXIT-'
        ]
    ]

    panel = [
        [
            sg.Text('00:00', key='-CURRENT_TIME-', size=(5, 0)),
            sg.Slider(orientation='h', key='-TIME-', enable_events=True, expand_x=True, range=(0, 0), disable_number_display=True, background_color=sg.theme_button_color()[1],
                      relief=sg.RELIEF_GROOVE),
            sg.Text('00:00', key='-ALL_TIME-', size=(5, 0)),
        ],
        [
            sg.Col([], expand_x=True, pad=(0, 0)),
            sg.Col([
                [
                    sg.ButtonMenu(key='-SUB-', menu_def=['', []], image_source=icons.sub, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Subtitles'], button_text=''),
                    sg.ButtonMenu(key='-AUDIO-', menu_def=['', []], image_source=icons.audio, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Soundtrack'], button_text=''),
                    sg.Button(key='-FS-', image_source=icons.fullscreen, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Fullscreen']),
                    sg.Button(key='-PREV-', image_source=icons.prev, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Previous file']),
                    sg.Button(key='-PLAY-', image_data=icons.play if is_pause else icons.pause, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Play']),
                    sg.Button(key='-NEXT-', image_source=icons.next, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Next file']),
                    sg.Button(key='-MENU-', image_source=icons.menu, button_color=sg.theme_background_color(), border_width=0, tooltip=loc['Menu']),
                    sg.Slider(orientation='h', key='-VOLUME-', default_value=volume, enable_events=True, range=(0, 100 if not volume_plus else 150), size=(14, 16), pad=((5, 5), (0, 8)),
                              tooltip=loc['Volume level'])
                ]
            ], expand_x=True, pad=(0, 0)),
        ]
    ]

    col = [
        [
            sg.Image(f'{os.path.dirname(__file__) + os.sep}images{os.sep}play-button.png', key='-VID_OUT-', subsample=3, right_click_menu=right_click_menu, expand_x=True, expand_y=True, pad=(0, 0)),
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
            sg.Listbox(values=files_list, size=(50, 1000), key='-FILELIST-', enable_events=True, horizontal_scroll=True, font=(font, 10), expand_x=True)
        ]
    ]

    layout = [
        [
            sg.Menu(menu, key='-MENUBAR-', font=(font, 10)),
            sg.Col(col, expand_x=True, expand_y=True, pad=(0, 0)),
            sg.Col(col_files, key='-LIST-', visible=is_files_list_visible)
        ]
    ]

    main_window = sg.Window(title, layout, resizable=True, finalize=True, size=(980, 540), margins=(0, 0), return_keyboard_events=True, enable_close_attempted_event=True)
    main_window['-FILELIST-'].update(set_to_index=filenum, scroll_to_index=filenum)
    main_window['-FILELIST-'].Widget.bind('<KeyPress>', 'break')
    main_window['-VID_OUT-'].bind('<Double-Button-1>', '+-double_click-')
    return main_window


window: sg.Window = make_window()
player: MPV = MPV(wid=window['-VID_OUT-'].Widget.winfo_id(), keep_open=True, profile='gpu-hq', hwdec='auto')


class Player:
    """
    Управление плеером
    """
    folder: str = ''
    filename: str = ''
    files: list = []
    filenames_only: list = []
    filenum: int = -1
    fullscreen: bool = False
    audio: dict = {}
    sub: dict = {}
    info: dict = {
        'preset': '',
        'codec': '',
        'resolution': '',
        'fps': 0,
        'frame_drop': 0
    }
    cursor_last: tuple = (0, 0)
    cursor_timer: int = 0

    @classmethod
    def list_files(cls):
        return [os.path.join(cls.folder, f) for f in os.listdir(cls.folder) if (f.split('.')[-1].lower() in formats)]

    @classmethod
    def list_filenames(cls):
        filenames = [f for f in os.listdir(cls.folder) if (f.split('.')[-1].lower() in formats)]
        return [f'{i + 1}) ' + filenames[i] for i in range(len(filenames))]

    @classmethod
    def update_tracks(cls):
        cls.audio = {}
        cls.sub = {}
        for track in player.track_list:
            if track['type'] == 'audio':
                if 'lang' in track.keys():
                    cls.audio[track['id']] = f'{track["lang"]} - {track["codec"]}'
                else:
                    cls.audio[track['id']] = track['codec']
            if track['type'] == 'sub':
                if 'lang' in track.keys():
                    cls.sub[track['id']] = f'{track["lang"]} - {track["codec"]}'
                else:
                    cls.sub[track['id']] = track['codec']
        if len(cls.audio) > 0:
            window['-AUDIO-'].update(menu_definition=['', [loc['Off'] + '::0'] + [f'{key}) {value}::{key}' for key, value in cls.audio.items()]])
        else:
            window['-AUDIO-'].update(menu_definition=['', []])
        if len(cls.sub) > 0:
            window['-SUB-'].update(menu_definition=['', [loc['Off'] + '::0'] + [f'{key}) {value}::{key}' for key, value in cls.sub.items()]])
        else:
            window['-SUB-'].update(menu_definition=['', []])

    @classmethod
    def update_info(cls, no_update_fps=False):
        duration = player.duration
        time_pos = player.time_pos
        Player.info['codec'] = player.video_format if player.video_format is not None else player.audio_codec_name
        Player.info['resolution'] = (player.width, player.height)
        if no_update_fps:
            Player.info['fps'] = player.estimated_vf_fps
        Player.info['frame_drop'] = player.frame_drop_count

        str_info = {
            'preset': Player.info['preset'],
            'codec': f'{Player.info["codec"].upper()}' if Player.info["codec"] is not None else '',
            'resolution': f'{Player.info["resolution"][0]}x{Player.info["resolution"][1]}' if Player.info["resolution"] != (None, None) else '',
            'fps': f'{round(Player.info["fps"], 1) if Player.info["fps"] is not None else "0.0"} FPS' if Player.info["resolution"] != (None, None) else '',
            'frame_drop': f'{loc["Frames lost"]}: {Player.info["frame_drop"]}' if Player.info["frame_drop"] is not None else ''
        }

        # Обновление информации о разрешении, FPS, кодеке и потерянных кадрах
        window['-MEDIA_INFO-'].update(' | '.join([string for string in str_info.values() if string != '']))
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

    @classmethod
    def update_fullscreen_layout(cls):
        # if window.mouse_location()[1] < 300:
        #     window['-MENUBAR-'].update(visible=True)
        # else:
        #     window['-MENUBAR-'].update(visible=False)
        if window.mouse_location()[1] > window.size[1] - 120 and window['-VID_OUT-'].get_size()[0] > window.size[0] - 1:
            window['-VID_OUT-'].set_size((window.size[0], 0))
        elif window.mouse_location()[0] > window.size[0] - 465:
            window['-VID_OUT-'].set_size((0, window.size[1]))
        else:
            window['-VID_OUT-'].set_size(window.size)

        if window.mouse_location() != cls.cursor_last:
            window['-VID_OUT-'].Widget.config(cursor='arrow')
            cls.cursor_last = window.mouse_location()
            cls.cursor_timer = 0
        elif window['-VID_OUT-'].get_size() == window.size:
            cls.cursor_timer += 1
            if cls.cursor_timer > 10:
                window['-VID_OUT-'].Widget.config(cursor='none')

    @classmethod
    def play_file(cls, file: str, timeout=3, position: float = 0):
        player.play(file)
        try:
            player.wait_for_property('duration', lambda val: val is not None, timeout=timeout)
        except TimeoutError:
            pass
        else:
            if position > 0:
                cls.new_position(position, slider_update=True)
        finally:
            cls.update_tracks()

    @classmethod
    def play(cls):
        """Воспроизведение / Пауза"""
        if cls.filename != '':
            if player.duration is None:
                Player.play_file(cls.filename)
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
        """Переход к следующему файлу"""
        if cls.filenum < len(cls.files) - 1:
            cls.filenum += 1
            cls.filename = cls.files[cls.filenum]
            window['-FILELIST-'].update(set_to_index=cls.filenum, scroll_to_index=cls.filenum)
            window.set_title(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
            Player.play_file(cls.filename)

    @classmethod
    def prev(cls):
        """Переход к предыдущему файлу"""
        if cls.filenum > 0:
            cls.filenum -= 1
            cls.filename = cls.files[cls.filenum]
            window['-FILELIST-'].update(set_to_index=cls.filenum, scroll_to_index=cls.filenum)
            window.set_title(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
            Player.play_file(cls.filename)
        else:
            cls.filenum = 0
            window['-FILELIST-'].update(set_to_index=cls.filenum, scroll_to_index=cls.filenum)
            window.set_title(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')

    @classmethod
    def open_file(cls, file: str, pause: bool = False, position: float = 0):
        """
        Открытие файла
        :param file: путь к файлу
        :param pause: должна ли стоять пауза после открытия
        :param position: позиция
        """
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
        cls.filename = file
        window['-FILELIST-'].update(values=cls.filenames_only, set_to_index=cls.filenum, scroll_to_index=cls.filenum)
        window['-INFO-'].update(value=cls.folder)
        window.set_title(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
        Player.play_file(cls.filename, position=position)
        sg.user_settings_set_entry('opened', ['file', file])

    @classmethod
    def open_url(cls, link: str, pause: bool = False, position: float = 0):
        """
        Открытие с помощью URL-адреса
        :param link: URL-адрес
        :param pause: должна ли стоять пауза после открытия
        :param position: позиция
        """
        player.stop()
        player.pause = pause
        if pause:
            window['-PLAY-'].update(image_data=icons.play)
        else:
            window['-PLAY-'].update(image_data=icons.pause)
        cls.folder = 'URL'
        cls.files = [link]
        cls.filenames_only = []
        cls.filenum = 0
        cls.filename = link
        window['-FILELIST-'].update(values=cls.files, set_to_index=cls.filenum, scroll_to_index=cls.filenum)
        window['-INFO-'].update(value=cls.folder)
        window.set_title(f'{cls.filename.rsplit("/", 1)[-1]} - {name_program}')
        Player.play_file(cls.filename, position=position, timeout=5)
        sg.user_settings_set_entry('opened', ['url', link])

    @classmethod
    def open_folder(cls, folder: str, pause: bool = True, file: str = '', position: float = 0):
        """
        Открытие папки
        :param file:
        :param folder: путь к папке
        :param pause: должна ли стоять пауза после открытия
        :param file: полное имя файла
        :param position: позиция
        """
        cls.folder = folder.replace('/', os.sep)
        player.stop()
        player.pause = pause
        if pause:
            window['-PLAY-'].update(image_data=icons.play)
        else:
            window['-PLAY-'].update(image_data=icons.pause)
        cls.files = cls.list_files()
        cls.filenames_only = cls.list_filenames()
        if file != '' and os.path.exists(file):
            cls.filenum = cls.files.index(file)
        else:
            cls.filenum = 0
        if len(cls.files) != 0:
            cls.filename = cls.files[cls.filenum]
            window.set_title(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
            Player.play_file(cls.filename, position=position)
        else:
            cls.filename = ''
            window.set_title(name_program)
        window['-FILELIST-'].update(values=cls.filenames_only, set_to_index=cls.filenum, scroll_to_index=cls.filenum)
        window['-LIST-'].update(visible=True)
        window['-INFO-'].update(value=cls.folder)
        sg.user_settings_set_entry('opened', ['folder', folder])

    @classmethod
    def close(cls):
        """
        Закрытие открытых фалов и переход в изначальное состояние
        """
        player.stop()
        player.pause = False
        window['-PLAY-'].update(image_data=icons.play)
        cls.folder = ''
        cls.filename = ''
        cls.files = []
        cls.filenames_only = []
        cls.filenum = -1
        window['-FILELIST-'].update(values=[])
        window['-INFO-'].update(value=loc['Information'])
        window['-AUDIO-'].update(menu_definition=['', []])
        window.set_title(name_program)
        sg.user_settings_set_entry('opened', ['', ''])

    @classmethod
    def update_filelist(cls, file_name_in_list: str):
        """
        Обновление списка файлов
        :param file_name_in_list: Имя файла в списке файлов (вместе с номером)
        """
        if len(cls.filenames_only) >= 1:
            if len(cls.filenames_only) > 1 or len(file_name_in_list) > 1 and file_name_in_list[1] == ')':
                filename_temp = os.path.join(cls.folder, file_name_in_list.split(' ', 1)[-1])
                if cls.filename != filename_temp or cls.filenum < 0:
                    cls.filename = filename_temp
                    cls.filenum = cls.files.index(cls.filename)
                    Player.play_file(cls.filename)
                    window.set_title(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')

    @classmethod
    def fullscreen_switch(cls):
        """
        Переключение полноэкранного режима
        """
        if not cls.fullscreen:
            cls.fullscreen = True
            window.TKroot.attributes('-fullscreen', True)
            window['-VID_OUT-'].set_size(window.size)
            window['-MENUBAR-'].update(visible=False)
            window['-VID_OUT-'].Widget.config(cursor='none')
        else:
            cls.fullscreen = False
            window.TKroot.attributes('-fullscreen', False)
            window['-VID_OUT-'].set_size((0, 0))
            window['-MENUBAR-'].update(visible=True)
            window['-VID_OUT-'].Widget.config(cursor='arrow')

    @staticmethod
    def new_position(position: float, slider_update: bool = False):
        """
        Установка новой позиции
        :param position: позиция
        :param slider_update: обновлять ли слайдер
        """
        if player.duration is not None:
            player.time_pos = position
            window['-CURRENT_TIME-'].update(value='{:02d}:{:02d}'.format(*divmod(int(player.time_pos), 60)))
            window['-ALL_TIME-'].update(value='{:02d}:{:02d}'.format(*divmod(int(player.duration), 60)))
            if slider_update:
                window['-TIME-'].update(range=(0, player.duration), value=player.time_pos)

    @staticmethod
    def volume_update(volume: int):
        """Изменение громкости"""
        player.volume = volume
        sg.user_settings_set_entry('volume', volume)

    @classmethod
    def save_parameters(cls):
        """Сохранение текущего открытого файла и позиции"""
        file = cls.filename
        position = player.time_pos
        sg.user_settings_set_entry('file', file)
        if position is not None and position >= 10:
            sg.user_settings_set_entry('position', position)
        else:
            sg.user_settings_set_entry('position', None)

    @classmethod
    def configuration(cls, open_prev: bool = True):
        """
        Начальная настройка плеера
        :param open_prev: открывать ли предыдущий файл
        """
        try:
            volume = sg.user_settings_get_entry('volume')
            opened = sg.user_settings_get_entry('opened')
            file = sg.user_settings_get_entry('file')
            position = sg.user_settings_get_entry('position')
            open_last = sg.user_settings_get_entry('onOpenLastFile')
            on_pos_last_file = sg.user_settings_get_entry('onPosLastFile')
            svp = sg.user_settings_get_entry('SVP')
            if on_pos_last_file is not None and not on_pos_last_file or position is None:
                position = 0
            if volume is not None:
                player.volume = volume
                window['-VOLUME-'].update(value=volume)
            if opened is not None and open_prev and (open_last is None or open_last):
                match opened[0]:
                    case 'file':
                        if os.path.exists(opened[1]):
                            cls.open_file(opened[1], pause=True, position=position)
                    case 'url':
                        if on_pos_last_file is None or on_pos_last_file:
                            cls.open_url(opened[1], pause=True, position=position)
                    case 'folder':
                        if os.path.exists(opened[1]):
                            cls.open_folder(opened[1], pause=True, file=file, position=position)
            if svp is not None and svp:
                player.input_ipc_server = 'mpvpipe'
                player.hwdec = 'auto-copy'
                player.hwdec_codecs = 'all'
                player.hr_seek_framedrop = False
        except ValueError:
            sg.user_settings_delete_entry('opened')
            sg.user_settings_delete_entry('file')
            sg.user_settings_delete_entry('position')

    @classmethod
    def start_player(cls, args: list):
        """
        Начальные действия при открытии плеера
        :param args: аргументы командной строки
        """
        if len(args) > 1:
            cls.configuration(open_prev=False)
            if os.path.isfile(args[1]):
                file = sg.user_settings_get_entry('opened')[1]
                position = sg.user_settings_get_entry('position')

                if file is not None and file == args[1] and position is not None:
                    cls.open_file(args[1], position=position)
                else:
                    cls.open_file(args[1])
            elif os.path.isdir(args[1]):
                cls.open_folder(args[1])
        else:
            cls.configuration(open_prev=True)


def main():
    global window
    screenshot_path = ''
    modes = []
    for quality in anime4k.qualities:
        modes += [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]

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
            case sg.WIN_CLOSED | '-EXIT-' | sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
                Player.save_parameters()
                break
            case '-VOLUME-':
                Player.volume_update(values['-VOLUME-'])
            case '-TIME-':
                Player.new_position(values['-TIME-'])
            case '-NEXT-':
                Player.next()
            case '-PREV-':
                Player.prev()
            case '-PLAY-' | '-TAB_PLAY-' | ' ':
                Player.play()
            case '-FS-' | '-TAB_FS-' | 'F11:122' | '-VID_OUT-+-double_click-':
                Player.fullscreen_switch()
            case '-SUB-':
                player.sid = values['-SUB-'].rsplit(':', 1)[1]
            case '-AUDIO-':
                player.aid = values['-AUDIO-'].rsplit(':', 1)[1]
            case '-MENU-':
                if not window['-LIST-'].visible:
                    window['-LIST-'].update(visible=True)
                else:
                    window['-LIST-'].update(visible=False)
            case '-FILELIST-':
                Player.update_filelist(values['-FILELIST-'][0])
            # ------------------ Клавиатура ------------------
            case 'Right:39':
                if player.time_pos is not None:
                    player.seek(5)
            case 'Left:37':
                if player.time_pos is not None:
                    if player.time_pos > 5:
                        player.seek(-5)
                    else:
                        player.time_pos = 0
            case 'Up:38':
                if player.volume > 95 and window['-VOLUME-'].Range[1] == 100:
                    player.volume = 100
                elif player.volume > 145 and window['-VOLUME-'].Range[1] == 150:
                    player.volume = 150
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
                if Player.fullscreen:
                    Player.fullscreen_switch()
            # ----------------- Верхнее меню -----------------
            case '-OPEN_FILE-':
                new_file = sg.popup_get_file(loc['Choose file'], no_window=True, file_types=((loc['All supported files'], ' '.join(['.' + f for f in formats])),))
                if new_file is not None and new_file != '':
                    Player.open_file(new_file)
            case '-OPEN_URL-':
                links_history = sg.user_settings_get_entry('linksHistory', [])
                new_link = ''
                open_url_layout = [
                    [sg.Text(loc['Enter the URL'])],
                    [sg.Combo(links_history, size=(35, 10), key='-INPUT-'), sg.Button(loc['Paste'], key='-PASTE-'), sg.Button(loc['Clear'], key='-CLEAR-')],
                    [sg.Button('OK', size=(6, 1)), sg.Button(loc['Cancel'], size=(6, 1))]
                ]
                open_url_window = sg.Window(loc['Opening a link'], open_url_layout, modal=True)
                while True:
                    event, values = open_url_window.read()
                    if event == sg.WINDOW_CLOSED or event == loc['Cancel']:
                        break
                    elif event == '-PASTE-':
                        open_url_window['-INPUT-'].update(sg.clipboard_get())
                    elif event == 'OK':
                        new_link = values['-INPUT-'].strip()
                        break
                    elif event == '-CLEAR-':
                        links_history = []
                        open_url_window['-INPUT-'].update(value='', values=[])
                        sg.user_settings_set_entry('linksHistory', [])
                open_url_window.close()
                if new_link is not None and new_link != '':
                    if links_history.count(new_link) > 0:
                        links_history.remove(new_link)
                    links_history.insert(0, new_link)
                    sg.user_settings_set_entry('linksHistory', links_history)
                    Player.open_url(new_link)
            case '-OPEN_FOLDER-':
                folders_history = sg.user_settings_get_entry('foldersHistory', [])
                new_folder = ''
                open_folder_layout = [
                    [
                        sg.Text(loc['Select a folder'])
                    ],
                    [
                        sg.Combo(folders_history, size=(35, 10), key='-INPUT-'),
                        sg.Button(loc['Select'], key='-BROWSE-'),
                        sg.Button(loc['Paste'], key='-PASTE-'),
                        sg.Button(loc['Clear'], key='-CLEAR-')
                    ],
                    [
                        sg.Button('OK', size=(6, 1)), sg.Button(loc['Cancel'], size=(6, 1))
                    ]
                ]
                open_folder_window = sg.Window(loc['Opening a folder'], open_folder_layout, modal=True)
                while True:
                    event, values = open_folder_window.read()
                    if event == sg.WINDOW_CLOSED or event == loc['Cancel']:
                        break
                    elif event == '-PASTE-':
                        open_folder_window['-INPUT-'].update(sg.clipboard_get())
                    elif event == 'OK':
                        new_folder = values['-INPUT-'].strip()
                        break
                    elif event == '-CLEAR-':
                        folders_history = []
                        open_folder_window['-INPUT-'].update(value='', values=[])
                        sg.user_settings_set_entry('foldersHistory', [])
                    elif event == '-BROWSE-':
                        path = sg.popup_get_folder(loc['Select a folder'], no_window=True).replace('/', os.sep)
                        if path != '':
                            open_folder_window['-INPUT-'].update(value=path)
                        pass
                open_folder_window.close()
                if new_folder is not None and new_folder != '':
                    if folders_history.count(new_folder) > 0:
                        folders_history.remove(new_folder)
                    folders_history.insert(0, new_folder)
                    sg.user_settings_set_entry('foldersHistory', folders_history)
                    Player.open_folder(new_folder)
            case '-CLOSE-':
                Player.close()
            case 'x0.25' | 'x0.5' | 'x0.75' | 'x1.0' | 'x1.25' | 'x1.5' | 'x1.75' | 'x2.0' | 'x2.25' | 'x2.5' | 'x2.75' | 'x3.0':
                player.speed = float(event[1:])
            case '-DISABLE-':
                anime4k.current_preset = ''
                player.glsl_shaders = ''
            case '-ABOUT-':
                sg.popup(f'Anime Player v{version}\n\n{loc["About program"]}\n\nCopyright © 2023 MazurDev', title=loc['About'])
            case '-REFERENCE-':
                if loc['lang'] == 'Русский':
                    reference_file_name = 'GLSL_Instructions_Advanced_ru.txt'
                else:
                    reference_file_name = 'GLSL_Instructions_Advanced.txt'
                with open(f'{os.path.dirname(__file__) + os.sep}doc{os.sep}{reference_file_name}', 'r',
                          encoding='utf-8') as ref_data:
                    reference = ref_data.read()
                    sg.popup_scrolled(reference, size=(180, 0), title=loc['Reference'], font=('Consolas', 11))
            case '-ANDROID_CONFIG-':
                config_layout = [
                    [sg.Text(loc['You can use this config to use the Anime4K algorithm in the mpv video player on android'])],
                    [sg.Text(loc['Enter the path to the shaders'])],
                    [sg.Input('/storage/emulated/0/mpv/shaders/')],
                    [sg.Text(loc['Select the algorithm configuration'])],
                    [sg.Combo(modes, readonly=True)],
                    [sg.Button(loc['Selected']), sg.Button(loc['All'])]
                ]
                config_windows = sg.Window(loc['Create config for Android'], config_layout, resizable=True, size=(500, 200), modal=True)
                while True:
                    event, values = config_windows.read()
                    if event == sg.WINDOW_CLOSED:
                        break
                    elif event == loc['Selected'] and values[1] != '':
                        quality = values[1].replace(')', '').split('(')[1]
                        mode = values[1].split(' ')[1]
                        sg.popup_scrolled(f'# {values[1]}\n' + anime4k.android_config(anime4k.create_preset(quality, mode), values[0]), title=values[1])
                    elif event == loc['All']:
                        mods = []
                        for mod in modes:
                            quality = mod.replace(')', '').split('(')[1]
                            mode = mod.split(' ')[1]
                            mods.append(f'# {mod}\n' + '# ' + anime4k.android_config(anime4k.create_preset(quality, mode), values[0]))
                        sg.popup_scrolled('\n\n'.join(mods), title='Все')
                config_windows.close()
            case '-SETTINGS-':
                match sg.user_settings_get_entry('language'):
                    case 'Русский':
                        lang = 'Русский'
                    case 'English':
                        lang = 'English'
                    case _:
                        lang = 'Auto'
                settings_layout = [
                    [
                        sg.Text(loc['Language selection']),
                        sg.Combo(['Auto', 'Русский', 'English'], readonly=True, default_value=lang, key='-LANGUAGE-')
                    ],
                    [
                        sg.Checkbox(loc['On startup, open the last opened file'], key='-OPEN_LAST_FILE-', default=sg.user_settings_get_entry('onOpenLastFile', True))
                    ],
                    [
                        sg.Checkbox(loc['Set the position of the last opened file'], key='-POS_LAST_FILE-', default=sg.user_settings_get_entry('onPosLastFile', True))
                    ],
                    [
                        sg.Checkbox(loc['Increase maximum volume up to 150%'], key='-VOLUME_PLUS-', default=sg.user_settings_get_entry('volumePlus', False))
                    ],
                    [
                        sg.Checkbox(loc['Activate SVP'], key='-SVP-', default=sg.user_settings_get_entry('SVP', False))
                    ],
                    [
                        sg.Checkbox(loc['Dark theme'], key='-DARK_THEME-', default=sg.user_settings_get_entry('darkTheme', False))
                    ],
                    [
                        sg.OK(size=(6, 1)), sg.Button(loc['Cancel'], key='-CANCEL-', size=(6, 1))
                    ]
                ]
                settings_windows = sg.Window(loc['Settings'], settings_layout, modal=True)
                while True:
                    event, values = settings_windows.read()
                    match event:
                        case sg.WINDOW_CLOSED | '-CANCEL-':
                            break
                        case 'OK':
                            sg.user_settings_set_entry('onOpenLastFile', values['-OPEN_LAST_FILE-'])
                            sg.user_settings_set_entry('onPosLastFile', values['-POS_LAST_FILE-'])
                            sg.user_settings_set_entry('SVP', values['-SVP-'])

                            if sg.user_settings_get_entry('volumePlus', lang) != values['-VOLUME_PLUS-']:
                                if not values['-VOLUME_PLUS-'] and player.volume > 100:
                                    player.volume = 100
                                    window['-VOLUME-'].update(value=100)
                                window['-VOLUME-'].update(range=(0, 100 if not values['-VOLUME_PLUS-'] else 150))
                                sg.user_settings_set_entry('volumePlus', values['-VOLUME_PLUS-'])

                            if sg.user_settings_get_entry('language', lang) != values['-LANGUAGE-'] or sg.user_settings_get_entry('darkTheme', False) != values['-DARK_THEME-']:
                                sg.user_settings_set_entry('language', values['-LANGUAGE-'])
                                sg.user_settings_set_entry('darkTheme', values['-DARK_THEME-'])
                                player.wid = -1
                                player.vo = 'null'
                                player.vo = ''
                                window.close()
                                window = make_window(title=f'{player.filename.rsplit("/", 1)[-1]} - {name_program}' if player.filename is not None or '' else name_program,
                                                     is_pause=player.pause if player.duration is not None else True, files_list=window['-FILELIST-'].get_list_values(), filenum=Player.filenum,
                                                     volume=player.volume, is_files_list_visible=window['-LIST-'].visible)
                                player.wid = window['-VID_OUT-'].Widget.winfo_id()
                                player.vo = 'null'
                                player.vo = ''
                                Player.update_tracks()

                            if values['-SVP-']:
                                if player.input_ipc_server != 'mpvpipe':
                                    player.input_ipc_server = 'mpvpipe'
                                    player.hwdec = 'auto-copy'
                                    player.hwdec_codecs = 'all'
                                    player.hr_seek_framedrop = False
                            else:
                                player.input_ipc_server = ''
                                player.hwdec = 'auto'
                                player.hr_seek_framedrop = True
                            break
                settings_windows.close()
            case '-SCREENSHOT-':
                open_url_layout = [
                    [
                        sg.Text(loc['Enter folder path for screenshots'])
                    ],
                    [
                        sg.Input(screenshot_path, size=(35, 10), key='-INPUT-'),
                        sg.Button(loc['Select'], key='-BROWSE-'),
                        sg.Button(loc['Paste'], key='-PASTE-')
                    ],
                    [
                        sg.Button(loc['Take a screenshot'], key='-TAKE_SCREENSHOT-'),
                        sg.Button(loc['Close'])
                    ]
                ]
                open_screenshot_window = sg.Window(loc['Screenshot'], open_url_layout, modal=True)
                while True:
                    event, values = open_screenshot_window.read()
                    if event == sg.WINDOW_CLOSED or event == loc['Close']:
                        screenshot_path = values['-INPUT-'].strip()
                        break
                    elif event == '-PASTE-':
                        open_screenshot_window['-INPUT-'].update(sg.clipboard_get())
                    elif event == '-TAKE_SCREENSHOT-':
                        screenshot_path = values['-INPUT-'].strip()
                        if screenshot_path is not None and screenshot_path != '':
                            player.screenshot_directory = screenshot_path
                            player.screenshot_jpeg_quality = 100
                            try:
                                player.screenshot()
                                break
                            except SystemError:
                                sg.popup_error('Error path')
                    elif event == '-BROWSE-':
                        path = sg.popup_get_folder(loc['Select a folder'], no_window=True).replace('/', os.sep)
                        if path != '':
                            open_screenshot_window['-INPUT-'].update(value=path)
                        pass
                open_screenshot_window.close()
            case _:
                if event in [f'{loc["Mode"]} {mode}' for mode in anime4k.ultra_hq_presets.keys()]:
                    player.glsl_shaders = anime4k.to_string(anime4k.ultra_hq_presets[event.split(' ', 1)[-1]], event + ' (HQ)')
                    Player.info['preset'] = anime4k.current_preset
                elif event in modes:
                    quality = event.replace(')', '').split('(')[1]
                    mode = event.split(' ')[1]
                    player.glsl_shaders = anime4k.to_string(anime4k.create_preset(quality, mode), event)
                    Player.info['preset'] = anime4k.current_preset

        Player.update_info(event not in ('-TIME-', 'Right:39', 'Left:37'))

        if Player.fullscreen:
            Player.update_fullscreen_layout()

    window.close()


main()
