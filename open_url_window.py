# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'open_url_window.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_OpenURLWindow(object):
    def setupUi(self, OpenURLWindow):
        if not OpenURLWindow.objectName():
            OpenURLWindow.setObjectName(u"OpenURLWindow")
        OpenURLWindow.resize(550, 120)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        OpenURLWindow.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(OpenURLWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(OpenURLWindow)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(OpenURLWindow)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMaximumSize(QSize(350, 16777215))
        self.comboBox.setEditable(True)

        self.horizontalLayout.addWidget(self.comboBox)

        self.paste = QPushButton(OpenURLWindow)
        self.paste.setObjectName(u"paste")

        self.horizontalLayout.addWidget(self.paste)

        self.clear = QPushButton(OpenURLWindow)
        self.clear.setObjectName(u"clear")

        self.horizontalLayout.addWidget(self.clear)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(OpenURLWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy2)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(OpenURLWindow)
        self.buttonBox.accepted.connect(OpenURLWindow.accept)
        self.buttonBox.rejected.connect(OpenURLWindow.reject)

        QMetaObject.connectSlotsByName(OpenURLWindow)
    # setupUi

    def retranslateUi(self, OpenURLWindow):
        OpenURLWindow.setWindowTitle(QCoreApplication.translate("OpenURLWindow", u"Openning a link", None))
        self.label.setText(QCoreApplication.translate("OpenURLWindow", u"Enter the URL", None))
        self.paste.setText(QCoreApplication.translate("OpenURLWindow", u"Paste", None))
        self.clear.setText(QCoreApplication.translate("OpenURLWindow", u"Clear", None))
    # retranslateUi

