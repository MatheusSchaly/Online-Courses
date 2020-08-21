from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report')
def report():
    username = request.args.get('username')
    has_upper = any(char.isupper() for char in username)
    has_lower = any(char.islower() for char in username)
    num_at_end = username[-1].isnumeric()
    passed = has_upper and has_lower and num_at_end
    return render_template('report.html', passed=passed, has_upper=has_upper,
                            has_lower=has_lower, num_at_end=num_at_end)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
