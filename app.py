from flask import Flask, render_template
import random

app = Flask(__name__)

def flipCoin():
    return "Heads" if random.randint(1, 2) == 1 else "Tails"

@app.route('/')
def index():
    result = flipCoin()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
