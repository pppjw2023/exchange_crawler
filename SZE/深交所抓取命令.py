#-*-coding:utf-8-*-


from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # 鼠键
from selenium.webdriver.common.action_chains import ActionChains # 鼠键连续
import  os
import random
import time
import re


# %%%%% %%%%% 定义抓取数据的子程序
def getData(driver):
    element = driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr") # 取出所有包含公告信息的tr元素
    
    tempDate = []
    tempLink = []
    tempTitle = []
    
    for k in range(len(element)):
        temp = element[k] # 取出第k个tr元素
        temp1 = temp.find_element_by_tag_name('a')  # 取出tr元素下面的a元素
        tempLink = tempLink + [temp1.get_attribute('href')] # 取出a元素下面的href属性
        tempTitle = tempTitle + [temp1.text] # 取出公告标题
        temp2 = temp.find_element_by_tag_name('span')  # 取出tr元素下面的span元素
        temp2 = temp2.text  # 取出标签中的文字内容
        temp2 = re.findall('\[(.*?)\]',temp2) # 只取出年份字符
        tempDate = tempDate + temp2 # 取出公告日期
    #End
    return([tempDate, tempLink, tempTitle]) # 返回抓取的数据
# %%%%% %%%%% 定义抓取数据的子程序

    
# %%%%% %%%%% 填写查询时段的子程序
def chooseFirmPeriod(driver, firmCode, startYear, endYear):
    # >>>>> >>>>> >>>>> >>>>> 填写公司代码
    element = driver.find_element_by_xpath("//input[@id='stockCode']") # 找到输入证券代码的元素
    element.clear() # 清空这个元素里面的内容
    element.send_keys(firmCode) # 填写公司代码
    # <<<<< <<<<< <<<<< <<<<< 填写公司代码
    
    # >>>>> >>>>> >>>>> >>>>> 填写起始日期
    element = driver.find_element_by_xpath("//input[@id='search'and @name='startTime']") # 找到输入查询起始日期的元素
    element.clear() # 清空这个元素里面的内容
    element.send_keys(str(startYear)+'-01-01') # 输入起始日期
    # <<<<< <<<<< <<<<< <<<<< 填写起始日期
    
    # >>>>> >>>>> >>>>> >>>>> 填写结束日期
    element = driver.find_element_by_xpath("//input[@id='search' and @name='endTime']") # 找到输入查询结束日期的元素
    element.clear()  # 清空这个元素里面的内容
    element.send_keys(str(endYear)+'-12-31') # 输入起始日期
    # <<<<< <<<<< <<<<< <<<<< 填写结束日期
# %%%%% %%%%% 填写查询时段的子程序


# %%%%% %%%%% 下翻页面到底部，并点击翻页
def scrollDownAndTurnPage(driver):
    abnormal = 'yes' # 标记异常
    while abnormal=='yes':
        try:
            element = driver.find_element_by_xpath("//img[@src='images2008/next.gif']") # 找到翻页按钮
            element.click() # 点击翻页
        except:
            abnormal = 'yes' # 标记异常
            ActionChains(driver).click().perform() # 点击页面一下
            ActionChains(driver).key_down(Keys.PAGE_DOWN).perform() # 页面往下翻滚
            time.sleep(1)
        else:
            abnormal = 'no' # 标记正常
    return
# %%%%% %%%%% 下翻页面到底部，并点击翻页


# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序
# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序
# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序
# %%%%% %%%%% %%%%% %%%%% %%%%% %%%%% 以下为主程序

# >>>>> >>>>> >>>>> >>>>> 读取深交所公司代码列表
firmList = [] # 建立空列表用来存储读取的数据
fh = open('D:\PythonProjects\深交所公告抓取\深交所公告抓取201801运行\深交所公司名单201712.txt', 'r')  # 建立用于读取的文件对象
lines = fh.readlines() # 逐行读取fh到列表
firmList = [k.strip() for k in lines ] # 逐行删除无用的空白和换行
fh.close() 
# <<<<< <<<<< <<<<< <<<<< 读取深交所公司代码列表


# >>>>> >>>>> >>>>> >>>>> 建立起止年份名单
startYear = [2017] # 建立查询起始年份名单
endYear = [2017] # 建立查询终止年份名单
# <<<<< <<<<< <<<<< <<<<< 建立起止年份名单


driver = webdriver.Chrome()   # 开启浏览器


for k in range(1, len(firmList)): # 按逐个要查询的公司循环
    
    firmCode = firmList[k]  # 取出第k个公司代码
    driver.get('http://disclosure.szse.cn/m/search0425.jsp')  # 进入公告查询页面

    for kk in range(0,len(startYear)): # 按逐个要查询的起始年份循环
        # >>>>> >>>>> >>>>> >>>>> 建立用来保存抓获数据的空列表
        
        allDate = [] # 保存公告日期的空列表
        allLink = [] # 保存下载链接的空列表
        allTitle = [] # 保存公告标题的空列表
        # <<<<< <<<<< <<<<< <<<<< 建立用来保存抓获数据的空列
        
        # >>>>> >>>>> >>>>> >>>>> 查询
        try:
            chooseFirmPeriod(driver, firmCode, startYear[kk], endYear[kk]) # 填写查询的公司和起止时间
            element = driver.find_element_by_xpath("//*[@id='queryHistoryForm']/table/tbody/tr/td[9]/input") # 找到查询的按钮
            element.click()  # 点击按钮
        except:
            print('出大事了')
            driver.close()   # 关闭浏览器
            time.sleep(20)   # 等待一会儿
            driver = webdriver.Firefox()   # 开启火狐浏览器
            driver.get('http://disclosure.szse.cn/m/search0425.jsp')  # 进入公告查询页面
            chooseFirmPeriod(driver, firmCode, startYear[kk], endYear[kk]) # 填写查询的公司和起止时间
  
            element = driver.find_element_by_xpath("//*[@id='queryHistoryForm']/table/tbody/tr/td[9]/input") # 找到查询的按钮
            element.click()  # 点击按钮
        #End End End
        # <<<<< <<<<< <<<<< <<<<< 查询
        
        
        # >>>>> >>>>> >>>>> >>>>> 取出本次查询的公告数据
        try:
            element = driver.find_elements_by_xpath("//td[text()='没有找到你搜索的公告!']")  # 查找是否有数据
            
        except:
            time.sleep(20)
            element = driver.find_elements_by_xpath("//td[text()='没有找到你搜索的公告!']")  # 查找是否有数据
            print('等了会儿')
        #End End End 
        if len(element)!=0:   # 如果没有数据
            print([k, kk, '没有找到你搜索的公告!'])
            time.sleep(random.uniform(2, 4)) # 随机暂停
        #End End End
        if len(element)==0:   # 如果有数据
            element= driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/span[2]") # 找出写明共多少页的元素
            pageAll = int(element.text) # 获取总页面数
            # >>>>> >>>>> >>>>> 取出第一页数据
            tempData=[[],[],[]]  # 初始化临时存储列表
            while len(tempData[0])==0: 
                time.sleep(1)  # 等待2秒
                try:
                    tempData = getData(driver) # 抓取该页面的公告数据
                except:
                    time.sleep(5)   # 等待5秒
                    tempData = getData(driver) # 抓取该页面的公告数据
                    print('等一会儿')
                #End End End End End
            #End End End End
            

            allDate = allDate + tempData[0] # 保存公告日期
            allLink = allLink + tempData[1] # 保存下载链接
            allTitle = allTitle + tempData[2] # 保存公告标题
            
            print([k, kk, 0, pageAll,len(firmList)])
            time.sleep(random.uniform(2, 4)) # 随机暂停
            # <<<<< <<<<< <<<<< 取出第一页数据
           
     
            # >>>>> >>>>> >>>>> 如果有更多页面，则翻页并取出后续页面的数据
            if pageAll>1:
                for kkk in range(1,pageAll):

                    scrollDownAndTurnPage(driver) # 下滚并翻页
                    tempData=[[],[],[]]  # 初始化临时存储列表
                    while len(tempData[0])==0: 
                        time.sleep(1)  # 等待1秒
                        try:
                            tempData = getData(driver) # 抓取该页面的公告数据
                        except:
                            time.sleep(5)   # 等待5秒
                            tempData = getData(driver) # 抓取该页面的公告数据
                            print('等一会儿')
                    #End End End End End End
                    
                    
                    allDate = allDate + tempData[0] # 保存公告日期
                    allLink = allLink + tempData[1] # 保存下载链接
                    allTitle = allTitle + tempData[2] # 保存公告标题
                    
                    print([k, kk, kkk, pageAll])
                    time.sleep(random.uniform(2, 4)) # 随机暂停
                #End End End End End
            #End End End End
            # <<<<< <<<<< <<<<< 如果有更多页面，则翻页并取出后续页面的数据
            # >>>>> >>>>> >>>>> >>>>> 每抓取1个公司-年度保存一次
            year = str(startYear[kk])[0:4] # 取出当前年度
            fh = open('D:\PythonProjects\深交所公告抓取\深交所公告抓取201801运行\深交所公司公告\年度'+year+'公司'+firmCode+'.txt', 'w', encoding = 'utf-8') # 创建要保存的文件对象，含文件保存路径和文件名
            for i in range(0,len(allDate)):
                allDate[i]=re.sub('-','',allDate[i]) # 去掉日期中的横线
                fh.write(firmCode+'^'+allDate[i]+'^'+allTitle[i]+'^'+allLink[i]+'\n') # 列表中间间隔^号，行末回车
            fh.close()
            # <<<<< <<<<< <<<<< <<<<< 每抓取1个公司-年度保存一次
        #End End End
        # <<<<< <<<<< <<<<< <<<<< 取出本次查询的公告数据
    #End End
#End
        
        
        

