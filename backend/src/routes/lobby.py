from flask import Blueprint
from ..model.game_session import GameState
import sys
import json
from ..model.map_handler import WorldMap
from ..model.game_session import LobbyManager

# setup
lobby_manager = LobbyManager()

# for now load 1 map
# world = WorldMap('blank_10.map')
# if not world.load_world():
#     sys.exit(1)

session_bp = Blueprint('session_bp', __name__)


@session_bp.route('/new/')
def new_lobby():
    lobby = lobby_manager.new_lobby()
    data = {'code': lobby.code, 'settings': lobby.settings}
    return json.dumps(data)


@session_bp.route('/get/<code>/')
def get_lobby(code=''):
    try:
        c = int(code)
    except ValueError:
        c = -1
    lobby = lobby_manager.lobbies.get(c)
    if lobby == None or lobby.gameState != GameState.LOBBY:
        return json.dumps({'code': '', 'settings': {}})
    data = {'code': lobby.code, 'settings': lobby.settings}
    return json.dumps(data)
