from flask import Flask , render_template




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get')
def get():
    return render_template('get.html')



if __name__ == '__main__':
    app.run(debug=True)