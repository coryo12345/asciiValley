# ===== IMPORTS =====
from enum import Enum

# ===== Enums =====
class GameState (Enum):
    LOBBY = 0
    SETUP = 1
    IN_GAME = 2
    POST_GAME = 3

class GameType (Enum):
    TEAM_DEATHMATCH = 0

# ====================== Lobby ==========================
class Lobby:

    DEFAULT_MAP = 'blank_10.map'

    def __init__(self, code) -> None:
        self.users = []
        self.code = code
        self.settings = {
            'world': Lobby.DEFAULT_MAP
        }
        self.world = None
        self.gameState = GameState.LOBBY
        self.gameType = GameType.TEAM_DEATHMATCH

    def addUser(self, user) -> bool:
        # players cant join once the game starts
        if self.gameState == GameState.LOBBY:
            self.users.append(user)
            return True
        return False

    def close(self):
        pass

# ====================== Lobby manager ==========================
class LobbyManager:

    LOBBY_CODE_LEN = 6

    def __init__(self) -> None:
        self.count = 0
        self.lobbies = {} # { code: Lobby }
    
    def new_lobby(self) -> Lobby:
        # generate code
        code = abs(hash(str(self.count))) % (10 ** LobbyManager.LOBBY_CODE_LEN)
        self.lobbies[code] = Lobby(code)
        self.count += 1
        return self.lobbies[code]

    def remove_lobby(self, code) -> Lobby:
        if self.lobbies.get(code) != None:
            l = self.lobbies.pop(code)
            l.close()
            return l
        return None
