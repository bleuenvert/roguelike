#!/usr/bin/env python3

import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main():
    # are these characters across? certainly not pixels
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # sets tileset to the image downloaded.
    tileset = tcod.tileset.load_tilesheet(
            "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
    event_handler = EventHandler()
    # saves some information into a variable 'context'
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title='Yet Another Roguelike Tutorial',
            vsync=True,
    )   as context:
            # This creates the screen (recall display surface from pygame)
            # order="F" makes access of 2D array (namely the board), as [x, y]
            root_console = tcod.Console(screen_width, screen_height, order="F")
            
            # main game loop
            while True:

                root_console.print(x=player_x, y=player_y, string='@')
                #This actually "prints" the console. (recall pygame.display.update())    
                context.present(root_console)
                # clears the console so not leave old positions drawn
                root_console.clear()

                #event handling!
                # tcod.event.wait() waits for an event, and then runs through the loop.
                for event in tcod.event.wait():
                    # sends event to the relevant part of event.handler (ie ev_keydown for keypresses)
                    action = event_handler.dispatch(event)

                    # ignore actions that are not handled yet
                    if action == None:
                        continue
                        
                    # isinstance checks if action is an instantiation of Movement Action (check isinstance(5, int)
                    if isinstance(action, MovementAction):
                        player_x += action.dx
                        player_y += action.dy

                    elif isinstance(action, EscapeAction):
                        raise SystemExit()





if __name__ == '__main__':
    main()
