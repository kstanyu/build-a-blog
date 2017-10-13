
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://build-a-blog:lc101unit2@localhost:8889/build-a-blog"

app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Blog(db.Model):
        
    id = db.Column(db.Integer, primary_key = True)
    blog_title = db.Column(db.String(120))
    blog_post = db.Column(db.Text)
    
    def __init__(self, blog_title, blog_post):
        self.blog_title = blog_title
        self.blog_post = blog_post

def is_empty(usr_string):
    empty = True
    if usr_string != "":
        empty = False
    return empty
    
@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("newpost.html")
 
@app.route("/blog", methods = ["POST", "GET"])
def blog():
    blog_posts = Blog.query.all()
    if request.method == "GET":
        btitle = request.args.get('blog_title')
        blog_id = Blog.query.get(btitle)
       return render_template("blog_post.html", block_title = )
    return render_template("homepage.html", title = "BUILD A BLOG", blogposts = blog_posts)

@app.route("/newpost", methods = ["POST", "GET"])
def newpost(): 
    if request.method == "POST":
        if (request.form["blog_title"] == "") or (request.form["blog_post"] == ""):
            return redirect (url_for("newpost"))
        else:
            blog_title = request.form["blog_title"]
            new_post = request.form["blog_post"]
            new_blog = Blog(blog_title, new_post)
            db.session.add(new_blog)
            db.session.commit()
            return redirect(url_for("blog"))
    
    return render_template("newpost.html")

#@app.route("/newpost", methods = ["POST","GET"])
#def newpost():
#    return render_template("newpost.html")

    
if __name__ == "__main__":
    app.run()
