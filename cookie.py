import os
import requests
import lxml
import re
import json
from bs4 import BeautifulSoup
from config import *

login_url = 'https://passport.weibo.cn/sso/login'
session = requests.Session()
login = session.post(login_url, data=data, headers=headers)
response = session.get('https://www.weibo.cn')

def save_session():
    if response.status_code == 200:
        tips = json.loads(login.text)
        if tips.get('retcode') == 20000000:
            pattern = re.compile('class="ut">(.*?)<a')
            hello = re.search(pattern, response.text).group(1)
            print('登录成功：欢迎您，{0}！'.format(hello))
            #保存cookie
            return session
        elif tips.get('retcode') == 50011015:
            print('登录失败：', tips.get('msg'))
            return None
        elif tips.get('retcode') == 50011002:
            print('登录失败：', tips.get('msg'))
            return None
        elif tips.get('retcode') == 50011005:
            print('登录失败：', tips.get('msg'))
            return None
    else:
        print('登录失败！问题是:{}。'.format(response.status_code))



# def get_session():
#     if not os.path.exists('cookie'):
#         save_session()
