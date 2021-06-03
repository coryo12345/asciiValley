from flask import Blueprint
from .lobby import lobby_manager
from ..model.map_handler import WorldMap

world_bp = Blueprint('world_bp', __name__)

@world_bp.route('/get/<code>')
def get_world(code):
    """
    returns current world status layout
    """
    lobby = lobby_manager.lobbies.get(code)
    if lobby == None:
        return WorldMap.to_json()
    world = lobby.world
    if world == None:
        return WorldMap.to_json()
    return world.to_json()

@world_bp.route('/icons/<code>')
def get_icons(code):
    """
    returns current world icons
    """
    lobby = lobby_manager.lobbies.get(code)
    if lobby == None:
        return WorldMap.to_json()
    world = lobby.world
    if world == None:
        return WorldMap.to_json()
    return world.to_icons_json()
