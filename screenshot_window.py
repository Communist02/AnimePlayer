# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screenshot_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ScreenshotWindow(object):
    def setupUi(self, ScreenshotWindow):
        if not ScreenshotWindow.objectName():
            ScreenshotWindow.setObjectName(u"ScreenshotWindow")
        ScreenshotWindow.resize(540, 120)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ScreenshotWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ScreenshotWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ScreenshotWindow)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(ScreenshotWindow)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.select = QPushButton(ScreenshotWindow)
        self.select.setObjectName(u"select")

        self.horizontalLayout.addWidget(self.select)

        self.paste = QPushButton(ScreenshotWindow)
        self.paste.setObjectName(u"paste")

        self.horizontalLayout.addWidget(self.paste)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(ScreenshotWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Close|QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ScreenshotWindow)
        self.buttonBox.accepted.connect(ScreenshotWindow.accept)
        self.buttonBox.rejected.connect(ScreenshotWindow.reject)

        QMetaObject.connectSlotsByName(ScreenshotWindow)
    # setupUi

    def retranslateUi(self, ScreenshotWindow):
        ScreenshotWindow.setWindowTitle(QCoreApplication.translate("ScreenshotWindow", u"Screenshot", None))
        self.label.setText(QCoreApplication.translate("ScreenshotWindow", u"Enter folder path for screenshots", None))
        self.select.setText(QCoreApplication.translate("ScreenshotWindow", u"Select", None))
        self.paste.setText(QCoreApplication.translate("ScreenshotWindow", u"Paste", None))
    # retranslateUi

