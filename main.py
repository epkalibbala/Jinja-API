from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    # print(response.json())
    data = response.json()
    return render_template("index.html", resp=data)


@app.route('/post/<int:blog_id>')
def view_post(blog_id):
    url = f"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    data = response.json()
    # (post for post in blog_posts if post["blog_id"] == blog_id): This is a
    # generator expression.It iterates over each post dictionary in the blog_posts
    # list and checks if the blog_id of each post matches the blog_id received as a
    # parameter in the route.
    post = next((post for post in data if post["id"] == blog_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        # Handle case when the blog post is not found
        return "Blog post not found", 404


if __name__ == "__main__":
    app.run(debug=True)
