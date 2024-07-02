from flask import Flask, render_template

#Create a flask instance
app = Flask(__name__)



#create a route decorateor
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"

def index():
    first_name ="Zawad"
    stuff = "This is a bold text"
    fav_pizza = ["chicken", "mushroom", "beef", 31]
    return render_template( "index.html",
                           first_name=first_name, 
                           stuff=stuff,
                           fav_pizza=fav_pizza)


# localhost:5000/user/Zawad
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", _username=name)


#Create Custom Error pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)