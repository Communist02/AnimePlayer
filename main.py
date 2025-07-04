import os
import sys
import platform

from PySide6.QtCore import QByteArray, Qt, QTimer, QPoint, Signal, Slot
from PySide6.QtGui import QCloseEvent, QIcon, QGuiApplication, QAction, QOpenGLContext, QPixmap, QCursor
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QMainWindow, QApplication, QDialog, QMenu, QFileDialog, QWidget, QStyleFactory

import about_window
import android_config_window
import anime4k
import icons
import launch_parameters_window
import localization
import main_window
import open_folder_window
import open_url_window
import reference_window
import screenshot_window
import settings_window
from config import ConfigManager
from mpv import MPV, MpvRenderContext, MpvGlGetProcAddressFn
from palettes import palettes

name_program = 'Anime Player'
version = '2.2.1'
video_formats = ('mp4', 'mkv', 'webm', 'avi',
                 'mov', 'wmv', '3gp', 'ts', 'mpeg')
audio_formats = ('m4a', 'mp3', 'flac', 'ogg', 'aac', 'opus', 'wav')
subtitles_formats = ('ass', 'idx', 'srt', 'ssa', 'sub', 'ttml', 'vtt')
formats = video_formats + audio_formats

config = ConfigManager('config.json')
localization.set_locale(config.get('language'))
loc = localization.strings


class AndroidConfigWindow(QDialog):
    def __init__(self):
        super(AndroidConfigWindow, self).__init__()
        self.ui = android_config_window.Ui_AndroidConfigWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.setWindowTitle(loc['Create config for Android'])
        self.ui.label.setText(
            loc['You can use this config to use the Anime4K algorithm in the mpv video player on android'])
        self.ui.label_2.setText(loc['Enter the path to the shaders'])
        self.ui.label_3.setText(loc['Select the algorithm configuration'])
        self.ui.selected.setText(loc['Selected'])
        self.ui.all.setText(loc['All'])

        self.ui.selected.clicked.connect(self.selected)
        self.ui.all.clicked.connect(self.all)

        self.modes = []
        for quality in anime4k.qualities:
            self.modes += [
                f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]

        self.ui.comboBox.addItems(self.modes)

    def selected(self):
        quality = self.ui.comboBox.currentText().replace(')', '').split('(')[1]
        mode = self.ui.comboBox.currentText().split(' ')[1]
        self.ui.plainTextEdit.setPlainText(f'# {self.ui.comboBox.currentText()}\n' + anime4k.android_config(
            anime4k.create_preset(quality, mode), self.ui.lineEdit.text()))

    def all(self):
        mods = []
        for mod in self.modes:
            quality = mod.replace(')', '').split('(')[1]
            mode = mod.split(' ')[1]
            mods.append(f'# {mod}\n' + '# ' + anime4k.android_config(
                anime4k.create_preset(quality, mode), self.ui.lineEdit.text()))
        self.ui.plainTextEdit.setPlainText('\n\n'.join(mods))


class LaunchParametersWindow(QDialog):
    def __init__(self):
        super(LaunchParametersWindow, self).__init__()
        self.ui = launch_parameters_window.Ui_LaunchParemetersWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

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
            Player.volume_update(mpv.volume)
            self.setWindowTitle(loc['Success'])
        except Exception:
            self.setWindowTitle(loc['Error'])


class ReferenceWindow(QDialog):
    def __init__(self):
        super(ReferenceWindow, self).__init__()
        self.ui = reference_window.Ui_ReferenceWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.setWindowTitle(loc['Reference'])
        self.ui.buttonBox.buttons()[0].setText(loc['Close'])

        if loc['lang'] == 'Русский':
            reference_file_name = 'GLSL_Instructions_Advanced_ru.txt'
        else:
            reference_file_name = 'GLSL_Instructions_Advanced.txt'

        with open(f'{os.path.dirname(__file__) + os.sep}docs{os.sep}{reference_file_name}', 'r', encoding='utf-8') as ref_data:
            reference = ref_data.read()
            self.ui.plainTextEdit.setPlainText(reference)


class ScreenshotWindow(QDialog):
    def __init__(self):
        super(ScreenshotWindow, self).__init__()
        self.ui = screenshot_window.Ui_ScreenshotWindow()
        self.ui.setupUi(self)

        self.setFixedSize(520, 120)
        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.ui.lineEdit.setText(screenshot_path)

        self.setWindowTitle(loc['Screenshot'])
        self.ui.label.setText(loc['Enter folder path for screenshots'])
        self.ui.select.setText(loc['Select'])
        self.ui.paste.setText(loc['Paste'])
        self.ui.buttonBox.buttons()[0].setText(loc['Save'])
        self.ui.buttonBox.buttons()[1].setText(loc['Close'])

        self.ui.paste.clicked.connect(
            lambda: self.ui.lineEdit.setText(QGuiApplication.clipboard().text()))
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
            mpv.screenshot_directory = screenshot_path
            mpv.screenshot_jpeg_quality = 100
            try:
                mpv.screenshot()
            except SystemError:
                self.ui.label.setText(loc['Error'])


class AboutWindow(QDialog):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = about_window.Ui_AboutWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))
        self.ui.image.setPixmap(QPixmap(
            f'{os.path.dirname(__file__) + os.sep}images{os.sep}anime-player-icon.png'))

        self.setWindowTitle(loc['About'])
        self.ui.label_2.setText(f'Anime Player v{version}')
        self.ui.label_3.setText(f'{mpv.mpv_version}\n\n{loc["About program"]}')
        self.ui.buttonBox.buttons()[0].setText(loc['Close'])


class SettingsWindow(QDialog):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = settings_window.Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        match config.get('language'):
            case 'Русский':
                self.lang = 'Русский'
            case 'English':
                self.lang = 'English'
            case 'Japanese':
                self.lang = 'Japanese'
            case _:
                self.lang = 'Auto'

        styles = QStyleFactory.keys()
        for i in range(len(styles)):
            styles[i] = styles[i].lower()
        self.ui.comboBox_style.addItems(styles)
        self.ui.comboBox_style.setCurrentText(
            config.get('style', self.style().name()))

        palettes_list: list = list(palettes.keys())
        for i in range(len(palettes_list)):
            palettes_list[i] = palettes_list[i].replace(
                ' Dark', '').replace(' Light', '')

        unique_list = []
        for palette in palettes_list:
            if palette not in unique_list:
                unique_list.append(palette)

        self.ui.comboBox_palette.addItems(unique_list)
        self.ui.comboBox_palette.setCurrentText(
            config.get('palette', 'System'))

        self.ui.language.setCurrentText(self.lang)
        self.ui.openLastFile.setChecked(config.get('onOpenLastFile', True))
        self.ui.posLastFile.setChecked(config.get('onPosLastFile', True))
        self.ui.volumePlus.setChecked(config.get('volumePlus', False))
        self.ui.svp.setChecked(config.get('SVP', False))

        self.ui.buttonBox.accepted.connect(self.ok)

        self.setWindowTitle(loc['Settings'])
        self.ui.label.setText(loc['Language selection'])
        self.ui.openLastFile.setText(
            loc['On startup open the last opened file'])
        self.ui.posLastFile.setText(
            loc['Set the position of the last opened file'])
        self.ui.volumePlus.setText(loc['Increase maximum volume up to 150%'])
        self.ui.svp.setText(loc['Activate SVP'])
        self.ui.buttonBox.buttons()[1].setText(loc['Cancel'])
        self.ui.label_palette.setText(loc['Palette'])
        self.ui.label_style.setText(loc['Theme'])

    def ok(self):
        config.set('onOpenLastFile', self.ui.openLastFile.isChecked())
        config.set('onPosLastFile', self.ui.posLastFile.isChecked())
        config.set('SVP', self.ui.svp.isChecked())
        config.set('volumePlus', self.ui.volumePlus.isChecked())
        config.set('style', self.ui.comboBox_style.currentText())
        config.set('palette', self.ui.comboBox_palette.currentText())

        if config.get('volumePlus', False) != self.ui.volumePlus.isChecked():
            if not self.ui.volumePlus.isChecked() and mpv.volume > 100:
                mpv.volume = 100
            config.set('volumePlus', self.ui.volumePlus.isChecked())

        if config.get('language', self.lang) != self.ui.language.currentText():
            config.set('language', self.ui.language.currentText())

        if self.ui.svp.isChecked():
            if mpv.input_ipc_server != 'mpvpipe':
                mpv.input_ipc_server = 'mpvpipe'
                mpv.hwdec = 'auto-copy'
                mpv.hwdec_codecs = 'all'
                mpv.hr_seek_framedrop = False
        else:
            mpv.input_ipc_server = ''
            mpv.hwdec = 'auto'
            mpv.hr_seek_framedrop = True

        app.setStyle(self.ui.comboBox_style.currentText())

        palette = self.ui.comboBox_palette.currentText()
        if app.styleHints().colorScheme() == Qt.ColorScheme.Light:
            palette += ' Light'
        else:
            palette += ' Dark'
        app.setPalette(palettes.get(palette, palettes['System']))


class OpenURLWindow(QDialog):
    def __init__(self):
        super(OpenURLWindow, self).__init__()
        self.ui = open_url_window.Ui_OpenURLWindow()
        self.ui.setupUi(self)

        self.setFixedSize(550, 120)
        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.links_history = config.get('linksHistory', [])

        self.ui.comboBox.addItems(self.links_history)

        self.ui.paste.clicked.connect(
            lambda: self.ui.comboBox.setCurrentText(QGuiApplication.clipboard().text()))
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
            player.open_url(new_link)


class OpenFolderWindow(QDialog):
    def __init__(self):
        super(OpenFolderWindow, self).__init__()
        self.ui = open_folder_window.Ui_OpenFolderWindow()
        self.ui.setupUi(self)

        self.setFixedSize(550, 120)
        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.folders_history = config.get('foldersHistory', [])

        self.ui.comboBox.addItems(self.folders_history)

        self.ui.paste.clicked.connect(
            lambda: self.ui.comboBox.setCurrentText(QGuiApplication.clipboard().text()))
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
            player.open_folder(new_folder)

    def select(self):
        folder_name = QFileDialog.getExistingDirectory()
        if folder_name is not None and folder_name != '':
            self.ui.comboBox.setCurrentText(folder_name)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = main_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(
            QIcon(f'{os.path.dirname(__file__) + os.sep}favicon.ico'))

        self.ui.rightPanel.setVisible(False)

        self.ui.play.setIcon(QIcon(icons.play))
        self.ui.prev.setIcon(QIcon(icons.prev))
        self.ui.next.setIcon(QIcon(icons.next))
        self.ui.fullscreen.setIcon(QIcon(icons.fullscreen))
        self.ui.audio.setIcon(QIcon(icons.audio))
        self.ui.sub.setIcon(QIcon(icons.sub))
        self.ui.menu.setIcon(QIcon(icons.menu))
        self.ui.video.setPixmap(
            QPixmap(f'{os.path.dirname(__file__) + os.sep}images{os.sep}play-button.png'))

        self.ui.rightPanel.setTitleBarWidget(QWidget())
        self.ui.controlPanel.setTitleBarWidget(QWidget())

        self.ui.play.setToolTip(f'{loc['Play']} / {loc['Pause']}')
        self.ui.prev.setToolTip(loc['Previous file'])
        self.ui.next.setToolTip(loc['Next file'])
        self.ui.fullscreen.setToolTip(loc['Fullscreen'])
        self.ui.audio.setToolTip(loc['Soundtrack'])
        self.ui.sub.setToolTip(loc['Subtitles'])
        self.ui.menu.setToolTip(loc['Menu'])
        self.ui.volume.setToolTip(loc['Volume level'])

        self.ui.play.clicked.connect(lambda: player.play())
        self.ui.prev.clicked.connect(lambda: player.prev())
        self.ui.next.clicked.connect(lambda: player.next())
        self.ui.fullscreen.clicked.connect(lambda: player.fullscreen_switch())
        self.ui.menu.clicked.connect(self.right_panel_visible)
        self.ui.sub.clicked.connect(lambda: player.sub_view())
        self.ui.audio.clicked.connect(lambda: player.audio_view())
        self.ui.volume.valueChanged.connect(
            lambda: player.volume_update(self.ui.volume.value()))
        self.ui.time.valueChanged.connect(lambda: self.change_time())

        self.ui.video.setMouseTracking(True)
        self.setMouseTracking(True)
        self.centralWidget().setMouseTracking(True)

        self.timer = QTimer(interval=500)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start()

        self.timer_click = QTimer(interval=300)
        self.timer_click.timeout.connect(self.timer_click.stop)

        self.ui.fileList.clicked.connect(
            lambda: player.update_filelist(self.ui.fileList.currentIndex().row()))

        # Верхнее меню
        self.ui.action_Exit.triggered.connect(lambda: self.close())
        self.ui.action_Close.triggered.connect(lambda: player.close())
        self.ui.action_Open_file.triggered.connect(self.open_file)
        self.ui.action_Open_folder.triggered.connect(self.open_folder)
        self.ui.action_Open_URL.triggered.connect(self.open_url)
        self.ui.action_Settings.triggered.connect(self.settings)
        self.ui.action_Reference.triggered.connect(self.reference)
        self.ui.action_Launch_parameters.triggered.connect(
            self.launch_parameters)
        self.ui.action_Create_config_Android.triggered.connect(
            self.android_config)
        self.ui.action_Fullscreen.triggered.connect(
            lambda: player.fullscreen_switch())
        self.ui.action_Play_Pause.triggered.connect(lambda: player.play())
        self.ui.action_Disable.triggered.connect(
            lambda: player.disable_anime4k())
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
        self.ui.menu_Increasing_image_quality.setTitle(
            loc['Increasing image quality'])
        self.ui.action_Disable.setText(loc['Disable'])
        self.ui.menu_Other.setTitle(loc['Other'])
        self.ui.action_About.setText(loc['About'])
        self.ui.action_Launch_parameters.setText(loc['Launch parameters'])
        self.ui.action_Take_a_screenshot.setText(loc['Take a screenshot'])
        self.ui.action_Create_config_Android.setText(
            loc['Create config for Android'])
        self.ui.action_Reference.setText(loc['Reference'])
        self.ui.menu_Playback_speed.setTitle(loc['Playback speed'])
        self.ui.action_Volume_plus.setText(loc['Volume +10'])
        self.ui.action_Volume_minus.setText(loc['Volume -10'])
        self.ui.action_Rewind_plus.setText(loc['Rewind +5 sec'])
        self.ui.action_Rewind_minus.setText(loc['Rewind -5 sec'])
        self.ui.action_Zoom_in.setText(loc['Zoom in'])
        self.ui.action_Zoom_out.setText(loc['Zoom out'])
        self.ui.action_Playlist.setText(loc['Playlist'])
        self.ui.sourceInfo.setText('')

        modes = []
        for quality in anime4k.qualities:
            modes += [f'{loc["Mode"]} {mode} ({quality})' for mode in anime4k.modes]

        tabs = {}
        for quality in anime4k.qualities:
            if f'{loc["Quality"]} {quality}' not in tabs.keys():
                tabs[f'{loc["Quality"]} {quality}'] = []
            tabs[f'{loc["Quality"]} {quality}'] += [
                f'{loc["Mode"]} {mode}' for mode in anime4k.modes]
        tabs[f'{loc["Quality"]} HQ'] = [
            f'{loc["Mode"]} {mode}' for mode in list(anime4k.ultra_hq_presets.keys())]

        for quality in tabs.keys():
            menu = QMenu(self.menuBar())
            menu.setTitle(quality)
            self.ui.menu_Increasing_image_quality.addMenu(menu)
            for mode in tabs[quality]:
                action = QAction(self)
                action.setText(mode)
                action.triggered.connect(
                    lambda ignore=False, q=quality, m=mode: player.set_preset_quality(q, m))
                menu.addAction(action)

        self.customContextMenuRequested.connect(self.show_context_menu)

        self.setAcceptDrops(True)

    def mouseMoveEvent(self, event):
        if player.fullscreen:
            player.update_fullscreen_layout(
                event.position().x(), event.position().y())

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()

    def dropEvent(self, event):
        is_new = True
        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            if os.path.isfile(file_name):
                if is_new:
                    player.open_file(file_name)
                    is_new = False
                else:
                    player.add_file(file_name)
            elif os.path.isdir(file_name):
                player.open_folder(file_name)
                break
            elif os.path.islink(file_name):
                player.open_url(file_name)
                break

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            player.play()
            if self.timer_click.isActive():
                Player.fullscreen_switch()
                self.timer_click.stop()
            else:
                self.timer_click.start()

    @staticmethod
    def screenshot():
        screenshot_win = ScreenshotWindow()
        screenshot_win.setModal(True)
        screenshot_win.exec()

    @staticmethod
    def zoom(value):
        mpv.video_zoom += value

    @staticmethod
    def speed(speed):
        mpv.speed = speed

    @staticmethod
    def timer_update():
        player.update_info()
        player.update_cursor()

    def change_time(self):
        if mpv.time_pos is not None and int(mpv.time_pos) != self.ui.time.value():
            player.new_position(self.ui.time.value())

    def closeEvent(self, event):
        player.save_parameters()

    def open_file(self):
        file_name = QFileDialog.getOpenFileName(self,
                                                filter=f"{loc['All supported files']} ({' '.join(['*.' + f for f in formats])});;{loc['Video']} ({' '.join(['*.' + f for f in video_formats])});;{loc['Audio']} ({' '.join(['*.' + f for f in audio_formats])});;{loc['All files']} (*.*)")
        if file_name[0] is not None and file_name[0] != '':
            player.open_file(file_name[0])

    @staticmethod
    def open_folder():
        open_folder_win = OpenFolderWindow()
        open_folder_win.setModal(True)
        open_folder_win.exec()

    @staticmethod
    def open_url():
        open_url_win = OpenURLWindow()
        open_url_win.setModal(True)
        open_url_win.exec()

    def settings(self):
        settings_win = SettingsWindow()
        settings_win.setModal(True)
        settings_win.exec()
        if not config.get('volumePlus', False):
            self.ui.volume.setValue(mpv.volume)
            self.ui.volume.setMaximum(100)
        else:
            self.ui.volume.setMaximum(150)

    @staticmethod
    def about():
        about_win = AboutWindow()
        about_win.setModal(True)
        about_win.exec()

    @staticmethod
    def reference():
        reference_win = ReferenceWindow()
        reference_win.setModal(True)
        reference_win.exec()

    def launch_parameters(self):
        launch_parameters_win = LaunchParametersWindow()
        launch_parameters_win.setModal(True)
        launch_parameters_win.exec()
        self.ui.volume.setValue(mpv.volume)

    @staticmethod
    def android_config():
        android_config_win = AndroidConfigWindow()
        android_config_win.setModal(True)
        android_config_win.exec()

    def right_panel_visible(self):
        if Player.fullscreen:
            Player.is_menu_visible = not Player.is_menu_visible
        else:
            self.ui.rightPanel.setVisible(not self.ui.rightPanel.isVisible())

    def show_context_menu(self):
        menu = QMenu()
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
        menu.exec(QCursor.pos())

    def volume_plus(self):
        if mpv.volume > 95 and self.ui.volume.maximum() == 100:
            mpv.volume = 100
        elif mpv.volume > 145 and self.ui.volume.maximum() == 150:
            mpv.volume = 150
        else:
            mpv.volume += 5
        self.ui.volume.setValue(mpv.volume)
        Player.volume_update(mpv.volume)

    def volume_minus(self):
        if mpv.volume < 5:
            mpv.volume = 0
        else:
            mpv.volume -= 5
        self.ui.volume.setValue(mpv.volume)
        Player.volume_update(mpv.volume)

    @staticmethod
    def rewind_plus():
        if mpv.time_pos is not None:
            mpv.seek(5)
            window.ui.time.setValue(mpv.time_pos)
            window.ui.currentTime.setText(
                '{:02d}:{:02d}'.format(*divmod(int(mpv.time_pos), 60)))

    @staticmethod
    def rewind_minus():
        if mpv.time_pos is not None:
            if mpv.time_pos > 5:
                mpv.seek(-5)
            else:
                mpv.time_pos = 0
            window.ui.time.setValue(mpv.time_pos)
            window.ui.currentTime.setText(
                '{:02d}:{:02d}'.format(*divmod(int(mpv.time_pos), 60)))


class Player:
    """
    Управление плеером
    """
    files: list = []
    filenames_only: list = []
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

    @staticmethod
    def list_files(folder: str):
        return [os.path.join(folder, f) for f in os.listdir(folder) if (f.split('.')[-1].lower() in formats)]

    @staticmethod
    def list_filenames(folder: str):
        filenames = [f for f in os.listdir(folder) if (
            f.split('.')[-1].lower() in formats)]
        return [f'{i + 1}) ' + filenames[i] for i in range(len(filenames))]

    def sub_view(self):
        self.sub = {}
        if mpv.track_list is not None:
            for track in mpv.track_list:
                if track['type'] == 'sub':
                    if 'title' in track.keys():
                        self.sub[track['id']] = f'{track["title"]}'
                        if 'lang' in track.keys():
                            self.sub[track['id']
                                     ] = f'{track["lang"]} - ' + self.sub[track['id']]
                    elif 'lang' in track.keys():
                        self.sub[track['id']
                                 ] = f'{track["lang"]} - {track["codec"]}'
                    else:
                        self.sub[track['id']] = track['codec']

            def set_sub(index: int):
                mpv.sid = index

            def add_subtitles():
                file_name = QFileDialog.getOpenFileName(
                    filter=f"{loc['Subtitles']} ({' '.join(['*.' + f for f in subtitles_formats])});;{loc['All files']} (*.*)")
                if file_name[0] is not None and file_name[0] != '':
                    mpv.sub_add(file_name[0])

            menu_sub = QMenu()
            if len(self.sub) > 0:
                action = QAction(window)
                action.setText(loc['Disable'])
                action.triggered.connect(lambda: set_sub(0))
                menu_sub.addAction(action)

                action = QAction(window)
                action.setText(loc['Add subtitles'])
                action.triggered.connect(add_subtitles)
                menu_sub.addAction(action)

                menu_sub.addSeparator()
                for key, value in self.sub.items():
                    action = QAction(window)
                    action.setText(f'{key}) {value}')
                    action.triggered.connect(
                        lambda ignore=False, x=key: set_sub(x))
                    menu_sub.addAction(action)
            else:
                action = QAction(window)
                action.setText(loc['Add subtitles'])
                action.triggered.connect(add_subtitles)
                menu_sub.addAction(action)

            menu_sub.exec(window.ui.sub.mapToGlobal(QPoint(0, 0)))

    def audio_view(self):
        self.audio = {}
        if mpv.track_list is not None:
            for track in mpv.track_list:
                if track['type'] == 'audio':
                    self.audio[track['id']
                               ] = f'{track['codec']} {track['audio-channels']}ch {track['demux-samplerate']} Hz'
                    if 'title' in track.keys():
                        self.audio[track['id']
                                   ] = f'{track["title"]} (' + self.audio[track['id']] + ')'
                        if 'lang' in track.keys():
                            self.audio[track['id']
                                       ] = f'{track["lang"]} - ' + self.audio[track['id']]
                    elif 'lang' in track.keys():
                        self.audio[track['id']
                                   ] = f'{track["lang"]} - {self.audio[track['id']]}'

            def set_audio(index: int):
                mpv.aid = index

            menu_audio = QMenu()
            if len(self.audio) > 0:
                action = QAction(window)
                action.setText(loc['Disable'])
                action.triggered.connect(lambda: set_audio(0))
                menu_audio.addAction(action)
                menu_audio.addSeparator()
                for key, value in self.audio.items():
                    action = QAction(window)
                    action.setText(f'{key}) {value}')
                    action.triggered.connect(
                        lambda ignore=False, a=key: set_audio(a))
                    menu_audio.addAction(action)
            else:
                action = QAction(window)
                action.setText(loc['No audio tracks'])
                menu_audio.addAction(action)
            menu_audio.exec(window.ui.audio.mapToGlobal(QPoint(0, 0)))

    def update_info(self, no_update_fps=True):
        # duration = player.duration
        time_pos = mpv.time_pos
        Player.info['codec'] = mpv.video_format if mpv.video_format is not None else mpv.audio_codec_name
        Player.info['resolution'] = (mpv.width, mpv.height)
        if no_update_fps:
            Player.info['fps'] = mpv.estimated_vf_fps
        Player.info['frame_drop'] = mpv.frame_drop_count

        # Обновление информации о разрешении, FPS, кодеке и потерянных кадрах
        str_info = {
            'preset': Player.info['preset'],
            'codec': f'{Player.info["codec"].upper()}' if Player.info["codec"] is not None else '',
            'resolution': f'{Player.info["resolution"][0]}x{Player.info["resolution"][1]}' if Player.info["resolution"] != (None, None) else '',
            'fps': f'{round(Player.info["fps"], 1) if Player.info["fps"] is not None else "0.0"} FPS' if Player.info["resolution"] != (None, None) else '',
            'frame_drop': f'{loc["Frames lost"]}: {Player.info["frame_drop"]}' if Player.info["frame_drop"] is not None else ''
        }

        window.ui.mediaInfo.setText(' | '.join(
            [string for string in str_info.values() if string != '']))
        # Обновление кнопки ИГРАТЬ
        if mpv.duration is not None and mpv.pause:
            window.ui.play.setIcon(QIcon(icons.play))
        # Обновление ползунка прокрутки и времени
        if mpv.duration is not None:
            if self.duration != mpv.duration:
                self.duration = mpv.duration
                window.ui.time.setMaximum(self.duration)
                window.ui.allTime.setText('{:02d}:{:02d}'.format(
                    *divmod(int(self.duration), 60)))
        else:
            window.ui.time.setMaximum(0)
            window.ui.allTime.setText('00:00')

        if time_pos is not None:
            window.ui.time.setValue(time_pos)
            window.ui.currentTime.setText(
                '{:02d}:{:02d}'.format(*divmod(int(time_pos), 60)))
        else:
            window.ui.currentTime.setText('00:00')
            window.ui.time.setValue(0)

    def play_file(self, file: str, timeout=3, position: float = 0):
        if os.name != 'nt':
            window.ui.video.hide()
            video.show()
        mpv.play(file)
        if position > 0:
            try:
                mpv.wait_for_property(
                    'duration', lambda val: val is not None, timeout=timeout)
            except TimeoutError:
                pass
            else:
                self.new_position(position, slider_update=True)

    def play(self):
        """Воспроизведение / Пауза"""
        if window.ui.fileList.currentIndex().row() >= 0:
            if mpv.duration is None:
                self.play_file(
                    self.files[window.ui.fileList.currentIndex().row()])
                mpv.pause = False
                window.ui.play.setIcon(QIcon(icons.pause))
            elif not mpv.pause:
                mpv.pause = True
                window.ui.play.setIcon(QIcon(icons.play))
            else:
                mpv.pause = False
                window.ui.play.setIcon(QIcon(icons.pause))

    def next(self):
        """Переход к следующему файлу"""
        current_index = window.ui.fileList.currentIndex().row()
        if current_index < len(self.files) - 1:
            window.ui.fileList.setCurrentRow(current_index + 1)
            window.setWindowTitle(
                f'{self.filenames_only[current_index]} - {name_program}')
            self.play_file(self.files[current_index])

    def prev(self):
        """Переход к предыдущему файлу"""
        if window.ui.fileList.currentIndex().row() > 0:
            file_num = window.ui.fileList.currentIndex().row() - 1
            file = self.files[file_num]
            window.ui.fileList.setCurrentRow(file_num)
            window.setWindowTitle(
                f'{file.rsplit(os.sep, 1)[-1]} - {name_program}')
            self.play_file(file)
        elif window.ui.fileList.count() > 0:
            window.ui.fileList.setCurrentRow(0)
            window.setWindowTitle(
                f'{self.files[0].rsplit(os.sep, 1)[-1]} - {name_program}')

    def open_file(self, file: str, pause: bool = False, position: float = 0):
        """
        Открытие файла
        :param file: путь к файлу
        :param pause: должна ли стоять пауза после открытия
        :param position: позиция
        """
        file = file.replace('/', os.sep)
        mpv.stop()
        mpv.pause = pause
        if pause:
            window.ui.play.setIcon(QIcon(icons.play))
        else:
            window.ui.play.setIcon(QIcon(icons.pause))
        folder = file.rsplit(os.sep, 1)[0]
        self.files = [file]
        self.filenames_only = [file.split(os.sep)[-1]]
        window.ui.fileList.clear()
        window.ui.fileList.addItems(self.filenames_only)
        window.ui.fileList.setCurrentRow(0)
        window.ui.sourceInfo.setText(folder)
        window.setWindowTitle(
            f'{self.filenames_only[window.ui.fileList.currentIndex().row()]} - {name_program}')
        self.play_file(
            self.files[window.ui.fileList.currentIndex().row()], position=position)
        config.set('opened', ['file', file])

    def add_file(self, file: str):
        file = file.replace('/', os.sep)
        self.files.append(file)
        self.filenames_only.append(file.split(os.sep)[-1])
        window.ui.fileList.addItem(file.split(os.sep)[-1])

    def open_url(self, link: str, pause: bool = False, position: float = 0):
        """
        Открытие с помощью URL-адреса
        :param link: URL-адрес
        :param pause: должна ли стоять пауза после открытия
        :param position: позиция
        """
        mpv.stop()
        mpv.pause = pause
        if pause:
            window.ui.play.setIcon(QIcon(icons.play))
        else:
            window.ui.play.setIcon(QIcon(icons.pause))
        folder = 'URL'
        self.files = [link]
        self.filenames_only = [link.rsplit("/", 1)[-1]]
        window.ui.fileList.clear()
        window.ui.fileList.addItems(self.files)
        window.ui.fileList.setCurrentRow(0)
        window.ui.sourceInfo.setText(folder)
        window.setWindowTitle(f'{link.rsplit("/", 1)[-1]} - {name_program}')
        self.play_file(link, position=position, timeout=5)
        config.set('opened', ['url', link])

    def open_folder(self, folder: str, pause: bool = True, file: str = '', position: float = 0):
        """
        Открытие папки
        :param file:
        :param folder: путь к папке
        :param pause: должна ли стоять пауза после открытия
        :param file: полное имя файла
        :param position: позиция
        """
        folder = folder.replace('/', os.sep)
        mpv.stop()
        mpv.pause = pause
        if pause:
            window.ui.play.setIcon(QIcon(icons.play))
        else:
            window.ui.play.setIcon(QIcon(icons.pause))
        self.files = self.list_files(folder)
        self.filenames_only = self.list_filenames(folder)
        if file is not None and file != '' and os.path.exists(file):
            file_num = self.files.index(file)
        else:
            if os.name != 'nt':
                video.hide()
                window.ui.video.show()
            file_num = 0
        if len(self.files) != 0:
            file_name = self.files[file_num]
            window.setWindowTitle(
                f'{file_name.rsplit(os.sep, 1)[-1]} - {name_program}')
            self.play_file(file_name, position=position)
        else:
            window.setWindowTitle(name_program)
        window.ui.fileList.clear()
        window.ui.fileList.addItems(self.filenames_only)
        window.ui.fileList.setCurrentRow(file_num)
        window.ui.rightPanel.setVisible(True)
        window.ui.sourceInfo.setText(folder)
        config.set('opened', ['folder', folder])

    def close(self):
        """
        Закрытие открытых фалов и переход в изначальное состояние
        """
        mpv.stop()
        if os.name != 'nt':
            video.hide()
            window.ui.video.show()
        mpv.pause = False
        window.ui.play.setIcon(QIcon(icons.play))
        self.files = []
        self.filenames_only = []
        self.duration = 0
        window.ui.fileList.clear()
        window.ui.sourceInfo.setText('')
        window.setWindowTitle(name_program)
        config.set('opened', ['', ''])

    def update_filelist(self, index: int):
        """
        Обновление списка файлов
        :param index: Номер файла в списке файлов
        """
        if len(self.filenames_only) >= 1:
            # if cls.filename != filename_temp or cls.filenum < 0:
            self.play_file(self.files[index])
            window.setWindowTitle(
                f'{self.files[index].rsplit(os.sep, 1)[-1]} - {name_program}')

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
            if os.name == 'nt':
                window.ui.controlPanel.setFloating(True)
            window.ui.controlPanel.setVisible(False)
            cls.is_menu_visible = window.ui.rightPanel.isVisible()
            window.ui.rightPanel.setVisible(False)
        else:
            cls.fullscreen = False
            window.ui.rightPanel.setFloating(False)
            if cls.is_maximized:
                window.showMaximized()
            else:
                window.showNormal()
            window.ui.menubar.setFixedHeight(
                window.ui.menubar.sizeHint().height() + 1)
            window.ui.controlPanel.setVisible(True)
            window.ui.rightPanel.setVisible(cls.is_menu_visible)
            window.ui.video.unsetCursor()
            cls.cursor_timer = 0
            window.ui.controlPanel.setFloating(False)

    def update_fullscreen_layout(self, x: float, y: float):
        if y > window.ui.centralwidget.size().height() - window.ui.controlPanel.height():
            window.ui.controlPanel.setVisible(True)
            if os.name != 'nt':
                window.ui.controlPanel.setFloating(True)
            window.ui.controlPanel.activateWindow()
        elif x > window.ui.centralwidget.size().width() - window.ui.rightPanel.width() - 20 and Player.is_menu_visible and not window.ui.rightPanel.isVisible():
            window.ui.rightPanel.setVisible(True)
        elif x > window.ui.centralwidget.size().width() - 20 and Player.is_menu_visible and window.ui.rightPanel.isVisible():
            window.ui.rightPanel.setVisible(True)
        else:
            window.ui.rightPanel.setVisible(False)
            window.ui.controlPanel.setVisible(False)

        window.ui.video.unsetCursor()
        self.cursor_last = (x, y)
        self.cursor_timer = 0

    def update_cursor(self):
        if not window.ui.controlPanel.isVisible() and not window.ui.rightPanel.isVisible():
            self.cursor_timer += 1
            if self.cursor_timer > 3:
                window.ui.video.setCursor(Qt.CursorShape.BlankCursor)

    @staticmethod
    def new_position(position: float, slider_update: bool = False):
        """
        Установка новой позиции
        :param position: позиция
        :param slider_update: обновлять ли слайдер
        """
        if mpv.duration is not None:
            mpv.time_pos = position
            window.ui.currentTime.setText(
                '{:02d}:{:02d}'.format(*divmod(int(mpv.time_pos), 60)))
            window.ui.allTime.setText(
                '{:02d}:{:02d}'.format(*divmod(int(mpv.duration), 60)))
            if slider_update:
                window.ui.time.setMaximum(mpv.duration)
                window.ui.time.setValue(mpv.time_pos)

    @staticmethod
    def volume_update(volume: int):
        """Изменение громкости"""
        mpv.volume = volume
        window.ui.volume.setToolTip(f'{volume}%')
        config.set('volume', volume)

    def save_parameters(self):
        """Сохранение текущего открытого файла и позиции"""
        if window.ui.fileList.count() > 0:
            file = self.files[window.ui.fileList.currentIndex().row()]
        else:
            file = None
        position = mpv.time_pos
        config.set('file', file)
        if position is not None and position >= 10:
            config.set('position', position)
        else:
            config.set('position', None)
        config.save_config()

    def configuration(self, open_prev: bool = True):
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
            style = config.get('style')
            launch_parameters = config.get('launchParameters')
            if on_pos_last_file is not None and not on_pos_last_file or position is None:
                position = 0
            if volume is not None:
                mpv.volume = volume
                window.ui.volume.setValue(volume)
                window.ui.volume.setToolTip(f'{volume}%')
            if volume_plus:
                window.ui.volume.setMaximum(150)
            if opened is not None and open_prev and (open_last is None or open_last):
                match opened[0]:
                    case 'file':
                        if os.path.exists(opened[1]):
                            self.open_file(
                                opened[1], pause=True, position=position)
                    case 'url':
                        if on_pos_last_file is None or on_pos_last_file:
                            self.open_url(
                                opened[1], pause=True, position=position)
                    case 'folder':
                        if os.path.exists(opened[1]):
                            self.open_folder(
                                opened[1], pause=True, file=file, position=position)
            if svp is not None and svp:
                mpv.input_ipc_server = 'mpvpipe'
                mpv.hwdec = 'auto-copy'
                mpv.hwdec_codecs = 'all'
                mpv.hr_seek_framedrop = False
            if launch_parameters is not None and launch_parameters != '':
                try:
                    exec(launch_parameters)
                    window.ui.volume.setValue(mpv.volume)
                    config.set('volume', mpv.volume)
                except Exception:
                    pass
            if style is not None:
                app.setStyle(style)
        except ValueError:
            config.delete('opened')
            config.delete('file')
            config.delete('position')

    def start_player(self, args: list):
        """
        Начальные действия при открытии плеера
        :param args: аргументы командной строки
        """
        if len(args) > 1:
            self.configuration(open_prev=False)
            if os.path.isfile(args[1]):
                file = config.get('opened', [None, None])[1]
                position = config.get('position')

                if file is not None and file == args[1] and position is not None:
                    self.open_file(args[1], position=position)
                else:
                    self.open_file(args[1])
            elif os.path.isdir(args[1]):
                self.open_folder(args[1])
        else:
            self.configuration(open_prev=True)

    def set_preset_quality(self, quality: str, mode: str):
        if quality == f'{loc["Quality"]} HQ':
            mpv.glsl_shaders = anime4k.to_string(
                anime4k.ultra_hq_presets[mode.split(' ', 1)[-1]], mode + ' (HQ)')
            self.info['preset'] = anime4k.current_preset
        else:
            mpv.glsl_shaders = anime4k.to_string(anime4k.create_preset(quality.split(
                ' ', 1)[-1], mode.split(' ', 1)[-1]), mode + f' ({quality.split(" ", 1)[-1]})')
            self.info['preset'] = anime4k.current_preset

    @staticmethod
    def disable_anime4k():
        anime4k.current_preset = ''
        mpv.glsl_shaders = ''
        Player.info['preset'] = ''


def get_process_address(_, name):
    glctx = QOpenGLContext.currentContext()
    address = int(glctx.getProcAddress(QByteArray(name)))
    return address


class Video(QOpenGLWidget):
    onUpdate = Signal()
    initialized = Signal()

    def __init__(self, parent, mpv) -> None:
        super().__init__(parent)
        self.mpv = mpv
        self.ctx = None
        self._proc_addr_wrapper = MpvGlGetProcAddressFn(get_process_address)
        self.onUpdate.connect(self.do_update)
        self.c = 0

        self.setUpdateBehavior(QOpenGLWidget.UpdateBehavior.PartialUpdate)

    def initializeGL(self) -> None:
        self.ctx = MpvRenderContext(
            self.mpv, 'opengl',
            opengl_init_params={
                'get_proc_address': self._proc_addr_wrapper
            },
        )

        if self.ctx:
            self.ctx.update_cb = self.on_update
            self.initialized.emit()

    def paintGL(self) -> None:
        if self.c > 100:
            self.c = 0
        else:
            self.c += 1
        rect = self.rect()
        if self.ctx:
            fbo = self.defaultFramebufferObject()
            self.ctx.render(flip_y=True, opengl_fbo={
                            'w': rect.width(), 'h': rect.height(), 'fbo': fbo})

    def do_update(self):
        self.update()

    @Slot()
    def on_update(self):
        self.onUpdate.emit()

    def closeEvent(self, event: QCloseEvent) -> None:
        """free mpv_context and terminate player brofre closing the widget"""
        self.ctx.free()
        self.mpv.terminate()
        event.accept()


if __name__ == '__main__':
    app = QApplication()

    palette = config.get('palette', 'System')
    if palette not in palettes.keys():
        if app.styleHints().colorScheme() == Qt.ColorScheme.Light:
            palette += ' Light'
        else:
            palette += ' Dark'
    app.setPalette(palettes.get(palette, palettes['System']))

    screenshot_path = ''

    window = MainWindow()

    if os.name == 'nt':
        if platform.release() != '11':
            app.setStyle('windows11')
        mpv: MPV = MPV(wid=window.ui.video.winId(), keep_open=True,
                       profile='gpu-hq', ytdl=True, terminal='yes')
    else:
        import locale
        locale.setlocale(locale.LC_NUMERIC, 'C')
        mpv: MPV = MPV(keep_open=True, vo='libmpv', profile='gpu-hq', terminal='yes')
        video = Video(window.ui.centralwidget, mpv)
        video.setMouseTracking(True)
        window.ui.verticalLayout_video.addWidget(video)
        video.hide()

    window.show()
    player = Player()
    player.start_player(sys.argv)
    sys.exit(app.exec())
