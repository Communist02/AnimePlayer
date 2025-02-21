# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'android_config_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_AndroidConfigWindow(object):
    def setupUi(self, AndroidConfigWindow):
        if not AndroidConfigWindow.objectName():
            AndroidConfigWindow.setObjectName(u"AndroidConfigWindow")
        AndroidConfigWindow.resize(500, 340)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        AndroidConfigWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(AndroidConfigWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AndroidConfigWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(AndroidConfigWindow)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit = QLineEdit(AndroidConfigWindow)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_3 = QLabel(AndroidConfigWindow)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(AndroidConfigWindow)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.plainTextEdit = QPlainTextEdit(AndroidConfigWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selected = QPushButton(AndroidConfigWindow)
        self.selected.setObjectName(u"selected")

        self.horizontalLayout.addWidget(self.selected)

        self.all = QPushButton(AndroidConfigWindow)
        self.all.setObjectName(u"all")

        self.horizontalLayout.addWidget(self.all)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AndroidConfigWindow)

        QMetaObject.connectSlotsByName(AndroidConfigWindow)
    # setupUi

    def retranslateUi(self, AndroidConfigWindow):
        AndroidConfigWindow.setWindowTitle(QCoreApplication.translate("AndroidConfigWindow", u"Create config for Android", None))
        self.label.setText(QCoreApplication.translate("AndroidConfigWindow", u"You can use this config to use the Anime4K algorithm in the mpv video player on android", None))
        self.label_2.setText(QCoreApplication.translate("AndroidConfigWindow", u"Enter the path to the shaders", None))
        self.lineEdit.setText(QCoreApplication.translate("AndroidConfigWindow", u"/storage/emulated/0/mpv/shaders/", None))
        self.label_3.setText(QCoreApplication.translate("AndroidConfigWindow", u"Select the algorithm configuration", None))
        self.selected.setText(QCoreApplication.translate("AndroidConfigWindow", u"Selected", None))
        self.all.setText(QCoreApplication.translate("AndroidConfigWindow", u"All", None))
    # retranslateUi

