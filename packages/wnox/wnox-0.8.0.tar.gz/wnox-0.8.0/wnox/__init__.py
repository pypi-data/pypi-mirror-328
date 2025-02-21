#%%
import asyncio
import nest_asyncio
import logging
from slixmpp import ClientXMPP 
import ssl
import json
from bson import ObjectId 
import requests as r

import random
import string

nest_asyncio.apply()
eventdatax = {}
eventsx = {}
# logging.basicConfig(level=logging.DEBUG)

def serial_generator(length: int) -> str:
    chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
    random_string = ''.join(random.choice(chars) for _ in range(length))
    return random_string

class EventEmitter:
    def __init__(self):
        self._events = {}

    def on(self, event_name, callback):
        if event_name not in self._events:
            self._events[event_name] = []
        self._events[event_name].append(callback)

    async def emit(self, event_name, *args, **kwargs):
        if event_name in self._events:
            # Collect the results of all event handlers
            results = []
            for callback in self._events[event_name]:
                result = callback(*args, **kwargs)
                if asyncio.iscoroutinefunction(callback):  # If callback is async
                    results.append(await result)
                else:  # If callback is sync
                    results.append(result)
            return results[0]

class WSX(ClientXMPP, EventEmitter):
    connected = False
    def __init__(self, jid, password, app:str, uid:str, resource:str):
    
        ClientXMPP.__init__(self, jid, password)
        EventEmitter.__init__(self)
        self.app = app
        self.uid = uid
        self._resource = resource
        self.password = password
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("failed_auth", self.on_failed_auth)
        self.add_event_handler("disconnected", self.on_disconnect)
        self.add_event_handler("message", self.on_message) 

    async def start(self, event):
        """Handle session start."""
        print("[bridge] connected.")
        self.send_presence(ptype="presence")
        await self.get_roster()
        await self.emit("__connect",{})
        self.connected = True
        

    def on_failed_auth(self, event):
        """Handle authentication failure."""

    async def on_disconnect(self, event):
        """Handle disconnection and attempt reconnection."""
        await self.emit("__disconnect",{})
        self.connected = False
        asyncio.create_task(self.reconnect())

    async def reconnect(self):
        await asyncio.sleep(5) 
        self.connect(address=("direct.qepal.com", 5222), disable_starttls=False, force_starttls=True)
        self.process(forever=False)

    async def on_message(self, stanza):
        """Handle incoming messages."""
        if stanza.tag == "{jabber:client}message":
            body = str(stanza['body'])
            from_jid = str(stanza['from'])
            itsme = from_jid and f"{self.boundjid.bare.split('@')[0]}-{self.boundjid.bare.split('@')[1]}" in from_jid
            itsbro = not itsme and f"{self.boundjid.bare.split('@')[0]}-" in from_jid
            
            if "conference.qepal.com" in from_jid:
                itsme = f"{self.app}-{self.uid}-{self._resource}" in from_jid
                itsbro = not itsme and f"{self.app}-{self.uid}-" in from_jid
                
            delayed = "urn:xmpp:delay" in str(stanza)

            if body and not delayed:
               
                    
                if body.startswith("{"):
                    try:
                        json_data = json.loads(body)
                        if "__connect" in json_data:
                            return
                        if "__disconnect" in  json_data:
                            return
                        if "__message" in  json_data:
                            return
                        
                        if "api" in json_data:
                            user_uid = from_jid.split('@')[0]
                            data = {key: val for key, val in json_data.items() if key != "api"}
                            data = {key: val for key, val in data.items() if key != "mid"}
                            data["from"] = from_jid
                            data["app"] = None
                            if len(user_uid) == 24 and ObjectId.is_valid(user_uid):
                                data["uid"] = user_uid
                                data["app"] = None
                                result = await self.emit(json_data["api"], data)
                                if result == None:
                                    result = {}
                                self.send_message(
                                    mto=from_jid,
                                    mbody=json.dumps({**result, "mid": json_data.get("mid")})
                                )
                            elif "conference.qepal.com" in from_jid:
                                pass
                            elif "-" in user_uid:
                                app = user_uid.split('-')[0]
                                user_uid = user_uid.split('-')[1]
                                data["app"] = app
                                data["uid"] = user_uid
                                
                        else:
                            if "mid" in json_data:
                                data = {key: val for key, val in json_data.items() if key != "mid"}
                                eventdatax[json_data.get("mid")] = data
                                if json_data.get("mid") in eventsx:
                                    eventsx.get(json_data.get("mid")).set()
                            else:
                                await self.emit("__message", {"from": from_jid, "body": body, "itsme": itsme, "itsbro": itsbro})
                   
                    except json.JSONDecodeError:
                        pass
                else:
                    await self.emit("__message", {"from": from_jid, "body": body, "itsme": itsme, "itsbro": itsbro})



class App:
    
    def __init__(self, *, app:str, resource:str, securekey:str, image:str, public:bool=False):
        self.app = app
        self.channels = set()
        self.resource = resource
        self.securekey = securekey
        self.image = image
        self.public = public
        
        _json = r.post("https://qepal.com/api/bridge/worker/init", json={
            "app":app, "resource":resource, "securekey":securekey, "image":image, "public":public}).json()
        
        self.uid = _json["uid"]
        self.myjid = self.app + "-" + str(self.uid) + "@qepal.com/" + self.resource
        self.password = _json["password"]
        self.xmpp = WSX(self.myjid, self.password, self.app, self.uid, self.resource)

    def on(self, api:str, cb:callable):
        self.xmpp.on(api, cb)
    
    def sendtojid(self, jid:str, body:str):
        self.xmpp.send_message(mto=jid, mbody=body)
        
    def connected(self):
        return self.xmpp.connected
        
    async def api(self, app:str, cmd:str, body:dict, jid:str = None, prioritize_public:bool = False):
        if jid == None:
            res:dict = r.post("https://qepal.com/api/bridge/worker/findfreeresource", json={ "app":app, "securekey": self.securekey }).json()
            jids = list(res.get("jids",[]))
            if len(jids) > 0:
                if prioritize_public:
                    jid = jids[-1]
                else:
                    jid = jids[0]
        if jid == None:
            print("unable to send api (-1)")
            return
    
        mid = serial_generator(10)
        msg = {"mid":mid, "api":cmd, **body }  
        eventsx[mid] = asyncio.Event()
        self.sendtojid(jid, json.dumps(msg))
        await eventsx[mid].wait()
        data = eventdatax.get(mid)
        return data
        
        
            
    def subscribe(self, channelname:str):
        self.xmpp.send_presence(pto=channelname+ "@conference.qepal.com/"+ self.app + "-" + self.uid + "-" + self.resource , ptype="presence")
        self.xmpp.get_roster()
        self.channels.add(channelname)
        
    def unsubscribe(self, channelname:str):
        self.xmpp.send_presence(pto=channelname+ "@conference.qepal.com" , ptype="unavailable")
        self.xmpp.get_roster()
        self.channels.remove(channelname)
        
    def sendtochannel(self, channelname:str, body:str):
        if channelname not in self.channels:
            self.subscribe(channelname)
        self.xmpp.send_message(mto=f"{channelname}@conference.qepal.com", mbody=body, mtype='groupchat')
        
    async def loop(self):

        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False 
        ssl_ctx.verify_mode = ssl.CERT_NONE  
        self.xmpp.ssl_context = ssl_ctx
    
        self.xmpp.connect(address=("direct.qepal.com", 5222), disable_starttls=False, force_starttls=True)
        self.xmpp.process(forever=True)



