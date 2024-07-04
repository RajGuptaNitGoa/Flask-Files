## Flask App Routing
# Flask routing is how you map URL patterns to functions that handle the requests. 
# In Flask, this is done using the @app.route decorator. This decorator associates a 
# URL with a view function, which is a Python function that returns a response for the corresponding URL.

# @app.route("/")
# Maps the root URL (/) to the home function.
# When a user accesses the root URL, the home function is called, 
# and its return value ("Welcome to the Home Page!") is sent as the response.

# @app.route("/about")
# Maps the /about URL to the about function.
# When a user accesses /about, the about function is called, 
# and its return value ("This is the About Page.") is sent as the response

# Dynamic Routing
# Flask can also handle dynamic URLs by capturing parts of the URL 
# and passing them as arguments to the view function. Here's an example:

# @app.route("/user/<username>")
# def show_user_profile(username):
#     return f"User: {username}"

# @app.route("/post/<int:post_id>")
# def show_post(post_id):
#     return f"Post ID: {post_id}"

# Explanation
# @app.route("/user/<username>")
# The <username> part is a variable part of the URL.
# When a user accesses a URL like /user/Alice, the username argument in the show_user_profile function will be set to "Alice".

# @app.route("/post/<int:post_id>")
# The <int:post_id> part specifies that the variable part should be an integer.
# When a user accesses a URL like /post/42, the post_id argument in the show_post function will be set to 42.

from flask import Flask,render_template, request,redirect, url_for

#### create simple flask application

# __name__ -> entry point of program
app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to the my 1st Flask app"

@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the index page<h2>"


# variable rule
@app.route("/success/<int:score>")
def success(score):
    return "the person has passed and the score is : " + str( score)

@app.route("/fail/<int:score>")
def fail(score):
    return "the person has failed and the score is : " + str( score)

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else :
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res,score=average_marks))
        # return render_template('form.html',score=average_marks)


# if __name__ == "__main__":
# This line checks if the script is being run directly (as opposed to being imported as a module in another script). 
# If true, the code block following it will execute.
# __name__ is a special built-in variable in Python that is set to "__main__" when the script is executed directly.
# 
# app.run(debug=True)
# app.run() starts the Flask development server.
# debug=True enables debug mode. In this mode, the server provides detailed error messages and auto-reloads when code changes are detected, which is useful for development purposes.
# Typical Usage

if __name__=="__main__":
    app.run(debug=True)


