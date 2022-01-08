#!/usr/bin/env python3

import tcod

from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main():
    # in character size. tcod definitely made with rogue in mind!
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45
    
    # colors for syntactic sugar
    #           R    G    B
    WHITE  = (255, 255, 255)
    YELLOW = (255, 255,   0)

    # sets tileset to the image downloaded.
    tileset = tcod.tileset.load_tilesheet(
            "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #save event handler function as a variable
    event_handler = EventHandler()
    
    # defines objects in terms of Entity class
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", WHITE)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", YELLOW)
    entities = {npc, player}
    
    # game map variable
    game_map = GameMap(map_width, map_height)

    #init engine as Engine class
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

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

                engine.render(console=root_console, context=context)

                events = tcod.event.wait()

                engine.handle_events(events)






if __name__ == '__main__':
    main()
