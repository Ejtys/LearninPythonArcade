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
        
        #Init walls
        for x in range(0, 1250, 64):
            wall = arcade.Sprite(cons.WALL_IMAGE, cons.TILE_SCALING)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)
            
        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            box = arcade.Sprite(cons.BOX_IMAGE, cons.TILE_SCALING)
            box.position = coordinate
            self.wall_list.append(box)
    
    def on_draw(self):
        
        self.clear()
        
        self.player_list.draw()
        self.wall_list.draw()




def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()