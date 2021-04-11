from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    texts = ["猫", "犬", "うさぎ", "亀", "馬"]
    return render_template("index.html", name=name, texts=texts)


if __name__ == "__main__":
    app.run(debug=True)
