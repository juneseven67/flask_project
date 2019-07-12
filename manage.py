import os
from app import app

# 當此程式是啟動點會啟動app.run(import到別的程式中則不會)
if __name__ == '__main__':
    print(os.getcwd())
    print(app.root_path)
    app.run(port=5000,debug=True)
