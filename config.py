import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
# SQLALCHEMY_DATABASE_URI = "postgresql://mbwpmhcftvzemp:efb770d6b73df787043549fb28d99251a0239998bc8eeeb6faa46f319a1b167f@ec2-52-200-5-135.compute-1.amazonaws.com:5432/dfkqfg5ui1kt9h"
