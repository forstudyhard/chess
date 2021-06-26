# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(446, 348)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.redside = QComboBox(Dialog)
        self.redside.addItem("")
        self.redside.addItem("")
        self.redside.setObjectName(u"redside")
        font = QFont()
        font.setFamily(u"DengXian")
        font.setPointSize(14)
        self.redside.setFont(font)

        self.gridLayout.addWidget(self.redside, 2, 1, 1, 1)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 3, 2, 1, 1)

        self.version = QLabel(Dialog)
        self.version.setObjectName(u"version")
        self.version.setFont(font)
        self.version.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.version, 5, 1, 1, 1)

        self.blackside = QComboBox(Dialog)
        self.blackside.addItem("")
        self.blackside.addItem("")
        self.blackside.setObjectName(u"blackside")
        self.blackside.setFont(font)

        self.gridLayout.addWidget(self.blackside, 2, 3, 1, 1)

        self.reverse = QCheckBox(Dialog)
        self.reverse.setObjectName(u"reverse")

        self.gridLayout.addWidget(self.reverse, 1, 1, 1, 1)

        self.transprancy = QSlider(Dialog)
        self.transprancy.setObjectName(u"transprancy")
        font1 = QFont()
        font1.setFamily(u"DengXian")
        font1.setPointSize(12)
        self.transprancy.setFont(font1)
        self.transprancy.setMinimum(0)
        self.transprancy.setMaximum(75)
        self.transprancy.setOrientation(Qt.Horizontal)
        self.transprancy.setTickPosition(QSlider.NoTicks)
        self.transprancy.setTickInterval(0)

        self.gridLayout.addWidget(self.transprancy, 0, 1, 1, 3)

        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.red_depth = QSpinBox(Dialog)
        self.red_depth.setObjectName(u"red_depth")
        self.red_depth.setFont(font)
        self.red_depth.setMaximum(10)
        self.red_depth.setValue(7)

        self.gridLayout.addWidget(self.red_depth, 3, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.black_depth = QSpinBox(Dialog)
        self.black_depth.setObjectName(u"black_depth")
        self.black_depth.setFont(font)
        self.black_depth.setMaximum(10)
        self.black_depth.setValue(1)

        self.gridLayout.addWidget(self.black_depth, 3, 3, 1, 1)

        self.delay = QSpinBox(Dialog)
        self.delay.setObjectName(u"delay")
        self.delay.setFont(font)
        self.delay.setMaximum(5000)
        self.delay.setValue(300)

        self.gridLayout.addWidget(self.delay, 4, 1, 1, 1)

        self.audio = QCheckBox(Dialog)
        self.audio.setObjectName(u"audio")
        self.audio.setChecked(True)

        self.gridLayout.addWidget(self.audio, 1, 3, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setFont(font)

        self.gridLayout.addWidget(self.cancel, 6, 3, 1, 1)

        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        self.ok.setFont(font)

        self.gridLayout.addWidget(self.ok, 6, 2, 1, 1)

        self.checkupdate = QPushButton(Dialog)
        self.checkupdate.setObjectName(u"checkupdate")
        self.checkupdate.setFont(font)

        self.gridLayout.addWidget(self.checkupdate, 5, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.redside.setItemText(0, QCoreApplication.translate("Dialog", u"\u68cb\u624b", None))
        self.redside.setItemText(1, QCoreApplication.translate("Dialog", u"\u7535\u8111", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u97f3\u6548", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u7ea2\u65b9", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u53cd\u8f6c\u68cb\u76d8", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u7248\u672c\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u9ed1\u65b9\u6df1\u5ea6", None))
        self.version.setText(QCoreApplication.translate("Dialog", u"1.1.0", None))
        self.blackside.setItemText(0, QCoreApplication.translate("Dialog", u"\u7535\u8111", None))
        self.blackside.setItemText(1, QCoreApplication.translate("Dialog", u"\u68cb\u624b", None))

        self.reverse.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u5f15\u64ce\u5ef6\u8fdf", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u9ed1\u65b9", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u7ea2\u65b9\u6df1\u5ea6", None))
        self.audio.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u900f\u660e\u5ea6", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"\u786e\u8ba4", None))
        self.checkupdate.setText(QCoreApplication.translate("Dialog", u"\u68c0\u67e5\u66f4\u65b0", None))
    # retranslateUi

