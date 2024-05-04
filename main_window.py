# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#info {\n"
"	border: 1px solid rgb(87, 86, 86);\n"
"	border-radius:7px;\n"
"}\n"
"\n"
"QListWidget {\n"
"	border: 1px solid rgb(87, 86, 86);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"#controlPanel {\n"
"	border: 1px solid rgb(87, 86, 86);\n"
"	border-radius: 9px;\n"
"	margin-top: 6px;\n"
"	margin-bottom: 8px;\n"
"	margin-left: 6px;\n"
"	margin-right: 6px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid rgb(87, 86, 86);\n"
"    height: 16px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"	width: 16px;\n"
"	border-radius: 5px;\n"
"	border: 3px solid rgb(87, 86, 86);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 0px solid rgb(87, 86, 86);\n"
"}")
        self.action_Open_file = QAction(MainWindow)
        self.action_Open_file.setObjectName(u"action_Open_file")
#if QT_CONFIG(shortcut)
        self.action_Open_file.setShortcut(u"Ctrl+O")
#endif // QT_CONFIG(shortcut)
        self.action_Open_URL = QAction(MainWindow)
        self.action_Open_URL.setObjectName(u"action_Open_URL")
#if QT_CONFIG(shortcut)
        self.action_Open_URL.setShortcut(u"Ctrl+U")
#endif // QT_CONFIG(shortcut)
        self.action_Open_folder = QAction(MainWindow)
        self.action_Open_folder.setObjectName(u"action_Open_folder")
#if QT_CONFIG(shortcut)
        self.action_Open_folder.setShortcut(u"F2")
#endif // QT_CONFIG(shortcut)
        self.action_Close = QAction(MainWindow)
        self.action_Close.setObjectName(u"action_Close")
#if QT_CONFIG(shortcut)
        self.action_Close.setShortcut(u"F4")
#endif // QT_CONFIG(shortcut)
        self.action_Settings = QAction(MainWindow)
        self.action_Settings.setObjectName(u"action_Settings")
#if QT_CONFIG(shortcut)
        self.action_Settings.setShortcut(u"F5")
#endif // QT_CONFIG(shortcut)
        self.action_Exit = QAction(MainWindow)
        self.action_Exit.setObjectName(u"action_Exit")
#if QT_CONFIG(shortcut)
        self.action_Exit.setShortcut(u"Alt+F4")
#endif // QT_CONFIG(shortcut)
        self.action_Play_Pause = QAction(MainWindow)
        self.action_Play_Pause.setObjectName(u"action_Play_Pause")
        self.action_Take_a_screenshot = QAction(MainWindow)
        self.action_Take_a_screenshot.setObjectName(u"action_Take_a_screenshot")
#if QT_CONFIG(shortcut)
        self.action_Take_a_screenshot.setShortcut(u"F12")
#endif // QT_CONFIG(shortcut)
        self.action_Fullscreen = QAction(MainWindow)
        self.action_Fullscreen.setObjectName(u"action_Fullscreen")
#if QT_CONFIG(shortcut)
        self.action_Fullscreen.setShortcut(u"F11")
#endif // QT_CONFIG(shortcut)
        self.action_Disable = QAction(MainWindow)
        self.action_Disable.setObjectName(u"action_Disable")
#if QT_CONFIG(shortcut)
        self.action_Disable.setShortcut(u"D")
#endif // QT_CONFIG(shortcut)
        self.action_Reference = QAction(MainWindow)
        self.action_Reference.setObjectName(u"action_Reference")
        self.action_Create_config_Android = QAction(MainWindow)
        self.action_Create_config_Android.setObjectName(u"action_Create_config_Android")
        self.action_Launch_parameters = QAction(MainWindow)
        self.action_Launch_parameters.setObjectName(u"action_Launch_parameters")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
#if QT_CONFIG(shortcut)
        self.action_About.setShortcut(u"F1")
#endif // QT_CONFIG(shortcut)
        self.action_x025 = QAction(MainWindow)
        self.action_x025.setObjectName(u"action_x025")
        self.action_x05 = QAction(MainWindow)
        self.action_x05.setObjectName(u"action_x05")
        self.action_x075 = QAction(MainWindow)
        self.action_x075.setObjectName(u"action_x075")
        self.action_x10 = QAction(MainWindow)
        self.action_x10.setObjectName(u"action_x10")
        self.action_x125 = QAction(MainWindow)
        self.action_x125.setObjectName(u"action_x125")
        self.action_x15 = QAction(MainWindow)
        self.action_x15.setObjectName(u"action_x15")
        self.action_x175 = QAction(MainWindow)
        self.action_x175.setObjectName(u"action_x175")
        self.action_x20 = QAction(MainWindow)
        self.action_x20.setObjectName(u"action_x20")
        self.action_x225 = QAction(MainWindow)
        self.action_x225.setObjectName(u"action_x225")
        self.action_x25 = QAction(MainWindow)
        self.action_x25.setObjectName(u"action_x25")
        self.action_x275 = QAction(MainWindow)
        self.action_x275.setObjectName(u"action_x275")
        self.action_x30 = QAction(MainWindow)
        self.action_x30.setObjectName(u"action_x30")
        self.action_Rewind_plus = QAction(MainWindow)
        self.action_Rewind_plus.setObjectName(u"action_Rewind_plus")
        self.action_Rewind_minus = QAction(MainWindow)
        self.action_Rewind_minus.setObjectName(u"action_Rewind_minus")
        self.action_Volume_plus = QAction(MainWindow)
        self.action_Volume_plus.setObjectName(u"action_Volume_plus")
        self.action_Volume_minus = QAction(MainWindow)
        self.action_Volume_minus.setObjectName(u"action_Volume_minus")
        self.action_Zoom_in = QAction(MainWindow)
        self.action_Zoom_in.setObjectName(u"action_Zoom_in")
        self.action_Zoom_out = QAction(MainWindow)
        self.action_Zoom_out.setObjectName(u"action_Zoom_out")
        self.action_Playlist = QAction(MainWindow)
        self.action_Playlist.setObjectName(u"action_Playlist")
#if QT_CONFIG(shortcut)
        self.action_Playlist.setShortcut(u"F6")
#endif // QT_CONFIG(shortcut)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.main = QVBoxLayout()
        self.main.setSpacing(0)
        self.main.setObjectName(u"main")
        self.video = QLabel(self.centralwidget)
        self.video.setObjectName(u"video")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy1)
        self.video.setPixmap(QPixmap(u"../images/play-button.png"))
        self.video.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video.setWordWrap(False)
        self.video.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.main.addWidget(self.video)

        self.controlPanel = QFrame(self.centralwidget)
        self.controlPanel.setObjectName(u"controlPanel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.controlPanel.sizePolicy().hasHeightForWidth())
        self.controlPanel.setSizePolicy(sizePolicy2)
        self.controlPanel.setMinimumSize(QSize(0, 120))
        self.controlPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.controlPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.controlPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, 0, -1)
        self.timeControl = QHBoxLayout()
        self.timeControl.setSpacing(20)
        self.timeControl.setObjectName(u"timeControl")
        self.currentTime = QLabel(self.controlPanel)
        self.currentTime.setObjectName(u"currentTime")
        self.currentTime.setMinimumSize(QSize(32, 0))
#if QT_CONFIG(statustip)
        self.currentTime.setStatusTip(u"")
#endif // QT_CONFIG(statustip)

        self.timeControl.addWidget(self.currentTime)

        self.time = QSlider(self.controlPanel)
        self.time.setObjectName(u"time")
        self.time.setMinimumSize(QSize(100, 30))
        self.time.setMaximum(60)
        self.time.setPageStep(5)
        self.time.setOrientation(Qt.Orientation.Horizontal)

        self.timeControl.addWidget(self.time)

        self.allTime = QLabel(self.controlPanel)
        self.allTime.setObjectName(u"allTime")
#if QT_CONFIG(statustip)
        self.allTime.setStatusTip(u"")
#endif // QT_CONFIG(statustip)

        self.timeControl.addWidget(self.allTime)


        self.verticalLayout.addLayout(self.timeControl)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.prev = QPushButton(self.controlPanel)
        self.prev.setObjectName(u"prev")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.prev.sizePolicy().hasHeightForWidth())
        self.prev.setSizePolicy(sizePolicy3)
        self.prev.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u"../images/icons/skip_previous_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.prev.setIcon(icon1)
        self.prev.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.prev)

        self.play = QPushButton(self.controlPanel)
        self.play.setObjectName(u"play")
        sizePolicy3.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy3)
        self.play.setMinimumSize(QSize(50, 50))
        self.play.setBaseSize(QSize(0, 0))
        icon2 = QIcon()
        icon2.addFile(u"../images/icons/play_arrow_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"images/icons/pause_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Disabled, QIcon.Off)
        self.play.setIcon(icon2)
        self.play.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.play)

        self.next = QPushButton(self.controlPanel)
        self.next.setObjectName(u"next")
        sizePolicy3.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy3)
        self.next.setMinimumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u"../images/icons/skip_next_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon3)
        self.next.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.next)

        self.volume = QSlider(self.controlPanel)
        self.volume.setObjectName(u"volume")
        sizePolicy1.setHeightForWidth(self.volume.sizePolicy().hasHeightForWidth())
        self.volume.setSizePolicy(sizePolicy1)
        self.volume.setMinimumSize(QSize(80, 30))
        self.volume.setMaximumSize(QSize(140, 16777215))
        self.volume.setMaximum(100)
        self.volume.setValue(100)
        self.volume.setOrientation(Qt.Orientation.Horizontal)
        self.volume.setTickPosition(QSlider.TickPosition.NoTicks)

        self.horizontalLayout_3.addWidget(self.volume)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.sub = QPushButton(self.controlPanel)
        self.sub.setObjectName(u"sub")
        sizePolicy3.setHeightForWidth(self.sub.sizePolicy().hasHeightForWidth())
        self.sub.setSizePolicy(sizePolicy3)
        self.sub.setMinimumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u"../images/icons/subtitles_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.sub.setIcon(icon4)
        self.sub.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.sub)

        self.audio = QPushButton(self.controlPanel)
        self.audio.setObjectName(u"audio")
        sizePolicy3.setHeightForWidth(self.audio.sizePolicy().hasHeightForWidth())
        self.audio.setSizePolicy(sizePolicy3)
        self.audio.setMinimumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u"../images/icons/music_note_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.audio.setIcon(icon5)
        self.audio.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.audio)

        self.menu = QPushButton(self.controlPanel)
        self.menu.setObjectName(u"menu")
        sizePolicy3.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy3)
        self.menu.setMinimumSize(QSize(50, 50))
        icon6 = QIcon()
        icon6.addFile(u"../images/icons/list_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.menu)

        self.fullscreen = QPushButton(self.controlPanel)
        self.fullscreen.setObjectName(u"fullscreen")
        sizePolicy3.setHeightForWidth(self.fullscreen.sizePolicy().hasHeightForWidth())
        self.fullscreen.setSizePolicy(sizePolicy3)
        self.fullscreen.setMinimumSize(QSize(50, 50))
        icon7 = QIcon()
        icon7.addFile(u"../images/icons/fullscreen_FILL0_wght400_GRAD0_opsz48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fullscreen.setIcon(icon7)
        self.fullscreen.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.fullscreen)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.main.addWidget(self.controlPanel)


        self.horizontalLayout.addLayout(self.main)

        self.rightPanel = QFrame(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.frame_2 = QVBoxLayout(self.rightPanel)
        self.frame_2.setSpacing(10)
        self.frame_2.setObjectName(u"frame_2")
        self.info = QFrame(self.rightPanel)
        self.info.setObjectName(u"info")
        self.info.setMinimumSize(QSize(300, 30))
        self.info.setFrameShape(QFrame.Shape.StyledPanel)
        self.info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sourceInfo = QLabel(self.info)
        self.sourceInfo.setObjectName(u"sourceInfo")

        self.verticalLayout_3.addWidget(self.sourceInfo)

        self.line = QFrame(self.info)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.mediaInfo = QLabel(self.info)
        self.mediaInfo.setObjectName(u"mediaInfo")

        self.verticalLayout_3.addWidget(self.mediaInfo)


        self.frame_2.addWidget(self.info)

        self.fileList = QListWidget(self.rightPanel)
        self.fileList.setObjectName(u"fileList")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.fileList.sizePolicy().hasHeightForWidth())
        self.fileList.setSizePolicy(sizePolicy4)

        self.frame_2.addWidget(self.fileList)

        self.fileList.raise_()
        self.info.raise_()

        self.horizontalLayout.addWidget(self.rightPanel)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 33))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menu_File = QMenu(self.menubar)
        self.menu_File.setObjectName(u"menu_File")
        self.menu_Playback = QMenu(self.menubar)
        self.menu_Playback.setObjectName(u"menu_Playback")
        self.menu_Playback_speed = QMenu(self.menu_Playback)
        self.menu_Playback_speed.setObjectName(u"menu_Playback_speed")
        self.menu_Increasing_image_quality = QMenu(self.menubar)
        self.menu_Increasing_image_quality.setObjectName(u"menu_Increasing_image_quality")
        self.menu_Other = QMenu(self.menubar)
        self.menu_Other.setObjectName(u"menu_Other")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Playback.menuAction())
        self.menubar.addAction(self.menu_Increasing_image_quality.menuAction())
        self.menubar.addAction(self.menu_Other.menuAction())
        self.menu_File.addAction(self.action_Open_file)
        self.menu_File.addAction(self.action_Open_URL)
        self.menu_File.addAction(self.action_Open_folder)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Settings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Playback.addAction(self.action_Play_Pause)
        self.menu_Playback.addAction(self.menu_Playback_speed.menuAction())
        self.menu_Playback.addAction(self.action_Playlist)
        self.menu_Playback.addAction(self.action_Zoom_in)
        self.menu_Playback.addAction(self.action_Zoom_out)
        self.menu_Playback.addAction(self.action_Volume_minus)
        self.menu_Playback.addAction(self.action_Volume_plus)
        self.menu_Playback.addAction(self.action_Rewind_minus)
        self.menu_Playback.addAction(self.action_Rewind_plus)
        self.menu_Playback.addAction(self.action_Take_a_screenshot)
        self.menu_Playback.addSeparator()
        self.menu_Playback.addAction(self.action_Fullscreen)
        self.menu_Playback_speed.addAction(self.action_x025)
        self.menu_Playback_speed.addAction(self.action_x05)
        self.menu_Playback_speed.addAction(self.action_x075)
        self.menu_Playback_speed.addAction(self.action_x10)
        self.menu_Playback_speed.addAction(self.action_x125)
        self.menu_Playback_speed.addAction(self.action_x15)
        self.menu_Playback_speed.addAction(self.action_x175)
        self.menu_Playback_speed.addAction(self.action_x20)
        self.menu_Playback_speed.addAction(self.action_x225)
        self.menu_Playback_speed.addAction(self.action_x25)
        self.menu_Playback_speed.addAction(self.action_x275)
        self.menu_Playback_speed.addAction(self.action_x30)
        self.menu_Increasing_image_quality.addAction(self.action_Disable)
        self.menu_Increasing_image_quality.addSeparator()
        self.menu_Other.addAction(self.action_Reference)
        self.menu_Other.addAction(self.action_Create_config_Android)
        self.menu_Other.addAction(self.action_Launch_parameters)
        self.menu_Other.addAction(self.action_About)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Anime Player", None))
        self.action_Open_file.setText(QCoreApplication.translate("MainWindow", u"Open file", None))
        self.action_Open_URL.setText(QCoreApplication.translate("MainWindow", u"Open URL", None))
        self.action_Open_folder.setText(QCoreApplication.translate("MainWindow", u"Open folder", None))
        self.action_Close.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.action_Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.action_Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_Play_Pause.setText(QCoreApplication.translate("MainWindow", u"Play | Pause", None))
#if QT_CONFIG(shortcut)
        self.action_Play_Pause.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.action_Take_a_screenshot.setText(QCoreApplication.translate("MainWindow", u"Take a screenshot", None))
        self.action_Fullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.action_Disable.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.action_Reference.setText(QCoreApplication.translate("MainWindow", u"Reference", None))
        self.action_Create_config_Android.setText(QCoreApplication.translate("MainWindow", u"Create config for Android", None))
        self.action_Launch_parameters.setText(QCoreApplication.translate("MainWindow", u"Launch parameters", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_x025.setText(QCoreApplication.translate("MainWindow", u"x0.25", None))
        self.action_x05.setText(QCoreApplication.translate("MainWindow", u"x0.5", None))
        self.action_x075.setText(QCoreApplication.translate("MainWindow", u"x0.75", None))
        self.action_x10.setText(QCoreApplication.translate("MainWindow", u"x1.0", None))
        self.action_x125.setText(QCoreApplication.translate("MainWindow", u"x1.25", None))
        self.action_x15.setText(QCoreApplication.translate("MainWindow", u"x1.5", None))
        self.action_x175.setText(QCoreApplication.translate("MainWindow", u"x1.75", None))
        self.action_x20.setText(QCoreApplication.translate("MainWindow", u"x2.0", None))
        self.action_x225.setText(QCoreApplication.translate("MainWindow", u"x2.25", None))
        self.action_x25.setText(QCoreApplication.translate("MainWindow", u"x2.5", None))
        self.action_x275.setText(QCoreApplication.translate("MainWindow", u"x2.75", None))
        self.action_x30.setText(QCoreApplication.translate("MainWindow", u"x3.0", None))
        self.action_Rewind_plus.setText(QCoreApplication.translate("MainWindow", u"Rewind +5 sec", None))
#if QT_CONFIG(shortcut)
        self.action_Rewind_plus.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.action_Rewind_minus.setText(QCoreApplication.translate("MainWindow", u"Rewind -5 sec", None))
#if QT_CONFIG(shortcut)
        self.action_Rewind_minus.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.action_Volume_plus.setText(QCoreApplication.translate("MainWindow", u"Volume +10", None))
#if QT_CONFIG(shortcut)
        self.action_Volume_plus.setShortcut(QCoreApplication.translate("MainWindow", u"Up", None))
#endif // QT_CONFIG(shortcut)
        self.action_Volume_minus.setText(QCoreApplication.translate("MainWindow", u"Volume -10", None))
#if QT_CONFIG(shortcut)
        self.action_Volume_minus.setShortcut(QCoreApplication.translate("MainWindow", u"Down", None))
#endif // QT_CONFIG(shortcut)
        self.action_Zoom_in.setText(QCoreApplication.translate("MainWindow", u"Zoom in", None))
#if QT_CONFIG(shortcut)
        self.action_Zoom_in.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.action_Zoom_out.setText(QCoreApplication.translate("MainWindow", u"Zoom out", None))
#if QT_CONFIG(shortcut)
        self.action_Zoom_out.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.action_Playlist.setText(QCoreApplication.translate("MainWindow", u"Playlist", None))
        self.video.setText("")
        self.currentTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.allTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.prev.setText("")
        self.play.setText("")
        self.next.setText("")
        self.sub.setText("")
        self.audio.setText("")
        self.menu.setText("")
        self.fullscreen.setText("")
        self.sourceInfo.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.mediaInfo.setText(QCoreApplication.translate("MainWindow", u"Media info", None))
        self.menu_File.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menu_Playback.setTitle(QCoreApplication.translate("MainWindow", u"Playback", None))
        self.menu_Playback_speed.setTitle(QCoreApplication.translate("MainWindow", u"Playback speed", None))
        self.menu_Increasing_image_quality.setTitle(QCoreApplication.translate("MainWindow", u"Increasing image quality", None))
        self.menu_Other.setTitle(QCoreApplication.translate("MainWindow", u"Other", None))
    # retranslateUi

