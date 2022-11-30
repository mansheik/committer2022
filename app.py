
from flask import Flask

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