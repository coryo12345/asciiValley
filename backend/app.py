import sys
from flask import Flask
from src.model.map_handler import WorldMap
from src.routes.world import world_bp

app = Flask(__name__)

app.register_blueprint(world_bp, url_prefix='/world')

if __name__ == '__main__':
    app.run(port=3001)
