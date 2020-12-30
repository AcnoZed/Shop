from flask import Flask, render_template
app = Flask(__name__)

products = [
    {
        'productname' : 'milk',
        'price'       : '0.80' 
    },
    {
        'productname' : 'juice',
        'price'       : '1.09'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', products = products, title= 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

##if __name__ == '__main__':
##    app.run(debug=True)