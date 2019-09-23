from flask import Flask, render_template
import connexion
from flask_cors import CORS

app = connexion.app(__name__, specification_dir="./")

app.add_api("swagger.yml")

if __name__ == "__main__":
    app.run(debug=True)