import requests
import os
import re
from urllib import request
from bs4 import BeautifulSoup




import settings

# class Craw():
#     def craw_text(self,url):
#         bs = requests.get(url=url, headers = settings.HEAD)
#         html = bs.content
#         html = BeautifulSoup(html,'lxml')
#
#         return html
#     def craw_img_url(self, html):
#         html = html.find_all('div', {'class': 'store_collist'})
#         html = BeautifulSoup(str(html),'lxml')
#         img_url = [s.extract() for s in html("img")]
#         url_list = [s.attrs['src'] for s in img_url if 'src' in s.attrs]
#         url_lists =[]
#         for img_url in url_list:
#             if not re.match(r'.*[jpg|png|gif|jpeg]$', img_url):
#                 pass
#             elif re.match(r'^http.*', img_url):
#
#                 url_lists.append(img_url)
#             else:
#                 img_url = settings.ROOT_URL + img_url
#                 url_lists.append(img_url)
#
#         # for link in img_url:
#         #     if 'src' in link.attrs:
#         #        print(link.attrs['src'])
#         return url_lists
#     # def craw_img_url(self, url):
#     #     bs = requests.get(url=url,headers=settings.HEAD)
#     #     html = bs.content
#     #     html = BeautifulSoup(html,'lxml')
#     #     img_url = [s.extract() for s in html("img")]
#     #     url_list = [s.attrs['src'] for s in img_url if 'src' in s.attrs]
#     #     url_lists =[]
#     #     for img_url in url_list:
#     #         if not re.match(r'.*[jpg|png|gif|jpeg]$', img_url):
#     #             pass
#     #         elif re.match(r'^http.*', img_url):
#     #
#     #             url_lists.append(img_url)
#     #         else:
#     #             img_url = settings.ROOT_URL + img_url
#     #             url_lists.append(img_url)
#     #
#     #     # for link in img_url:
#     #     #     if 'src' in link.attrs:
#     #     #        print(link.attrs['src'])
#     #     return url_lists
#
#     def craw_page_url(self, url):
#             pass
#     def craw_next_next(self):
#         return [f'http://book.zongheng.com/store/c0/c0/b0/u0/p{page}/v9/s1/t0/u0/i1/ALL.html' for page in range(1,75)]
#
#
#     def craw_img(self,url):
#         try:
#             request.urlretrieve(url=url,filename=os.path.join(settings.IMG_PATH,url.split('/')[-1]))
#         except:
#             with open('rizhi.txt','a') as fs:
#                 print(f'下载失败,url为{url}\n',file=fs)




# c = Craw()
# html = c.craw_text('http://book.zongheng.com/store/c0/c0/b0/u0/p2/v9/s1/t0/u0/i1/ALL.html')
# url_lsits = c.craw_img_url(html)
# for i in url_lsits:
#     c.craw_img(i)

#爬取页内容
def craw_text(url):
    bs = requests.get(url=url, headers = settings.HEAD)
    print(bs)
    html = bs.content
    html = BeautifulSoup(html,'lxml')
    return html
#获取图片的url
def craw_img_url( html):
    html = html.find_all('div', {'class': 'store_collist'})
    html = BeautifulSoup(str(html),'lxml')
    img_url = [s.extract() for s in html("img")]
    url_list = [s.attrs['src'] for s in img_url if 'src' in s.attrs]
    url_lists =[]
    for img_url in url_list:
        if not re.match(r'.*(jpg|png|gif|jpeg)$', img_url):
            pass
        elif re.match(r'^http.*', img_url):

            url_lists.append(img_url)
        else:
            img_url = settings.ROOT_URL + img_url
            url_lists.append(img_url)

    # for link in img_url:
    #     if 'src' in link.attrs:
    #        print(link.attrs['src'])
    return url_lists
    # def craw_img_url(self, url):
    #     bs = requests.get(url=url,headers=settings.HEAD)
    #     html = bs.content
    #     html = BeautifulSoup(html,'lxml')
    #     img_url = [s.extract() for s in html("img")]
    #     url_list = [s.attrs['src'] for s in img_url if 'src' in s.attrs]
    #     url_lists =[]
    #     for img_url in url_list:
    #         if not re.match(r'.*(jpg|png|gif|jpeg)$', img_url):
    #             pass
    #         elif re.match(r'^http.*', img_url):
    #
    #             url_lists.append(img_url)
    #         else:
    #             img_url = settings.ROOT_URL + img_url
    #             url_lists.append(img_url)
    #
    #     # for link in img_url:
    #     #     if 'src' in link.attrs:
    #     #        print(link.attrs['src'])
    #     return url_lists

def craw_page_url( url):
    pass

#生成爬取页的链接
def craw_next():
    return [f'http://book.zongheng.com/store/c0/c0/b0/u0/p{page}/v9/s1/t0/u0/i1/ALL.html' for page in range(1,75)]

#下载
def craw_img(url):
    try:
        request.urlretrieve(url=url,filename=os.path.join(settings.IMG_PATH,url.split('/')[-1]))
    except:
        with open('rizhi.txt','a') as fs:
            print(f'下载失败,url为{url}\n',file=fs)

def craw_next_url():

    return 0


# def craw_next(url):
#
#     if url == None:
#         return False
#     yield url


def get_text(url):
    text = requests.get(url=url,headers = settings.HEAD)
    html = BeautifulSoup(text.content,'lxml')
    html = html.find_all(name='div', attrs={'class': 'store_collist'})
    html = BeautifulSoup(str(html),'lxml')
    return html



def get_html_name(html):
    html_name = html.find_all(name='div', attrs={'class': 'bookname'})
    html_name = str(BeautifulSoup(str(html_name),'lxml'))
    kk = re.compile(settings.RE_NAME)
    return kk.findall(html_name)

def get_html_name_a(html):
    html = html.find_all(name='div', attrs={'class': 'bookname'})
    html_name_a = BeautifulSoup(str(html), 'lxml')
    list_url = [s.extract() for s in html_name_a("a")]
    return [s.attrs['href'] for s in list_url if 'href' in s.attrs]

def get_html_ilnk(html):
    html_ilnk = str(BeautifulSoup(str(html), 'lxml'))
    html_ilnk = str(BeautifulSoup(str(html_ilnk), 'lxml'))
    kk = re.compile(settings.RE_ILNK)
    return kk.findall(html_ilnk)


# a = 'http://book.zongheng.com/store/c0/c0/b0/u0/p75/v9/s1/t0/u0/i1/ALL.html'
#
# s = get_text(a)
# ss = get_html_ilnk(s)
# ss = get_html_name_a(s)
# ss = get_html_name(s)
# print(ss)