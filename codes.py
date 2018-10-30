import requests
# import re
# 网易云音乐的歌单都是有 id 的
# 可以根据 id 来查找
# 注意 headers 。
import re


url = 'https://music.163.com/playlist?id=2256615030'
# 更换 id= 即可实现不同歌单的下载

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x6'
                  '4; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Referer': 'https://music.163.com/',
    'Host': 'music.163.com',
    'Cookie': 'JSESSIONID-WYYY=syS%2FeQT1X690JQBlhKWc7hWTN'
              '0Vow0oGMQtKvzSVHxE%2BZz07h81D%2BhiQqw6eH9Xl'
              'UCb8X3o1fIBoX8357yQppA9fkMqwFuOHAbXySp%2FkK'
              'P7BjVBPr7ee%2B88u6zawnONX%2BcPz8xhd%2BSGo8r'
              '8Ci9UkJZUbRX%5CkvG0xmj1q%2Fw8pCTSaxbWX%3A15'
              '40829337762; _iuqxldmzr_=32; _ntes_nnid=f18'
              '13c7102d3a1c932957cc89b3b85cf,154082405766'
              '1; _ntes_nuid=f1813c7102d3a1c932957cc89b3b'
              '85cf; __utma=94650624.652102838.1540824059.1'
              '540824059.1540824059.1; __utmb=94650624.22.1'
              '0.1540824059; __utmc=94650624; __utmz=94650'
              '624.1540824059.1.1.utmcsr=baidu|utmccn=(orga'
              'nic)|utmcmd=organic; WM_NI=HEBQ%2FhEZ8gjyXw'
              'Zc4k4tEYInt2taK4Jgmgb4fmdJBA2XqfHwgbD3Lmmv%2'
              'ByISgbC75m%2FWSgpRkrmrbWxTbqYcc3BTZR2VP3o0q5'
              'RTJwWT8trPeJXGal9jIIzFQcdyR9CFamE%3D; WM_NIK'
              'E=9ca17ae2e6ffcda170e2e6eeb0ea3cf8f5e5bbc93a'
              '98968eb3d14b868f8faaf26ea68b9eb0f64392edaa98'
              'e62af0fea7c3b92a8c9b8eb2ae648786f888e9739ca9'
              '9684b761f8ac8bbacc66b8eebc82ca408ab9a388e140'
              'a6b3acabc14bf288bf87cb7da5be8cd4cf67afaae59a'
              'cc59a5be8dd8b867ed899d88f35aa9aea393e15dbc8c'
              'ae92dc69a1ed8eb5d95af28aa0d4ee3cb3eb9eb5c97d'
              '958cf895f15ca79698a8e468fbb687aaf94e93bdac9ad'
              '133819aaf8ec837e2a3; WM_TID=FIGfA%2FDa7jxBQE'
              'VFBRd4PLBQcSdzA6L7; playerid=33825571'
}
# headers 是必须的

result = requests.get(url, headers=head)
result.encoding = result.apparent_encoding
# 获得歌单源代码
string = result.text
urllist = re.findall(r'href="/song\?id=(\d*?)"', string)
# 正则比 bs4 好使些
songnamelist = re.findall(r'"/song\?id=\d*">(.*?)</a><', string)
# 到源代码里去找歌名到底在哪儿，有时候看网页上的代码看不出来
count = 1
long = len(urllist)
for n in range(0, 10):
    link = 'http://music.163.com/song/media/outer/url?id={0}.mp3'.format(urllist[n])
    with open(r'C:\Users\******\Desktop\temp\{0}.mp3'.format(songnamelist[n]), 'wb') as song:
        # 就把文件放在桌面吧，使用时请替换掉 * 。
        song.write(requests.get(link).content)
        # 用requests.get() 方法来下载
    print('\r正在下载第 %d 首歌。' % count, end='')
    # \r 可以实现原地显示，而不是循环一次输出一行
    count += 1
