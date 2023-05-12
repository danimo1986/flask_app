# coding: utf-8

from flask import Flask, render_template

# app という変数でFlaskオブジェクトをインスタンス化
app = Flask(__name__)

# --- View 側の設定 ---
# rootディレクトリにアクセスした場合の挙動
@app.route('/')

# def 以下がアクセス後の操作
def index():
    # return 'Hello World!'
    return render_template('index.html') #追加

# メイン関数
if __name__ == '__main__':
    app.run()

# pip list memo
#Package            Version
#blinker            1.6.2
#click              8.1.3
#colorama           0.4.6
#Flask              2.3.2
#gunicorn           20.1.0
#importlib-metadata 6.6.0
#itsdangerous       2.1.2
#Jinja2             3.1.2
#MarkupSafe         2.1.23
#pip                23.1.2
#setuptools         58.1.0
#Werkzeug           2.3.4
#zipp               3.15.0

# [Memo] requirements.text作成の手順
# https://qiita.com/sakusaku12/items/21083c73c8afa4f6c78d
# pip freeze > requirements.txt
# pip install -r requirements.txt

# [Memo]git add .でLF will be replaced by CRLF the next time Git touches iが出まくった
# https://normalblog.net/system/lf_replaced_crlf/