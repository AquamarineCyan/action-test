# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QComboBox,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QTabWidget, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 551, 451))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        self.tabWidget.setFont(font)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.groupBox_basic = QGroupBox(self.tab_home)
        self.groupBox_basic.setObjectName(u"groupBox_basic")
        self.groupBox_basic.setGeometry(QRect(4, 20, 231, 131))
        self.groupBox_basic.setFont(font)
        self.button_game_handle = QPushButton(self.groupBox_basic)
        self.button_game_handle.setObjectName(u"button_game_handle")
        self.button_game_handle.setGeometry(QRect(70, 90, 71, 23))
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(10)
        self.button_game_handle.setFont(font1)
        self.combo_choice = QComboBox(self.groupBox_basic)
        self.combo_choice.setObjectName(u"combo_choice")
        self.combo_choice.setGeometry(QRect(81, 24, 141, 19))
        font2 = QFont()
        font2.setFamilies([u"\u5b8b\u4f53"])
        font2.setPointSize(9)
        self.combo_choice.setFont(font2)
        self.label_function = QLabel(self.groupBox_basic)
        self.label_function.setObjectName(u"label_function")
        self.label_function.setGeometry(QRect(26, 27, 26, 15))
        self.label_function.setFont(font2)
        self.spinB_num = QSpinBox(self.groupBox_basic)
        self.spinB_num.setObjectName(u"spinB_num")
        self.spinB_num.setGeometry(QRect(81, 55, 51, 19))
        self.spinB_num.setFont(font1)
        self.spinB_num.setMaximum(999)
        self.label_numbers = QLabel(self.groupBox_basic)
        self.label_numbers.setObjectName(u"label_numbers")
        self.label_numbers.setGeometry(QRect(26, 57, 26, 15))
        self.groupBox_senior = QGroupBox(self.tab_home)
        self.groupBox_senior.setObjectName(u"groupBox_senior")
        self.groupBox_senior.setGeometry(QRect(6, 156, 231, 201))
        self.groupBox_senior.setFont(font)
        self.stackedWidget = QStackedWidget(self.groupBox_senior)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 20, 211, 161))
        self._0_none = QWidget()
        self._0_none.setObjectName(u"_0_none")
        self.stackedWidget.addWidget(self._0_none)
        self._1_yuhun = QWidget()
        self._1_yuhun.setObjectName(u"_1_yuhun")
        self.label_driver = QLabel(self._1_yuhun)
        self.label_driver.setObjectName(u"label_driver")
        self.label_driver.setGeometry(QRect(20, 55, 48, 21))
        self.label_driver.setFont(font2)
        self.button_driver_False = QRadioButton(self._1_yuhun)
        self.buttonGroup_driver = QButtonGroup(MainWindow)
        self.buttonGroup_driver.setObjectName(u"buttonGroup_driver")
        self.buttonGroup_driver.addButton(self.button_driver_False)
        self.button_driver_False.setObjectName(u"button_driver_False")
        self.button_driver_False.setGeometry(QRect(78, 55, 38, 20))
        self.button_driver_False.setFont(font2)
        self.button_driver_False.setMouseTracking(True)
        self.button_driver_True = QRadioButton(self._1_yuhun)
        self.buttonGroup_driver.addButton(self.button_driver_True)
        self.button_driver_True.setObjectName(u"button_driver_True")
        self.button_driver_True.setGeometry(QRect(128, 55, 38, 20))
        self.button_driver_True.setFont(font2)
        self.button_passengers_3 = QRadioButton(self._1_yuhun)
        self.buttonGroup_passengers = QButtonGroup(MainWindow)
        self.buttonGroup_passengers.setObjectName(u"buttonGroup_passengers")
        self.buttonGroup_passengers.addButton(self.button_passengers_3)
        self.button_passengers_3.setObjectName(u"button_passengers_3")
        self.button_passengers_3.setGeometry(QRect(128, 81, 33, 20))
        self.button_passengers_3.setFont(font2)
        self.button_passengers_2 = QRadioButton(self._1_yuhun)
        self.buttonGroup_passengers.addButton(self.button_passengers_2)
        self.button_passengers_2.setObjectName(u"button_passengers_2")
        self.button_passengers_2.setGeometry(QRect(79, 81, 33, 20))
        self.button_passengers_2.setFont(font2)
        self.label_passengers = QLabel(self._1_yuhun)
        self.label_passengers.setObjectName(u"label_passengers")
        self.label_passengers.setGeometry(QRect(20, 81, 48, 21))
        self.label_passengers.setFont(font2)
        self.label_tips = QLabel(self._1_yuhun)
        self.label_tips.setObjectName(u"label_tips")
        self.label_tips.setGeometry(QRect(20, 130, 141, 31))
        self.button_yuhun_drop_statistics = QCheckBox(self._1_yuhun)
        self.button_yuhun_drop_statistics.setObjectName(u"button_yuhun_drop_statistics")
        self.button_yuhun_drop_statistics.setGeometry(QRect(20, 109, 100, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_yuhun_drop_statistics.sizePolicy().hasHeightForWidth())
        self.button_yuhun_drop_statistics.setSizePolicy(sizePolicy)
        self.button_yuhun_drop_statistics.setMinimumSize(QSize(100, 0))
        self.button_yuhun_drop_statistics.setMaximumSize(QSize(100, 16777215))
        self.button_mode_single = QRadioButton(self._1_yuhun)
        self.buttonGroup_mode = QButtonGroup(MainWindow)
        self.buttonGroup_mode.setObjectName(u"buttonGroup_mode")
        self.buttonGroup_mode.addButton(self.button_mode_single)
        self.button_mode_single.setObjectName(u"button_mode_single")
        self.button_mode_single.setGeometry(QRect(128, 28, 51, 20))
        self.button_mode_single.setFont(font2)
        self.button_mode_team = QRadioButton(self._1_yuhun)
        self.buttonGroup_mode.addButton(self.button_mode_team)
        self.button_mode_team.setObjectName(u"button_mode_team")
        self.button_mode_team.setGeometry(QRect(78, 28, 51, 20))
        self.button_mode_team.setFont(font2)
        self.button_mode_team.setMouseTracking(True)
        self.label_mode = QLabel(self._1_yuhun)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setGeometry(QRect(20, 28, 48, 21))
        self.label_mode.setFont(font2)
        self.stackedWidget.addWidget(self._1_yuhun)
        self._2_jiejietupo = QWidget()
        self._2_jiejietupo.setObjectName(u"_2_jiejietupo")
        self.button_jiejietupo_3victory = QRadioButton(self._2_jiejietupo)
        self.button_jiejietupo_3victory.setObjectName(u"button_jiejietupo_3victory")
        self.button_jiejietupo_3victory.setGeometry(QRect(80, 60, 51, 20))
        self.button_kaji = QCheckBox(self._2_jiejietupo)
        self.button_kaji.setObjectName(u"button_kaji")
        self.button_kaji.setGeometry(QRect(80, 100, 47, 20))
        self.button_jiejietupo_9victory = QRadioButton(self._2_jiejietupo)
        self.button_jiejietupo_9victory.setObjectName(u"button_jiejietupo_9victory")
        self.button_jiejietupo_9victory.setGeometry(QRect(140, 60, 51, 20))
        self.label_refresh_rule = QLabel(self._2_jiejietupo)
        self.label_refresh_rule.setObjectName(u"label_refresh_rule")
        self.label_refresh_rule.setGeometry(QRect(10, 60, 48, 16))
        self.label_refresh_rule.setFont(font2)
        self.stackedWidget.addWidget(self._2_jiejietupo)
        self._3_daoguantupo = QWidget()
        self._3_daoguantupo.setObjectName(u"_3_daoguantupo")
        self.button_guanzhan = QCheckBox(self._3_daoguantupo)
        self.button_guanzhan.setObjectName(u"button_guanzhan")
        self.button_guanzhan.setGeometry(QRect(60, 40, 51, 20))
        self.stackedWidget.addWidget(self._3_daoguantupo)
        self._4_qiling = QWidget()
        self._4_qiling.setObjectName(u"_4_qiling")
        self.button_qiling_tancha = QCheckBox(self._4_qiling)
        self.button_qiling_tancha.setObjectName(u"button_qiling_tancha")
        self.button_qiling_tancha.setGeometry(QRect(30, 40, 51, 20))
        self.button_qiling_jieqi = QCheckBox(self._4_qiling)
        self.button_qiling_jieqi.setObjectName(u"button_qiling_jieqi")
        self.button_qiling_jieqi.setGeometry(QRect(30, 80, 51, 20))
        self.stackedWidget.addWidget(self._4_qiling)
        self.groupBox_info = QGroupBox(self.tab_home)
        self.groupBox_info.setObjectName(u"groupBox_info")
        self.groupBox_info.setGeometry(QRect(250, 10, 281, 411))
        self.groupBox_info.setFont(font)
        self.text_num = QLineEdit(self.groupBox_info)
        self.text_num.setObjectName(u"text_num")
        self.text_num.setEnabled(True)
        self.text_num.setGeometry(QRect(90, 30, 71, 21))
        self.text_num.setFont(font2)
        self.text_num.setMaxLength(32764)
        self.text_print = QTextBrowser(self.groupBox_info)
        self.text_print.setObjectName(u"text_print")
        self.text_print.setGeometry(QRect(10, 60, 261, 341))
        self.text_print.setFont(font)
        self.label_completion = QLabel(self.groupBox_info)
        self.label_completion.setObjectName(u"label_completion")
        self.label_completion.setGeometry(QRect(22, 32, 52, 17))
        self.label_completion.setFont(font)
        self.button_start = QPushButton(self.tab_home)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(70, 370, 81, 31))
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        font3.setPointSize(11)
        font3.setBold(True)
        self.button_start.setFont(font3)
        self.tabWidget.addTab(self.tab_home, "")
        self.tab_setting = QWidget()
        self.tab_setting.setObjectName(u"tab_setting")
        self.scrollArea = QScrollArea(self.tab_setting)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-4, -1, 551, 431))
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 532, 1000))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 1000))
        self.horizontalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 60, 451, 51))
        self.horizontalLayout_setting_update = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_setting_update.setObjectName(u"horizontalLayout_setting_update")
        self.horizontalLayout_setting_update.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_setting_update_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_update.addItem(self.horizontalSpacer_setting_update_left)

        self.setting_update_label = QLabel(self.horizontalLayoutWidget)
        self.setting_update_label.setObjectName(u"setting_update_label")
        self.setting_update_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_setting_update.addWidget(self.setting_update_label)

        self.horizontalSpacer_setting_update_middle = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_update.addItem(self.horizontalSpacer_setting_update_middle)

        self.setting_update_comboBox = QComboBox(self.horizontalLayoutWidget)
        self.setting_update_comboBox.setObjectName(u"setting_update_comboBox")

        self.horizontalLayout_setting_update.addWidget(self.setting_update_comboBox)

        self.horizontalSpacer_setting_update_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_update.addItem(self.horizontalSpacer_setting_update_right)

        self.horizontalLayout_setting_update.setStretch(0, 4)
        self.horizontalLayout_setting_update.setStretch(1, 2)
        self.horizontalLayout_setting_update.setStretch(3, 2)
        self.horizontalLayout_setting_update.setStretch(4, 4)
        self.horizontalLayoutWidget_2 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(40, 158, 451, 51))
        self.horizontalLayout_setting_xuanshangfengyin = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_setting_xuanshangfengyin.setObjectName(u"horizontalLayout_setting_xuanshangfengyin")
        self.horizontalLayout_setting_xuanshangfengyin.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_setting_xuanshangfengyin_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_xuanshangfengyin.addItem(self.horizontalSpacer_setting_xuanshangfengyin_left)

        self.setting_xuanshangfengyin_label = QLabel(self.horizontalLayoutWidget_2)
        self.setting_xuanshangfengyin_label.setObjectName(u"setting_xuanshangfengyin_label")
        self.setting_xuanshangfengyin_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_setting_xuanshangfengyin.addWidget(self.setting_xuanshangfengyin_label)

        self.horizontalSpacer_setting_xuanshangfengyin_middle = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_xuanshangfengyin.addItem(self.horizontalSpacer_setting_xuanshangfengyin_middle)

        self.setting_xuanshangfengyin_comboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.setting_xuanshangfengyin_comboBox.setObjectName(u"setting_xuanshangfengyin_comboBox")

        self.horizontalLayout_setting_xuanshangfengyin.addWidget(self.setting_xuanshangfengyin_comboBox)

        self.horizontalSpacer_setting_xuanshangfengyin_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_xuanshangfengyin.addItem(self.horizontalSpacer_setting_xuanshangfengyin_right)

        self.horizontalLayout_setting_xuanshangfengyin.setStretch(0, 4)
        self.horizontalLayout_setting_xuanshangfengyin.setStretch(1, 2)
        self.horizontalLayout_setting_xuanshangfengyin.setStretch(3, 2)
        self.horizontalLayout_setting_xuanshangfengyin.setStretch(4, 4)
        self.button_update_record = QPushButton(self.scrollAreaWidgetContents)
        self.button_update_record.setObjectName(u"button_update_record")
        self.button_update_record.setGeometry(QRect(310, 340, 75, 24))
        self.label_GitHub_address = QLabel(self.scrollAreaWidgetContents)
        self.label_GitHub_address.setObjectName(u"label_GitHub_address")
        self.label_GitHub_address.setGeometry(QRect(106, 380, 312, 16))
        self.label_GitHub_address.setFocusPolicy(Qt.NoFocus)
        self.label_GitHub_address.setLayoutDirection(Qt.LeftToRight)
        self.label_GitHub_address.setAlignment(Qt.AlignCenter)
        self.button_restart = QPushButton(self.scrollAreaWidgetContents)
        self.button_restart.setObjectName(u"button_restart")
        self.button_restart.setGeometry(QRect(155, 340, 75, 24))
        self.label_tip_setting_restart = QLabel(self.scrollAreaWidgetContents)
        self.label_tip_setting_restart.setObjectName(u"label_tip_setting_restart")
        self.label_tip_setting_restart.setGeometry(QRect(191, 22, 141, 21))
        self.label_tip_setting_restart.setMouseTracking(False)
        self.label_tip_setting_restart.setLayoutDirection(Qt.LeftToRight)
        self.label_tip_setting_restart.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_3 = QWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(40, 110, 451, 49))
        self.horizontalLayout_setting_update_download = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_setting_update_download.setObjectName(u"horizontalLayout_setting_update_download")
        self.horizontalLayout_setting_update_download.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_setting_update_download_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_update_download.addItem(self.horizontalSpacer_setting_update_download_left)

        self.setting_update_download_label = QLabel(self.horizontalLayoutWidget_3)
        self.setting_update_download_label.setObjectName(u"setting_update_download_label")
        self.setting_update_download_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_setting_update_download.addWidget(self.setting_update_download_label)

        self.horizontalSpacer_setting_update_download_middle = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_update_download.addItem(self.horizontalSpacer_setting_update_download_middle)

        self.setting_update_download_comboBox = QComboBox(self.horizontalLayoutWidget_3)
        self.setting_update_download_comboBox.setObjectName(u"setting_update_download_comboBox")

        self.horizontalLayout_setting_update_download.addWidget(self.setting_update_download_comboBox)

        self.horizontalSpacer_setting_update_download_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_setting_update_download.addItem(self.horizontalSpacer_setting_update_download_right)

        self.horizontalLayout_setting_update_download.setStretch(0, 4)
        self.horizontalLayout_setting_update_download.setStretch(1, 2)
        self.horizontalLayout_setting_update_download.setStretch(3, 2)
        self.horizontalLayout_setting_update_download.setStretch(4, 4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_setting, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_basic.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u529f\u80fd", None))
        self.button_game_handle.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u68c0\u6d4b", None))
        self.combo_choice.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u529f\u80fd", None))
        self.label_function.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u529f\u80fd</span></p></body></html>", None))
        self.label_numbers.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u6b21\u6570</span></p></body></html>", None))
        self.groupBox_senior.setTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u8bbe\u7f6e", None))
        self.label_driver.setText(QCoreApplication.translate("MainWindow", u"\u662f\u5426\u53f8\u673a", None))
        self.button_driver_False.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.button_driver_True.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.button_passengers_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_passengers_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_passengers.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u961f\u4eba\u6570", None))
        self.label_tips.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.button_yuhun_drop_statistics.setText(QCoreApplication.translate("MainWindow", u"\u6389\u843d\u7edf\u8ba1beta", None))
        self.button_mode_single.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4eba", None))
        self.button_mode_team.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u961f", None))
        self.label_mode.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f", None))
        self.button_jiejietupo_3victory.setText(QCoreApplication.translate("MainWindow", u"3\u80dc", None))
        self.button_kaji.setText(QCoreApplication.translate("MainWindow", u"\u5361\u7ea7", None))
        self.button_jiejietupo_9victory.setText(QCoreApplication.translate("MainWindow", u"9\u80dc", None))
        self.label_refresh_rule.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0\u89c4\u5219", None))
        self.button_guanzhan.setText(QCoreApplication.translate("MainWindow", u"\u89c2\u6218", None))
        self.button_qiling_tancha.setText(QCoreApplication.translate("MainWindow", u"\u63a2\u67e5", None))
        self.button_qiling_jieqi.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u5951", None))
        self.groupBox_info.setTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f", None))
        self.text_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210\u60c5\u51b5", None))
        self.text_print.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u4fe1\u606f", None))
        self.label_completion.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u5b8c\u6210\u60c5\u51b5</span></p></body></html>", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.setting_update_label.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u6a21\u5f0f", None))
        self.setting_xuanshangfengyin_label.setText(QCoreApplication.translate("MainWindow", u"\u60ac\u8d4f\u5c01\u5370", None))
        self.button_update_record.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u8bb0\u5f55", None))
        self.label_GitHub_address.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" text-decoration: underline;\">https://github.com/AquamarineCyan/Onmyoji_Python</span></p></body></html>", None))
        self.button_restart.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u542f", None))
        self.label_tip_setting_restart.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u5206\u8bbe\u7f6e\u9700\u8981\u91cd\u542f\u751f\u6548", None))
        self.setting_update_download_label.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u7ebf\u8def", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_setting), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

