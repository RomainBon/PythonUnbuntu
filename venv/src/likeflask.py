#Met les info sur le navigateur https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532
# DOSSIER DU PROJET (VUE)

from linkbdd import Bdd
from flask import Flask, render_template

if __name__ == '__main__':

    app = Flask(__name__,
                static_folder="./dist/static",
                template_folder="./dist")


    @app.route('/')
    def index():
        return render_template("index.html")