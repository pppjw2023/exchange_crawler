import chardet


# >>>>> >>>>> >>>>> >>>>> 读取文件名单
fh = open('D:\PythonProjects\深交所公告抓取\深交所公告抓取201801运行\深交所公司公告\文件名单.txt', 'r')  # 建立用于读取的文件对象
lines = fh.readlines() # 逐行读取fh到列表
fileList = [k.strip() for k in lines ] # 逐行删除无用的空白和换行，并保存
fh.close()
# <<<<< <<<<< <<<<< <<<<< 读取文件名单


# >>>>> >>>>> >>>>> >>>>> 自动读取每个文件中的数据
allData = [] # 创建保存全部数据的空列表
for k in range(0,len(fileList)):
    print([k, len(fileList)])
    
    # >>>>> >>>>> >>>>> 判定待读取文件的编码
    fh = open('D:/PythonProjects/深交所公告抓取/深交所公告抓取201801运行/深交所公司公告/'+fileList[k], "rb") # 创建读取文件的对象
    temp = fh.read() # 将文件内容读到对象temp中
    tempInfo = chardet.detect(temp) # 探测对象temp的编码信息
    fh.close()
    # <<<<< <<<<< <<<<< 判定待读取文件的编码
    
    # >>>>> >>>>> >>>>> 根据获取到的编码信息进行读取
    fh = open('D:/PythonProjects/深交所公告抓取/深交所公告抓取201801运行/深交所公司公告/'+fileList[k], 'r', encoding = tempInfo['encoding'])
    lines = fh.readlines() # 逐行读取fh到列表
    allData = allData + lines  # 添加到数据列表中
    fh.close()
    # <<<<< <<<<< <<<<< 根据获取到的编码信息进行读取
#End
# <<<<< <<<<< <<<<< <<<<< 自动读取每个文件中的数据


# >>>>> >>>>> >>>>> >>>>> 保存合并后的数据
allData = [k.strip() for k in allData ] # 逐行删除无用的空白和换行，并保存

fh = open('D:\PythonProjects\深交所公告抓取\深交所公告抓取201801运行\全部深交所公告.txt', 'w', encoding = 'utf-8') # 创建要保存的文件对象，含文件保存路径和文件名
for i in range(0,len(allData)):
    fh.write(allData[i]+'\n') # 逐行保存，行末回车
fh.close()
# <<<<< <<<<< <<<<< <<<<< 保存合并后的数据

