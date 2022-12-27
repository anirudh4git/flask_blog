from flask import Flask, render_template

app = Flask(__name__)

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
def hello_world():
    return render_template('home.html', posts = posts1, title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')



if __name__ == '__main__':
    app.run(debug = True)