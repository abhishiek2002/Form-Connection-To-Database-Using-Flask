from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('service.html')

@app.route('/contacts')
def contacts():
    return render_template('contact.html')

@app.route('/my_portfolio')
def my_portfolio():
    return render_template('portfolio.html')


if __name__=="__main__":
    app.run(debug=True)
    