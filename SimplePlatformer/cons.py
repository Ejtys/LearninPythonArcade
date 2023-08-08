SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

PLAYER_START_X = 64
PLAYER_START_Y = 225

PLAYER_IMAGE = ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png"
WALL_IMAGE = ":resources:images/tiles/grassMid.png"
BOX_IMAGE = ":resources:images/tiles/boxCrate.png"

COLLECT_COIN_SOUND = ":resources:sounds/coin1.wav"
JUMP_SOUND = ":resources:sounds/jump3.wav"
GAME_OVER_SOUND = ":resources:sounds/gameover1.wav"

LEVEL_MAP = ["SimplePlatformer/map/map2_level_1.json", "SimplePlatformer/map/map2_level_2.json"]

LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_DONT_TOUCH = "Don't Touch"

LAYER_OPTIONS = {
            LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_COINS: {
                "use_spatial_hash": True,
            },
            LAYER_NAME_DONT_TOUCH: {
                "use_spatial_hash": True,
            },
        }

