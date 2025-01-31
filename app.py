from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)


## if we sucessful open home page then go basehtml
@app.get("/")
#@app.route("/",methods = ["GET"]) 
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO:check if text is valid
    respone = get_response(text)
    message = {"answer": respone}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)