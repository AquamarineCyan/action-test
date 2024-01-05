from pathlib import Path

VERSION: str = "1.7.11"
"""版本号"""
APP_NAME: str = "Onmyoji_Python"
"""程序名称"""
APP_EXE_NAME: str = f"{APP_NAME}.exe"
"""程序本体文件名称"""

APP_PATH: Path = Path().cwd()
"""程序本体路径"""
CONFIG_PATH: Path = APP_PATH / "config.yaml"
"""配置文件路径"""
LOG_DIR_PATH: Path = APP_PATH / "log"
"""日志文件夹路径"""
if not LOG_DIR_PATH.exists():
    LOG_DIR_PATH.mkdir(parents=True)

RESOURCE_DIR_PATH: Path = None
"""资源/素材文件夹路径"""
for _ in [Path(APP_PATH/"src/resource"), Path(APP_PATH/"resource")]:
    # 开发路径/实际路径
    RESOURCE_DIR_PATH = _
    if _.exists():
        break
    elif _ == Path(APP_PATH/"resource"):
        RESOURCE_DIR_PATH.mkdir(parents=True, exist_ok=True)
RESOURCE_FIGHT_PATH = RESOURCE_DIR_PATH / "fight"
"""通用战斗资源路径"""
SCREENSHOT_DIR_PATH: Path = APP_PATH / "screenshot"
"""截图文件夹路径"""


class Connect:
    owner = "AquamarineCyan"
    repo = APP_NAME
    releases_api = f"https://api.github.com/repos/{owner}/{repo}/releases"
    github_api = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
    gitee_api = f"https://gitee.com/api/v5/repos/{owner}/{repo}/releases/latest"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
