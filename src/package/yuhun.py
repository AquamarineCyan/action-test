#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# yuhun.py
"""御魂副本"""

import pyautogui

from ..utils.decorator import log_function_call
from ..utils.event import event_thread
from ..utils.function import (
    RESOURCE_FIGHT_PATH,
    check_scene_multiple_once,
    click,
    finish,
    finish_random_left_right,
    is_passengers_on_position,
    random_sleep,
    result
)
from ..utils.log import logger
from ..utils.window import window
from .utils import Package


class YuHun(Package):
    """御魂副本"""
    scene_name = "御魂副本"
    resource_path = "yuhun"
    resource_list = [
        "title_10",  # 魂十
        "title_11",  # 魂土
        "title_12",  # 神罚
        "xiezhanduiwu",  # 组队界面
        "passenger_2",  # 队员2
        "passenger_3",  # 队员3
        "start_team",  # 组队挑战
        "start_single",  # 单人挑战
        "fighting",  # 魂土进行中
        "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
        "fighting_shenfa",  # 神罚战斗场景
        "finish_damage",  # 结束特征图像
        "finish_damage_2000",  # 结束特征图像-鎏金圣域
        "finish_damage_shenfa",  # 结束特征图像-神罚
        "accept_invitation",  # 接受邀请
    ]
    description = "已适配组队/单人 魂十、魂土、神罚副本\
                    新设备第一次接受邀请会有弹窗，需手动勾选“不再提醒”"
    fast_time = 13 - 2

    @log_function_call
    def start(self) -> None:
        """挑战"""
        if isinstance(self, YuHunTeam):
            self.check_click("start_team")
        elif isinstance(self, YuHunSingle):
            self.check_click("start_single")


class YuHunTeam(YuHun):
    """组队御魂副本"""
    scene_name = "组队御魂副本"
    resource_list = [  # 资源列表
        "xiezhanduiwu",  # 组队界面
        "passenger_2",  # 队员2
        "passenger_3",  # 队员3
        "start_team",  # 组队挑战
        "fighting",  # 魂土进行中
        "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
        "fighting_shenfa",  # 神罚战斗场景
        "finish_damage",  # 结束特征图像
        "finish_damage_2000",  # 结束特征图像-鎏金圣域
        "finish_damage_shenfa",  # 结束特征图像-神罚
        "accept_invitation",  # 接受邀请
    ]

    @log_function_call
    def __init__(
        self,
        n: int = 0,
        flag_driver: bool = False,
        flag_passengers: int = 2,
        flag_drop_statistics: bool = False
    ) -> None:
        super().__init__(n)
        """组队御魂副本

        参数:
            n (int): 次数，默认0次
            flag_driver (bool): 是否司机，默认否
            flag_passengers (int): 组队人数，默认2人
            flag_drop_statistics (bool): 是否开启掉落统计，默认否
        """
        self.flag_driver: bool = flag_driver  # 是否为司机（默认否）
        self.flag_passengers: int = flag_passengers  # 组队人数
        self.flag_drop_statistics: bool = flag_drop_statistics  # 是否开启掉落统计

    @log_function_call
    def finish(self):
        """结束

        掉落物大体分为2种情况：
        1.正常情况，达摩蛋能被识别
        2.掉落过多情况（指神罚一排紫蛇皮），达摩蛋被遮挡，此时贪吃鬼必定（可能）出现
        """
        _flag_screenshot = True
        _flag_first = True
        result()
        random_sleep(0.4, 0.8)
        # 结算
        coor = finish_random_left_right(False, is_multiple_drops_x=True)

        if event_thread.is_set():
            return
        pyautogui.moveTo(coor.x + window.window_left, coor.y + window.window_top, duration=0.25)
        pyautogui.doubleClick()
        while True:
            if event_thread.is_set():
                return
            # 检测到任一图像
            scene, coor = check_scene_multiple_once([
                f"{RESOURCE_FIGHT_PATH}/finish",
                f"{self.resource_path}/finish_2000",
                f"{RESOURCE_FIGHT_PATH}/tanchigui"
            ])
            if coor.is_effective:
                if _flag_screenshot and self.flag_drop_statistics:
                    self.screenshot()
                    _flag_screenshot = False
                click()
                _flag_first = False
                random_sleep(0.6, 1)
            # 所有图像都未检测到，退出循环
            elif _flag_first:
                continue
            elif coor.is_zero:
                logger.ui("结束")
                return

    def run(self):
        # 保留必需图像，提高识别效率
        _g_resource_list: list = [
            f"{self.resource_path}/xiezhanduiwu",  # 组队界面
            # f"{RESOURCE_FIGHT_PATH}/start_team",  # 组队挑战
            f"{RESOURCE_FIGHT_PATH}/fighting_friend_default",  # 战斗中好友图标
            f"{RESOURCE_FIGHT_PATH}/fighting_friend_linshuanghanxue",
            f"{RESOURCE_FIGHT_PATH}/fighting_friend_chunlvhanqing",
            f"{RESOURCE_FIGHT_PATH}/accept_invitation"  # 接受邀请
        ]
        if self.flag_driver:
            _g_resource_list.append(f"{RESOURCE_FIGHT_PATH}/start_team")
        _resource_list: list = None
        _flag_title_msg: bool = True

        logger.num(f"0/{self.max}")
        while self.n < self.max:
            if event_thread.is_set():
                return
            _resource_list = _g_resource_list if _resource_list is None else _resource_list
            scene, coor = check_scene_multiple_once(_resource_list)
            if scene is None:
                continue
            self.scene_handle(scene)

            match self.current_scene:
                case "xiezhanduiwu":
                    logger.ui('组队界面准备中')
                    if self.flag_driver:
                        is_passengers_on_position(self.flag_passengers)
                        self.start()
                    random_sleep()
                    _flag_title_msg = False
                case "fighting_friend_default" | "fighting_friend_linshuanghanxue" | "fighting_friend_chunlvhanqing":
                    logger.ui("对局进行中")
                    self.finish()
                    self.done()
                    _resource_list = None
                    _flag_title_msg = False
                    random_sleep()
                case "accept_invitation":
                    # TODO 新设备第一次接受邀请会有弹窗，需手动勾选“不再提醒”
                    logger.ui("接受邀请")
                    click(coor)
                case _:
                    if _flag_title_msg:
                        logger.ui("请检查游戏场景", "warn")
                        _flag_title_msg = False


class YuHunSingle(YuHun):
    """单人御魂副本"""
    scene_name = "单人御魂副本"
    resource_list = [
        "title_10",  # 魂十
        "title_11",  # 魂土
        "title_12",  # 神罚
        "start_single",  # 单人挑战
        "fighting",  # 魂土进行中
        "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
        "fighting_shenfa",  # 神罚战斗场景
        # "finish_damage",  # 结束特征图像
        # "finish_damage_2000",  # 结束特征图像-鎏金圣域
        # "finish_damage_shenfa",  # 结束特征图像-神罚
    ]

    @log_function_call
    def __init__(self, n: int = 0, flag_drop_statistics: bool = False):
        super().__init__(n)
        """单人御魂副本

        参数:
            n (int): 次数，默认0次
            flag_drop_statistics (bool): 是否开启掉落统计，默认否
        """
        self.flag_drop_statistics: bool = flag_drop_statistics  # 是否开启掉落统计

    @log_function_call
    def finish_fast(self):  # FIXME
        """结束"""
        result()
        random_sleep(0.4, 0.8)
        # 结算
        coor = finish_random_left_right(False, is_multiple_drops_x=True)
        _flag_screenshot = True
        pyautogui.moveTo(coor.x + window.window_left, coor.y + window.window_top, duration=0.25)
        pyautogui.doubleClick()
        while True:
            if event_thread.is_set():
                return

            # 检测到任一图像
            scene, coor = check_scene_multiple_once([
                f"{RESOURCE_FIGHT_PATH}/finish",
                f"{self.resource_path}/finish_2000",
                f"{RESOURCE_FIGHT_PATH}/tanchigui"
            ])
            if coor.is_effective:
                if _flag_screenshot and self.flag_drop_statistics:
                    self.screenshot()
                    _flag_screenshot = False
                click()
                random_sleep(0.6, 1)
            # 所有图像都未检测到，退出循环
            elif coor.is_zero:
                logger.ui("结束")
                return

    def finish_slow(self):
        """
        结束 等待自动掉落
        """
        finish()
        random_sleep(0.4, 0.8)
        # 结算
        coor = finish_random_left_right(False, is_multiple_drops_x=True)
        _flag_screenshot = True
        pyautogui.moveTo(coor.x + window.window_left, coor.y + window.window_top, duration=0.25)
        # pyautogui.doubleClick()
        while True:
            if event_thread.is_set():
                return

            # 检测到任一图像
            scene, coor = check_scene_multiple_once([
                f"{RESOURCE_FIGHT_PATH}/finish",
                f"{self.resource_path}/finish_2000",
                f"{RESOURCE_FIGHT_PATH}/tanchigui"
            ])
            if coor.is_effective:
                if _flag_screenshot and self.flag_drop_statistics:
                    self.screenshot()
                    _flag_screenshot = False
                click()
                random_sleep()
            # 所有图像都未检测到，退出循环
            elif coor.is_zero:
                logger.ui("结束")
                return

    def run(self):
        _g_resource_list: list = [
            "title_10",  # 魂十
            "title_11",  # 魂土
            "title_12",  # 神罚
            "start_single",  # 单人挑战
            "fighting",  # 魂土进行中
            "fighting_linshuanghanxue",  # 凛霜寒雪战斗主题
            "fighting_shenfa",  # 神罚战斗场景
        ]
        _resource_list: list = None
        _flag_title_msg: bool = True

        logger.num(f"0/{self.max}")
        while self.n < self.max:
            if event_thread.is_set():
                return
            _resource_list = _g_resource_list if _resource_list is None else _resource_list
            scene, coor = check_scene_multiple_once(_resource_list, self.resource_path)
            if scene is None:
                continue
            self.scene_handle(scene)

            match self.current_scene:
                case "title_10" | "title_11" | "title_12":
                    self.start()
                    random_sleep(self.fast_time)
                    _flag_title_msg = False
                case "start_single":
                    click(coor)
                    random_sleep(self.fast_time)
                    # 只判断下列图像，提高效率
                    _resource_list = ["fighting", "fighting_linshuanghanxue", "fighting_shenfa"]
                    _flag_title_msg = False
                case "fighting" | "fighting_linshuanghanxue" | "fighting_shenfa":
                    logger.ui("对局进行中")
                    self.finish_slow()
                    self.done()
                    _resource_list = None
                    _flag_title_msg = False
                case _:
                    if _flag_title_msg:
                        logger.ui("请检查游戏场景", "warn")
                        _flag_title_msg = False
