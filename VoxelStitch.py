import gettext
import locale
from PIL import Image

# i18n
gettext.install('messages', './locale')
defaultLocale = locale.getdefaultlocale() # 获取语言
print ('Language:', defaultLocale[0])
if defaultLocale[0] == 'zh_CN': # 设置语言
  gettext.translation('messages', './locale', languages=['cn']).install()

# 获取图像
regions = []
for i in range(-200,200):
  y = i
  for i in range(-200,200): # 最多200×200张图像
    try:
      filename = "images/" + str(i) + "," + str(y) + ".png" # 获取图像名称
      im = Image.open(filename)
      print(filename)
      print("\x20\x20", _("Image format:"), im.format, _("; Image size:"), im.size, 
        _("; Image mode:"), im.mode) # 打印图像信息
      regions.append((i,y))
    except IOError:
      pass
print(_("Image region list:"), "\n", regions)

# 生成图像信息
# 范围
minRegionMap = map(min, zip(*regions))
maxRegionMap = map(max, zip(*regions))
minRegion = list(minRegionMap)
maxRegion = list(maxRegionMap)
print(_("Min region: "), minRegion)
print(_("Max region: "), maxRegion)
# 坐标
minCoords = (minRegion[0]*256,minRegion[1]*256)
maxCoords = (maxRegion[0]*256,maxRegion[1]*256)
print(_("Min coordinate: "), minCoords)
print(_("Max coordinate: "), maxCoords)
# 偏移值
xOffset = minRegion[0]
yOffset = minRegion[1]
print(_("X offset: "), xOffset)
print(_("Y offset: "), yOffset)
# 区域分辨率
totalRegionResolution = (maxRegion[0]-minRegion[0]+1,
  maxRegion[1]-minRegion[1]+1)
print(_("Total region resolution: "), totalRegionResolution)
# 图像分辨率
pixelResolution = (totalRegionResolution[0]*256,
  totalRegionResolution[1]*256)
print(_("Image resolution: "), pixelResolution)

# 生成+保存图像
outputFilename = "compiledMap.png"
canvas = Image.new("RGBA", pixelResolution, "black")
canvas.format = "PNG"
for i in range(len(regions)):
  currentRegion = regions[i]
  filename = "images/" + str(currentRegion[0]) + "," + \
    str(currentRegion[1]) + ".png"
  print(filename)
  openRegion = Image.open(filename)
  #print(str(currentRegion[0]-xOffset))
  #print(str(currentRegion[1]-yOffset))
  canvas.paste(openRegion, ((currentRegion[0]-xOffset)*256,
    (currentRegion[1]-yOffset)*256))
canvas.save(outputFilename)

print("\n", _("Complete!"))
