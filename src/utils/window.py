import win32con
import win32gui

from .decorator import log_function_call
from .log import logger
from .mysignal import global_ms as ms


def enum_windows(hwnd, result_list):
    result_list.append(hwnd)
    return True


def get_all_same_title_window_numbers(title: str = None) -> tuple[int, tuple[int, int, int, int] | None]:
    """返回相同标题的窗口数量和矩形坐标

    参数:
        title (str, optional): 窗口标题

    返回:
        int: 窗口数量
        tuple[int, int, int, int]: 窗口矩形坐标
    """
    # 全部窗口句柄
    window_list = []
    win32gui.EnumWindows(enum_windows, window_list)
    _window_number = 0
    _rect = None
    for hwnd in window_list:
        _title = win32gui.GetWindowText(hwnd)
        if _title == title:
            _window_number += 1
            _rect = win32gui.GetWindowRect(hwnd)
    return _window_number, _rect


class GameWindow:
    """游戏窗口"""

    window_standard_width: int = 1136 + 18
    """窗口标准宽度（官方1136+外框18=1154）"""
    window_standard_height: int = 640 + 39 + 8
    """窗口标准高度（官方640+标题栏39+外框8=687）"""
    window_title: str = "阴阳师-网易游戏"

    window_left: int = 0
    """窗口左侧横坐标"""
    window_top: int = 0
    """窗口顶部纵坐标"""
    window_right: int = 0
    """窗口右侧横坐标"""
    window_bottom: int = 0
    """窗口底部纵坐标"""

    window_width: int = 0
    """窗口宽度"""
    window_height: int = 0
    """窗口高度"""

    handle: int = None
    """窗口句柄"""
    handle_rect: tuple[int, int, int, int] = (0, 0, 0, 0)
    """窗口坐标 (left, top, right, bottom)"""
    handle_number: int = 0
    """单开/多开数量"""

    def window_info_display(self):
        if self.handle_number == 0:
            return
        s = "游戏窗口信息\n"
        s += f"左侧横坐标:{self.window_left}\n"
        s += f"顶部纵坐标:{self.window_top}\n"
        s += f"右侧横坐标:{self.window_right}\n"
        s += f"底部纵坐标:{self.window_bottom}\n"
        s += f"窗口宽度:{self.window_width}\n"
        s += f"窗口高度:{self.window_height}\n"
        logger.ui(s)

    def get_top_window_handle(self) -> tuple[int, int, int, int]:
        """获得最顶层的游戏窗口信息"""
        try:
            self.handle = win32gui.FindWindow("Win32Window", self.window_title)
            _rect = win32gui.GetWindowRect(self.handle)
        except Exception:
            _rect = (0, 0, 0, 0)
        return _rect

    def compare_window_rect(self, new_rect: tuple[int, int, int, int]) -> bool:
        """比较新旧窗口矩形坐标是否相同

        参数:
            new_rect (tuple[int, int, int, int]): 新窗口坐标

        返回:
            bool: 是否相同
        """
        return self.handle_rect == new_rect

    def update_game_window_rect(self, rect: tuple[int, int, int, int]):
        """更新游戏窗口矩形坐标       

        参数:
            rect (tuple[int, int, int, int]): 窗口矩形坐标
        """
        # 偏移量见类初始定义
        self.handle_rect = rect
        self.window_left = rect[0] + 9
        self.window_top = rect[1]
        self.window_right = rect[2] - 9
        self.window_bottom = rect[3] - 8
        self.window_width = rect[2] - rect[0] - 18
        self.window_height = rect[3] - rect[1] - 47

    @log_function_call
    def get_game_window_handle(self) -> tuple[int, int, int, int]:
        """获取游戏窗口信息

        返回:
            tuple[int, int, int, int]: 窗口坐标(left, top, width, height)
        """
        _window_number, _rect = get_all_same_title_window_numbers(self.window_title)
        self.handle_number = _window_number

        if _window_number == 0:
            logger.ui("未找到游戏窗口", "error")
            return
        _rect = self.get_top_window_handle()

        self.update_game_window_rect(_rect)
        self.window_info_display()

    def force_zoom(self):  # TODO 比例差一点
        """强制缩放 1154*687"""
        if (self.handle is not None) and (self.handle_rect[0] != 0) and (self.window_top != 0):
            win32gui.SetWindowPos(
                self.handle,
                win32con.HWND_TOP,
                self.handle_rect[0],
                self.handle_rect[1],
                self.window_standard_width,
                self.window_standard_height,
                win32con.SWP_SHOWWINDOW
            )
            self.update_game_window_rect(win32gui.GetWindowRect(self.handle))
            logger.info(f"new_handle_coor:{self.handle_rect}")
        else:
            logger.ui("强制缩放失败", "error")

    def scheduler_get_game_window_handle(self):
        """定时任务：获取游戏窗口句柄"""
        _window_number, _rect = get_all_same_title_window_numbers(self.window_title)
        if _window_number != 1:  # 多开或者未检测到游戏窗口，跳过
            return

        # 单开，自动更新窗口
        # _rect = self.get_top_window_handle()
        if not self.compare_window_rect(_rect):
            self.update_game_window_rect(_rect)
            logger.ui("已自动更新游戏窗口坐标")


window = GameWindow()


def check_game_handle() -> bool:
    """游戏窗口检测

    返回:
        bool: 检测结果
    """
    # 获取游戏窗口信息
    window.get_game_window_handle()
    handle_rect = window.handle_rect
    if handle_rect == (0, 0, 0, 0):
        logger.error("Game is close!")
        ms.main.qmessagbox_update.emit("ERROR", "请在打开游戏后点击 游戏检测！")
    elif handle_rect[0] < -9 or handle_rect[1] < 0 or handle_rect[2] < 0 or handle_rect[3] < 0:
        logger.error(f"Game is background, handle_rect:{handle_rect}")
        ms.main.qmessagbox_update.emit("ERROR", "请前置游戏窗口！")
    elif handle_rect[2] - handle_rect[0] != window.window_standard_width and \
            handle_rect[3] - handle_rect[1] != window.window_standard_height:
        ms.main.qmessagbox_update.emit("question", "强制缩放")
    else:
        logger.ui("游戏窗口检测成功")
        return True
    logger.ui("游戏窗口检测失败", "error")
    return False
