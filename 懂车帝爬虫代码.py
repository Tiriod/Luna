import os.path
import time

import openpyxl
from lxml import etree
from selenium import webdriver


# 懂车帝数据爬取
def dongchedi():
    # 实例化浏览器对象, edgeDriver.exe为浏览器的启动器, 实际版本需要与自己的浏览器版本相对应
    # 参考网址: https://blog.csdn.net/kenny_pj/article/details/103646745
    browser = webdriver.Edge(executable_path="edgeDriver.exe")
    # 让浏览器发起指定的url请求
    # url如下
    url = ["https://www.dongchedi.com/sales/sale-energy-202207-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-energy-202208-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-energy-202209-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-energy-202210-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-energy-202211-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-energy-202212-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-x-202207-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-x-202208-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-x-202209-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-x-202210-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-x-202211-x-x-x-x",
           "https://www.dongchedi.com/sales/sale-x-202212-x-x-x-x"
           ]
    # 根据上方内容进行手动切换
    browser.get("https://www.dongchedi.com/sales/sale-energy-202207-x-x-x-x")
    browser.execute_script("window.scrollTo(0, 100000)")
    # 程序挂起18秒, 期间需要手动下翻网页
    time.sleep(18)
    # 获取当前页面源码
    response = browser.page_source
    # 更改为自己的桌面路径
    path = r"C:\Users\29646\Desktop"
    os.chdir(path)
    # 优先在桌面创建文件夹:懂车帝新能源汽车7月销.xlsx,懂车帝新能源汽车8月销.xlsx,懂车帝新能源汽车9月销.xlsx,懂车帝新能源汽车10月销.xlsx,懂车帝新能源汽车11月销.xlsx,懂车帝新能源汽车12月销.xlsx,
    # 懂车帝汽车7月销.xlsx,懂车帝汽车8月销.xlsx,懂车帝汽车9月销.xlsx,懂车帝汽车10月销.xlsx,懂车帝汽车11月销.xlsx,懂车帝汽车12月销.xlsx
    workbook = openpyxl.load_workbook("懂车帝新能源汽车7月销.xlsx")
    sheet = workbook.active
    tree = etree.HTML(response)
    carList = tree.xpath("//ol[@class='tw-mt-12']/li")
    data = []
    for i in carList:
        # 月份根据文件夹对应月份进行更改
        list = ["7月"]
        name = i.xpath("./div[3]/div[1]/a/text()")[0]
        list.append(name)
        type = i.xpath("./div[3]/div[1]/span/text()")[0]
        list.append(type)
        price = i.xpath("./div[3]/p/text()")[0]
        list.append(price)
        sales = i.xpath("./div[4]/div/p/text()")[0]
        list.append(sales)
        data.append(list)
    for i in data:
        sheet.append(i)
        print(i)
    # 与上述的workbook = openpyxl.load_workbook("懂车帝新能源汽车7月销.xlsx")文件夹内文件名称对应
    workbook.save("懂车帝新能源汽车7月销.xlsx")
    browser.quit()


if __name__ == '__main__':
    dongchedi()
