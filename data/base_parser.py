import os

import carball
from carball.json_parser.game import Game


def compile_to_json():
    carball.decompile_replay(os.path.abspath('test/replays/516E50BF491D3ECE8D1E9FAD08C00F9B.replay'),
                             os.path.abspath('test/replays/516E50BF491D3ECE8D1E9FAD08C00F9B.json'), overwrite=False)


def get_decompiled_replay():
    game = Game(os.path.abspath(
        'test/replays/516E50BF491D3ECE8D1E9FAD08C00F9B.json'))
    return game
