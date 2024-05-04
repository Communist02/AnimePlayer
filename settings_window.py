# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(254, 206)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(SettingsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.language = QComboBox(SettingsWindow)
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.language.setObjectName(u"language")

        self.horizontalLayout.addWidget(self.language)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelTheme = QLabel(SettingsWindow)
        self.labelTheme.setObjectName(u"labelTheme")

        self.horizontalLayout_2.addWidget(self.labelTheme)

        self.theme = QComboBox(SettingsWindow)
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.addItem("")
        self.theme.setObjectName(u"theme")

        self.horizontalLayout_2.addWidget(self.theme)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.openLastFile = QCheckBox(SettingsWindow)
        self.openLastFile.setObjectName(u"openLastFile")

        self.verticalLayout.addWidget(self.openLastFile)

        self.posLastFile = QCheckBox(SettingsWindow)
        self.posLastFile.setObjectName(u"posLastFile")

        self.verticalLayout.addWidget(self.posLastFile)

        self.volumePlus = QCheckBox(SettingsWindow)
        self.volumePlus.setObjectName(u"volumePlus")

        self.verticalLayout.addWidget(self.volumePlus)

        self.svp = QCheckBox(SettingsWindow)
        self.svp.setObjectName(u"svp")

        self.verticalLayout.addWidget(self.svp)

        self.buttonBox = QDialogButtonBox(SettingsWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SettingsWindow)
        self.buttonBox.accepted.connect(SettingsWindow.accept)
        self.buttonBox.rejected.connect(SettingsWindow.reject)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"Language selection", None))
        self.language.setItemText(0, QCoreApplication.translate("SettingsWindow", u"Auto", None))
        self.language.setItemText(1, QCoreApplication.translate("SettingsWindow", u"English", None))
        self.language.setItemText(2, QCoreApplication.translate("SettingsWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))

        self.labelTheme.setText(QCoreApplication.translate("SettingsWindow", u"Theme", None))
        self.theme.setItemText(0, QCoreApplication.translate("SettingsWindow", u"System", None))
        self.theme.setItemText(1, QCoreApplication.translate("SettingsWindow", u"Light", None))
        self.theme.setItemText(2, QCoreApplication.translate("SettingsWindow", u"Dark", None))

        self.theme.setCurrentText(QCoreApplication.translate("SettingsWindow", u"System", None))
        self.openLastFile.setText(QCoreApplication.translate("SettingsWindow", u"On startup open the last opened file", None))
        self.posLastFile.setText(QCoreApplication.translate("SettingsWindow", u"Set the position of the last opened file", None))
        self.volumePlus.setText(QCoreApplication.translate("SettingsWindow", u"Increase maxumum volume up to 150%", None))
        self.svp.setText(QCoreApplication.translate("SettingsWindow", u"Activate SVP", None))
    # retranslateUi

