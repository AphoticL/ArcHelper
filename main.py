import json
import sys
import sqlite3
sys.path.append("./lib")

from SongClass import Song
from SongClass import parseToSong as parse

db = sqlite3.connect("data.db")
cursor = db.cursor()

cursor.execute('SELECT * FROM songData')
r = cursor.fetchall()
for row in r:
    print ('''{1} - {0}: 
    Past:
    \t diff: {2}
    \t poten:{3}
    \t note: {4}
    Prs:
    \t diff: {5}
    \t poten:{6}
    \t note: {7}
    Ftr:
    \t diff: {8}
    \t poten:{9}
    \t note: {10}
    
    {11}'''.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

