import arcade
import cons
import sys


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT, cons.SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        #Init scene var
        self.scene = None
        
        #Init var for player sprite
        self.player = None
        
        #Init physics engine
        self.engine = None
        
        #Track pressed keys
        self.pressed_keys = set()
        

    def setup(self):
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
            
        self.engine = arcade.PhysicsEnginePlatformer(
                        self.player, gravity_constant=cons.GRAVITY, 
                        walls = self.scene["Walls"])
    
    def update_player_movement(self):
        up = {arcade.key.UP, arcade.key.W}
        down = {arcade.key.DOWN, arcade.key.S}
        left = {arcade.key.LEFT, arcade.key.A}
        right = {arcade.key.RIGHT, arcade.key.D}
        
        self.player.change_x = 0
        
        if self.pressed_keys & up and self.engine.can_jump():
            self.player.change_y = cons.PLAYER_JUMP_SPEED
            
        if self.pressed_keys & left and not (self.pressed_keys & right):
            self.player.change_x = -cons.PLAYER_MOVEMENT_SPEED
        elif self.pressed_keys & right and not (self.pressed_keys & left):
            self.player.change_x = cons.PLAYER_MOVEMENT_SPEED
        
    
    def on_key_press(self, symbol: int, modifiers: int):
        self.pressed_keys.add(symbol)
        
            
            
    def on_key_release(self, symbol: int, modifiers: int):
        self.pressed_keys.remove(symbol)
    
    def on_update(self, delta_time: float):
        self.update_player_movement()
        self.engine.update()
    
    def on_draw(self):
        
        self.clear()
        
        self.scene.draw()



def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()