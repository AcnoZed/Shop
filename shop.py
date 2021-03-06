from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e02e24972dd55502ab821dac9d817430'
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

@app.route("/register",methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created succesfully {form.username.data}','succes')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form = form)

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login succesfully {form.email.data}')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form = form)



if __name__ == '__main__':
    app.run(debug=True)