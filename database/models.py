import os
from sqlalchemy import Column, String, Integer, Float, Date, Boolean
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask import json
from werkzeug.security import generate_password_hash
from datetime import date
load_dotenv()

# database_filename = "database.db"
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_path = "sqlite:///{}".format(
#     os.path.join(project_dir, database_filename))

DB_DIALECT=os.getenv("DB_DIALECT")
DB_USERNAME=os.getenv("DB_USERNAME")
DB_PASSWORD=os.getenv("DB_PASSWORD")
DB_SERVER=os.getenv("DB_SERVER")
DB_NAME=os.getenv("DB_NAME")
DB_PORT=os.getenv("DB_PORT")

database_name = DB_NAME
database_path = f"{DB_DIALECT}://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}"
db = SQLAlchemy()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

    admin2 = User(
        username="shehu",
        name="shehu malami",
        email="stjabo@jamail.com",
        password=generate_password_hash("adminpass")
    )
    db.session.add(admin2)
    admin1 = User(
        username="alawiyah",
        name="alawiyah Bt abdulwahab",
        email="alawiyah@uum.edu.my",
        password=generate_password_hash("adminpass1")
    )
    db.session.add(admin1)

    enquirer = Enquiry(
        name="Alawiyah Abdulwahab",
        education="Doctorate",
        email="alawiyah@uum.edu.my",
        region="asia",
        fin_gain=5,
        int_learn=4,
        dev_inv=4,
        proj_desertion=4,
        dev_experience=4,
        sys_int=3,
        tech_norm=3,
        code_test=3,
        cont_code_dec=3,
        dec_right_del=3,
        proj_age=5,
        promoted=0,
        date_submitted=date.today()
    )

    enquirer1 = Enquiry(
        name="Jamilu Tahir",
        education="Doctorate",
        email="jamiltahir010@gmail.com",
        region="africa",
        fin_gain=6,
        int_learn=6,
        dev_inv=6,
        proj_desertion=2,
        dev_experience=5,
        sys_int=6,
        tech_norm=6,
        code_test=6,
        cont_code_dec=6,
        dec_right_del=6,
        proj_age=6,
        promoted=0,
        date_submitted=date.today()
    )
    db.session.add(enquirer)
    db.session.add(enquirer1)
    db.session.commit()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    name = Column(String(200))
    email = Column(String(120))
    password = Column(String(256))

    def details(self):

        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'name': self.name
        }

    def __repr__(self):
        return json.dumps(self.details())


class Enquiry(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    education = Column(String(20))
    email = Column(String(120))
    region = Column(String(20))
    fin_gain = Column(Float)
    int_learn = Column(Float)
    dev_inv = Column(Float)
    proj_desertion = Column(Integer)
    dev_experience = Column(Integer)
    sys_int = Column(Float)
    tech_norm = Column(Float)
    code_test = Column(Float)
    cont_code_dec = Column(Float)
    dec_right_del = Column(Float)
    proj_age = Column(Integer)
    promoted = Column(Boolean, default=0)
    date_submitted = Column(Date)

    def details(self):

        return {
            'e_id': self.id,
            'name': self.name.capitalize(),
            'education': self.education.capitalize(),
            'email': self.email,
            'region': self.region.capitalize(),
            'fin_gain': self.fin_gain,
            'int_learn': self.int_learn,
            'dev_inv': self.dev_inv,
            'proj_desertion': self.proj_desertion,
            'dev_experience': self.dev_experience,
            'sys_int': self.sys_int,
            'tech_norm': self.tech_norm,
            'code_test': self.code_test,
            'cont_code_dec': self.cont_code_dec,
            'dec_right_del': self.dec_right_del,
            'proj_age': self.proj_age,
            'promoted': self.promoted,
            'date_submitted': self.date_submitted
        }

    def __repr__(self):
        return json.dumps(self.details())
