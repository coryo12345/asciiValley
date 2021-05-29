from os import path
import enum
import json

MAPS_DIR = './maps'
ICONS_DIR = './icon_packs'
DEFAULT_ICON_PACK = 'default.ipac'

MAP_HEADER_KEYS = {
    'width': 'width',
    'height': 'height',
    'icon_pack': 'icons'
}

class WorldMap:
    def __init__(self, filename):
        self.width = 0
        self.height = 0
        self.map = []
        self.icon_pack = ''
        self.icons = {}
        self.filename = filename

    def load_world(self) -> bool: #-----------------------------------------
        def map_load_error(info=""):
            print('-ERROR-')
            print("Error loading map file:", self.filename)
            if info != "":
                print(info)

        # read in world
        file_path = path.join(MAPS_DIR, self.filename)
        f = open(file_path, 'r')
        # read header
        lines = f.readlines()
        f.close()
        if lines[0].replace(' ', '').strip() != '-header':
            map_load_error()
            return False
        
        line_index = 1
        while True:
            line = lines[line_index].strip()
            if line.replace(' ', '') == '-body':
                line_index += 1
                break

            parts = line.split('=')
            if parts[0] not in MAP_HEADER_KEYS.values():
                map_load_error()
                return False
            
            if parts[0] == MAP_HEADER_KEYS['width']:
                self.width = int(parts[1])
            elif parts[0] == MAP_HEADER_KEYS['height']:
                self.height = int(parts[1])
            elif parts[0] == MAP_HEADER_KEYS['icon_pack']:
                self.icon_pack = parts[1].strip()
            line_index += 1
        
        # load in icon pack
        if self.icon_pack == '':
            map_load_error()
            return False
        icon_path = path.join(ICONS_DIR, self.icon_pack)
        ifile = open(icon_path, "r")
        idata = ifile.readlines()
        ifile.close()
        for line in idata:
            # comments
            if line[0] == '#':
                continue
            parts = line.split(' ')
            self.icons[parts[0]] = parts[1].replace('\n', '')

        # parse map body
        # temporary inversion of icons map
        icons_t = {v: k for k, v in self.icons.items()}
        for row_idx_t in range(self.height):
            self.map.append([])
            row_idx = line_index + row_idx_t
            row = lines[row_idx].strip()
            for col_idx in range(self.width):
                try:
                    cell = row[col_idx]
                except IndexError:
                    map_load_error("Check width and height")
                try:
                    tile_type = icons_t[cell]
                except KeyError:
                    map_load_error("Unexpected symbol: %s"%(cell))
                self.map[row_idx_t].append(Tile(tile_type))
        # success
        return True
    #------------------------------------------------------------------------------------------

    def to_json(self):
        data = {
            'map': []
        }
        for row in self.map:
            r = []
            for col in row:
                r.append(self.icons[col.type])
            data['map'].append(r)
        return json.dumps(data)

    def to_icons_json(self):
        return json.dumps(self.icons)

    def __str__(self):
        s = ''
        for r in range(self.height):
            for c in range(self.width):
                s += self.icons[self.map[r][c].type]
            s += '\n'
        return s
                
class Tile:
    def __init__(self, cell_type):
        self.type = cell_type
        self.entity_type = EntityType.none # uses EntityType enum

    def playerCanOccupy(self) -> bool:
        if self.type in ['empty'] and self.entity_type in [EntityType.none, EntityType.player]:
            return True

class EntityType(enum.Enum):
    none = 0
    player = 1
    item = 2
