import os,sys,re,time
print('start scan...')
start_time = time.time()
PATH = sys.path[0]
scan_ip = []
# os.popen('{}/tools_file/nmap_win/nmap.exe -sn -PR 192.168.1.0/24 -oN {}/tools_file/nmap_win/scan_all_ip.txt'.format(PATH,PATH),'w')
with open(PATH + '/resources_file/ip_list.txt','w') as f:
    for i in os.popen('{}/tools_file/nmap_win/nmap.exe -sn -PR 192.168.1.0/24'.format(PATH)).readlines():
        if 'Nmap scan report for' in i:
            f.write(re.findall(r'[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}',i)[0] + '\n')
f.close()
end_time = time.time()
print('scan end | spend time >> {}s'.format(end_time - start_time))