import hlt
from hlt import constants
from hlt.positionals import Direction
import random
import logging
from bot import Bot

""" <<<Game Begin>>> """

game = hlt.Game()
bot = Bot()
game.ready(bot.bot_name())
logging.info("Successfully created bot! My Player ID is {}.".format(game.my_id))

""" <<<Game Loop>>> """

while True:
    game.update_frame()
    bot.update_game_info(game)

    command_queue = bot.generate_command()
    game.end_turn(command_queue)
