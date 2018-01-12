import requests
import json
import hashlib
import time

#Login via stuNum and password
def login(session, j_username, j_password):
    md5 = hashlib.md5()
    md5.update(j_password.encode('utf-8'))
    j_password = md5.hexdigest()
    # print(j_password)
    data = {
        'j_username': j_username,
        'j_password': j_password
    }
    headers = {
        'Host': "bkjwxk.sdu.edu.cn",
        'Accept-Language': "zh-CN,zh;q=0.9",
        'Accept-Encoding': "gzip, deflate",
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
        'Referer': 'http://bkjwxk.sdu.edu.cn/f/login',
        'X-Requested-With': 'XMLHttpRequest'
    }
    login_url = 'http://bkjwxk.sdu.edu.cn/b/ajaxLogin'
    print('[登录中...]')
    response = session.post(login_url, headers=headers, data=data).content.decode('utf-8')
    # print(response)
    if response == r'"success"':
        print('[登录成功！]')
        return True
    else:
        print('[登录失败，请检查账号密码是否输入正确！]')
        return False


def start_fucking_the_server(session, j_username, j_password, kch, kxh):
    url = 'http://bkjwxk.sdu.edu.cn/b/xk/xs/add/%s/%s' % (kch, kxh)
    while True:
        response = session.post(url)
        response.encoding = 'utf-8'
        if '成功' in response.text:
            print('课程号：%s 课序号：%s 选课成功' % (kch, kxh))
            break
        time.sleep(3)
        print(response.text)



if __name__ == '__main__':
    print('>>>欢迎使用山东大学选课脚本，你可以在任何时间按下ctrl+c退出本程序。')
    j_username = input('>>>请输入你的学号\n')
    j_password = input('>>>请输入你的选课密码\n')

    session = requests.Session()

    login_succeeded = login(session, j_username, j_password)
    while not login_succeeded:
        j_username = input('>>>请输入你的学号\n')
        j_password = input('>>>请输入你的选课密码\n')
        login_succeeded = login(session, j_username, j_password)
    print(session.cookies)

    print('>>>请自行登录选课网站，查询想要抢的课程的课程号和课序号。每次只能抢一门课哟！')
    kch = input('>>>请输入课程号 (eg:sd03031770)')
    kxh = input('>>>请输入课序号 (eg:100)')
    start_fucking_the_server(session, j_username, j_password, 'sd03031770', '100')
