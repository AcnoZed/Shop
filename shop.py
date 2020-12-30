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
    return render_template('home.html', products = products)

@app.route("/about")
def about():
    return "<h4>About Page</h4>"

##if __name__ == '__main__':
##    app.run(debug=True)