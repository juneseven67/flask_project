from flask import Flask, render_template

# 實體化一個applicaiton
# 帶入的__name__可以是任意字串,但通常都使用__name__
app = Flask(__name__)

# 定義路由,只要打上此application的IP:port/route就會啟動此function
# 當使用html作為回傳的內容,需要使用render_template的功能
# 要記住flask預設抓取html的資料夾為templates
# 只要是flask的程式就需要有回傳值不然會報錯
@app.route('/')
def index():
    # return 'hello world'
    return render_template('index.html')

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    app.run(port=5000,debug=True)