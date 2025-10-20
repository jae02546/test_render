from flask import Flask, render_template

app = Flask(__name__)

# トップページ（ボタンあり）
@app.route("/")
def index():
    return render_template("index.html")

# ボタン押下時に呼ばれる（HTMXがここにアクセス）
@app.route("/hello")
def hello():
    return "<p>こんにちは、HTMXとFlaskの世界！😸</p>"

if __name__ == "__main__":
    app.run(debug=True)
