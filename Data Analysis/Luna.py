import random
import re
import sys

import matplotlib.pyplot as plt
import pandas
import pygame

from util import ButtonUtil
from util import CorrectionUtil

# 初始化语言, SimHei: 黑体
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 读取Excel文件
pokedex = pandas.read_excel(r"data/图鉴.xlsx", sheet_name="pokedex")
attribute = pandas.read_excel(r"data/属性表.xlsx", sheet_name="attribute")
move = pandas.read_excel(r"data/招式表.xlsx", sheet_name="move")
# 初始化pygame, 加载页面
pygame.init()
# 设置pygame窗体大小
size = width, height = 660, 420
# 导入图标
iconLauncher = pygame.image.load("image/icon.png")
# 设置pygame窗体图标
pygame.display.set_icon(iconLauncher)
# 设置pygame窗体名称
pygame.display.set_caption("宝可梦能力数据分析")

'''
颜色: 白色, 蓝色, 浅粉色, 绯红色, 紫罗兰色, 洋红色, 靛青色, 皇家蓝色, 钢蓝色, 天蓝色, 军校蓝色, 青色, 深绿松石色, 春绿色, 蜂蜜色,
    酸柠绿, 黄色, 橄榄色, 金色, 巧克力色, 珊瑚色, 雪色, 红色, 浅灰色, 黑色
'''
COLOR = {"WHITE": (255, 255, 255), "BLUE": (0, 0, 255), "LIGHTPINK": (255, 182, 193), "CRIMSON": (220, 20, 60),
         "VIOLET": (199, 21, 133), "MAGENTA": (255, 0, 255), "INDIGO": (75, 0, 130), "ROYALBLUE": (65, 105, 225),
         "STEELBLUE": (70, 130, 180), "SKYBLUE": (135, 206, 235), "CADETBLUE": (95, 158, 160),
         "CYAN": (0, 255, 255),
         "DARKTURQUOISE": (0, 206, 209), "SPRINGGREEN": (245, 255, 250), "HONEYDEW": (240, 255, 240),
         "LIME": (0, 255, 0), "YELLOW": (255, 255, 0), "OLIVE": (128, 128, 0), "GOLD": (255, 215, 0),
         "CHOCOLATE": (210, 105, 30), "CORAL": (255, 127, 80), "SNOW": (255, 250, 250), "RED": (255, 0, 0),
         "LIGHTGREY": (211, 211, 211), "SLIVER": (192, 192, 192), "BLACK": (0, 0, 0)}

# 显示窗口
screen = pygame.display.set_mode(size)
# 设置pygame窗体背景颜色
screen.fill(COLOR["BLACK"])
# 设置pygame窗体背景
screen.blit(pygame.image.load(r"image\background.png"), (10, 10))
# 小游戏数据
list = []
shiny = []
pokemonList = []


# 高速速度能力分析
def abilityHighSpeed():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(20, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    # 降序排列
    pokedex.sort_values(by="速度", inplace=True, ascending=False)
    # 选取前30条数据
    data = pokedex.head(30)
    labelX = data["宝可梦"].values
    labelY = data["速度"].values
    for i in range(30):
        labelY[i] = CorrectionUtil.add(labelY[i])
    plt.bar(labelX, labelY, 0.8)
    for x, y in enumerate(labelY):
        plt.text(x, y, str(y), ha="center")
    plt.xlabel("50级高速速度宝可梦")
    plt.ylabel("50级速度点数")
    plt.title("高速速度能力分析")
    plt.show()


# 低速速度能力分析
def abilityLowSpeed():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(16, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    pokedex.sort_values(by="速度", inplace=True)
    # 选取前30条数据
    data = pokedex.head(30)
    labelX = data["宝可梦"].values
    labelY = data["速度"].values
    for i in range(30):
        labelY[i] = CorrectionUtil.low(labelY[i])
    plt.bar(labelX, labelY, 0.8)
    for x, y in enumerate(labelY):
        plt.text(x, y, str(y), ha="center")
    plt.xlabel("50级低速速度宝可梦")
    plt.ylabel("50级速度点数")
    plt.title("低速速度能力分析")
    plt.show()


# 综合耐久能力分析
def comprehensiveDurability():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(20, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    pokedex.sort_values(by="耐久", inplace=True, ascending=False)
    # 选取前30条数据
    data = pokedex.head(30)
    labelX = data["宝可梦"].values
    labelY = data["HP"].values
    HP = data["HP"].values
    defense = data["防御"].values
    spDefense = data["特防"].values
    for i in range(30):
        labelY[i] = CorrectionUtil.durable(HP[i], defense[i], spDefense[i])
    plt.bar(labelX, labelY, 0.8)
    for x, y in enumerate(labelY):
        plt.text(x, y, str(y), ha="center")
    plt.xlabel("50级综合耐久宝可梦")
    plt.ylabel("50级综合耐久点数")
    plt.title("综合耐久分析")
    plt.show()


# 物理招式期望伤害分析
def physicsMovePower():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(20, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    remainder = move.loc[move["分类"] == "物理"]
    remainder.sort_values(by="威力", inplace=True, ascending=False)
    # 选取前50条数据
    data = remainder.head(50)
    labelX = data["名称"].values
    labelY = data["威力"].values
    plt.plot(labelX, labelY, 0.8)
    for x, y in enumerate(labelY):
        plt.text(x, y, str(y), ha="center")
    plt.xlabel("物理招式名称")
    plt.ylabel("期望伤害数值")
    plt.title("物理招式伤害分析")
    plt.show()


# 特殊招式伤害分析
def specialMovePower():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(20, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    remainder = move.loc[move["分类"] == "特殊"]
    remainder.sort_values(by="威力", inplace=True, ascending=False)
    # 选取前50条数据
    data = remainder.head(50)
    labelX = data["名称"].values
    labelY = data["威力"].values
    plt.plot(labelX, labelY, 0.8)
    for x, y in enumerate(labelY):
        plt.text(x, y, str(y), ha="center")
    plt.xlabel("特殊招式名称")
    plt.ylabel("期望伤害数值")
    plt.title("特殊招式伤害分析")
    plt.show()


# 招式属性分布分析
def moveAttribute():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(20, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    move.sort_values(by="属性", inplace=True, ascending=False)
    attributeWater = move[move["属性"].str.contains("水")]
    attributeFire = move[move["属性"].str.contains("火")]
    attributeGress = move[move["属性"].str.contains("草")]
    attributeNormal = move[move["属性"].str.contains("一般")]
    attributeFight = move[move["属性"].str.contains("格斗")]
    attributePsychic = move[move["属性"].str.contains("超能力")]
    attributeGhost = move[move["属性"].str.contains("幽灵")]
    attributePoison = move[move["属性"].str.contains("毒")]
    attributeSteel = move[move["属性"].str.contains("钢")]
    attributeDark = move[move["属性"].str.contains("恶")]
    attributeIce = move[move["属性"].str.contains("冰")]
    attributeDragon = move[move["属性"].str.contains("龙")]
    attributeBug = move[move["属性"].str.contains("虫")]
    attributeFairy = move[move["属性"].str.contains("妖精")]
    attributeFly = move[move["属性"].str.contains("飞行")]
    attributeGround = move[move["属性"].str.contains("地面")]
    attributeRock = move[move["属性"].str.contains("岩石")]
    attributeElectric = move[move["属性"].str.contains("电")]
    labelX = ["水", "火", "草", "一般", "格斗", "超能力", "幽灵", "毒", "钢", "恶", "冰", "龙", "虫", "妖精", "飞行",
              "地面", "岩石", "电"]
    labelY = [len(attributeNormal), len(attributeFire), len(attributeWater), len(attributeGress), len(attributeFight),
              len(attributePsychic), len(attributeGhost), len(attributePoison), len(attributeDark), len(attributeSteel),
              len(attributeIce), len(attributeDragon), len(attributeBug), len(attributeFairy), len(attributeFly),
              len(attributeGround), len(attributeRock), len(attributeElectric)]
    plt.pie(labelY, labels=labelX, autopct="%1.1f%%",
            colors=["blue", "red", "limegreen", "silver", "darkorange", "magenta", "blueviolet", "indigo", "cadetblue",
                    "dimgray", "aqua", "royalblue", "yellowgreen", "hotpink", "skyblue", "darkgoldenrod", "darkkhaki",
                    "yellow"])
    plt.legend(loc="upper right", fontsize=16, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)
    plt.title("招式属性分布分析")
    plt.show()


# 宝可梦属性分布分析
def pokemonAttribute():
    # 配置画布大小-figsize
    plt.figure(dpi=200, figsize=(20, 12))
    # 配置文字大小参数-fontsize
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=16)
    attribute.sort_values(by="第一属性", inplace=True, ascending=False)
    attributeWater = len(attribute[attribute["第一属性"].str.contains("水")])
    attributeFire = len(attribute[attribute["第一属性"].str.contains("火")])
    attributeGress = len(attribute[attribute["第一属性"].str.contains("草")])
    attributeNormal = len(attribute[attribute["第一属性"].str.contains("一般")])
    attributeFight = len(attribute[attribute["第一属性"].str.contains("格斗")])
    attributePsychic = len(attribute[attribute["第一属性"].str.contains("超能力")])
    attributeGhost = len(attribute[attribute["第一属性"].str.contains("幽灵")])
    attributePoison = len(attribute[attribute["第一属性"].str.contains("毒")])
    attributeSteel = len(attribute[attribute["第一属性"].str.contains("钢")])
    attributeDark = len(attribute[attribute["第一属性"].str.contains("恶")])
    attributeIce = len(attribute[attribute["第一属性"].str.contains("冰")])
    attributeDragon = len(attribute[attribute["第一属性"].str.contains("龙")])
    attributeBug = len(attribute[attribute["第一属性"].str.contains("虫")])
    attributeFairy = len(attribute[attribute["第一属性"].str.contains("妖精")])
    attributeFly = len(attribute[attribute["第一属性"].str.contains("飞行")])
    attributeGround = len(attribute[attribute["第一属性"].str.contains("地面")])
    attributeRock = len(attribute[attribute["第一属性"].str.contains("岩石")])
    attributeElectric = len(attribute[attribute["第一属性"].str.contains("电")])
    labelX = ["水", "火", "草", "一般", "格斗", "超能力", "幽灵", "毒", "钢", "恶", "冰", "龙", "虫", "妖精", "飞行",
              "地面", "岩石", "电"]
    labelY = [attributeNormal, attributeFire, attributeWater, attributeGress, attributeFight,
              attributePsychic, attributeGhost, attributePoison, attributeDark, attributeSteel,
              attributeIce, attributeDragon, attributeBug, attributeFairy, attributeFly,
              attributeGround, attributeRock, attributeElectric]
    plt.pie(labelY, labels=labelX, autopct="%1.1f%%",
            colors=["blue", "red", "limegreen", "silver", "darkorange", "magenta", "blueviolet", "indigo", "cadetblue",
                    "dimgray", "aqua", "royalblue", "yellowgreen", "hotpink", "skyblue", "darkgoldenrod", "darkkhaki",
                    "yellow"])
    plt.legend(loc="upper right", fontsize=16, bbox_to_anchor=(1.1, 1.05), borderaxespad=0.3)
    plt.title("宝可梦属性分布分析")
    plt.show()


# 消遣小游戏
def encounter():
    labelX = pokedex["宝可梦"].values
    for i in range(len(labelX)):
        list.append(labelX[i])
    number = random.randint(0, len(list) - 1)
    pokemon = list[number]
    isShiny = random.randint(0, 9)
    if isShiny == 0:
        print("你遭遇了:", "闪光" + pokemon)
        pokemonList.append("闪光" + pokemon)
        shiny.append("Yes")
    else:
        print("你遭遇了:", pokemon)
        pokemonList.append(pokemon)


def gameData():
    print("遭遇列表:", pokemonList, "\n")
    print("遭遇次数:", len(pokemonList), "\n")
    print("闪光个数:", len(shiny))


# 执行死循环, 保持窗口始终处于打开状态
while True:
    '''
    屏幕, 中心点[(90 - 140/2, 50 - 60/2) ——> (20, 20)], 背景颜色, 字体颜色, 文本内容, 字体大小
    '''
    buttonA = ButtonUtil.Button(screen, (110, 70), 200, 120, COLOR["CRIMSON"], COLOR["HONEYDEW"],
                                "高速速度能力分析", 18)
    buttonB = ButtonUtil.Button(screen, (330, 70), 200, 120, COLOR["CORAL"], COLOR["HONEYDEW"],
                                "低速速度能力分析", 18)
    buttonC = ButtonUtil.Button(screen, (550, 70), 200, 120, COLOR["GOLD"], COLOR["HONEYDEW"],
                                "综合耐久能力分析", 18)
    buttonD = ButtonUtil.Button(screen, (110, 210), 200, 120, COLOR["VIOLET"], COLOR["HONEYDEW"],
                                "物理招式伤害分析", 18)
    buttonE = ButtonUtil.Button(screen, (330, 210), 200, 120, COLOR["LIME"], COLOR["HONEYDEW"],
                                "特殊招式伤害分析", 18)
    buttonF = ButtonUtil.Button(screen, (550, 210), 200, 120, COLOR["CYAN"], COLOR["HONEYDEW"],
                                "招式属性分布分析", 18)
    buttonG = ButtonUtil.Button(screen, (110, 350), 200, 120, COLOR["ROYALBLUE"], COLOR["HONEYDEW"],
                                "宝可梦属性分布分析", 18)
    buttonH = ButtonUtil.Button(screen, (330, 350), 200, 120, COLOR["STEELBLUE"], COLOR["HONEYDEW"],
                                "小游戏", 18)
    buttonI = ButtonUtil.Button(screen, (550, 350), 200, 120, COLOR["DARKTURQUOISE"], COLOR["HONEYDEW"],
                                "遭遇列表", 18)
    buttonA.drawButton()
    buttonB.drawButton()
    buttonC.drawButton()
    buttonD.drawButton()
    buttonE.drawButton()
    buttonF.drawButton()
    buttonG.drawButton()
    buttonH.drawButton()
    buttonI.drawButton()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 高速速度能力分析
            if 20 <= event.pos[0] <= 210 and 20 <= event.pos[1] <= 130:
                abilityHighSpeed()
                pass
            # 低速速度能力分析
            elif 230 <= event.pos[0] <= 430 and 20 <= event.pos[1] <= 130:
                abilityLowSpeed()
                pass
            # 综合耐久能力分析
            elif 450 <= event.pos[0] <= 650 and 20 <= event.pos[1] <= 130:
                comprehensiveDurability()
                pass
            # 物理招式伤害分析
            elif 20 <= event.pos[0] <= 210 and 150 <= event.pos[1] <= 270:
                physicsMovePower()
                pass
            # 特殊招式伤害分析
            elif 230 <= event.pos[0] <= 430 and 150 <= event.pos[1] <= 270:
                specialMovePower()
                pass
            # 招式属性分布分析
            elif 450 <= event.pos[0] <= 650 and 150 <= event.pos[1] <= 270:
                moveAttribute()
                pass
            # 宝可梦属性分布分析
            elif 20 <= event.pos[0] <= 210 and 290 <= event.pos[1] <= 410:
                pokemonAttribute()
                pass
            # 小游戏
            elif 230 <= event.pos[0] <= 430 and 290 <= event.pos[1] <= 410:
                encounter()
                pass
            # 小游戏数据
            elif 450 <= event.pos[0] <= 650 and 290 <= event.pos[1] <= 410:
                gameData()
                pass
            else:
                pass
