# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launch_parameters_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPlainTextEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LaunchParemetersWindow(object):
    def setupUi(self, LaunchParemetersWindow):
        if not LaunchParemetersWindow.objectName():
            LaunchParemetersWindow.setObjectName(u"LaunchParemetersWindow")
        LaunchParemetersWindow.resize(400, 300)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        LaunchParemetersWindow.setWindowIcon(icon)
        LaunchParemetersWindow.setStyleSheet(u"QDialog {\n"
"	background-color: rgb(245, 241, 235);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(87, 86, 86);\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: rgb(87, 86, 86);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(87, 86, 86);\n"
"	color: rgb(245, 241, 235);\n"
"}")
        self.verticalLayout = QVBoxLayout(LaunchParemetersWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(LaunchParemetersWindow)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.plainTextEdit = QPlainTextEdit(LaunchParemetersWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.buttonBox = QDialogButtonBox(LaunchParemetersWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(LaunchParemetersWindow)
        self.buttonBox.accepted.connect(LaunchParemetersWindow.accept)
        self.buttonBox.rejected.connect(LaunchParemetersWindow.reject)

        QMetaObject.connectSlotsByName(LaunchParemetersWindow)
    # setupUi

    def retranslateUi(self, LaunchParemetersWindow):
        LaunchParemetersWindow.setWindowTitle(QCoreApplication.translate("LaunchParemetersWindow", u"Launch paremeters", None))
        self.label.setText(QCoreApplication.translate("LaunchParemetersWindow", u"Use the mpv manual https://mpv.io/manual/\n"
"But keep in mind that Python syntax is required.\n"
"For example, instead of --volume=50 use player.volume = 50", None))
    # retranslateUi

