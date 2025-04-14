from flask import Flask, render_template

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"
    
@app.route('/zeronevape')
def zeronevape():
    return render_template('zeronevape.html')

@app.route('/zeronevape/ddd/<string:zeronevape>')
def getnama(zeronevape):
    return "zeronevape adalah toko {}".format(zeronevape)


@app.route('/mynamee/<name>')  # Variabel name diambil dari URL
def user(name):
    return f"Hello, {name}!"

@app.route('/user/<int:zeronevape>')  # Hanya menerima angka
def user_id(zeronevape):
    return f"User ID: {zeronevape}"

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', username=name)

app_name = "My Flask App"  # Variabel global

@app.route('/')
def home():
    return f"Welcome to {app_name}!"



if __name__ == '__main__':
    app.run(debug=True)




