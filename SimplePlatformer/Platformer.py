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
    
    def on_draw(self):
        
        self.clear()
        
        self.scene.draw()




def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()