from flask import Flask, render_template ,request

# 實體化一個applicaiton
# 帶入的__name__可以是任意字串,但通常都使用__name__
app = Flask(__name__)

# 當需要比較多的參數就需要使用 request
# 這時候要注意的是 request.args 是客戶端使用GET方法時存放參數的地方
# 當客戶端使用POST方法時, 參數則是存放在 request.form 之中
@app.route('/person_detail')
def person_detail():
    dic = request.args
    return render_template('index2.html', dic=dic)

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    app.run(port=5000,debug=True)