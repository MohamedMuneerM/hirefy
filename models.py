import harperdb
from user_secrets import HIREFY_PASSWORD, HIREFY_USERNAME

schema = f"hirefy"

db = harperdb.HarperDB(
    url="https://hirefy-projects.harperdbcloud.com",
    username=HIREFY_USERNAME,
    password=HIREFY_PASSWORD
    )

class UserAttributes:
    USERNAME = "username"
    PASSWORD = "password"
    EMAIL = "email"
    IS_ACTIVE = "is_active"
    PROFILE_PICTIRE = "profile_picture"
    BIO = "bio"
    LOCATION = "location"
    EXPERIENCE_PROFILE = "experience_profile"
    GITHUB_LINK = "github_link"
    LINKEDIN_LINK = "linkedin_link"
    FACEBOOK_LINK = "facebook_link"
    TWITTER_LINK = "twitter_link"
    WEBSITE_LINK = "website_link"

class User:
    table = "users"

    def create(self, user):
        return db.insert(
            schema,
            self.table,
            [user]
        )

    def update(self, id, data):
        return db.sql(
            f"""update {schema}.{self.table} set username='{data['username']}',
            password='{data['password']}', email='{data['email']}', is_active='{data['is_active']}', bio={data.location},
            profile_picture={data['profile_picture']}, location={data['location']}, experience_profile={data['experience_profile']},
            github_link={data['github_link']}, linkedin_link={data['linkedin_link']}, facebook_link={data['facebook_link']},
            twitter_link={data['twitter_link']}, website_link={data['website_link']} where id={id}""")

        # "or" optimze for select update "or" no sql-- later

    def delete(self, id):
        return db.sql(f"delete from {schema}.{self.table} where id={id}")
    
    def get_by_id(self, id):
        return db.sql(f"select * from {schema}.{self.table} where id={id}")

    def get_by_username(self, username):
        return db.sql(f"select * from {schema}.{self.table} where username='{username}' limit 1")
    
    def get_all(self):
        return db.sql(f"select * from {schema}.{self.table}")

    def get_initial_data(self):
        return {
            "username": None,
            "password": None,
            "email": None,
            "is_active": None,
            "profile_picture": None,
            "bio": None,
            "location_id": None,
            "category_id": None,
            "experience_profile": None,
            "github_link": None,
            "linkedin_link": None,
            "facebook_link": None,
            "twitter_link": None,
            "website_link": None,
            "is_remote": None,
        }


class Location:
    table = "locations"
    def create(self, location):
        # not handled sanitizations and validations, just for demo :)
        # but if you this for real world, you should sanitize and validate inputs
        # -- handle password1 and password2 matching
        return db.insert(
            schema,
            self.table,
            [location]
        )
    
    # --
    def update(self, id, location):
        return db.sql(f"update {schema}.{self.table} set location='{location}' where id={id}")

    def delete(self, id):
        return db.sql(f"delete from {schema}.{self.table} where id={id}")
    
    def get(self, id):
        return db.sql(f"select * from {schema}.{self.table} where id={id}")
    
    def get_all(self):
        return db.sql(f"select * from {schema}.{self.table}")



class Category:
    table = "categories"
    def create(self, category):
        # not handled sanitizations and validations, just for demo :)
        # but if you this for real world, you should sanitize and validate inputs
        # -- handle password1 and password2 matching
        return db.insert(
            schema,
            self.table,
            [category]
        )
    
    # --
    def update(self, id, category):
        return db.sql(f"update {schema}.{self.table} set category='{category}' where id={id}")

    def delete(self, id):
        return db.sql(f"delete from {schema}.{self.table} where id={id}")
    
    def get(self, id):
        return db.sql(f"select * from {schema}.{self.table} where id={id}")
    
    def get_all(self):
        return db.sql(f"select * from {schema}.{self.table}")





