from hlt import constants
from hlt.positionals import Direction
import random

class Bot:
    def __init__(self):
        self.g = None # Game Object

    def bot_name(self):
        # Potentially we want to put relevant parameters
        return 'My Bot Ver.1'

    def _my_ships(self):
        assert self.g != None
        return self.g.me.get_ships()

    def update_game_info(self, game):
        self.g = game

    def generate_command(self):
        command_queue = []
        g = self.g
        me = self.g.me
        map = self.g.game_map

        for ship in self._my_ships():
            if map[ship.position].halite_amount < constants.MAX_HALITE / 10 or ship.is_full:
                command_queue.append(
                    ship.move(
                        random.choice([ Direction.North, Direction.South, Direction.East, Direction.West ])))
            else:
                command_queue.append(ship.stay_still())

        if g.turn_number <= 200 and \
           me.halite_amount >= constants.SHIP_COST and \
           not map[me.shipyard].is_occupied:
            command_queue.append(me.shipyard.spawn())

        return command_queue

