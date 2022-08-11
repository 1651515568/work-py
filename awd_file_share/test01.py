from flask import Flask,abort,Response,send_file,render_template
from flask import request as req
import json,requests,os,sys,pymysql,time
PATH = sys.path[0]
app = Flask(__name__)
@app.route('/index.html',methods=['GET','POST'])
def show_file():
    file_list = os.listdir(PATH + '/share_file')
    file_down = req.args.get('flag')#get数据
    file_read = req.args.get('read')#get数据
    #f = req.files['file']

    # file_name = req.values.get('flag')#所有数据
    if file_down:
        print('down',file_down)
        return send_file(PATH + '/share_file/{}'.format(file_down),as_attachment=True)#,attachment_filename='b.txt'
    elif file_read:
        try:
            print('read',file_read)
            can_konw = ['html','txt','jpg','png','art','au','aiff','xbm']
            if file_read.split('.')[-1].lower() in can_konw:
                return send_file(PATH + '/share_file/{}'.format(file_read),as_attachment=False)#,attachment_filename='b.txt'
            else:
                tmp_file = []
                with open(PATH + '/share_file/{}'.format(file_read), 'r',encoding='utf-8') as f:
                    for i in f.readlines():
                        tmp_file.append(i)
                return render_template('show.html',file = tmp_file)
        except Exception as e:
            return 'can\'t open this file!!!'
    elif req.method == 'POST' and req.values.get('upload') == '提交':
        file = req.files['upload']
        the_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) 
        file.save("{}/share_file/up-{}-{}".format(PATH,the_time,file.filename))
        return render_template('index.html',file = file_list)
    else:
        return render_template('index.html',file = file_list)
if __name__ == '__main__':
    app.run(debug=True)