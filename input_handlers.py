

from typing import Optional

import tcod.event
# import from actions.py the class action and the subclasses
from actions import Action, EscapeAction, MovementAction


# creat EventHandler class which is a subclass of EventDispatch
class EventHandler(tcod.event.EventDispatch[Action]):

    # this quits the program when the x in the top left is clicked.
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    # this method recieves keypresses and returns either a action subclass or None
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        # variable that is set subclass or None
        action: Optional[Action] = None
        # variable that holds the actual key pressed (won't save modifiers ie alt)
        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()


        # No valid key was pressed *** what? lol
        # action is then returned
        return action
