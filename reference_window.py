# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reference_window.ui'
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
    QPlainTextEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_ReferenceWindow(object):
    def setupUi(self, ReferenceWindow):
        if not ReferenceWindow.objectName():
            ReferenceWindow.setObjectName(u"ReferenceWindow")
        ReferenceWindow.resize(1024, 720)
        icon = QIcon()
        icon.addFile(u"../favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        ReferenceWindow.setWindowIcon(icon)
        ReferenceWindow.setStyleSheet(u"QDialog {\n"
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
        self.verticalLayout = QVBoxLayout(ReferenceWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(ReferenceWindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setInputMethodHints(Qt.ImhNone)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.buttonBox = QDialogButtonBox(ReferenceWindow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ReferenceWindow)
        self.buttonBox.accepted.connect(ReferenceWindow.accept)
        self.buttonBox.rejected.connect(ReferenceWindow.reject)

        QMetaObject.connectSlotsByName(ReferenceWindow)
    # setupUi

    def retranslateUi(self, ReferenceWindow):
        ReferenceWindow.setWindowTitle(QCoreApplication.translate("ReferenceWindow", u"Reference", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("ReferenceWindow", u"Advanced Usage Instructions (GLSL / MPV) (v4.x)\n"
"\n"
"Anime4K has 3 major modes, as the small CNN networks cannot learn effectively every type of distribution shift\n"
"and degradation seen in the wild. Human judgement will serve (for now) as the stopgap solution. Usually the correct\n"
"mode is the one that looks best.\n"
"\n"
"The easiest way is to first visually inspect each mode in the A-B-C order. Mode A has the most visible artifacts of the\n"
"three modes if used incorrectly. B and C can be harder to distinguish for lower resolution anime.\n"
"\n"
"If you want increased perceptual quality, use the corresponding secondary mode.\n"
"\n"
"| Primary Mode | Corresponding Secondary Mode |\n"
"|--------------|------------------------------|\n"
"| A            | A+A                          |\n"
"| B            | B+B                          |\n"
"| C            | C+A                          |\n"
"\n"
"Here's what each mode is optimized for and what it does:\n"
"\n"
"Modes: A\n"
"Optimized for: Most 1080p a"
                        "nime. Some older 720p anime. Most old SD anime. (High amounts of blur). (A lot of resampling artifacts). (Smearing due to compression)\n"
"Positive effects: High perceptual quality. Reduces compression artifacts. Reconstructs most degraded lines. Reduces large amounts of blur. Reduces noise\n"
"Negative effects (If used incorrectly): Can amplify ringing if already presentCan amplify banding if already present. Strong denoising might blur textures\n"
"\n"
"Modes: B\n"
"Optimized for: Some 1080p anime. Most 720p anime. 1080p->720p downscaled anime. (Low amounts of blur). (Some resampling artifacts). (Ringing due to downsampling)\n"
"Positive effects: Reduces compression artifacts. Reconstructs some degraded lines. Reduces some blur. Reduces noise. Reduces ringing. Reduces aliasing\n"
"Negative effects (If used incorrectly): Some artifacts might not be removed. Some lines might still be blurry. Strong denoising might blur textures\n"
"\n"
"Modes: C\n"
"Optimized for: 1080p->480p downscaled anime. Very rarely, 108"
                        "0p animated movies. Images with no degradation. Wallpapers. Pixiv art\n"
"Positive effects: Highest PSNR. Reduces noise\n"
"Negative effects (If used incorrectly): Low perceptual quality. Can amplify ringing if already present. Can amplify resampling artifacts\n"
"\n"
"Modes: A+A*\n"
"Optimized for: Same as A\n"
"Positive effects: Highest perceptual quality. Reconstructs almost all degraded lines. Same positive effects from mode A\n"
"Negative effects (If used incorrectly): Can cause severe ringing. Can cause banding. Can cause aliasing. Same negative effects from mode A. Slower than mode A\n"
"\n"
"Modes: B+B*\n"
"Optimized for: Same as B\n"
"Positive effects: High perceptual quality. Same positive effects from mode B\n"
"Negative effects (If used incorrectly): Same negative effects from mode B. Slower than mode B\n"
"\n"
"Modes: C+A*\n"
"Optimized for: Same as C\n"
"Positive effects: Slightly higher perceptual quality. Same positive effects from mode C\n"
"Negative effects (If used incorrectly): Same negativ"
                        "e effects from mode C. Slower than mode C\n"
"\n"
"*These modes should only be used on upscaling ratios of x2 or higher. If you have a 1080p screen, using mode A on\n"
"1080p anime will improve image quality, but mode A+A will most likely oversharpen and degrade the image.\n"
"\n"
"Advanced Customization\n"
"\n"
"Not satisfied from simply using the default options? Curious about unsupported/weird modes such as B+A, A+B or B+A\n"
"+A ? This quick guide will get you started on customizing your own restoration pipeline.\n"
"\n"
"First, the basics.\n"
"   \u2022 All the shaders can be used standalone or in combination with any other shaders.\n"
"   \u2022 You can only use each shader file once. Using the same file two or more times causes buggy behaviour and loss of\n"
"     performance. Either use a different variant or copy and rename the duplicate shaders.\n"
"   \u2022 The shaders process the image in the same order as the filename order given in input.conf. One exception is\n"
"     Clamp_Highlights, explaine"
                        "d in the table below.\n"
"   \u2022 You are free to choose the CNN variant (S, M, L, VL, UL) for better speed or quality. Each step in size for CNN\n"
"     shaders doubles the processing time. For example, if the M version takes 5ms to run, the L version should take\n"
"     approximately 10ms to run, 20ms for VL and so on.\n"
"   \u2022 Non-CNN shaders are significantly faster but might be of lower quality.\n"
"\n"
"Quick explanation of each shader type:\n"
"\n"
"Restore\n"
"The shader that makes Anime4K different from other upscalers. Restores image, best used before upscaling. Removes compression artifacts, blur, ringing, etc. Restore is more optimized for upsampling artifacts and blur, while Restore_Soft is more optimized for downsampling artifacts and aliasing.\n"
"\n"
"Upscale\n"
"Upscales an image by a factor of x2, assumes image contains no degradation.\n"
"\n"
"Upscale_Denoise\n"
"Upscales an image by a factor of x2 and denoises it with no GPU performance penality.\n"
"\n"
"Clamp_Highlights\n"
"Compu"
                        "tes and saves image statistics at the location it is placed in the shader stage, then clamps the image highlights at the end after all the shaders to prevent overshoot and reduce ringing.\n"
"\n"
"Darken\n"
"Darkens lines in image. As what constitutes a line is ambiguous, might darken other stuff. Use according to personal taste.\n"
"\n"
"Thin\n"
"Makes lines thinner in image. As what constitutes a line is ambiguous, might thin other stuff. Use according to personal taste.\n"
"\n"
"Denoise\n"
"Applies a denoising filter to the image.\n"
"\n"
"Deblur\n"
"Applies a deblur filter to the image. Sharpens details without overshoot or ringing.\n"
"\n"
"AutoDownscalePre_x4\n"
"Downscales an image after a first upscaling step, so that the second x2 upscaling step exactly matches screen size. This improves performance without noticeably impacting quality as you will not be working with images larger than the screen size. Should be placed between two Upscale shaders. Without this shader, the default behaviour is to downs"
                        "cale to the screen size after running all shaders.\n"
"\n"
"AutoDownscalePre_x2\n"
"Downscales an image after a first upscaling step to match screen size. This improves performance without noticeably impacting quality as you will not be working with images larger than the screen size. Should be placed after the first Upscale shader. Without this shader, the default behaviour is to downscale to the screen size after running all shaders.\n"
"\n"
"\n"
"Overview of default modes:\n"
"\n"
"| Mode | Shaders                                            |\n"
"|------|----------------------------------------------------|\n"
"| A    | Restore -> Upscale -> Upscale                      |\n"
"| B    | Restore_Soft -> Upscale -> Upscale                 |\n"
"| C    | Upscale_Denoise -> Upscale                         |\n"
"| A+A  | Restore -> Upscale -> Restore -> Upscale           |\n"
"| B+B  | Restore_Soft -> Upscale -> Restore_Soft -> Upscale |\n"
"| C+A  | Upscale_Denoise -> Restore -> Upscale              |\n"
"\n"
"\n"
""
                        "Note: Clamp_Highlights and AutoDownscalePre were removed from table for clarity.\n"
" How the modes are defined:\n"
"    \u2022 Mode A is defined initially as: Restore -> Upscale\n"
"    \u2022 Mode B is defined initially as: Restore_Soft -> Upscale\n"
"    \u2022 Mode C is defined initially as: Upscale\n"
"    \u2022 If the mode does not start with a Restore shader, it must start with a Upscale_Denoise or Denoise shader, as\n"
"      almost every video compression algorithm is lossy.\n"
"    \u2022 All modes have to add upscale shaders until the entire shader pipeline upscales at least 4x. A reasonable\n"
"      assumption is the smallest reasonable video size being 480p and the largest screen being 4K, upscaling at 4x is\n"
"      close to the 4.5x of 480p->4K.\n"
"\n"
"With the definitions above, we can see for example, what C+A+B is.\n"
"   1. Initial definition:\n"
"      C (Upscale) -> A (Restore -> Upscale) -> B (Restore_Soft -> Upscale)\n"
"   2. All modes have to start with restore/denoise:\n"
"      "
                        "C (Upscale_Denoise) -> A (Restore -> Upscale) -> B (Restore_Soft -> Upscale)\n"
"   3. Upscale ratio of 4x is already met.\n"
"   4. C+A+B is:\n"
"      Upscale_Denoise -> Restore -> Upscale -> Restore_Soft -> Upscale\n"
"   5. Shader variants (S/M/L/VL/UL) can be chosen at will.\n"
"Best Practices\n"
"\n"
"It is recommended to always include Clamp_Highlights at the beginning to prevent ringing in some anime, but\n"
"removing it will slightly improve speed.\n"
"\n"
"Adding a Restore shader after an upscaling step improves perceptual quality, but makes processing slower and might\n"
"introduce artifacts.\n"
"\n"
"Shaders applied after a x2 upscaling step will take four times the processing time. For example, if a shader takes 10ms to\n"
"run when placed before a upscaler, it will need 40ms if placed after the upscaler. This can be counteracted by using a\n"
"smaller CNN variant two steps below. (eg. S instead of L)\n"
"\n"
"Artifacts introduced by lower quality shaders (eg. M or S variants) usually are not noti"
                        "ceable when working at very high\n"
"resolutions. This advantage can be used to reduce GPU fan noise/heat and power use if you do not mind slightly lower\n"
"image quality.\n"
"\n"
"The target for 24fps video is usually ~41ms. Frame drops will appear if the GPU cannot keep up. If that happens, use\n"
"lower quality/faster shader variants. Use the mpv profiler (press Shift+I and then 2 on the keyboard's top row) to verify\n"
"whether your GPU can keep up.\n"
"\n"
"| Video Framerate | Maximum time (ms) |\n"
"|-----------------|-------------------|\n"
"| 24              | 41                |\n"
"| 30              | 33                |\n"
"| 60              | 16                |\n"
"", None))
    # retranslateUi

