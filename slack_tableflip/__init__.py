#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# EM Slack Tableflip
# Copyright (c) 2015 Erin Morelli
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
'''
Module: slack_tableflip

    - Sets up Flask application and module constants
'''

import os
import logging
from flask import Flask
from datetime import date
from pkg_resources import get_provider


# =============================================================================
# App Logging
# =============================================================================

__logfile__ = os.path.join(os.path.expanduser("~"), 'logs', 'tableflip.log')

# Config logging
logging.basicConfig(
    filename=__logfile__,
    format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s',
    level=30,
)


# =============================================================================
#  App Constants
# =============================================================================

# Set module name
__module__ = "slack_tableflip.{0}".format(__file__)


# Get module info
def set_project_info():
    ''' Set project information from setup tools installation
    '''

    # CUSTOMIZE THIS VALUE FOR YOUR OWN INSTALLATION
    base_url = 'http://dev.erinmorelli.com/slack/flip'

    # Get app info from the dist
    app_name = 'slack_tableflip'
    provider = get_provider(app_name)

    return {
        'name': app_name,
        'name_full': 'EM Slack Tableflip',
        'author_url': 'http://www.erinmorelli.com',
        'version': '0.2b1',
        'version_int': 0.201,
        'package_path': provider.module_path,
        'copyright': str(date.today().year),
        'base_url': base_url,
        'auth_url': '{0}/authenticate'.format(base_url),
        'valid_url': '{0}/validate'.format(base_url)
    }

# Project info
PROJECT_INFO = set_project_info()

# Set the template directory
TEMPLATE_DIR = os.path.join(PROJECT_INFO['package_path'], 'templates')

# Allowed slash commands
ALLOWED_COMMANDS = [
    '/flip',
    '/fliptable',
    '/tableflip',
    '/flip_table',
    '/table_flip'
]

# Allowed flip types
# Sources:
#   http://www.emoticonfun.org/flip/
#   http://emojicons.com/table-flipping
#   http://tableflipping.com/
ALLOWED_TYPES = {
    'classic': "(╯°□°)╯︵ ┻━┻",
    'rage': "(ﾉಥ益ಥ）ﾉ﻿ ┻━┻",
    'whoops': "┬──┬﻿ ¯\_(ツ)",
    'two': "┻━┻ ︵╰(°□°)╯︵ ┻━┻",
    'tantrum': "┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻",
    'fury': "┻━┻彡 ヽ(ಠДಠ)ノ彡┻━┻﻿",
    'relax': "┬─┬ノ( º _ ºノ)",
    'teeth': "(ノಠ益ಠ)ノ彡┻━┻",
    'monocle': "(╯ಠ_ರೃ)╯︵ ┻━┻",
    'person': "(╯°□°）╯︵ /(.□. \)",
    'jake': "(┛❍ᴥ❍﻿)┛彡┻━┻",
    'owl': "(ʘ∇ʘ)ク 彡 ┻━┻",
    'laptop': "(ノÒ益Ó)ノ彡▔▔▏",
    'strong': "/(ò.ó)┛彡┻━┻",
    'yelling': "(┛◉Д◉)┛彡┻━┻",
    'shrug': "┻━┻ ︵﻿ ¯\(ツ)/¯ ︵ ┻━┻",
    'pudgy': "(ノ ゜Д゜)ノ ︵ ┻━┻",
    'battle': "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)",
    'return': "(ノ^_^)ノ┻━┻ ┬─┬ ノ( ^_^ノ)",
    'cry': "(╯'□')╯︵ ┻━┻",
    'freakout': "(ﾉಥДಥ)ﾉ︵┻━┻･/",
    'people': "(/ .□.)\ ︵╰(゜Д゜)╯︵ /(.□. \)",
    'force': "(._.) ~ ︵ ┻━┻",
    'bear': "ʕノ•ᴥ•ʔノ ︵ ┻━┻",
    'magic': "(/¯◡ ‿ ◡)/¯ ~ ┻━┻",
    'robot': "┗[© ♒ ©]┛ ︵ ┻━┻",
    'opposite': "ノ┬─┬ノ ︵ ( \o°o)\\",
    'cute': "┻━┻ ︵ ლ(⌒-⌒ლ)",
    'glare': "(╯ಠ_ಠ）╯︵ ┳━┳",
    'dead': "(╯°□°）╯︵ /(x_x)|",
    'buffet': "(╯°□°）╯︵ ┻━━━┻ ",
    'adorable': "(づ｡◕‿‿◕｡)づ ︵ ┻━┻",
    'hynotic': "(╯°.°）╯ ┻━┻",
    'bored': "(ノ゜-゜)ノ ︵ ┻━┻",
    'bomb': "( ・_・)ノ⌒●~*"
}

# Allowed word flip types
WORD_TYPES = ['word', 'restore']

# Flipped character mapping
FLIPPED_CHARS = {
    " ": " ",
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ı",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "q",
    "C": "Ɔ",
    "D": "p",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "ʞ",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "ɹ",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    ",": "'",
    "!": "¡",
    "?": "¿",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    ".": "˙",
    '"': ",,",
    "'": ",",
    "’": ",",
    "“": ",,",
    "”": ",,",
    "¿": "?"
}

# =============================================================================
# Flask App Configuration
# =============================================================================

# Initalize flask app
APP = Flask(
    'em-slack-tableflip',
    template_folder=TEMPLATE_DIR,
    static_folder=TEMPLATE_DIR
)

# Set up flask config
# SET THESE ENV VALUES FOR YOUR OWN INSTALLATION
APP.config.update({
    'SQLALCHEMY_DATABASE_URI': os.environ['EMST_DATABASE_URI'],
    'SECRET_KEY': os.environ['EMST_SECRET_KEY']
})
