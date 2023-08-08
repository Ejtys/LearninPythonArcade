import arcade
import cons
import sys


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT, cons.SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        #Init vars
        self.tile_map = None
        self.scene = None
        self.player = None
        self.engine = None
        self.camera = None
        self.gui_camera = None
        
        #Init sounds
        self.collect_coin_sound = arcade.load_sound(cons.COLLECT_COIN_SOUND)
        self.jump_sound = arcade.load_sound(cons.JUMP_SOUND)
        self.game_over_sound = arcade.load_sound(cons.GAME_OVER_SOUND)
        
        #Track pressed keys
        self.pressed_keys = set()
        
        self.score = 0
        self.reset_score = True
        self.end_of_map = 0
        self.level = 1
        

    def setup(self):
        #Init cameras
        self.camera = arcade.Camera(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT)
        
        #Init scene
        self.tile_map = arcade.load_tilemap(cons.LEVEL_MAP[self.level - 1], 
                                            cons.TILE_SCALING, 
                                            cons.LAYER_OPTIONS)
        
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)
        
        self.scene.add_sprite_list_after("Player", cons.LAYER_NAME_FOREGROUND)
        
        #Init player
        self.player = arcade.Sprite(cons.PLAYER_IMAGE, cons.CHARACTER_SCALING)
        self.player.center_x = cons.PLAYER_START_X
        self.player.center_y = cons.PLAYER_START_Y
        self.scene.add_sprite("Playe", self.player)
        
        
        #Init engine
        
        self.engine = arcade.PhysicsEnginePlatformer(self.player, 
                                                     gravity_constant=cons.GRAVITY, 
                                                     walls = self.scene["Platforms"])
        
        if self.reset_score:
            self.score = 0
        self.reset_score = True
        
        self.end_of_map = self.tile_map.width * cons.GRID_PIXEL_SIZE
    
    def update_player_movement(self):
        up = {arcade.key.UP, arcade.key.W}
        down = {arcade.key.DOWN, arcade.key.S}
        left = {arcade.key.LEFT, arcade.key.A}
        right = {arcade.key.RIGHT, arcade.key.D}
        
        self.player.change_x = 0
        
        if self.pressed_keys & up and self.engine.can_jump():
            self.player.change_y = cons.PLAYER_JUMP_SPEED
            arcade.play_sound(self.jump_sound)
            
        if self.pressed_keys & left and not (self.pressed_keys & right):
            self.player.change_x = -cons.PLAYER_MOVEMENT_SPEED
        elif self.pressed_keys & right and not (self.pressed_keys & left):
            self.player.change_x = cons.PLAYER_MOVEMENT_SPEED
        
    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player.center_y - (self.camera.viewport_height / 2)

        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered, speed=0.05)
    
    def on_key_press(self, symbol: int, modifiers: int):
        self.pressed_keys.add(symbol)
            
    def on_key_release(self, symbol: int, modifiers: int):
        self.pressed_keys.remove(symbol)
    
    def on_update(self, delta_time: float):
        self.update_player_movement()
        self.engine.update()
        self.center_camera_to_player()
        
        coin_hit_list = arcade.check_for_collision_with_list(self.player, self.scene["Coins"])
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            arcade.play_sound(self.collect_coin_sound)
            self.score += 1
            
        if self.player.center_y < -100:
            self.player.center_x = cons.PLAYER_START_X
            self.player.center_y = cons.PLAYER_START_Y

            arcade.play_sound(self.game_over_sound)
            
        if arcade.check_for_collision_with_list(
            self.player, self.scene[cons.LAYER_NAME_DONT_TOUCH]
        ):
            self.player.change_x = 0
            self.player.change_y = 0
            self.player.center_x = cons.PLAYER_START_X
            self.player.center_y = cons.PLAYER_START_Y

            arcade.play_sound(self.game_over_sound)
            
        if self.player.center_x >= self.end_of_map:
            self.level += 1
            self.reset_score = False
            self.setup()
    
    def on_draw(self):       
        self.clear()
        
        self.camera.use()
        
        self.scene.draw()
        
        self.gui_camera.use()
        
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.WHITE,
            18,
        )



def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()