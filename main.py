import json
import sys
sys.path.append("./lib")

from SongClass import Song

a = Song("test", "Sakuzyo", 
{"diff": 1,"scorepoten": 1,"notecount": 1}, 
{"diff": 2,"scorepoten": 2,"notecount": 2}, 
{"diff": 3,"scorepoten": 3,"notecount": 3}, 
"test")

a.print()

