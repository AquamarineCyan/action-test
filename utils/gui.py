#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# gui.py

import time
from pathlib import Path
from threading import Thread

from PySide6.QtGui import QIcon, QPixmap, QTextCursor
from PySide6.QtWidgets import QMainWindow, QMessageBox, QWidget, QComboBox

from .config import config
from .event import event_thread
from .log import log
from .mysignal import global_ms as ms
from .mythread import MyThread
from .upgrade import *
from .window import window
from ui.mainui import Ui_MainWindow
from package import *


class MainWindow(QMainWindow):
    _list_function = [  # 功能列表
        "1.组队御魂副本",
        "2.组队永生之海副本",
        "3.业原火副本",
        "4.御灵副本",
        "5.个人突破",
        "6.寮突破",
        "7.道馆突破",
        "8.普通召唤",
        "9.百鬼夜行",
        "10.限时活动",
        "11.组队日轮副本",
        # "12.探索beta"
    ]
    _package_ = [  # 图片素材文件夹
        "yuhun",
        "yongshengzhihai",
        "yeyuanhuo",
        "yuling",
        "jiejietupo",
        "daoguantupo",
        "zhaohuan",
        "baiguiyexing",
        "huodong"
    ]
    _choice: int  # 功能

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.setFixedSize(550, 450)  # 固定宽高
        self.ui.setupUi(self)
        # 窗口图标
        icon = QIcon()
        icon.addPixmap(QPixmap("buzhihuo.ico"))
        self.setWindowIcon(icon)
        self.setWindowTitle(f"Onmyoji_Python - v{config.version}")  # 版本号显示
        timenow = time.strftime("%H:%M:%S")
        try:
            log._write_to_file("[START]")
            log._write_to_file(f"{timenow} [VERSION] {config.version}")
        except:
            pass

        # 初始化控件
        self.ui.combo_choice.addItems(self._list_function)
        self.ui.button_start.setEnabled(False)
        self.ui.combo_choice.setEnabled(False)
        self.ui.spinB_num.setEnabled(False)
        self.ui.stackedWidget.setCurrentIndex(0)  # 索引0，空白
        self.ui.text_print.document().setMaximumBlockCount(50)
        # setting
        self.ui.setting_update_comboBox.addItems(
            config.config_default["更新模式"]
        )
        self.ui.setting_xuanshangfengyin_comboBox.addItems(
            config.config_default["悬赏封印"]
        )

        # 自定义信号
        # 弹窗更新
        ms.qmessagbox_update.connect(self.qmessagbox_update_func)
        # 主界面信息文本更新
        ms.text_print_update.connect(self.text_print_update_func)
        # 运行状态更新
        ms.is_fighting_update.connect(self.is_fighting)
        # 完成情况文本更新
        ms.text_num_update.connect(self.text_num_update_func)
        ms.setting_to_ui_update.connect(self.setting_to_ui_update_func)

        # 事件连接
        # 环境检测按钮
        self.ui.button_enviroment.clicked.connect(self.application_init)
        # 开始按钮
        self.ui.button_start.clicked.connect(self.start_stop)
        # 功能选择事件
        self.ui.combo_choice.currentIndexChanged.connect(self.choice_text)

        # 设置项
        # 更新模式
        self.ui.setting_update_comboBox.currentIndexChanged.connect(
            self.setting_update_comboBox_func
        )
        # 悬赏封印
        self.ui.setting_xuanshangfengyin_comboBox.currentIndexChanged.connect(
            self.setting_xuanshangfengyin_comboBox_func
        )

        # 程序开启运行
        # application_init
        thread_application_init = Thread(
            target=self.application_init,
            daemon=True
        )
        # thread_application_init.daemon = True
        thread_application_init.start()

    def application_init(self) -> None:
        """程序初始化"""
        def init_enviroment_testing_func():
            thread_enviroment_testing = Thread(
                target=self.enviroment_testing_func,
                daemon=True
            )
            # thread_enviroment_testing.daemon = True
            thread_enviroment_testing.start()
            thread_enviroment_testing.join()

        log.ui("未正确使用所产生的一切后果自负\n保持您的肝度与日常无较大差距\n")
        log.ui(f"application path:{config.application_path}")
        log.ui(f"resource path:{config.resource_path}")
        thread_upgrade = Thread(
            target=Upgrade().upgrade_auto,
            daemon=True
        )
        thread_upgrade.start()

        window.get_game_window_handle()
        init_enviroment_testing_func()
        log.ui("初始化完成")
        log.ui("主要战斗场景UI为「怀旧主题」，持续兼容部分新场景中，可在游戏内图鉴中设置")
        # 悬赏封印
        thread_xuanshang = Thread(
            target=xuanshangfengyin.xuanshangfengyin.judge,
            daemon=True
        )
        # thread_xuanshang.daemon = True
        thread_xuanshang.start()

    def qmessagbox_update_func(self, level: str, msg: str) -> None:
        match level:
            case "ERROR":
                QMessageBox.critical(self, level, msg)
            case "question":
                match msg:
                    case "强制缩放":
                        log.error("游戏窗口大小不匹配")
                        choice = QMessageBox.question(
                            self,
                            "窗口大小不匹配",
                            "是否强制缩放，如不缩放，请自行靠近1136*640或者替换pic文件夹中对应素材"
                        )
                        if choice == QMessageBox.Yes:
                            log._write_to_file("用户接受强制缩放")
                            window.force_zoom()
                        elif choice == QMessageBox.No:
                            log._write_to_file("用户拒绝强制缩放")

    def text_print_update_func(self, text: str) -> None:
        """输出内容至文本框

        WARN -> 红色

        SCENE -> 绿色

        Args:
            text(str): 文本内容
        """
        if "[WARN]" in text:
            self.ui.text_print.setTextColor("red")
        elif "[SCENE]" in text:
            self.ui.text_print.setTextColor("green")

        self.ui.text_print.append(text)
        # 自动换行
        self.ui.text_print.ensureCursorVisible()
        # 自动滑动到底
        self.ui.text_print.moveCursor(self.ui.text_print.textCursor().End)
        self.ui.text_print.setTextColor("black")

    def text_num_update_func(self, text: str) -> None:
        """输出内容至文本框“完成情况”

        Args:
            text (str): 文本
        """
        self.ui.text_num.setText(text)

    def setting_to_ui_update_func(self, key: str, text: str) -> None:
        match key:
            case "悬赏封印":
                self.ui.setting_xuanshangfengyin_comboBox.setCurrentText(text)

    def enviroment_testing_func(self) -> bool:
        """环境检测

        Returns:
            bool: 是否完成
        """
        log.info("环境检测中...")
        handle_coor = window.handle_coor
        # log检测
        if not log.init():
            ms.qmessagbox_update.emit("ERROR", "创建log目录失败，请重试！")
        # 图片资源检测
        elif not config.resource_path.exists():
            log.error("资源文件夹不存在")
            ms.qmessagbox_update.emit("ERROR", "资源文件夹不存在！")
        # 图片资源是否完整
        elif not self.resource_is_complete():
            pass
        # 游戏窗口检测
        elif handle_coor == (0, 0, 0, 0):
            log.error("未打开游戏")
            ms.qmessagbox_update.emit("ERROR", "请打开游戏！")
        elif handle_coor[0] < -9 or handle_coor[1] < 0 or handle_coor[2] < 0 or handle_coor[3] < 0:
            log.error("未前置游戏窗口")
            ms.qmessagbox_update.emit("ERROR", "请前置游戏窗口！")
        # 环境完整
        # TODO 解除窗口大小限制，待优化
        elif handle_coor[2] - handle_coor[0] != window.absolute_window_width and handle_coor[3] - handle_coor[
                1] != window.absolute_window_height:
            ms.qmessagbox_update.emit("question", "强制缩放")
        else:
            log.ui("环境完整")
            self.ui.combo_choice.setEnabled(True)
            self.ui.spinB_num.setEnabled(True)
            log.ui("移动游戏窗口后，点击下方“环境检测”即可\n请选择功能以加载内容")
            # 悬赏封印
            return True
        log.ui("环境损坏")
        return False

    def resource_is_complete(self) -> bool:
        """资源文件夹完整度

        Returns:
            bool: 是否完整
        """
        for i in range(len(self._package_)):
            flag = Path(config.resource_path.joinpath(
                self._package_[i])).exists()
            if not Path(config.resource_path.joinpath(self._package_[i])).exists():
                # QMessageBox.critical(self, "ERROR", f"无{self._package_[i]}文件夹")
                log.error(f"无{self._package_[i]}文件夹")
                ms.qmessagbox_update.emit("ERROR", f"无{self._package_[i]}文件夹")
                return False
        return True

    def setting_update_comboBox_func(self) -> None:
        """设置-更新模式-更改"""
        text = self.ui.setting_update_comboBox.currentText()
        log.info(f"设置项：更新模式已更改为 {text}")
        config.config_user_changed("更新模式", text)

    def setting_xuanshangfengyin_comboBox_func(self) -> None:
        """设置-悬赏封印-更改"""
        text = self.ui.setting_xuanshangfengyin_comboBox.currentText()
        log.info(f"设置项：悬赏封印已更改为 {text}")
        config.config_user_changed("悬赏封印", text)

    def choice_text(self):
        """功能描述"""
        text = self.ui.combo_choice.currentText()
        self.ui.button_start.setEnabled(True)
        self.ui.spinB_num.setEnabled(True)
        # self.is_fighting_yuhun(False)
        self.ui.stackedWidget.setCurrentIndex(0)  # 索引0，空白
        if text == self._list_function[0]:
            # 1.组队御魂副本
            self._choice = 1
            log.ui("请确保阵容稳定，仅适用于队友挂饼，不适用于极限卡速，默认打手\n待开发：手动第一次锁定阵容")
            self.ui.stackedWidget.setCurrentIndex(1)  # 索引1，御魂
            # 默认值
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 200)
            # self.is_fighting_yuhun(True)
            self.ui.button_driver_False.setChecked(True)
            self.ui.button_passengers_2.setChecked(True)
        elif text == self._list_function[1]:
            # 2.组队永生之海副本
            self._choice = 2
            log.ui("默认打手30次\n阴阳师技能自行选择，如晴明灭\n待开发：手动第一次锁定阵容")
            self.ui.stackedWidget.setCurrentIndex(1)  # 索引1，御魂
            # 默认值
            self.ui.spinB_num.setValue(30)
            self.ui.spinB_num.setRange(1, 100)
            # self.is_fighting_yuhun(True)
            self.ui.button_driver_False.setChecked(True)
            self.ui.button_passengers_2.setChecked(True)
        elif text == self._list_function[2]:
            # 3.业原火副本
            self._choice = 3
            log.ui("默认为“痴”，有“贪”“嗔”需求的，可替换pic路径下tiaozhan.png素材")
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 100)
        elif text == self._list_function[3]:
            # 4.御灵副本
            self._choice = 4
            log.ui("暗神龙-周二六日\n暗白藏主-周三六日\n暗黑豹-周四六\n暗孔雀-周五六日\n绘卷期间请减少使用")
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 100)
        elif text == self._list_function[4]:
            # 5.个人突破
            self._choice = 5
            log.ui("默认3胜刷新，上限30")
            # self.ui.stackedWidget.setCurrentIndex(2)  # 索引2，结界突破
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 30)
        elif text == self._list_function[5]:
            # 6.寮突破
            self._choice = 6
            now = time.strftime("%H:%M:%S")
            if now >= "21:00:00":
                log.warn("CD无限", True)
                log.ui("请尽情挑战，桌面版单账号上限100次")
            else:
                log.warn("CD受限", True)
                log.ui("默认6次，可在每日21时后无限挑战")
            log.ui("待开发：滚轮翻页")
            self.ui.spinB_num.setValue(6)
            self.ui.spinB_num.setRange(1, 200)
        elif text == self._list_function[6]:
            # 7.道馆突破
            self._choice = 7
            log.ui("目前仅支持正在进行中的道馆突破，无法实现跳转道馆场景\n待开发：冷却时间、观战助威")
            self.ui.stackedWidget.setCurrentIndex(3)  # 索引3，道馆突破
            self.ui.spinB_num.setEnabled(False)
        elif text == self._list_function[7]:
            # 8.普通召唤
            self._choice = 8
            log.ui("普通召唤，请选择十连次数")
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 100)
        elif text == self._list_function[8]:
            # 9.百鬼夜行
            self._choice = 9
            log.ui("仅适用于清票，且无法指定鬼王")
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 100)
        elif text == self._list_function[9]:
            # 10.限时活动
            self._choice = 10
            log.ui(
                "适用于限时活动及其他连点，请提前确保阵容完好并锁定，替换pic文件夹huodong下的title.png、tiaozhan.png，周年庆活动素材已替换"
            )
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 999)
        elif text == self._list_function[10]:
            # 11.组队日轮副本
            self._choice = 11
            log.ui("请确保阵容稳定，仅适用于队友挂饼，不适用于极限卡速，默认打手\n待开发：手动第一次锁定阵容")
            self.ui.stackedWidget.setCurrentIndex(1)  # 索引1，御魂
            # 默认值
            self.ui.spinB_num.setValue(1)
            self.ui.spinB_num.setRange(1, 100)
            self.ui.button_driver_False.setChecked(True)
            self.ui.button_passengers_2.setChecked(True)
        elif text == self._list_function[11]:
            # 12.探索beta
            self._choice = 12
            log.warn("测试功能", True)

    def start_stop(self) -> None:
        """开始&停止按钮"""

        def start() -> None:
            """开始函数"""
            n = self.ui.spinB_num.value()
            self.ui.text_num.clear()
            self.is_fighting(True)
            thread = None  # 线程
            match self._choice:
                case 1:
                    # 1.组队御魂副本
                    # 是否司机（默认否）
                    # 组队人数（默认2人）
                    driver = self.ui.buttonGroup_driver.checkedButton().text()
                    if driver == "否":
                        flag_driver = False
                    else:
                        flag_driver = True
                    flag_passengers = int(
                        self.ui.buttonGroup_passengers.checkedButton().text()
                    )
                    thread = Thread(
                        target=yuhun.YuHun().run,
                        args=(n, flag_driver, flag_passengers)
                    )
                    # 当前线程id
                    # print('main id', int(QThread.currentThreadId()))
                    # thread = MyThread(
                    #     func=yuhun.YuHun().run,
                    #     args=(n, flag_driver, flag_passengers)
                    # )
                    # self._thread.finished.connect(self._thread.deleteLater())
                case 2:
                    # 2.组队永生之海副本
                    # 是否司机（默认否）
                    driver = self.ui.buttonGroup_driver.checkedButton().text()
                    if driver == "否":
                        flag_driver = False
                    else:
                        flag_driver = True
                    thread = Thread(
                        target=yongshengzhihai.YongShengZhiHai().run,
                        args=(n, flag_driver)
                    )
                case 3:
                    # 3.业原火
                    thread = Thread(
                        target=yeyuanhuo.YeYuanHuo().run,
                        args=(n,)
                    )
                case 4:
                    # 4.御灵
                    thread = Thread(
                        target=yuling.YuLing().run,
                        args=(n,)
                    )
                case 5:
                    # 5.个人突破
                    thread = Thread(
                        target=jiejietupo.JieJieTuPoGeRen().run,
                        args=(n,)
                    )
                case 6:
                    # 6.寮突破
                    thread = Thread(
                        target=jiejietupo.JieJieTuPoYinYangLiao().run,
                        args=(n,)
                    )
                case 7:
                    # 7.道馆突破
                    flag_guanzhan = self.ui.button_guanzhan.isChecked()
                    thread = Thread(
                        target=daoguantupo.DaoGuanTuPo().run,
                        args=(flag_guanzhan,)
                    )
                case 8:
                    # 8.普通召唤
                    thread = Thread(
                        target=zhaohuan.ZhaoHuan().run,
                        args=(n,)
                    )
                case 9:
                    # 9.百鬼夜行
                    thread = Thread(
                        target=baiguiyexing.BaiGuiYeXing().run,
                        args=(n,)
                    )
                case 10:
                    # 10.限时活动
                    thread = Thread(target=huodong.HuoDong(n).run)
                case 11:
                    # 11.组队日轮副本
                    # 是否司机（默认否）
                    # 组队人数（默认2人）
                    driver = self.ui.buttonGroup_driver.checkedButton().text()
                    if driver == "否":
                        flag_driver = False
                    else:
                        flag_driver = True
                    flag_passengers = int(
                        self.ui.buttonGroup_passengers.checkedButton().text()
                    )
                    thread = Thread(
                        target=rilun.RiLun().run,
                        args=(n, flag_driver, flag_passengers)
                    )
                case 12:
                    thread = Thread(target=tansuo.TanSuo().running)
            # 线程存在
            if thread is not None:
                thread.daemon = True  # 线程守护
                thread.start()
            # 进行中
            self.is_fighting(True)

        def stop() -> None:
            """停止函数"""
            # ret = ctypes.windll.kernel32.TerminateThread(self._thread.handle, 0)
            # print('终止线程', self._thread.handle, ret)
            event_thread.set()
            print("尝试停止线程")

        match self.ui.button_start.text():
            case "开始":
                start()
            case "停止":  # TODO unable to use
                stop()
            case _:
                pass

    def is_fighting(self, flag: bool):
        """程序是否运行中，启用/禁用其他控件"""
        if flag:
            self.ui.button_start.setText("进行中")
        else:
            self.ui.button_start.setText("开始")
        self.ui.combo_choice.setEnabled(not flag)
        self.ui.spinB_num.setEnabled(not flag)
        self.ui.button_start.setEnabled(not flag)
        # 御魂类小按钮
        self.ui.button_driver_False.setEnabled(not flag)
        self.ui.button_driver_True.setEnabled(not flag)
        self.ui.button_passengers_2.setEnabled(not flag)
        self.ui.button_passengers_3.setEnabled(not flag)

    def is_fighting_yuhun(self, flag: bool):
        """初始化组队御魂副本默认配置，显示/隐藏其他控件"""
        if flag:
            self.ui.label_driver.show()
            self.ui.button_driver_False.show()
            self.ui.button_driver_True.show()
            self.ui.label_passengers.show()
            self.ui.button_passengers_2.show()
            self.ui.button_passengers_3.show()
            self.ui.button_driver_False.setChecked(True)
            self.ui.button_passengers_2.setChecked(True)
        else:
            self.ui.label_driver.hide()
            self.ui.button_driver_False.hide()
            self.ui.button_driver_True.hide()
            self.ui.label_passengers.hide()
            self.ui.button_passengers_2.hide()
            self.ui.button_passengers_3.hide()

    # 关闭程序
    def closeEvent(self, event) -> None:
        try:
            log._write_to_file("[EXIT]")
        except:
            pass
        event.accept()
