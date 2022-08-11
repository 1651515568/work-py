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
    # file_name = req.values.get('flag')#所有数据
    if file_down:
        print(file_down)
        return send_file(PATH + '/share_file/{}'.format(file_down),as_attachment=True)#,attachment_filename='b.txt'
    elif file_read:
        print(file_read)
        return send_file(PATH + '/share_file/{}'.format(file_read),as_attachment=False)#,attachment_filename='b.txt'
    else:
        return render_template('index.html',file = file_list)
@app.route('/downfile.html',methods=['GET','POST'])
def get_date_for_qq_robot():
    # msg = req.get_data()
    file_tag = req.args.get('flag')
    file_name = req.values.get('flag')

    if file_name == 'a':
        
        # return send_file('E:/work-code\python-code\ctf/a.txt',mimetype=None,as_attachment=True,attachment_filename='b.txt')
        return 'dwadawdaw'
    else:
        return 'fwafawd'
if __name__ == '__main__':
    app.run()
