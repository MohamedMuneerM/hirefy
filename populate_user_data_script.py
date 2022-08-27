import harperdb
import random
import json

schema = f"hirefy"

db = harperdb.HarperDB(
    url="https://hirefy-projects.harperdbcloud.com",
    username="YOUR USERNAME",
    password="YOUR PASSWORD"
    )

def sqlquote(value):
    """Naive SQL quoting

    All values except NULL are returned as SQL strings in single quotes,
    with any embedded quotes doubled.

    """
    if value is None:
         return 'NULL'
    if value == "yes":
        return 'true'
    if value == "no":
        return 'false'
    if value is True:
        return 'true'
    if value is False:
        return 'false'

    return "'{}'".format(str(value).replace("'", "''"))

categories = db.sql("select categories.id from hirefy.categories")
locations = db.sql("select locations.id from hirefy.locations")
experience_types = db.sql("select experience_types.id from hirefy.experience_types")

categories = [value for category in categories for _, value in category.items()]
locations = [value for location in locations for _, value in location.items()]
experience_types = [value for experience_type in experience_types for _, value in experience_type.items()]

profile_captions = [
    "I am a data scientist who is passionate about data science and machine learning.",
    "Full stack developer with a passion for data science and machine learning.",
    "I am a backend engineer who is passionate about backend development.",
    "Full stack developer with a passion for backend development.",
    "I am a frontend engineer who is passionate about frontend development.",
    "Full stack developer with a passion for frontend development.", 
    "I am a accountant who is passionate about finance and markets.",
    "Buisness lawyer with a passion for finance and markets.",
]

skills = [
    "Python, r, numpy, pandas, seaborn, excel",
    "financial modeling, data analysis, data visualization",
    "data science, machine learning, data visualization",
    "algorithms, data structures, data visualization",
    "statistics, bi tools, tableau",
    "sql, mysql, postgresql",
    "buisness law, tax, final accounts",
    "accounting, finance, tax",
    "javascript, react, angular",
    "figma, adobe xd, adobe photoshop",
    "html, css, javascript",
    "html, css, javascript, react",
    "vue, firebase, nodejs",

]



"""
    bio
    category_id
    email
    experience_type_id
    is_remote
    is_verified
    location_id
    profile_caption
    skills
    username
    password
    portfolio_url

"""

lorem_text_bio = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Donec euismod, nisi eget consectetur consectetur, nisi nisi consectetur
nisi, eget consectetur nisi nisi eget consectetur. Donec euismod, 
nisi eget consectetur consectetur, nisi nisi consectetur nisi, eget consectetur
nisi nisi eget consectetur. Donec euismod, nisi eget consectetur cnsectetur,
nisi nisi consectetur nisi, eget consectetur nisi nisi eget consectetur.
Donec euismod, nisi eget consectetur consectetur, nisi nisi consectetur
"""

with open('src/users.json', 'r') as f:
    users = json.load(f)

# print(users)


# random.choice(data_scientist_profile_captions)
# print(random.choice(categories))
insert_command = f""" insert into hirefy.users (bio, category_id, email, experience_type_id, is_remote, is_verified, location_id, profile_caption, skills, username, password, portfolio_url) values """


for user_data in users.get('users'):
    sub_command = f""" ({sqlquote(lorem_text_bio)}, {sqlquote(random.choice(categories))}, {sqlquote(user_data['email'])}, {sqlquote(random.choice(experience_types))}, {random.choice([True, False])}, {random.choice([True, False])}, {sqlquote(random.choice(locations))}, {sqlquote(random.choice(profile_captions))}, {sqlquote(random.choice(skills))}, {sqlquote(user_data['firstName']+ " " +user_data['lastName'])}, {sqlquote(user_data['password'])}, 'example.com') """
    insert_command += sub_command
    if user_data != users.get('users')[-1]:
        insert_command += ","

print(db.sql(insert_command))

# db.csv_data_load()
# db.csv_file_load()
# db.insert()





