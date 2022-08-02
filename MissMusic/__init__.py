#
# Copyright (C) 2021-2022 by miss097@Github, <https://github.com/miss097 >.
#
# This file is part of < https://github.com/miss097/MissMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miss097/MissMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from MissMusic.core.bot import MissBot
from MissMusic.core.dir import dirr
from MissMusic.core.git import git
from MissMusic.core.userbot import Userbot
from MissMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = MissBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
