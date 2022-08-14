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