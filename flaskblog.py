from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asjvdjh87237216f3heg66v77'

posts1 = [ 

    { 
        'author' : 'Anirudh',
        'title'  : 'First Content',
        'content': 'Hi, this is my first post on my flask hosted local host',
        'date_posted' : 'December 25, 2022'
           
     },
     { 
        'author' : 'Levon',
        'title'  : 'Arm Wrestling',
        'content': 'Rules for arm wrestling, here is the link - https://en.wikipedia.org/wiki/Arm_wrestling',
        'date_posted' : 'December 15, 2022'
           
     }

         ]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts1, title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

'''@app.route("/login",  methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
    return render_template('login.html', title = 'Login', form = form)'''

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug = True)