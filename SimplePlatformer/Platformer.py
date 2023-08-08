import arcade
import cons


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(cons.SCREEN_WIDTH, cons.SCREEN_HEIGHT, cons.SCREEN_TITLE)
        
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
        
        #Init vars for sprites lists
        self.wall_list = None
        self.player_list = None
        
        #Init var for player sprite
        self.player = None
        

    def setup(self):
        #Init sprites lists
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)
        self.player_list = arcade.SpriteList()
        
        #Init player
        self.player = arcade.Sprite(cons.PLAYER_IMAGE, cons.CHARACTER_SCALING)
        self.player.center_x = 64
        self.player.center_y = 128
        self.player_list.append(self.player)
    
    def on_draw(self):
        
        self.clear()
        
        self.player_list.draw()




def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()