import  os


#请求头
HEAD ={}
HEAD['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'



#数据库
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'root'
DATABASWE = 'gushu'


#数据库执行语句
INSERT_START = 'insert into zh (book_name,writer,type,book_url,img_url) values '
INSERT_END = ';'

ROOT_URL = 'http://www.126139.net'

#图片保存位置
#IMG_PATH = os.path.dirname(__file__)
IMG_PATH = r'C:\Users\dieman\Desktop\python爬虫\img'

#正则表达式
RE_NAME = r'target="_blank">(.*)</a>'

RE_ILNK = r'target="_blank">(.*)</a>'





