import time
import queue
import threading

import thread_craw
import thread_insert




if __name__ == '__main__':
    #下载图片
    # q = queue.Queue()
    # thread_craw.thrad_pool(q)
    # thread_craw.thrad_craw_img(q)

    q_get = queue.Queue()
    q_put = queue.Queue()

    thread_craw.zh_pool(q_get)

    for i in range(10):
        i = threading.Thread(target=thread_craw.to_dispose,args=(q_get,q_put))
        i.start()
    time.sleep(3)
    for i in range(7):
        threading.Thread(target=thread_insert.gouzhao,args=(q_put,)).start()





