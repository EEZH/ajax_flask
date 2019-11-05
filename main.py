from flask import Flask, render_template, request
from controls import UsersControl

app = Flask(__name__)
usersControl = UsersControl("data.db")


@app.route("/")
def main_page():
    return render_template("index.html")


@app.errorhandler(404)
def not_found():
    return render_template("<h1>Page not  found</h1>")


@app.route("/users")
def users():
    """/users?name=Har"""
    name = request.args["name"]
    ready_users = usersControl.search_users(name)
    return dict(users=ready_users)


@app.route("/user_data")
def user_data():
    """/user_data?user_id=1&user_name=Harry"""
    user_id = request.args["user_id"]
    user_name = request.args["user_name"]
    user = usersControl.get_user_data(user_id)
    user = {
        "name": user_name,
        "id": user_id,
        "email": user[0],
        "age": user[1],
        "about": user[2]
    }
    return user


if __name__ == "__main__":
    app.run(debug=True)
