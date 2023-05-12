# <<環境構築時のメモ>>
# "flask"という名前で仮想環境を構築==>右記コードをターミナルで実行：conda create -n flask python=3.9
# condaが認識されず、右記リンク先で修正：https://qiita.com/syoukera/items/da2a5b11f99b71df9f42 ==>エラー変わらず
# python 3.6.5 ==> 3.9.13にupgrade: https://kamesuke-blog.com/programming/python_version/
# pipが古いバージョンだったので、upgradeした。
# condaは認識されたが、OpenSSLを要求された。
# 右記でOpenSSLをDL, インストール：https://slproweb.com/products/Win32OpenSSL.html


# 必要なモジュールのインポート
from flask import Flask

# Flaskをインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスがあった時の処理
@app.route("/")
def hello():
    return "Hello World!"

# エントリーポイント
if __name__ == "__main__":
    app.run()