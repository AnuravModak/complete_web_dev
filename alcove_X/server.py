import flask
from flask import Flask,render_template
import codecs
from flask import request
import connector
import requests
import random
from mysql.connector import Error
import time
import mysql.connector
# import connector



app=Flask("__name__")

@app.route("/")
def welcome_page():
    return render_template('welcome.html')

@app.route("/login")
def login_page():
    return render_template('login.html')

@app.route("/email_not_found")
def not_registered():
    return render_template('email_not_found.html')

@app.route("/register")
def register_page():
    return render_template('register.html')

@app.route("/users/register",methods=["POST"])
def register_user():
    fname = request.form.get("fname")
    lname = request.form.get("fname")
    email = request.form.get("email")
    password2 = request.form.get("password2")
    password = request.form.get("password")
    if password!=password2:
        return render_template('register.html')
    y=connector.connector_register(email,password,fname,lname)
    if not y:
        # print(y)
        return flask.redirect('/regd_user/{}'.format(email))
    else:

        return render_template('try_again.html')



@app.route("/regd_user/<email>")
def redirect_user(email):
    y=connector.check_login(email)
    if type(y) is not list:
        if not y=="False":
            return render_template('dashboard.html')
        else:
            return render_template('login.html')

    else:
        return render_template('login.html')

@app.route("/users/login",methods=["POST"])
def login_users():
    email = request.form.get("email")
    password = request.form.get("password")
    y=connector.find_user(email)
    # print(y)
    # print(email,password)

    if y:
        if password==y:
            connector.login_user(email)
            return flask.redirect("/dashboard/{}".format(email))
        else:
            return render_template('try_again_login.html')
    else:
        return flask.redirect("/email_not_found")
@app.route("/dashboard/<uid>")
def dashboard(uid):
    if connector.find_user(uid):
        if not connector.check_login(uid) == "False":
            return render_template('dashboard.html')
    elif not connector.find_user(uid):
        return flask.redirect("/")
    if  not connector.check_login(uid)=="False":
        print(connector.check_login(uid))
        return render_template('dashboard.html')
    else:
        return flask.redirect("/login")


@app.route("/users/logout")
def logout_users():
    # connector.logout_user(email)
    s=str(request.referrer)

    arr=s.split("/")
    para=arr[-1]
    connector.logout_user(para)

    return flask.redirect("/login")

@app.route("/users/edit")
def edit_details():
    s = str(request.referrer)

    arr = s.split("/")
    para = arr[-1]
    return flask.redirect("/users/edit/{}".format(para))

@app.route("/users/edit/<email>")
def Edit_details(email):

    return render_template("edit_details.html")

@app.route("/mydashboard")
def mydashboard():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]
    return flask.redirect("/dashboard/{}".format(email))

@app.route("/back/dashboard",methods=["POST"])
def back_func():
    s = str(request.referrer)
    arr = s.split("/")
    email = arr[-1]
    fname=request.form.get("newfname")
    lname=request.form.get("newlname")
    password=request.form.get("newpass")
    # print(fname,lname,password)

    connector.edit_details(email,fname,lname,password)

    return flask.redirect("/dashboard/{}".format(email))

@app.route("/users/delete")
def direct_details():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]
    return flask.redirect("/users/delete/{}".format(email))

@app.route("/users/delete/<email>")
def del_details(email):
    return  render_template("delete.html")



@app.route("/delete")
def delete_details():
    s = str(request.referrer)
    arr = s.split("/")
    email = arr[-1]
    connector.delete_account(email)
    return flask.redirect("/")


@app.route("/direct_add_todolist")
def direct_lists():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]
    return flask.redirect("/users/add_todolist/{}".format(email))

@app.route("/users/add_todolist/<email>")
def add_lists(email):
    return render_template("add_todo_list.html")

@app.route("/users/add_todo_list",methods=["POST"])
def add_to_database():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]


    name=request.form.get("add")
    status=request.form.get("status")
    notes=request.form.get("list_notes")
    connector.add_todo_list(email,name,status,notes)
    return flask.redirect("/users/add_todolist/{}".format(email))

@app.route("/users/redirect_delete")
def rem_activities():
    s = str(request.referrer)
    arr = s.split("/")
    email = arr[-1]
    return flask.redirect("/users/del_act/{}".format(email))

@app.route("/users/del_act/<name>")
def del_activities(name):
    return render_template("delete_activities.html")


@app.route("/users/remove_act",methods=["POST"])
def remove_activities():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]
    name=request.form.get("name")
    print(name)
    print(connector.find_activity(email, name))


    if connector.find_activity(email, name)=="False":
        return render_template('error_message.html')
    if type(connector.find_activity(email, name)) is list:
        return render_template('error_message.html')

    connector.delete_activity(email, name)
    return flask.redirect("/users/del_act/{}".format(email))



@app.route("/users/redirect_edit")
def redirect_edit_activities():
    s = str(request.referrer)
    arr = s.split("/")
    email = arr[-1]
    return flask.redirect("/users/edit_act/{}".format(email))

@app.route("/users/edit_act/<name>")
def edit_activities(name):
    return render_template("edit_activities.html")

@app.route("/users/edit_activity",methods=["POST"])
def edit_act():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]
    name=request.form.get("name")
    print(name)

    if connector.find_activity(email, name) == "False":
        return "Item not found"
    if type(connector.find_activity(email, name)) is list:
        return "Item not found"
    name=request.form.get("name")
    nname = request.form.get("nname")
    status = request.form.get("status")
    notes = request.form.get("notes")
    connector.edit_activity(email,name,nname,status,notes)



    return flask.redirect("/users/edit_act/{}".format(email))

@app.route("/users/get_activity")
def get_act():
    s = str(request.referrer)

    arr = s.split("/")
    email = arr[-1]


    y=connector.get_activity(email)
    s=" "
    if y[::-1]!=-1 and len(y)>0:
        for i in y:
            s+=i+","
        return "Your activities are: "+s
    else:
        return "No items"




if __name__ == "__main__":
    app.run()
