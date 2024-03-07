from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QIcon, QGuiApplication, QAction, QPixmap
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMenu, QFileDialog

import main_window
import open_folder_window
import open_url_window
import settings_window
import about_window
import screenshot_window
import reference_window
import launch_parameters_window
import android_config_window

import os
from mpv import MPV
import anime4k
import localization
import sys
import icons
from config import ConfigManager

name_program = 'Anime Player'
version = '2.0 Beta 2'
formats = ('mp4', 'mkv', 'webm', 'avi', 'mov', 'wmv', '3gp', 'm4a', 'mp3', 'flac', 'ogg', 'aac', 'opus', 'wav')

config = ConfigManager('config.json')
localization.set_locale(config.get('language'))
loc = localization.strings


class AndroidConfigWindow(QDialog):
    def __init__(self):
        super(AndroidConfigWindow, self).__init__()
        self.ui = android_config_window.Ui_AndroidConfigWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.setWindowTitle(loc['Create config for Android'])
        self.ui.label.setText(loc['You can use this config to use the Anime4K algorithm in the mpv video player on android'])
        self.ui.label_2.setText(loc['Enter the path to the shaders'])
        self.ui.label_3.setText(loc['Select the algorithm configuration'])
        self.ui.selected.setText(loc['Selected'])
        self.ui.all.setText(loc['All'])

        self.ui.selected.clicked.connect(self.selected)
        self.ui.all.clicked.connect(self.all)

        self.modes = []
        for quality in anime4k.qualities:
            self.modes += [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]

        self.ui.comboBox.addItems(self.modes)

    def selected(self):
        quality = self.ui.comboBox.currentText().replace(')', '').split('(')[1]
        mode = self.ui.comboBox.currentText().split(' ')[1]
        self.ui.plainTextEdit.setPlainText(f'# {self.ui.comboBox.currentText()}\n' + anime4k.android_config(anime4k.create_preset(quality, mode), self.ui.lineEdit.text()))

    def all(self):
        mods = []
        for mod in self.modes:
            quality = mod.replace(')', '').split('(')[1]
            mode = mod.split(' ')[1]
            mods.append(f'# {mod}\n' + '# ' + anime4k.android_config(anime4k.create_preset(quality, mode), self.ui.lineEdit.text()))
        self.ui.plainTextEdit.setPlainText('\n\n'.join(mods))


class LaunchParametersWindow(QDialog):
    def __init__(self):
        super(LaunchParametersWindow, self).__init__()
        self.ui = launch_parameters_window.Ui_LaunchParemetersWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.setWindowTitle(loc['Launch parameters'])
        self.ui.label.setText(loc['Manual launch parameters'])
        self.ui.buttonBox.buttons()[0].setText(loc['Save'])
        self.ui.buttonBox.buttons()[1].setText(loc['Cancel'])
        self.ui.buttonBox.buttons()[2].setText(loc['Apply'])

        self.ui.plainTextEdit.setPlainText(config.get('launchParameters', ''))

        self.ui.buttonBox.buttons()[0].clicked.connect(self.save)
        self.ui.buttonBox.buttons()[2].clicked.connect(self.apply)

    def save(self):
        config.set('launchParameters', self.ui.plainTextEdit.toPlainText())

    def apply(self):
        try:
            exec(self.ui.plainTextEdit.toPlainText())
            config.set('launchParameters', self.ui.plainTextEdit.toPlainText())
            Player.volume_update(player.volume)
            self.setWindowTitle(loc['Success'])
        except Exception:
            self.setWindowTitle(loc['Error'])


class ReferenceWindow(QDialog):
    def __init__(self):
        super(ReferenceWindow, self).__init__()
        self.ui = reference_window.Ui_ReferenceWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.setWindowTitle(loc['Reference'])
        self.ui.buttonBox.buttons()[0].setText(loc['Close'])

        if loc['lang'] == 'Русский':
            reference_file_name = 'GLSL_Instructions_Advanced_ru.txt'
        else:
            reference_file_name = 'GLSL_Instructions_Advanced.txt'

        with open(f'{os.path.dirname(__file__) + os.sep}doc{os.sep}{reference_file_name}', 'r', encoding='utf-8') as ref_data:
            reference = ref_data.read()
            self.ui.plainTextEdit.setPlainText(reference)


class ScreenshotWindow(QDialog):
    def __init__(self):
        super(ScreenshotWindow, self).__init__()
        self.ui = screenshot_window.Ui_ScreenshotWindow()
        self.ui.setupUi(self)

        self.setFixedSize(520, 120)
        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.ui.lineEdit.setText(screenshot_path)

        self.setWindowTitle(loc['Screenshot'])
        self.ui.label.setText(loc['Enter folder path for screenshots'])
        self.ui.select.setText(loc['Select'])
        self.ui.paste.setText(loc['Paste'])

        self.ui.paste.clicked.connect(lambda: self.ui.lineEdit.setText(QGuiApplication.clipboard().text()))
        self.ui.select.clicked.connect(self.select)
        self.ui.buttonBox.accepted.connect(self.save)

    def select(self):
        folder_name = QFileDialog.getExistingDirectory()
        if folder_name is not None and folder_name != '':
            self.ui.lineEdit.setText(folder_name)

    def save(self):
        global screenshot_path
        screenshot_path = self.ui.lineEdit.text().strip()
        if screenshot_path is not None and screenshot_path != '':
            player.screenshot_directory = screenshot_path
            player.screenshot_jpeg_quality = 100
            try:
                player.screenshot()
            except SystemError:
                self.ui.label.setText(loc['Error'])


class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = about_window.Ui_AboutWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))
        self.ui.image.setPixmap(QPixmap(f'{os.path.dirname(__file__) + os.sep}images{os.sep}anime-player-icon.png'))

        self.setWindowTitle(loc['About'])
        self.ui.label_2.setText(f'Anime Player v{version}')
        self.ui.label_3.setText(loc['About program'])
        self.ui.buttonBox.buttons()[0].setText(loc['Close'])


class SettingsWindow(QDialog):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = settings_window.Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.setFixedHeight(220)
        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        match config.get('language'):
            case 'Русский':
                self.lang = 'Русский'
            case 'English':
                self.lang = 'English'
            case _:
                self.lang = 'Auto'

        self.ui.language.setCurrentText(self.lang)
        self.ui.openLastFile.setChecked(config.get('onOpenLastFile', True))
        self.ui.posLastFile.setChecked(config.get('onPosLastFile', True))
        self.ui.volumePlus.setChecked(config.get('volumePlus', False))
        self.ui.svp.setChecked(config.get('SVP', False))
        self.ui.darkTheme.setChecked(config.get('darkTheme', False))

        self.ui.darkTheme.setVisible(False)

        self.ui.buttonBox.accepted.connect(self.ok)

        self.setWindowTitle(loc['Settings'])
        self.ui.label.setText(loc['Language selection'])
        self.ui.openLastFile.setText(loc['On startup open the last opened file'])
        self.ui.posLastFile.setText(loc['Set the position of the last opened file'])
        self.ui.volumePlus.setText(loc['Increase maximum volume up to 150%'])
        self.ui.svp.setText(loc['Activate SVP'])
        self.ui.buttonBox.buttons()[1].setText(loc['Cancel'])

    def ok(self):
        config.set('onOpenLastFile', self.ui.openLastFile.isChecked())
        config.set('onPosLastFile', self.ui.posLastFile.isChecked())
        config.set('SVP', self.ui.svp.isChecked())
        config.set('volumePlus', self.ui.volumePlus.isChecked())

        if config.get('volumePlus', False) != self.ui.volumePlus.isChecked():
            if not self.ui.volumePlus.isChecked() and player.volume > 100:
                player.volume = 100
                # window['-VOLUME-'].update(value=100)
            # window['-VOLUME-'].update(range=(0, 100 if not values['-VOLUME_PLUS-'] else 150))
            config.set('volumePlus', self.ui.volumePlus.isChecked())

        if config.get('language', self.lang) != self.ui.language.currentText() or config.get('darkTheme', False) != self.ui.darkTheme.isChecked():
            config.set('language', self.ui.language.currentText())
            config.set('darkTheme', self.ui.darkTheme.isChecked())
            # player.wid = -1
            # player.vo = 'null'
            # player.vo = ''
            # window.close()
            # window = make_window(title=f'{player.filename.rsplit("/", 1)[-1]} - {name_program}' if player.filename is not None or '' else name_program,
            #                      is_pause=player.pause if player.duration is not None else True, files_list=window['-FILELIST-'].get_list_values(), filenum=Player.filenum,
            #                      volume=player.volume, is_files_list_visible=window['-LIST-'].visible)
            # player.wid = window['-VID_OUT-'].Widget.winfo_id()
            # player.vo = 'null'
            # player.vo = ''
            # Player.update_tracks()

        if self.ui.svp.isChecked():
            if player.input_ipc_server != 'mpvpipe':
                player.input_ipc_server = 'mpvpipe'
                player.hwdec = 'auto-copy'
                player.hwdec_codecs = 'all'
                player.hr_seek_framedrop = False
        else:
            player.input_ipc_server = ''
            player.hwdec = 'auto'
            player.hr_seek_framedrop = True


class OpenURLWindow(QDialog):
    def __init__(self):
        super(OpenURLWindow, self).__init__()
        self.ui = open_url_window.Ui_OpenURLWindow()
        self.ui.setupUi(self)

        self.setFixedSize(550, 120)
        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.links_history = config.get('linksHistory', [])

        self.ui.comboBox.addItems(self.links_history)

        self.ui.paste.clicked.connect(lambda: self.ui.comboBox.setCurrentText(QGuiApplication.clipboard().text()))
        self.ui.clear.clicked.connect(self.clear)
        self.ui.buttonBox.accepted.connect(self.ok)

        self.setWindowTitle(loc['Opening a link'])
        self.ui.label.setText(loc['Enter the URL'])
        self.ui.paste.setText(loc['Paste'])
        self.ui.clear.setText(loc['Clear'])
        self.ui.buttonBox.buttons()[1].setText(loc['Cancel'])

    def clear(self):
        self.links_history = []
        self.ui.comboBox.clear()
        self.ui.comboBox.clearEditText()
        config.set('linksHistory', [])

    def ok(self):
        new_link = self.ui.comboBox.currentText().strip()
        if new_link is not None and new_link != '':
            if self.links_history.count(new_link) > 0:
                self.links_history.remove(new_link)
            self.links_history.insert(0, new_link)
            config.set('linksHistory', self.links_history)
            Player.open_url(new_link)


class OpenFolderWindow(QDialog):
    def __init__(self):
        super(OpenFolderWindow, self).__init__()
        self.ui = open_folder_window.Ui_OpenFolderWindow()
        self.ui.setupUi(self)

        self.setFixedSize(550, 120)
        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.folders_history = config.get('foldersHistory', [])

        self.ui.comboBox.addItems(self.folders_history)

        self.ui.paste.clicked.connect(lambda: self.ui.comboBox.setCurrentText(QGuiApplication.clipboard().text()))
        self.ui.clear.clicked.connect(self.clear)
        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.select.clicked.connect(self.select)

        self.setWindowTitle(loc['Opening a folder'])
        self.ui.label.setText(loc['Select a folder'])
        self.ui.select.setText(loc['Select'])
        self.ui.paste.setText(loc['Paste'])
        self.ui.clear.setText(loc['Clear'])
        self.ui.buttonBox.buttons()[1].setText(loc['Cancel'])

    def clear(self):
        self.folders_history = []
        self.ui.comboBox.clear()
        self.ui.comboBox.clearEditText()
        config.set('foldersHistory', [])

    def ok(self):
        new_folder = self.ui.comboBox.currentText().strip()
        if new_folder is not None and new_folder != '':
            if self.folders_history.count(new_folder) > 0:
                self.folders_history.remove(new_folder)
            self.folders_history.insert(0, new_folder)
            config.set('foldersHistory', self.folders_history)
            Player.open_folder(new_folder)

    def select(self):
        folder_name = QFileDialog.getExistingDirectory()
        if folder_name is not None and folder_name != '':
            self.ui.comboBox.setCurrentText(folder_name)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.menu_audio = QMenu(self.ui.centralwidget)
        self.ui.audio.setMenu(self.menu_audio)

        self.sub_audio = QMenu(self.ui.centralwidget)
        self.ui.sub.setMenu(self.sub_audio)

        self.ui.rightPanel.setVisible(False)

        self.ui.play.setIcon(QIcon(icons.play))
        self.ui.prev.setIcon(QIcon(icons.prev))
        self.ui.next.setIcon(QIcon(icons.next))
        self.ui.fullscreen.setIcon(QIcon(icons.fullscreen))
        self.ui.audio.setIcon(QIcon(icons.audio))
        self.ui.sub.setIcon(QIcon(icons.sub))
        self.ui.menu.setIcon(QIcon(icons.menu))
        self.ui.video.setPixmap(QPixmap(f'{os.path.dirname(__file__) + os.sep}images{os.sep}play-button.png'))

        self.ui.play.clicked.connect(lambda: Player.play())
        self.ui.prev.clicked.connect(lambda: Player.prev())
        self.ui.next.clicked.connect(lambda: Player.next())
        self.ui.fullscreen.clicked.connect(lambda: Player.fullscreen_switch())
        self.ui.menu.clicked.connect(self.right_panel_visible)
        self.ui.volume.valueChanged.connect(lambda: Player.volume_update(self.ui.volume.value()))
        self.ui.time.valueChanged.connect(lambda: self.change_time())

        self.ui.video.setMouseTracking(True)
        self.ui.controlPanel.setMouseTracking(True)
        self.setMouseTracking(True)
        self.centralWidget().setMouseTracking(True)

        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start()

        self.ui.fileList.clicked.connect(lambda: Player.update_filelist(self.ui.fileList.currentItem().text()))

        # Верхнее меню
        self.ui.action_Exit.triggered.connect(lambda: self.close())
        self.ui.action_Close.triggered.connect(lambda: Player.close())
        self.ui.action_Open_file.triggered.connect(self.open_file)
        self.ui.action_Open_folder.triggered.connect(self.open_folder)
        self.ui.action_Open_URL.triggered.connect(self.open_url)
        self.ui.action_Settings.triggered.connect(self.settings)
        self.ui.action_Reference.triggered.connect(self.reference)
        self.ui.action_Launch_parameters.triggered.connect(self.launch_parameters)
        self.ui.action_Create_config_Android.triggered.connect(self.android_config)
        self.ui.action_Fullscreen.triggered.connect(lambda: Player.fullscreen_switch())
        self.ui.action_Play_Pause.triggered.connect(lambda: Player.play())
        self.ui.action_Disable.triggered.connect(lambda: Player.disable_anime4k())
        self.ui.action_Volume_plus.triggered.connect(self.volume_plus)
        self.ui.action_Volume_minus.triggered.connect(self.volume_minus)
        self.ui.action_Rewind_plus.triggered.connect(self.rewind_plus)
        self.ui.action_Rewind_minus.triggered.connect(self.rewind_minus)
        self.ui.action_About.triggered.connect(self.about)
        self.ui.action_Playlist.triggered.connect(self.right_panel_visible)
        self.ui.action_Take_a_screenshot.triggered.connect(self.screenshot)
        self.ui.action_Zoom_in.triggered.connect(lambda: self.zoom(0.01))
        self.ui.action_Zoom_out.triggered.connect(lambda: self.zoom(-0.01))

        self.ui.action_x025.triggered.connect(lambda: self.speed(0.25))
        self.ui.action_x05.triggered.connect(lambda: self.speed(0.5))
        self.ui.action_x075.triggered.connect(lambda: self.speed(0.75))
        self.ui.action_x10.triggered.connect(lambda: self.speed(1.0))
        self.ui.action_x125.triggered.connect(lambda: self.speed(1.25))
        self.ui.action_x15.triggered.connect(lambda: self.speed(1.5))
        self.ui.action_x175.triggered.connect(lambda: self.speed(1.75))
        self.ui.action_x20.triggered.connect(lambda: self.speed(2.0))
        self.ui.action_x225.triggered.connect(lambda: self.speed(2.25))
        self.ui.action_x25.triggered.connect(lambda: self.speed(2.5))
        self.ui.action_x275.triggered.connect(lambda: self.speed(2.75))
        self.ui.action_x30.triggered.connect(lambda: self.speed(3.0))

        self.ui.action_Settings.setText(loc['Settings'])
        self.ui.menu_File.setTitle(loc['File'])
        self.ui.action_Open_file.setText(loc['Open file'])
        self.ui.action_Open_URL.setText(loc['Open URL'])
        self.ui.action_Open_folder.setText(loc['Open folder'])
        self.ui.action_Close.setText(loc['Close'])
        self.ui.action_Exit.setText(loc['Exit'])
        self.ui.menu_Playback.setTitle(loc['Playback'])
        self.ui.action_Play_Pause.setText(loc['Play | Pause'])
        self.ui.action_Fullscreen.setText(loc['Fullscreen'])
        self.ui.menu_Increasing_image_quality.setTitle(loc['Increasing image quality'])
        self.ui.action_Disable.setText(loc['Disable'])
        self.ui.menu_Other.setTitle(loc['Other'])
        self.ui.action_About.setText(loc['About'])
        self.ui.action_Launch_parameters.setText(loc['Launch parameters'])
        self.ui.action_Take_a_screenshot.setText(loc['Take a screenshot'])
        self.ui.action_Create_config_Android.setText(loc['Create config for Android'])
        self.ui.action_Reference.setText(loc['Reference'])
        self.ui.menu_Playback_speed.setTitle(loc['Playback speed'])
        self.ui.action_Volume_plus.setText(loc['Volume +10'])
        self.ui.action_Volume_minus.setText(loc['Volume -10'])
        self.ui.action_Rewind_plus.setText(loc['Rewind +5 sec'])
        self.ui.action_Rewind_minus.setText(loc['Rewind -5 sec'])
        self.ui.action_Zoom_in.setText(loc['Zoom in'])
        self.ui.action_Zoom_out.setText(loc['Zoom out'])
        self.ui.action_Playlist.setText(loc['Playlist'])
        self.ui.sourceInfo.setText(loc['Information'])

        modes = []
        for quality in anime4k.qualities:
            modes += [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]

        tabs = {}
        for quality in anime4k.qualities:
            if f'{loc["Quality"]} {quality}' not in tabs.keys():
                tabs[f'{loc["Quality"]} {quality}'] = []
            tabs[f'{loc["Quality"]} {quality}'] += [f'{loc["Mode"]} {mode}' for mode in anime4k.modes]
        tabs[f'{loc["Quality"]} HQ'] = [f'{loc["Mode"]} {mode}' for mode in list(anime4k.ultra_hq_presets.keys())]

        for quality in tabs.keys():
            menu = QMenu(self.menuBar())
            menu.setTitle(quality)
            self.ui.menu_Increasing_image_quality.addMenu(menu)
            for mode in tabs[quality]:
                action = QAction(self)
                action.setText(mode)
                action.triggered.connect(lambda q=quality, m=mode: Player.set_preset_quality(q, m))
                menu.addAction(action)

        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        self.setAcceptDrops(True)

    def mouseMoveEvent(self, event):
        if Player.fullscreen:
            Player.update_fullscreen_layout(event.position().x(), event.position().y())

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            Player.open_file(file_name)
            break

    def mouseDoubleClickEvent(self, event):
        Player.fullscreen_switch()

    def screenshot(self):
        screenshot_win = ScreenshotWindow()
        screenshot_win.setModal(True)
        screenshot_win.exec()

    def zoom(self, value):
        player.video_zoom += value

    def speed(self, speed):
        player.speed = speed

    def timer_update(self):
        Player.update_info()
        Player.update_cursor()

    def change_time(self):
        if player.time_pos is not None and int(player.time_pos) != self.ui.time.value():
            Player.new_position(self.ui.time.value())

    def closeEvent(self, event):
        Player.save_parameters()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self, filter=loc['All supported files'] + ' (' + ' '.join(['*.' + f for f in formats]) + ')')
        if file_name[0] is not None and file_name[0] != '':
            Player.open_file(file_name[0])

    def open_folder(self):
        open_folder_win = OpenFolderWindow()
        open_folder_win.setModal(True)
        open_folder_win.exec()

    def open_url(self):
        open_url_win = OpenURLWindow()
        open_url_win.setModal(True)
        open_url_win.exec()

    def settings(self):
        settings_win = SettingsWindow()
        settings_win.setModal(True)
        settings_win.exec()
        if not config.get('volumePlus', False):
            self.ui.volume.setValue(player.volume)
            self.ui.volume.setMaximum(100)
        else:
            self.ui.volume.setMaximum(150)

    def about(self):
        about_win = AboutWindow()
        about_win.setModal(True)
        about_win.exec()

    def reference(self):
        reference_win = ReferenceWindow()
        reference_win.setModal(True)
        reference_win.exec()

    def launch_parameters(self):
        launch_parameters_win = LaunchParametersWindow()
        launch_parameters_win.setModal(True)
        launch_parameters_win.exec()
        self.ui.volume.setValue(player.volume)

    def android_config(self):
        android_config_win = AndroidConfigWindow()
        android_config_win.setModal(True)
        android_config_win.exec()

    def right_panel_visible(self):
        if Player.fullscreen:
            Player.is_menu_visible = not Player.is_menu_visible
        else:
            self.ui.rightPanel.setVisible(not self.ui.rightPanel.isVisible())

    def show_context_menu(self, position):
        menu = QMenu(self.ui.centralwidget)
        menu.addAction(self.ui.action_Open_file)
        menu.addAction(self.ui.action_Open_folder)
        menu.addAction(self.ui.action_Open_URL)
        menu.addAction(self.ui.action_Close)
        menu.addSeparator()
        menu.addMenu(self.ui.menu_Increasing_image_quality)
        menu.addSeparator()
        menu.addAction(self.ui.action_Play_Pause)
        menu.addMenu(self.ui.menu_Playback_speed)
        menu.addAction(self.ui.action_Playlist)
        menu.addAction(self.ui.action_Zoom_in)
        menu.addAction(self.ui.action_Zoom_out)
        menu.addAction(self.ui.action_Take_a_screenshot)
        menu.addAction(self.ui.action_Fullscreen)
        menu.addSeparator()
        menu.addAction(self.ui.action_Settings)
        menu.addAction(self.ui.action_About)
        menu.addSeparator()
        menu.addAction(self.ui.action_Exit)
        menu.exec(self.ui.video.mapToGlobal(position))

    def volume_plus(self):
        if player.volume > 95 and self.ui.volume.maximum() == 100:
            player.volume = 100
        elif player.volume > 145 and self.ui.volume.maximum() == 150:
            player.volume = 150
        else:
            player.volume += 5
        self.ui.volume.setValue(player.volume)
        Player.volume_update(player.volume)

    def volume_minus(self):
        if player.volume < 5:
            player.volume = 0
        else:
            player.volume -= 5
        self.ui.volume.setValue(player.volume)
        Player.volume_update(player.volume)

    def rewind_plus(self):
        if player.time_pos is not None:
            player.seek(5)
            window.ui.time.setValue(player.time_pos)
            window.ui.currentTime.setText('{:02d}:{:02d}'.format(*divmod(int(player.time_pos), 60)))

    def rewind_minus(self):
        if player.time_pos is not None:
            if player.time_pos > 5:
                player.seek(-5)
            else:
                player.time_pos = 0
            window.ui.time.setValue(player.time_pos)
            window.ui.currentTime.setText('{:02d}:{:02d}'.format(*divmod(int(player.time_pos), 60)))


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
    is_menu_visible: bool = True
    is_maximized: bool = False
    audio: dict = {}
    sub: dict = {}
    duration: int = 0
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

        def set_sub(index: int):
            player.sid = index

        def set_audio(index: int):
            player.aid = index

        window.ui.audio.menu().clear()
        window.ui.sub.menu().clear()
        if len(cls.audio) > 0:
            action = QAction(window)
            action.setText(loc['Disable'])
            action.triggered.connect(lambda: set_audio(0))
            window.ui.audio.menu().addAction(action)
            window.ui.audio.menu().addSeparator()
            for key, value in cls.audio.items():
                action = QAction(window)
                action.setText(f'{key}) {value}')
                action.triggered.connect(lambda ignore=False, a=key: set_audio(a))
                window.ui.audio.menu().addAction(action)

        if len(cls.sub) > 0:
            action = QAction(window)
            action.setText(loc['Disable'])
            action.triggered.connect(lambda: set_sub(0))
            window.ui.sub.menu().addAction(action)
            window.ui.sub.menu().addSeparator()
            window.ui.sub.menu().addSeparator()
            for key, value in cls.sub.items():
                action = QAction(window)
                action.setText(f'{key}) {value}')
                action.triggered.connect(lambda ignore=False, x=key: set_sub(x))
                window.ui.sub.menu().addAction(action)

    @classmethod
    def update_info(cls, no_update_fps=True):
        # duration = player.duration
        time_pos = player.time_pos
        Player.info['codec'] = player.video_format if player.video_format is not None else player.audio_codec_name
        Player.info['resolution'] = (player.width, player.height)
        if no_update_fps:
            Player.info['fps'] = player.estimated_vf_fps
        Player.info['frame_drop'] = player.frame_drop_count

        # Обновление информации о разрешении, FPS, кодеке и потерянных кадрах
        str_info = {
            'preset': Player.info['preset'],
            'codec': f'{Player.info["codec"].upper()}' if Player.info["codec"] is not None else '',
            'resolution': f'{Player.info["resolution"][0]}x{Player.info["resolution"][1]}' if Player.info["resolution"] != (None, None) else '',
            'fps': f'{round(Player.info["fps"], 1) if Player.info["fps"] is not None else "0.0"} FPS' if Player.info["resolution"] != (None, None) else '',
            'frame_drop': f'{loc["Frames lost"]}: {Player.info["frame_drop"]}' if Player.info["frame_drop"] is not None else ''
        }

        window.ui.mediaInfo.setText(' | '.join([string for string in str_info.values() if string != '']))
        # Обновление кнопки ИГРАТЬ
        if player.duration is not None and player.pause:
            window.ui.play.setIcon(QIcon(icons.play))
        # Обновление ползунка прокрутки и времени

        if player.duration is not None and time_pos is not None:
            if cls.duration != player.duration:
                cls.duration = player.duration
                window.ui.time.setMaximum(cls.duration)
                window.ui.allTime.setText('{:02d}:{:02d}'.format(*divmod(int(cls.duration), 60)))

            window.ui.time.setValue(time_pos)
            window.ui.currentTime.setText('{:02d}:{:02d}'.format(*divmod(int(time_pos), 60)))
        else:
            window.ui.time.setMaximum(0)
            window.ui.time.setValue(0)
            window.ui.currentTime.setText('00:00')
            window.ui.allTime.setText('00:00')

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
                window.ui.play.setIcon(QIcon(icons.pause))
            elif not player.pause:
                player.pause = True
                window.ui.play.setIcon(QIcon(icons.play))
            else:
                player.pause = False
                window.ui.play.setIcon(QIcon(icons.pause))

    @classmethod
    def next(cls):
        """Переход к следующему файлу"""
        if cls.filenum < len(cls.files) - 1:
            cls.filenum += 1
            cls.filename = cls.files[cls.filenum]
            window.ui.fileList.setCurrentRow(cls.filenum)
            window.setWindowTitle(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
            Player.play_file(cls.filename)

    @classmethod
    def prev(cls):
        """Переход к предыдущему файлу"""
        if cls.filenum > 0:
            cls.filenum -= 1
            cls.filename = cls.files[cls.filenum]
            window.ui.fileList.setCurrentRow(cls.filenum)
            window.setWindowTitle(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
            Player.play_file(cls.filename)
        else:
            cls.filenum = 0
            window.ui.fileList.setCurrentRow(cls.filenum)
            window.setWindowTitle(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')

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
            window.ui.play.setIcon(QIcon(icons.play))
        else:
            window.ui.play.setIcon(QIcon(icons.pause))
        cls.folder = file.rsplit(os.sep, 1)[0]
        cls.files = [file]
        cls.filenames_only = [file.split(os.sep)[-1]]
        cls.filenum = 0
        cls.filename = file
        window.ui.fileList.clear()
        window.ui.fileList.addItems(cls.filenames_only)
        window.ui.fileList.setCurrentRow(cls.filenum)
        window.ui.sourceInfo.setText(cls.folder)
        window.setWindowTitle(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
        Player.play_file(cls.filename, position=position)
        config.set('opened', ['file', file])

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
            window.ui.play.setIcon(QIcon(icons.play))
        else:
            window.ui.play.setIcon(QIcon(icons.pause))
        cls.folder = 'URL'
        cls.files = [link]
        cls.filenames_only = []
        cls.filenum = 0
        cls.filename = link
        window.ui.fileList.clear()
        window.ui.fileList.addItems(cls.files)
        window.ui.fileList.setCurrentRow(cls.filenum)
        window.ui.sourceInfo.setText(cls.folder)
        window.setWindowTitle(f'{cls.filename.rsplit("/", 1)[-1]} - {name_program}')
        Player.play_file(cls.filename, position=position, timeout=5)
        config.set('opened', ['url', link])

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
            window.ui.play.setIcon(QIcon(icons.play))
        else:
            window.ui.play.setIcon(QIcon(icons.pause))
        cls.files = cls.list_files()
        cls.filenames_only = cls.list_filenames()
        if file != '' and os.path.exists(file):
            cls.filenum = cls.files.index(file)
        else:
            cls.filenum = 0
        if len(cls.files) != 0:
            cls.filename = cls.files[cls.filenum]
            window.setWindowTitle(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')
            Player.play_file(cls.filename, position=position)
        else:
            cls.filename = ''
            window.setWindowTitle(name_program)
        window.ui.fileList.clear()
        window.ui.fileList.addItems(cls.filenames_only)
        window.ui.fileList.setCurrentRow(cls.filenum)
        window.ui.rightPanel.setVisible(True)
        window.ui.sourceInfo.setText(cls.folder)
        config.set('opened', ['folder', folder])

    @classmethod
    def close(cls):
        """
        Закрытие открытых фалов и переход в изначальное состояние
        """
        player.stop()
        player.pause = False
        icon = QIcon()
        icon.addFile(icons.play, QSize(), QIcon.Normal, QIcon.Off)
        window.ui.play.setIcon(icon)
        cls.folder = ''
        cls.filename = ''
        cls.files = []
        cls.filenames_only = []
        cls.filenum = -1
        window.ui.fileList.clear()
        window.ui.sourceInfo.setText(loc['Information'])
        # window['-AUDIO-'].update(menu_definition=['', []])
        window.setWindowTitle(name_program)
        config.set('opened', ['', ''])

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
                    window.setWindowTitle(f'{cls.filename.rsplit(os.sep, 1)[-1]} - {name_program}')

    @classmethod
    def fullscreen_switch(cls):
        """
        Переключение полноэкранного режима
        """
        if not cls.fullscreen:
            cls.fullscreen = True
            cls.is_maximized = window.isMaximized()
            window.showFullScreen()
            window.ui.menubar.setFixedHeight(0)
            window.ui.controlPanel.setVisible(False)
            cls.is_menu_visible = window.ui.rightPanel.isVisible()
            window.ui.rightPanel.setVisible(False)
        else:
            cls.fullscreen = False
            if cls.is_maximized:
                window.showMaximized()
            else:
                window.showNormal()
            window.ui.menubar.setFixedHeight(22)
            window.ui.controlPanel.setVisible(True)
            window.ui.rightPanel.setVisible(cls.is_menu_visible)
            window.ui.video.unsetCursor()
            cls.cursor_timer = 0

    @classmethod
    def update_fullscreen_layout(cls, x: int, y: int):
        if y > window.ui.centralwidget.size().height() - window.ui.controlPanel.height():
            window.ui.controlPanel.setVisible(True)
        elif x > window.ui.centralwidget.size().width() - window.ui.rightPanel.width() and Player.is_menu_visible:
            window.ui.rightPanel.setVisible(True)
            pass
        else:
            window.ui.rightPanel.setVisible(False)
            window.ui.controlPanel.setVisible(False)
            pass

        window.ui.video.unsetCursor()
        cls.cursor_last = (x, y)
        cls.cursor_timer = 0

    @classmethod
    def update_cursor(cls):
        if not window.ui.controlPanel.isVisible() and not window.ui.rightPanel.isVisible():
            cls.cursor_timer += 1
            if cls.cursor_timer > 3:
                window.ui.video.setCursor(Qt.BlankCursor)

    @staticmethod
    def new_position(position: float, slider_update: bool = False):
        """
        Установка новой позиции
        :param position: позиция
        :param slider_update: обновлять ли слайдер
        """
        if player.duration is not None:
            player.time_pos = position
            window.ui.currentTime.setText('{:02d}:{:02d}'.format(*divmod(int(player.time_pos), 60)))
            window.ui.allTime.setText('{:02d}:{:02d}'.format(*divmod(int(player.duration), 60)))
            if slider_update:
                window.ui.time.setMaximum(player.duration)
                window.ui.time.setValue(player.time_pos)

    @staticmethod
    def volume_update(volume: int):
        """Изменение громкости"""
        player.volume = volume
        config.set('volume', volume)

    @classmethod
    def save_parameters(cls):
        """Сохранение текущего открытого файла и позиции"""
        file = cls.filename
        position = player.time_pos
        config.set('file', file)
        if position is not None and position >= 10:
            config.set('position', position)
        else:
            config.set('position', None)
        config.save_config()

    @classmethod
    def configuration(cls, open_prev: bool = True):
        """
        Начальная настройка плеера
        :param open_prev: открывать ли предыдущий файл
        """
        try:
            volume = config.get('volume')
            opened = config.get('opened')
            file = config.get('file')
            position = config.get('position')
            open_last = config.get('onOpenLastFile')
            on_pos_last_file = config.get('onPosLastFile')
            volume_plus = config.get('volumePlus', False)
            svp = config.get('SVP')
            launch_parameters = config.get('launchParameters')
            if on_pos_last_file is not None and not on_pos_last_file or position is None:
                position = 0
            if volume is not None:
                player.volume = volume
                window.ui.volume.setValue(volume)
            if volume_plus:
                window.ui.volume.setMaximum(150)
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
            if launch_parameters is not None and launch_parameters != '':
                try:
                    exec(launch_parameters)
                    window.ui.volume.setValue(player.volume)
                    config.set('volume', player.volume)
                except Exception:
                    pass
        except ValueError:
            config.delete('opened')
            config.delete('file')
            config.delete('position')

    @classmethod
    def start_player(cls, args: list):
        """
        Начальные действия при открытии плеера
        :param args: аргументы командной строки
        """
        if len(args) > 1:
            cls.configuration(open_prev=False)
            if os.path.isfile(args[1]):
                file = config.get('opened')[1]
                position = config.get('position')

                if file is not None and file == args[1] and position is not None:
                    cls.open_file(args[1], position=position)
                else:
                    cls.open_file(args[1])
            elif os.path.isdir(args[1]):
                cls.open_folder(args[1])
        else:
            cls.configuration(open_prev=True)

    @classmethod
    def set_preset_quality(cls, quality: str, mode: str):
        if quality == f'{loc["Quality"]} HQ':
            player.glsl_shaders = anime4k.to_string(anime4k.ultra_hq_presets[mode.split(' ', 1)[-1]], mode + ' (HQ)')
            Player.info['preset'] = anime4k.current_preset
        else:
            player.glsl_shaders = anime4k.to_string(anime4k.create_preset(quality.split(' ', 1)[-1], mode.split(' ', 1)[-1]), mode + f' ({quality.split(" ", 1)[-1]})')
            Player.info['preset'] = anime4k.current_preset

    @classmethod
    def disable_anime4k(cls):
        anime4k.current_preset = ''
        player.glsl_shaders = ''
        Player.info['preset'] = ''


if __name__ == '__main__':
    # font = 'Balsamiq Sans Regular'
    # fonts.load_font(f'{os.path.dirname(__file__) + os.sep}fonts{os.sep}BalsamiqSans-Regular.ttf')
    # newFont = QFont("Balsamiq Sans", 10)

    app = QApplication()
    # app.setFont(newFont)
    window = MainWindow()

    screenshot_path = ''

    if os.name != 'nt':
        import locale
        locale.setlocale(locale.LC_NUMERIC, 'C')

    player: MPV = MPV(wid=window.ui.video.winId(), keep_open=True, profile='gpu-hq', hwdec='auto')

    window.show()
    Player.start_player(sys.argv)
    sys.exit(app.exec())
