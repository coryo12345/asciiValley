from flask import Blueprint
import sys
from ..model.map_handler import WorldMap

# setup
# for now load 1 map
world = WorldMap('blank_10.map')
if not world.load_world():
    sys.exit(1)

world_bp = Blueprint('world_bp', __name__)


@world_bp.route('/')
def get_world():
    """
    returns current world status layout
    """
    return world.to_json()

@world_bp.route('/icons')
def get_icons():
    return world.to_icons_json()