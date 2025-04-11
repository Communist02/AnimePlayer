# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_folder_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OpenFolderWindow(object):
    def setupUi(self, OpenFolderWindow):
        if not OpenFolderWindow.objectName():
            OpenFolderWindow.setObjectName(u"OpenFolderWindow")
        OpenFolderWindow.resize(550, 120)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        OpenFolderWindow.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(OpenFolderWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(OpenFolderWindow)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(OpenFolderWindow)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox)

        self.select = QPushButton(OpenFolderWindow)
        self.select.setObjectName(u"select")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.select.sizePolicy().hasHeightForWidth())
        self.select.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.select)

        self.paste = QPushButton(OpenFolderWindow)
        self.paste.setObjectName(u"paste")

        self.horizontalLayout.addWidget(self.paste)

        self.clear = QPushButton(OpenFolderWindow)
        self.clear.setObjectName(u"clear")

        self.horizontalLayout.addWidget(self.clear)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(OpenFolderWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy3)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(OpenFolderWindow)
        self.buttonBox.accepted.connect(OpenFolderWindow.accept)
        self.buttonBox.rejected.connect(OpenFolderWindow.reject)

        QMetaObject.connectSlotsByName(OpenFolderWindow)
    # setupUi

    def retranslateUi(self, OpenFolderWindow):
        OpenFolderWindow.setWindowTitle(QCoreApplication.translate("OpenFolderWindow", u"Opening a folder", None))
        self.label.setText(QCoreApplication.translate("OpenFolderWindow", u"Select a folder", None))
        self.select.setText(QCoreApplication.translate("OpenFolderWindow", u"Select", None))
        self.paste.setText(QCoreApplication.translate("OpenFolderWindow", u"Paste", None))
        self.clear.setText(QCoreApplication.translate("OpenFolderWindow", u"Clear", None))
    # retranslateUi

