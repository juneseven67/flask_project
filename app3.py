from flask import Flask, render_template ,request

# 實體化一個applicaiton
# 帶入的__name__可以是任意字串,但通常都使用__name__
app = Flask(__name__)

# POST沒辦法透過網址列打上想要的參數而傳遞,要透過以下方法
@app.route('/click_to_post')
def click_to_post():
    return render_template('index3_1.html')

@app.route('/person_detail_post',methods=['POST'])
def person_detail_post():
    dic = request.form
    return render_template('index3_2.html', dic=dic)

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    app.run(port=5000,debug=True)