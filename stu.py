from enum import Enum

class Season(Enum):
    SUMMER = 1
    MONSOON = 2
    WINTER = 3


for season in Season:
    print(season.name)