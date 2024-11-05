#-*-coding:utf-8-*-


from selenium import webdriver
import random
import time
import re


# %%%%% %%%%% 定义抓取数据的子程序
def getData(driver):
    element = driver.find_elements_by_xpath("//dl[@class='modal_pdf_list']/dd") # 取出所有包含公告信息的dd元素
    
    tempFirm = []
    tempDate = []
    tempLink = []
    tempTitle = []
    
    for k in range(len(element)):
        temp = element[k] # 取出第k个dd元素
        tempFirm = tempFirm + [temp.get_attribute('data-seecode')] # 取出该元素的公司代码属性
        tempDate = tempDate + [temp.get_attribute('data-time')]  # 取出该元素的公告日期属性
        temp = temp.find_element_by_tag_name('a')  # 取出dd元素下面的a元素
        tempLink = tempLink + [temp.get_attribute('href')] # 取出a元素下面的href属性
        tempTitle = tempTitle + [temp.get_attribute('title')]
    #End
    return([tempFirm, tempDate, tempLink, tempTitle]) # 返回抓取的数据
# %%%%% %%%%% 定义抓取数据的子程序


# %%%%% %%%%% 填写查询时段的子程序
def chooseFirmPeriod(driver, firmCode, yearStart, yearEnd):
    # >>>>> >>>>> >>>>> >>>>> 填写公司代码
    element = driver.find_element_by_xpath("//input[@id='inputCode']") # 找到输入证券代码的元素
    element.clear() # 清空这个元素里面的内容
    element.send_keys(firmCode) # 填写公司代码
    # <<<<< <<<<< <<<<< <<<<< 填写公司代码
    
    # >>>>> >>>>> >>>>> >>>>> 填写起始日期
    element = driver.find_element_by_xpath("//input[@id='start_date']") # 找到输入查询起始日期的元素
    element.click()  # 鼠标点击这个元素
    
    element = driver.find_element_by_xpath("/html/body/div[14]/div[3]/table/thead/tr[1]/th[2]") # 找到选择年份与月份的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath("/html/body/div[14]/div[4]/table/thead/tr/th[2]") # 找到选择年份的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath('/html/body/div[14]/div[5]/table/thead/tr/th[2]')  # 找到年份段选择按钮
    if element.text=='2010-2019':   # 如果是靠近现在的年份段    
        element = driver.find_element_by_xpath("/html/body/div[14]/div[5]/table/thead/tr/th[1]/i") # 找到左退按钮
        element.click()  # 点击按钮
    #End
    
    element = driver.find_element_by_xpath("/html/body/div[14]/div[5]/table/tbody/tr/td/span[text()='2001']") # 找到2001年份的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath("/html/body/div[14]/div[4]/table/thead/tr/th[3]/i") # 找到年份右进按钮
    clickNumber = yearStart - 2001 # 计算需要点击的次数
    if clickNumber > 0:  # 如果点击次数大于0
        for k in range(clickNumber):
            element.click()  # 点击按钮
        #End End  
    #End
    
    element = driver.find_element_by_xpath("/html/body/div[14]/div[4]/table/tbody/tr/td/span[text()='一月']") # 找到选择一月的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath("/html/body/div[14]/div[3]/table/tbody//td[text()='1']") # 找到选择1日的按钮
    element.click()  # 点击按钮
    # <<<<< <<<<< <<<<< <<<<< 填写起始日期
    
    
    # >>>>> >>>>> >>>>> >>>>> 填写结束日期
    element = driver.find_element_by_xpath("//input[@id='end_date']") # 找到输入查询结束日期的元素
    element.click()  # 鼠标点击这个元素
    
    element = driver.find_element_by_xpath("/html/body/div[15]/div[3]/table/thead/tr[1]/th[2]") # 找到选择年份与月份的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath("/html/body/div[15]/div[4]/table/thead/tr/th[2]") # 找到选择年份的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath('/html/body/div[15]/div[5]/table/thead/tr/th[2]')  # 找到年份段选择按钮
    if element.text=='2010-2019':   # 如果是靠近现在的年份段    
        element = driver.find_element_by_xpath("/html/body/div[15]/div[5]/table/thead/tr/th[1]/i") # 找到左退按钮
        element.click()  # 点击按钮
    #End
    
    element = driver.find_element_by_xpath("/html/body/div[15]/div[5]/table/tbody/tr/td/span[text()='2001']") # 找到2001年份的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath("/html/body/div[15]/div[4]/table/thead/tr/th[3]/i") # 找到年份右进按钮
    clickNumber = yearEnd - 2001 # 计算需要点击的次数
    if clickNumber > 0:  # 如果点击次数大于0
        for k in range(clickNumber):
            element.click()  # 点击按钮
        #End End  
    #End
    
    element = driver.find_element_by_xpath("/html/body/div[15]/div[4]/table/tbody/tr/td/span[text()='十二月']") # 找到选择十二月的按钮
    element.click()  # 点击按钮
    
    element = driver.find_element_by_xpath("/html/body/div[15]/div[3]/table/tbody//td[text()='31']") # 找到选择1日的按钮
    element.click()  # 点击按钮
    # <<<<< <<<<< <<<<< <<<<< 填写结束日期
    
# %%%%% %%%%% 填写查询时段的子程序


# %%%%% %%%%% 填写查询时段的子程序

# %%%%% %%%%% 填写查询时段的子程序

# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序
# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序
# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序
# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序

# >>>>> >>>>> >>>>> >>>>> 读取上交所公司代码列表
firmList = [] # 建立空列表用来存储读取的数据
fh = open('D:\\PythonProjects\\上交所公告抓取\\上交所公告抓取201801运行\\上交所公司名单201712.txt', 'r')  # 建立用于读取的文件对象
lines = fh.readlines() # 逐行读取fh到列表
firmList = [k.strip() for k in lines ] # 逐行删除无用的空白和换行
fh.close() 
# <<<<< <<<<< <<<<< <<<<< 读取上交所公司代码列表


# >>>>> >>>>> >>>>> >>>>> 建立起止年份名单
startYear = [2017] # 建立查询起始年份名单
endYear = [2017] # 建立查询终止年份名单
# <<<<< <<<<< <<<<< <<<<< 建立起止年份名单


driver = webdriver.Chrome()   # 开启谷歌浏览器

for k in range(15, len(firmList)): # 按逐个要查询的公司循环
    
    firmCode = firmList[k]  # 取出第k个公司代码
    driver.get('http://www.sse.com.cn/assortment/stock/list/info/announcement/')  # 进入公告查询页面
    time.sleep(3)
    for kk in range(0,len(startYear)): # 按逐个要查询的起始年份循环
    
        # >>>>> >>>>> >>>>> >>>>> 建立用来保存抓获数据的空列表
        allFirm = [] # 保存公司代码的空列表
        allDate = [] # 保存公告日期的空列表
        allLink = [] # 保存下载链接的空列表
        allTitle = [] # 保存公告标题的空列表
        # <<<<< <<<<< <<<<< <<<<< 建立用来保存抓获数据的空列表
        
        # >>>>> >>>>> >>>>> >>>>> 查询
        try:
            chooseFirmPeriod(driver, firmCode, startYear[kk], endYear[kk]) # 填写查询的公司和起止时间
            element = driver.find_element_by_xpath("//button[@id='btnQuery']") # 找到查询的按钮
            element.click()  # 点击按钮
            time.sleep(5)
        except:
            print('出大事了')
            driver.close()   # 关闭浏览器
            time.sleep(10)   # 等待一会儿
            driver = webdriver.Chrome()   # 开启谷歌浏览器
            driver.get('http://www.sse.com.cn/assortment/stock/list/info/announcement/')  # 进入公告查询页面
            chooseFirmPeriod(driver, firmCode, startYear[kk], endYear[kk]) # 填写查询的公司和起止时间
            element = driver.find_element_by_xpath("//button[@id='btnQuery']") # 找到查询的按钮
            element.click()  # 点击按钮   
            time.sleep(3)
        #End End End
        # <<<<< <<<<< <<<<< <<<<< 查询
        
        # >>>>> >>>>> >>>>> >>>>> 取出本次查询的公告数据
        try:
            element = driver.find_elements_by_xpath("//dd[text()='暂无数据']")  # 查找是否有数据
        except:
            time.sleep(5)
            element = driver.find_elements_by_xpath("//dd[text()='暂无数据']")  # 查找是否有数据
        #End End End
        if len(element)!=0:
            print([k, kk, '暂无数据'])
            time.sleep(random.uniform(2, 4)) # 随机暂停
        #End End End
        if len(element)==0:   # 如果有数据
        # >>>>> >>>>> >>>>> >>>>> 取出本次查询的公告数据
            try:
                time.sleep(2)
                element = driver.find_elements_by_xpath('//*[@class="classStr" and @id="idStr" and @page="2"]')  # 查找是否有页数‘2’
            except:
                time.sleep(5)
                element = driver.find_elements_by_xpath('//*[@class="classStr" and @id="idStr" and @page="2"]')  # 查找是否有页数‘2’
            #End End End End
            
            if len(element)==0 :
                pageAll = 1 # 总共只有1页
            else:            
                element = driver.find_elements_by_xpath("//*[@id='idStr' and @class='classStr']") # 找出包含翻页的元素
                time.sleep(1)
                print('休息1秒钟')
                element = element[len(element)-1] # 取出最后一个单元的对象
                pageAll = int(element.text) # 取出最大页数
            #End End End End
            # >>>>> >>>>> >>>>> 取出第一页数据
            try:
                tempData = getData(driver) # 抓取该页面的公告数据
            except:
                time.sleep(20)
                tempData = getData(driver) # 抓取该页面的公告数据
                print('等了会儿')
            #End End End End
            
            allFirm = allFirm + tempData[0] # 保存公司代码
            allDate = allDate + tempData[1] # 保存公告日期
            allLink = allLink + tempData[2] # 保存下载链接
            allTitle = allTitle + tempData[3] # 保存公告标题
            
            print([k, kk, 0, pageAll])
            time.sleep(random.uniform(2, 4)) # 随机暂停
            # <<<<< <<<<< <<<<< 取出第一页数据
            
            # >>>>> >>>>> >>>>> 如果有更多页面，则翻页并取出后续页面的数据
            if pageAll>1:
                for kkk in range(1,pageAll):
                    try:
                        element=driver.find_element_by_xpath('//*[@id="ht_codeinput"]')  # 找出填写页码的单元
                        element.send_keys(str(kkk+1))# 填写页码
                        time.sleep(1)
                        element=driver.find_element_by_xpath('//*[@id="pagebutton"]')  #  找到Go按钮
                        element.click() #点击
                        time.sleep(3)
                    except:
                        print('翻页出大事了')
                    #End End End End End End
                    try:
                        tempData = getData(driver) # 抓取该页面的公告数据
                    except:
                        time.sleep(20)
                        tempData = getData(driver) # 抓取该页面的公告数据
                        print('等了会儿')
                    #End End End End End End
                    
                    allFirm = allFirm + tempData[0] # 保存公司代码
                    allDate = allDate + tempData[1] # 保存公告日期
                    allLink = allLink + tempData[2] # 保存下载链接
                    allTitle = allTitle + tempData[3] # 保存公告标题
                    
                    print([k, kk, kkk, pageAll, len(firmList)])
                    time.sleep(random.uniform(2, 4)) # 随机暂停
                #End End End End End
            #End End End End
            # <<<<< <<<<< <<<<< 如果有更多页面，则翻页并取出后续页面的数据
            # >>>>> >>>>> >>>>> >>>>> 每抓取1个公司-年度保存一次
            fh = open('D:\PythonProjects\上交所公告抓取\上交所公告抓取201801运行\上交所公司公告\年度'+str(startYear[kk])+'公司'+firmCode+'.txt', 'w', encoding = 'utf-8') # 创建要保存的文件对象，含文件保存路径和文件名
            for i in range(0,len(allFirm)):
                allDate[i]=re.sub('-','',allDate[i]) # 去掉日期中的横线
                fh.write(allFirm[i]+'^'+allDate[i]+'^'+allTitle[i]+'^'+allLink[i]+'\n') # 列表中间间隔^号，行末回车
            fh.close()
            # <<<<< <<<<< <<<<< <<<<< 每抓取1个公司-年度保存一次
        #End End End
        # <<<<< <<<<< <<<<< <<<<< 取出本次查询的公告数据
    #End End
#End