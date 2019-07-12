from flask import Flask, render_template, request, url_for, redirect

# 實體化一個applicaiton
# 帶入的__name__可以是任意字串,但通常都使用__name__
app = Flask(__name__)

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

@app.route('/<name>')
def index(name):
    return render_template('index1.html', name=name)

# 當需要對於每個route都想做預先(或之後)執行某個function的時候可以使用before_request跟after_request
# 比較需要注意的是after_request需要接收response參數,這是由route傳出來需要傳到客戶端的,並且需要再把它傳出去
@app.before_request
def before_request():
    print('before request, I want to return a response.')

@app.after_request
def after_request(response):
    print('After request, I make a response.')
    return response

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    app.run(port=5000,debug=True)