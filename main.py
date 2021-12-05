from flask import Flask, render_template

app = Flask(__name__) # initalizing flask app

@app.route('/') # creating a route to the main screen
def home(): # function
    return "Hello, Orion!"

@app.route('/about') # creating a route to the main screen
def about(): # function
    return "The About Page"

@app.route('/blog') # creating a route to the main screen
def blog():
    posts = [{'title': 'The Journey of a self taught developer', 'author': 'Bob'},
             {'title': 'Python will not bite you', 'author': 'Timmy'}]
    return render_template('blog.html', author = "Orion", sunny = False, posts=posts) # template for the blog is on blog.html
@app.route('/blog/<string:blog_id>') # specifing a rule and the type
def blogpost(blog_id): # function
    return "This is blog post number " + blog_id

if __name__ == '__main__': # running our application
    app.run()
