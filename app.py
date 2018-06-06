from __future__ import unicode_literals

# Load Flask Packages
from flask import Flask
from flask import render_template
from flask import request


# You need to input the interface path for this folder
rootPath = '/Users/ValarMorghulis/Projects/DesignChallenge'
flask_app = Flask(__name__,static_url_path='',root_path=rootPath)

# Main Page to Guide all users : Can be deleted
@flask_app.route("/")
def index():
    # return render_template('landing_page.html', **context)
    return render_template('bundle.html')

if __name__ == "__main__":
    flask_app.run(debug=True) # Debug model - Flask provides many other self-defined functions
