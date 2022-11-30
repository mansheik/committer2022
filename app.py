#----------------------------------------------------------------------------#
# Imports.
#----------------------------------------------------------------------------#
import os, csv
from flask import Flask, request, render_template, redirect, url_for, flash, session, send_file, jsonify, abort
from flask_cors import CORS
from flask_session import Session
from tempfile import mkdtemp
from datetime import timedelta, date
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

# from database.models import db, setup_db, db_drop_and_create_all, User, Enquiry
# from auth import login_required
# from Prediction_of_UserInput.prediction_file import Prediction_from_api
# from Prediction_from_file.prediction_from_file import Prediction_from_file
# from File_operation import file_op

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ == '__main__':
    # app.run(debug=True)
    port_nr = int(os.environ.get("PORT", 5000))
    app.run(port=port_nr, host='0.0.0.0')

# For replit
# if __name__ == "__main__":  # Makes sure this is the main process
#     app.run( # Starts the site
#         host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
#         port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
#     )