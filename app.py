from flask import Flask, render_template, request, url_for, redirect, send_from_directory
import os
from admin import admin  
# from 資料夾,檔案 import 藍圖
# from admin.admin import admin

# 實體化一個applicaiton
# 帶入的__name__可以是任意字串,但通常都使用__name__
app = Flask(__name__)

# 搭配admin.py使用
# 將admin裡面設定的route註冊到app裡面
# 透過設定url_prefix將admin的route都加上admin的前綴
app.register_blueprint(admin, url_prefix='/admin')

# 定義路由,只要打上此application的IP:port/route就會啟動此function
# 當使用html作為回傳的內容,需要使用render_template的功能
# 要記住flask預設抓取html的資料夾為templates
# 只要是flask的程式就需要有回傳值不然會報錯
@app.route('/')
def index():
    # return 'hello world'
    return render_template('index.html')

# 可以透過參數傳遞,獲取不同的參數
# 但大多數不適用,應該更仔細定義路由(URL)
@app.route('/<name>')
def name(name):
    return render_template('index1.html', name=name)

# 當需要比較多的參數就需要使用 request
# 這時候要注意的是 request.args 是客戶端使用GET方法時存放參數的地方
# 當客戶端使用POST方法時, 參數則是存放在 request.form 之中
@app.route('/person_detail')
def person_detail():
    dic = request.args
    return render_template('index2.html', dic=dic)

# POST沒辦法透過網址列打上想要的參數而傳遞,要透過以下方法
@app.route('/click_to_post')
def click_to_post():
    return render_template('index3_1.html')

@app.route('/person_detail_post',methods=['POST'])
def person_detail_post():
    dic = request.form
    return render_template('index3_2.html', dic=dic)

# 若要跳轉到不同頁面時, 最好的做好就是redirect到指定頁面
# 例如會員登出要跳轉回首頁等等
# 注意url_for裡要放的是function的名字而不是route的字串
# 當在網址上打to_hello/<name>時,回傳的頁面會是hello/<name>
@app.route('/to_hello/<name>')
def to_hello(name):
    return redirect(url_for('hello_name', name=name))

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('index4.html', name=name)

# 當需要對於"每個"route都想做預先(或之後)執行某個function的時候可以使用before_request跟after_request
# 比較需要注意的是after_request需要接收response參數,這是由route傳出來需要傳到客戶端的,並且需要再把它傳出去
@app.before_request
def before_request():
    print('before request, I want to return a response.')
    #if 'name' in request.url:
        #print('got a name!')
        #print('client ip is : ', request.remote_addr)

@app.after_request
def after_request(response):
    print('After request, I make a response.')
    return response

# 有時會遇到使用者進行錯誤的操作
# 可能是故意或不小心,需控制這種情控,需要errorhandler
# 針對不同的錯誤碼給予自定義的回應
# @app.app_errorhandler(404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(404)
def internal_server_error(e):
    return render_template('500.html'), 500

# flask有個特殊的route需要自行定義
# 就是favicon.ico(一定要這個名字),在網頁的頁籤圖示
# 習慣會將圖檔存在static資料夾中
# 於是需要定義直接從檔案回傳檔案的機制將路由導向static中的檔案
@app.route('/favicon.ico')
def mushroom():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                                'mushroom.ico',
                                mimetype='image/vnd.mcrosoft.icon')

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    app.run(port=5000,debug=True)
    