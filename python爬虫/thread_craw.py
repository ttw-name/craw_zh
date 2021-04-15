

import time

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


import main_craw



def thrad_craw_img(img_qeueu_get):
    while True:
        time.sleep(0.5)
        if img_qeueu_get.empty():
            break
        img_urls = img_qeueu_get.get()
        with ThreadPoolExecutor() as pool:
            for url in img_urls:
                pool.submit(main_craw.craw_img,url)

class Thrad_craw_img_url():
    def __init__(self,url_queue_put):
         self.url_queue_put = url_queue_put
    def thrad_craw_img_url(self,url):
        html = main_craw.craw_text(url=url)
        url_img_urls = main_craw.craw_img_url(html=html)
        self.url_queue_put.put(url_img_urls)

def thrad_pool(url_queue_put):
    q = Thrad_craw_img_url(url_queue_put)
    urls = main_craw.craw_next()
    with ThreadPoolExecutor() as pool:
        pool.map(q.thrad_craw_img_url,urls)

def zh_craw(url):
    html = main_craw.get_text(url=url)
    list_name = main_craw.get_html_name(html)
    list_ilnk = main_craw.get_html_ilnk(html)
    list_name_a = main_craw.get_html_name_a(html)
    list_name_img_a = main_craw.craw_img_url(html)
    return {'list_name':list_name,'list_ilnk':list_ilnk,'list_name_a':list_name_a,'list_name_img_a':list_name_img_a}

class ZhCrawPool():
    def __init__(self,queue_put):
        self.queue_put = queue_put
    def zh_Craw_Pool(self,url):
        html = main_craw.get_text(url=url)
        list_name = main_craw.get_html_name(html)
        list_ilnk = main_craw.get_html_ilnk(html)
        list_name_a = main_craw.get_html_name_a(html)
        list_name_img_a = main_craw.craw_img_url(html)
        ditc_list = {'list_name':list_name,'list_ilnk':list_ilnk,'list_name_a':list_name_a,'list_name_img_a':list_name_img_a}
        self.queue_put.put(ditc_list)


def zh_pool(q):
    q_put = ZhCrawPool(q)
    urls  = main_craw.craw_next()
    with ThreadPoolExecutor() as pool:
        pool.map(q_put.zh_Craw_Pool,urls)
# class Dispose_Pool():
#     def __init__(self,q_get:queue.Queue,q_put:queue.Queue):
#         self.q_get = q_get
#         self.q_put = q_put
#     def to_dispose(self):
#         dict_list = self.q_get.get()
#         list_name = dict_list['list_name']
#         list_ilnk = dict_list['list_ilnk']
#         list_wirter = []
#         list_type = []
#         for i in range(0,len(list_ilnk),2):
#             list_wirter.append(list_wirter[i])
#             list_wirter.append(list_type[i+1])
#         list_name_a = dict_list['list_name_a']
#         list_name_img_a = dict_list['list_name_img_a']
#         sql_cont = "('%s','%s','%s','%s','%s')"
#         sql_list = []
#         for w,t,i,u,b in zip(list_wirter,list_type,list_name_a,list_name_img_a):
#             sql_cont = sql_cont%(w,t,i,u,b)
#             sql_list.append(sql_cont)
#         self.q_put.put( ",".join(sql_list))
# def dispose_Pool(q_get:queue.Queue,q_put:queue.Queue):
#     q = Dispose_Pool(q_get,q_put)
#     with ThreadPoolExecutor() as pool :
#         pool.map(q.to_dispose)



def to_dispose(q_get,q_put):
    while True:
        dict_list = q_get.get()
        list_name = dict_list['list_name']
        list_ilnk = dict_list['list_ilnk']
        list_wirter = []
        list_type = []
        for i in range(0,len(list_ilnk),3):
            list_wirter.append(list_ilnk[i+1])
            list_type.append(list_ilnk[i+2])
        list_name_a = dict_list['list_name_a']
        list_name_img_a = dict_list['list_name_img_a']

        sql_list = []
        for b,w,t,u,i in zip(list_name,list_wirter,list_type,list_name_a,list_name_img_a,):
            sql_cont = "('%s','%s','%s','%s','%s')"%(b,w,t,u,i)
            sql_list.append(sql_cont)
        q_put.put( ",".join(sql_list))
        if q_get.qsize() == 0:
            break
























if __name__ == '__main__':
    q = queue.Queue()
    thrad_pool(q)
    thrad_craw_img(q)



