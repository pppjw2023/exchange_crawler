The file "深交所公司名单201712.txt" contains the codes of all companies listed on the Shenzhen Stock Exchange as of the close of trading on December 31, 2017.

The code file "深交所抓取命令.py" performs the following tasks:

1. Uses Selenium to launch the Chrome browser and access the Shanghai Stock Exchange website,
2. Reads all company codes listed on the Shanghai Stock Exchange,
3. Inputs each company code and the desired time period into the announcement search bar on the exchange's webpage, then simulates clicking the "Search" button,
4. Extracts all announcement titles and download URLs using XPath,
5. Writes the collected data into a text file.

The code file "合并所有公告文件的命令.py" is used to merge data written in multiple text files into a single final text file, making it easier to manage the data results afterward.

The data recorded in the text file is then imported into the "全部深交所公告2017年度.xlsx" file, allowing for batch copying of these URLs. These download URLs are subsequently batch-imported into a specialized download tool to enable bulk downloading of company announcements.