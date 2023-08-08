SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1.3
PLAYER_JUMP_SPEED = 20

PLAYER_IMAGE = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
WALL_IMAGE = ":resources:images/tiles/grassMid.png"
BOX_IMAGE = ":resources:images/tiles/boxCrate.png"

COLLECT_COIN_SOUND = ":resources:sounds/coin1.wav"
JUMP_SOUND = ":resources:sounds/jump3.wav"

TILE_MAP = "SimplePlatformer/map/map.json"

LAYER_OPTIONS = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }