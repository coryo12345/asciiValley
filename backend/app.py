import sys
from flask import Flask
from src.routes.lobby import session_bp
from src.routes.world import world_bp

app = Flask(__name__)

app.register_blueprint(world_bp, url_prefix='/world')
app.register_blueprint(session_bp, url_prefix='/session')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001)
