from flask import Flask, render_template
import connexion
from flask_cors import CORS
from nba_api.stats.endpoints import commonallplayers

app = connexion.App(__name__, specification_dir="./")
CORS(app.app)
app.add_api("swagger.yml")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)