import re
import requests

from bs4 import BeautifulSoup





import settings


# url_list = ['/upload/cover/22/d6/22d6e673d824334bb552750011a42410.jpeg', 'http://static.zongheng.com/upload/cover/ff/20/ff20ebfe3f4e86e4f917342fb6d6929f.jpeg', 'http://static.zongheng.com/upload/cover/ec/12/ec12c61d5f471e4a2a24a6d4a5c317bc1594605806570.jpeg', 'http://static.zongheng.com/upload/cover/f4/a8/f4a8527dafe120251e3dde3d49a9e06f.jpeg', 'http://static.zongheng.com/upload/cover/85/ed/85ed908e7deb81b66e2f9572eecf2808.jpeg', 'http://static.zongheng.com/upload/cover/f1/f6/f1f6ba286ee2d19e225e91b3c0379644.jpeg', 'http://static.zongheng.com/upload/cover/28/23/2823dd5af335ef91b81130b097c8afde.jpeg', 'http://static.zongheng.com/upload/cover/4f/d1/4fd1ac0b2f09cc2e0a64f5247b85b6d1.jpeg', 'http://static.zongheng.com/upload/cover/74/cf/74cfe56ff7cc36c99fbeaf668191bbc21602902017148.jpeg', 'http://static.zongheng.com/upload/cover/c9/3d/c93deceb1073f0d90670b3bb305904bf.jpeg', 'http://static.zongheng.com/upload/cover/dc/db/dcdbb9776f5c91e8d84721e20c4ce9bb.jpeg', 'http://static.zongheng.com/upload/cover/97/3e/973e45a7a52d8d9f14bb23efff7f9741.jpeg', 'http://static.zongheng.com/upload/cover/0c/25/0c25d1ca9c932b009442b9f6319f015f.jpeg', 'http://static.zongheng.com/upload/cover/02/2e/022ec21b3ec2478a2b5cbbb5ca5b7a1f.jpeg', 'http://static.zongheng.com/upload/cover/95/5b/955b6425f2976a126a878060f9df6756.jpeg', 'http://static.zongheng.com/upload/cover/c6/16/c616a93ed5faee29cc08534db6c5d37b1596611209768.jpeg', 'http://static.zongheng.com/upload/cover/96/2b/962bd1d307fb90e0b9b3b68131ebc5a2.jpeg', 'http://static.zongheng.com/upload/cover/74/26/74261edba426385bf83969db0265d8f6.jpeg', 'http://static.zongheng.com/upload/cover/53/08/53080a7099b450af0f48c10caddfe6d4.jpeg', 'http://static.zongheng.com/upload/cover/63/48/634889b224382b4a3189601b5e2d04a5.jpeg', 'http://static.zongheng.com/upload/cover/41/7f/417fb63b7ae9002e9667ab700ee82bbf.jpeg', 'http://static.zongheng.com/upload/cover/23/48/23482f5d461d3b467e118eefee524ac2.jpeg', 'http://static.zongheng.com/upload/cover/7f/43/7f43d3c5557fe2c9731ee54b132ebc3e.jpeg', 'http://static.zongheng.com/upload/cover/e4/dc/e4dc1db39771ab248d7020d1b569341a.jpeg', 'http://static.zongheng.com/upload/cover/4b/f4/4bf41e69ec973dd939fa8c9394c583dd.png', 'http://static.zongheng.com/upload/cover/ef/df/efdf7cec87fb5a5ad71ad99ddb9d217b.jpeg', 'http://static.zongheng.com/upload/cover/9d/d0/9dd04b6864f48a7f35ffa8aba3c12052.jpeg', 'http://static.zongheng.com/upload/cover/68/5e/685e2bc7ddcc95530f96252e4fd06e90.jpeg', 'http://static.zongheng.com/upload/cover/3b/a9/3ba9b8ff2308e3205db68915186c9d83.jpeg', 'http://static.zongheng.com/upload/cover/0a/71/0a71d94a81c3a4757769a43c946723cf.jpeg', 'http://static.zongheng.com/upload/cover/6c/ec/6cec626ed857f1daab884a3ba3e92116.jpeg', 'http://static.zongheng.com/upload/cover/05/3b/053b181c15f42f479e6addc70e45dc5b.jpeg', 'http://static.zongheng.com/upload/cover/8a/79/8a791dfd640b81719113de85fc770ede.jpeg', 'http://static.zongheng.com/upload/cover/4c/c6/4cc62058fc480a251cb35df688f39ffa.jpeg', 'http://static.zongheng.com/upload/cover/5e/60/5e6044ec127d4d965352168528a5f454.jpeg', 'http://static.zongheng.com/upload/cover/26/76/2676460169b68c3946f5a7083aceebc2.jpeg', 'http://static.zongheng.com/upload/cover/36/3b/363b08c69586dd56c8213690966585e1.jpeg', 'http://static.zongheng.com/upload/cover/68/72/6872cd5d66efce1128dc2fed0ff0d1c2.jpeg', 'http://static.zongheng.com/upload/cover/6e/76/6e765e4afde90da0e9673c943e45bd2c.jpeg', 'http://static.zongheng.com/upload/cover/38/e3/38e3113d0ab64944debd71140320d356.jpeg', 'http://static.zongheng.com/upload/cover/05/fc/05fc45de9599423449c8e83a705239a3.jpeg', 'http://static.zongheng.com/upload/cover/fe/cd/fecda73773dde283edef9c9a775bcc7d.jpeg', 'http://static.zongheng.com/upload/cover/74/e1/74e1c96b8218bce8236f728bcdcdc1e0.jpeg', 'http://static.zongheng.com/upload/cover/48/00/480039f47c727aec18d368f57e5c20c1.png', 'http://static.zongheng.com/upload/cover/5a/8c/5a8c43271cd2f3ed6c1ecc80134336b4.jpeg', 'http://static.zongheng.com/upload/cover/ca/58/ca58d95d00225db050f14b7667c6395e.jpeg', 'http://static.zongheng.com/upload/cover/1d/3b/1d3b36aa1bae30740cbb1d2ff28d64fb.jpeg', 'http://static.zongheng.com/upload/cover/5a/a5/5aa5cd7ab660aa53b7efb59ef06cc6721596596658289.jpeg', 'http://static.zongheng.com/upload/cover/2a/bf/2abf9092a6f035b8764fb36f2b98c21f.jpeg', 'http://static.zongheng.com/upload/cover/ee/b9/eeb9d45a338d4ab21376d787ce82f04a.jpeg']
#
# url_lists = []
# for img_url in url_list:
#     if not re.match(r'.*(jpg|png|gif|jpeg)$', img_url):
#         continue
#     elif re.match(r'^http.*', img_url):
#         url_lists.append(img_url)
#     else:
#         img_url = settings.ROOT_URL + img_url
#         url_lists.append(img_url)
#
# print(url_lists)




    # html_ilnk = html.find_all(name='div', attrs={'class': 'bookilnk'})
    # html_name_a = BeautifulSoup(str(html_name), 'lxml')
    # list_url = [s.extract() for s in html_name_a("a")]
    # list_urls= [s.attrs['href'] for s in list_url if 'href' in s.attrs]
    # print(list_urls)
    # html_name = str(html_name_a)
    # html_ilnk = str(BeautifulSoup(str(html_ilnk), 'lxml'))
    # kk = re.compile(r'target="_blank">(.*)</a>')
    #
    # list_name = kk.findall(html_name)
    # list_ilnk = kk.findall(html_ilnk)
    # print(list_name)
    # print(list_ilnk)


