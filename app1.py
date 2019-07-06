from flask import Flask, render_template

# 實體化一個applicaiton
# 帶入的__name__可以是任意字串,但通常都使用__name__
app = Flask(__name__)

# 可以透過參數傳遞,獲取不同的參數
# 但大多數不適用,應該更仔細定義路由(URL)
@app.route('/<name>')
def index(name):
    return render_template('index1.html', name=name)

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    app.run(port=5000,debug=True)