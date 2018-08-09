import json
class Song:
    '''
    Initiates a song object. 
    Args [info, past, present, future, added in]
    info : dictionary
    {
        name: "name",
        composer: "composer"
    }
    past/present/future: dictionary 
    {
        diff: [1-11],
        scorepoten: [0.00-11.2],
        notecount: [0-1450]
    }
    '''
    def __init__ (self, name, comp, pst, prs, ftr, incl):
        self.name = name
        self.comp = comp
        self.pst = pst
        self.prs = prs
        self.ftr = ftr
        self.incl = incl
    
    def outAsString(self):
        out = {
            "name": self.name,
            "composer": self.comp,
            "past": self.pst,
            "present": self.prs,
            "future": self.ftr,
            "incl": self.incl
        }
        return json.dumps(out, indent=4)
    
    def print(self):
        print (self.outAsString())