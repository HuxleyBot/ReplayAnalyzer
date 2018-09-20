import logging

import data.base_parser as parser

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # Do things
    game = parser.get_decompiled_replay()
    print(game.replay_data)
