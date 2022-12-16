from flask import Flask, render_template, request
from plant import playSound

app = Flask(__name__, template_folder='../views', static_folder='../views/public')

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == "POST":
        playSound()
    return render_template('index.html')

@app.route('/button', methods=["GET", "POST"])
def button():
    if request.method == "POST":
        return render_template("button.html", ButtonPressed = ButtonPressed)
    return render_template("button.html", ButtonPressed = ButtonPressed)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
