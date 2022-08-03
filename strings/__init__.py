#
# Copyright (C) 2021-2022 by miss097@Github, <https://github.com/miss097 >.
#
# This file is part of < https://github.com/miss097/MissMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/miss097/MissMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import os
import sys
from typing import List

import yaml

languages = {}
commands = {}


languages_present = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./strings/" + filename, encoding="utf8")
        )


for filename in os.listdir(r"./strings/langs/"):
    if "id" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/id.yml", encoding="utf8")
        )
        languages_present["id"] = languages["id"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "id":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["id"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["id"][item]
    try:
        languages_present[language_name] = languages[language_name][
            "name"
        ]
    except:
        print(
            "There is some issue with the language file inside bot. Please report it to the TeamMiss at @MissSupport on Telegram"
        )
        sys.exit()
