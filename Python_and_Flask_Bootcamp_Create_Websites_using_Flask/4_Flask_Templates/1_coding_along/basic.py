from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Looks for basic.html inside the templates folder
    return render_template('basic.html')

if __name__ == '__main__':
    app.run(debug=True)
