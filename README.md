# VoxelStitch-Python3
Forked from [GauthIronstaff/VoxelStitch](https://github.com/GauthIronstaff/VoxelStitch) 。

在 [GauthIronstaff/VoxelStitch](https://github.com/GauthIronstaff/VoxelStitch) 的基础上进行修改。

## 使用
### 获取图像
找到Voxelmap配置文件 (`voxelmap.properties`) , 它可能位于:
* `.minecraft/mods/mamiyaotaru/voxelmap`
* `.minecraft/config`

在其结尾添加一行:`Output Images:true`。

启动 Minecraft!

加入世界/服务器, 打开世界地图, 四处拖动直到要生成地图的区域全部加载完毕, 然后退出世界/服务器, 最后退出 Minecraft<sup>[需验证]</sup>。

找到输出的图像, 它可能位于
* `.minecraft/mods/mamiyaotaru/voxelmap/catch/<世界名称>/<子世界名称>/images`
* `.minecraft/voxelmap/catch/<世界名称>/<子世界名称>/images`

文件夹, 复制它们。

### 程序
下载此仓库 (`Code ▼/Download zip`) , 解压到当前文件夹。

假设你安装了[Python](https://python.org) 3和pip, 打开控制台, 定位到 `VoxelStitch-Python3-main` 中, 输入:
```
$ pip install Pillow
```
回车, 等待安装完成。

完成后将复制的图像粘贴到 `VoxelStitch-Python3-main/images` 文件夹中, 然后在控制台中输入:
```
$ python VoxelStitch.py
```
回车。

如果不出意外, 控制台将会开始打印信息。当输出 `完成!` 时, 一张 `compiledMap.png` 就会出现在 `VoxelStitch-Python3` 中。

### 致谢
[GauthIronstaff](https://github.com/GauthIronstaff) — 原程序开发。
