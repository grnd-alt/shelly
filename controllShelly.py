import requests
from time import sleep
import private
import asyncio
import datetime
class Morse:
        def __init__(self,parent) -> None:
            self.parent = parent
            pass
        def long(self):
            print("long")
            self.parent.TurnOn()
            sleep(1.2)
            self.parent.TurnOff()
            sleep(.1)
        def short(self):
            print("short")
            self.parent.TurnOn()
            sleep(.6)
            self.parent.TurnOff()
            sleep(.1)
        def SOS(self):
            while True:
                for i in range(3):
                    self.parent.morse.short()
                for i in range(3):
                    self.parent.morse.long()
                for i in range(3):
                    self.parent.morse.short()
                sleep(5)
class ShellyPlug:
    def __init__(self,url,key,channel,id) -> None:
        self.url = url
        self.key = key
        self.channel=channel
        self.id = id
        self.lastreq = datetime.datetime.now().timestamp()
        pass
    async def GetInfo(self)->None:
        requests.get(url=self.url+"/device/status/?auth_key="+self.key+"&id=c18a2f")
    async def ToggleStatus(self)->None:
        requests.get("http://"+self.url+"/relay/0?turn=toggle")
    def TurnOn(self):
        towait = datetime.datetime.now().timestamp()-self.lastreq
        if(towait<1.5):
            sleep(2-towait)
        resp = requests.post(self.url+"/device/relay/control/",data={"channel":"0","turn":"on","id":self.id,"auth_key":self.key})
        print(resp.json())
        self.lastreq = datetime.datetime.now().timestamp()
    def TurnOff(self):
        towait = datetime.datetime.now().timestamp()-self.lastreq
        if(towait<1.5):
            sleep(2-towait)
        resp = requests.post(self.url+"/device/relay/control/",data={"channel":"0","turn":"off","id":self.id,"auth_key":self.key})
        print(resp.json())
        self.lastreq = datetime.datetime.now().timestamp()
        pass
        
async def main():
    LivingRoomPlug = ShellyPlug("https://shelly-35-eu.shelly.cloud",private.SHELLY_KEY,channel="0",id=private.SHELLY_ID)
    # LivingRoomPlug.GetInfo()
    LivingRoomPlug.TurnOn()
    sleep(1.6)
    LivingRoomPlug.TurnOff()
    LivingRoomPlug.TurnOn()
    LivingRoomPlug.TurnOff()
if __name__ =="__main__":
    asyncio.run(main())