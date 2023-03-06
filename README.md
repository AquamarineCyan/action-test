# Onmyoji_Python


大风刮倒梧桐树，自有旁人论长短


## 主要功能
1. 组队御魂副本
2. 组队永生之海副本
3. 业原火副本
4. 御灵副本
5. 个人突破
6. 寮突破
7. 道馆突破
8. 普通召唤
9. 百鬼夜行
10. 限时活动
11. 组队日轮副本


## 功能说明
1. 组队御魂副本
   - 仅适用于组队中
   - 适配司机/打手
2. 组队永生之海副本
    - 仅适用于组队中
    - 适配司机/打手
3. 业原火副本
4. 御灵副本
5. 个人突破
    - 3胜刷新
    - 锁定阵容
6. 寮突破
    - 锁定阵容，从上至下进攻
7. 道馆突破
    - 等待系统进入/手动挑战/正在进行中
    - 挂机阵容
8. 普通召唤
    - 清票/狗粮
9. 百鬼夜行
   - 清票
   - 截图，默认启用
10. 限时活动
11. 组队日轮副本


## 环境安装
* 阴阳师桌面版 [提供NGA下载地址](https://nga.178.com/read.php?tid=29661629)
* 本项目 [releases](https://github.com/AquamarineCyan/Onmyoji_Python/releases)


## 使用方法

~~**无论哪种都需要管理员权限**~~

1. 前往 [releases](https://github.com/AquamarineCyan/Onmyoji_Python/releases) 下载解压打包完成的应用程序，点开即用
2. 需要一定的基础，更新较勤，可能存在bug  
   - 使用`git`命令下载源码  
     `git close https://github.com/AquamarineCyan/Onmyoji_Python.git`  
     后续只需`git pull`
   - 安装依赖 
     - venv 方式 
       `pip install -r requestments.txt`
     - poetry 方式
       `poetry install`
   - 自行打包，打包配置已存在`main.spec`    
     `pyinstaller main.spec`
   - 或者不打包，直接运行（理论上能够生成UI）  
     `python main.py`


## UI

- 功能模块
    - 1.组队御魂副本
    - 2.组队永生之海副本
    - 3.业原火副本
    - 4.御灵副本
    - 5.个人突破
    - 6.寮突破
    - 7.道馆突破
    - 8.普通召唤
    - 9.百鬼夜行
    - 10.限时活动
    - 11.组队日轮副本
- 游戏检测
    - 手动更新游戏窗口信息，适合窗口移动，或双开
- 设置
    - 更新方式
      - GitHub/ghproxy
    - 悬赏封印
      - 接受/拒绝/忽略


## 更新记录

[更新记录wiki](https://github.com/AquamarineCyan/Onmyoji_Python/wiki)


## Tips

**请自行合理使用，所产生的一切后果自负**

移动游戏窗口后，点击 `游戏检测` 即可

由于官方更新了~~很多~~较多UI，目前仅适配部分高频功能（例魂土）
