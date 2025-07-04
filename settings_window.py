# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
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
        SettingsWindow.resize(254, 242)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.language.addItem("")
        self.language.setObjectName(u"language")

        self.horizontalLayout.addWidget(self.language)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_style = QLabel(SettingsWindow)
        self.label_style.setObjectName(u"label_style")

        self.horizontalLayout_3.addWidget(self.label_style)

        self.comboBox_style = QComboBox(SettingsWindow)
        self.comboBox_style.setObjectName(u"comboBox_style")

        self.horizontalLayout_3.addWidget(self.comboBox_style)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_palette = QLabel(SettingsWindow)
        self.label_palette.setObjectName(u"label_palette")

        self.horizontalLayout_2.addWidget(self.label_palette)

        self.comboBox_palette = QComboBox(SettingsWindow)
        self.comboBox_palette.setObjectName(u"comboBox_palette")

        self.horizontalLayout_2.addWidget(self.comboBox_palette)


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
        self.language.setItemText(3, QCoreApplication.translate("SettingsWindow", u"Japanese", None))

        self.label_style.setText(QCoreApplication.translate("SettingsWindow", u"Style", None))
        self.label_palette.setText(QCoreApplication.translate("SettingsWindow", u"Palette", None))
        self.comboBox_palette.setCurrentText("")
        self.openLastFile.setText(QCoreApplication.translate("SettingsWindow", u"On startup open the last opened file", None))
        self.posLastFile.setText(QCoreApplication.translate("SettingsWindow", u"Set the position of the last opened file", None))
        self.volumePlus.setText(QCoreApplication.translate("SettingsWindow", u"Increase maxumum volume up to 150%", None))
        self.svp.setText(QCoreApplication.translate("SettingsWindow", u"Activate SVP", None))
    # retranslateUi

