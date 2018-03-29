import configparser
import os

proDir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


class getConfig:
    def __init__(self):
        self.conffile = os.path.join(proDir,"conf.cfg")
        print(self.conffile)
        self.cf = configparser.ConfigParser()
        self.cf.read(self.conffile)

    def getConfig(self,section,key):
        return self.cf.get(section,key)

    def setConfig(self,section,key,value):
        if self.cf.has_option(section,key):
            print("**************")
            self.cf.set(section,key,value)
            self.cf.write(open(self.conffile,"w"))

if __name__=="__main__":
    print("--------------")
    r = getConfig()
    print(r.conffile)
    getConfig().setConfig("wx","test","2")