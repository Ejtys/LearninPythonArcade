import arcade
import cons


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
            
        self.engine = arcade.PhysicsEngineSimple(self.player, self.scene.get_sprite_list("Walls"))
    
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.W):
            self.player.change_y = cons.PLAYER_MOVEMENT_SPEED
        elif symbol in (arcade.key.DOWN, arcade.key.S):
            self.player.change_y = -cons.PLAYER_MOVEMENT_SPEED
        if symbol in (arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = cons.PLAYER_MOVEMENT_SPEED
        elif symbol in (arcade.key.LEFT, arcade.key.A):
            self.player.change_x = -cons.PLAYER_MOVEMENT_SPEED
        
            
            
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in (arcade.key.UP, arcade.key.W):
            self.player.change_y = 0
        elif symbol in (arcade.key.DOWN, arcade.key.S):
            self.player.change_y = 0
        if symbol in (arcade.key.RIGHT, arcade.key.D):
            self.player.change_x = 0
        elif symbol in (arcade.key.LEFT, arcade.key.A):
            self.player.change_x = 0
    
    def on_update(self, delta_time: float):
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