import arcade
import cons
import sys


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT, cons.SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        #Init vars
        self.scene = None
        self.player = None
        self.engine = None
        self.camera = None
        self.gui_camera = None
        
        #Init sounds
        self.collect_coin_sound = arcade.load_sound(cons.COLLECT_COIN_SOUND)
        self.jump_sound = arcade.load_sound(cons.JUMP_SOUND)
        
        #Track pressed keys
        self.pressed_keys = set()
        
        self.score = 0
        

    def setup(self):
        #Init cameras
        self.camera = arcade.Camera(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT)
        self.gui_camera = arcade.Camera(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT)
        
        #Init scene
        self.scene = arcade.Scene()
        
        #Init sprites lists
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Walls", use_spatial_hash=True)
        
        #Init player
        self.player = arcade.Sprite(cons.PLAYER_IMAGE, cons.CHARACTER_SCALING)
        self.player.center_x = 64
        self.player.center_y = 128
        self.scene.add_sprite("Playe", self.player)
        
        #Init walls
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(cons.WALL_IMAGE, cons.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.scene.add_sprite("Walls", wall)
            
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            box = arcade.Sprite(cons.BOX_IMAGE, cons.TILE_SCALING)
            box.position = coordinate
            self.scene.add_sprite("Walls", box)
            
        for x in range(128, 1250, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", cons.COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.scene.add_sprite("Coins", coin)
            
        self.engine = arcade.PhysicsEnginePlatformer(
                        self.player, gravity_constant=cons.GRAVITY, 
                        walls = self.scene["Walls"])
        
        
        self.score = 0
    
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