from flask_session import Session
from flask import Flask, request, render_template, redirect, url_for, flash, session
from models import db, User

app = Flask(__name__, static_url_path='/static')   
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/profiles/<id>')
def profile_detail(id):
    command = f"select *, locations.location as location from hirefy.users inner join hirefy.locations on users.location_id = locations.id where users.id = {sqlquote(id)}"
    data = db.sql(command)
    data = data[0] if len(data) > 0 else []
    return render_template('user_profile.html', data=data, user=session.get('hirefy_username'))

@app.route("/save-applicant", methods=["GET","POST"])
def save_applicant():
    applicant_id = request.form.get('applicant_id')
    if not session.get('saved_applicants'):
        session['saved_applicants'] = []
    if applicant_id in session['saved_applicants']:
        session['saved_applicants'].remove(applicant_id)
        return render_template("snippets/save_profile_button.html", msg="Save this profile")
    session['saved_applicants'].append(applicant_id)
    return render_template("snippets/save_profile_button.html", msg="Unsave this profile")

 
@app.route("/saved-applicants", methods=["GET"])
def get_saved_applicants():
    saved_applicants = session.get('saved_applicants') or []
    command = f"select users.username, categories.category, users.id from hirefy.users inner join hirefy.categories on users.category_id = categories.id where users.id in ({', '.join(sqlquote(x) for x in saved_applicants)});"
    saved_applicants = db.sql(command)
    return render_template("saved_applicants.html", saved_applicants=saved_applicants, user=session.get('hirefy_username'))


def get_user(username):
    users = db.list_users()
    for user in users:
        if user['username'] == username:
            return user
    return None

def sqlquote(value):
    if value is None:
         return 'NULL'
    if value == "yes":
        return 'true'
    if value == "no":
        return 'false'

    return "'{}'".format(str(value).replace("'", "''"))

# snippets
@app.route("/search", methods=["POST"])
def search_results():
    search_term = request.form.get("search")
    if len(search_term) <= 0:
        return render_template("snippets/search_results.html", data=[])
    data = db.search_by_value("hirefy","users","username",search_term)
    data = db.sql("""select username, id from hirefy.users where username like '%{}%'""".format(search_term))
    return render_template("snippets/search_results.html", data=data)

@app.route("/filter-table", methods=["POST"])
def table_results():
    is_remote = request.form.get("is_remote")
    if is_remote == "" or is_remote is None:
        is_remote = "no"
    command1 = f"select id as location_id from hirefy.locations where location = {sqlquote(request.form.get('location'))} "
    command2 = f"select id as experience_type_id from hirefy.experience_types where experience_type = {sqlquote(request.form.get('experience_type'))}"

    hirefy_exp = db.sql(command2)
    hirefy_loc = db.sql(command1)
    hirefy_exp = hirefy_exp if len(hirefy_exp) > 0 else [{'id':''}]
    hirefy_loc = hirefy_loc if len(hirefy_loc) > 0 else [{'id':''}]

    filters = [hirefy_exp[0], hirefy_loc[0], {"is_remote": is_remote}]
    filters = list(filter(lambda item: list(item.values())[0] != "", filters))
    main_command = "select categories.category, count(users.username) as total_count from hirefy.categories inner join hirefy.users on categories.id = users.category_id "

    for item in filters:
        for key, value in item.items():
            if "where" not in main_command:
                main_command+=f"where users.{key}={sqlquote(value)}"
            else:
                main_command+=f" and users.{key}={sqlquote(value)}"

    main_command += " group by categories.category"
    table_data = db.sql(main_command)
    hirefy_categories = db.sql("""select category from hirefy.categories""")
    categories = {item['category']: 0 for item in hirefy_categories}
    table_data = {item['category']: item['total_count'] for item in table_data}
    table_data = {**categories, **table_data}
    table_data = dict(sorted(table_data.items(), key=lambda item: item[1], reverse=True))

    return render_template("snippets/table_items.html", table_data=table_data)


@app.route("/slide", methods=["POST"])
def slide():
    main_command = """select * from hirefy.users """
    is_remote = request.form.get("is_remote")

    if is_remote == "" or is_remote is None:
        is_remote = ""
    command1 = f"select id as location_id from hirefy.locations where location = {sqlquote(request.form.get('location'))} "
    command2 = f"select id as experience_type_id from hirefy.experience_types where experience_type = {sqlquote(request.form.get('experience_type'))}"
    command3 = f"select id as category_id from hirefy.categories where category = {sqlquote(request.form.get('category'))}"

    hirefy_exp = db.sql(command2)
    hirefy_loc = db.sql(command1)
    hirefy_cat = db.sql(command3)
    hirefy_exp = hirefy_exp if len(hirefy_exp) > 0 else [{'id':''}]
    hirefy_loc = hirefy_loc if len(hirefy_loc) > 0 else [{'id':''}]

    filters = [hirefy_exp[0], hirefy_loc[0], {"is_remote": is_remote}, hirefy_cat[0]]
    filters = list(filter(lambda item: list(item.values())[0] != "", filters))

    for item in filters:
        for key, value in item.items():
            if "where" not in main_command:
                main_command+=f"where users.{key}={sqlquote(value)}"
            else:
                main_command+=f" and users.{key}={sqlquote(value)}"

    slide_data = db.sql(main_command)

    return render_template("snippets/slide.html", slide_data=slide_data)

@app.route('/applicant-settings', methods=['GET'])
def applicant_settings():
    username = session.get('hirefy_username')
    command = f"select *, locations.location as location, categories.category as category, experience_types.experience_type as experience_type from hirefy.users inner join hirefy.experience_types on users.experience_type_id = experience_types.id inner join hirefy.categories on users.category_id = categories.id inner join hirefy.locations on users.location_id = locations.id where users.username = {sqlquote(username)}"
    data = db.sql(command)
    data = data[0] if len(data) > 0 else []
    return render_template("user_profile_settings.html", data=data, user=username)

@app.route("/home")
def home():
    return render_template("pre_home.html", user=session.get("hirefy_username"))

@app.route("/")
def main():
    sql_command = """select categories.category, count(users.username) as total_count from hirefy.users inner join hirefy.categories on categories.id = users.category_id group by categories.category"""
    table_data = db.sql(sql_command)
    locations = db.sql("select location from hirefy.locations") 
    remotes = ["yes", "no"]
    experience_types = db.sql("select experience_type from hirefy.experience_types")
    hirefy_categories = db.sql("""select category from hirefy.categories""")
    categories = {item['category']: 0 for item in hirefy_categories}
    table_data = {item['category']: item['total_count'] for item in table_data}
    table_data = {**categories, **table_data}
    table_data = dict(sorted(table_data.items(), key=lambda item: item[1], reverse=True))

    return render_template(
        "main.html", user=session.get("hirefy_username"),
        table_data=table_data,
        locations=locations,
        remotes=remotes,
        experience_types=experience_types)



@app.route("/register", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User().get_by_username(username)
        if username and password:
            # hash the password 
            user = User().get_by_username(username)
            if user:
                session["hirefy_username"] = username
                flash(f"User {username} already exists")
                return redirect(url_for("home"))
            else:
                data = User().get_initial_data()
                data.update(request.form.to_dict())
                User().create(data)
                session["hirefy_username"] = username
                # db.add_user(role="standard_user", username=username, password=password, active=True)
                flash(f"User {username} created successfully")
                return redirect(url_for("main"))
        else:
            flash("Please enter username and password")
            return render_template("signup.html")
    return render_template("signup.html")

    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User().get_by_username(username)
        user = user[0] if len(user) > 0 else {}

        if user and user.get('password') == password:
            session["hirefy_username"] = user["username"]
            flash(f"User {username} logged in successfully")
            return redirect(url_for("main"))
        else:
            flash(f"Username or password is incorrect")
            return render_template("signin.html", error=True)
    else:
        return render_template("signin.html")

@app.route("/logout", methods=["GET"])
def logout():
    session["hirefy_username"] = None
    return redirect(url_for("main"))

if __name__ == "__main__":
    app.run(debug=True, port=5000) 
