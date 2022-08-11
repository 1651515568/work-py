import sys
PATH = sys.path[0]
clear_url = []
http_url = []
https_url = []
with open(PATH + '/resources_file/ip_list.txt','r') as f:
    for i in f:
        t = i.split('\n')[0]
        clear_url.append(t)
        t = 'http://{}'.format(t)
        http_url.append(t)
        tt = 'https://{}'.format(t)
        https_url.append(tt)

