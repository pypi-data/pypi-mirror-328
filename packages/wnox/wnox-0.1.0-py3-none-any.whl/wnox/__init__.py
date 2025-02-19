#%%
import asyncio
import nest_asyncio
import logging
from slixmpp import ClientXMPP 
import ssl
import json
from bson import ObjectId  # If you need ObjectId validation
import requests as r

nest_asyncio.apply()
# logging.basicConfig(level=logging.DEBUG)
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

class __WebSocketXMPP(ClientXMPP, EventEmitter):
    def __init__(self, jid, password):
    
                
        ClientXMPP.__init__(self, jid, password)
        EventEmitter.__init__(self)
        print(f"connecting to {jid} - {password}")
        # self.jid = jid
        self.password = password
        # self.callback = callback  # Store the callback function
        self.add_event_handler("session_start", self.start)
        self.add_event_handler("failed_auth", self.on_failed_auth)
        self.add_event_handler("disconnected", self.on_disconnect)
        self.add_event_handler("message", self.on_message)  # Add event handler for incoming messages

    async def start(self, event):
        """Handle session start."""
        print("[bridge] connected.")
        self.send_presence()
        await self.get_roster()
        
        # Send a test message
        self.send_message(mto="ethan@qepal.com", mbody="Hello via WebSocket!")
        print("[📩] Message sent to ethan@qepal.com")

    def on_failed_auth(self, event):
        """Handle authentication failure."""
        # print("[❌] Authentication failed. Check username/password.")

    def on_disconnect(self, event):
        """Handle disconnection and attempt reconnection."""
        # print("[❌] Disconnected from server. Attempting to reconnect...")
        asyncio.create_task(self.reconnect())

    async def reconnect(self):
        await asyncio.sleep(5)  # Wait before reconnecting
        print("[🔄] Reconnecting...")
        self.connect(address=("direct.qepal.com", 5222), disable_starttls=False, force_starttls=True)
        self.process(forever=False)

    async def on_message(self, stanza):
        """Handle incoming messages."""
        if stanza.tag == "{jabber:client}message":
            body = str(stanza['body'])
            from_jid = str(stanza['from'])
            itsme = from_jid and f"{self.boundjid.bare.split('@')[0]}-{self.boundjid.bare.split('@')[1]}" in from_jid
            itsbro = not itsme and f"{self.boundjid.bare.split('@')[0]}-" in from_jid
            delayed = "urn:xmpp:delay" in str(stanza)

            if body and not delayed:
                user_uid = from_jid.split('@')[0]
                is_app = False
                if len(user_uid) != 24 or not ObjectId.is_valid(user_uid):
                    user_uid = user_uid.split("-")[-1]
                    is_app = True
                    
                if body.startswith("{"):
                    try:
                        json_data = json.loads(body)
                        if "api" in json_data:
                            data = {key: val for key, val in json_data.items() if key != "api"}
                            data = {key: val for key, val in data.items() if key != "mid"}

                            if True or len(user_uid) == 24 and ObjectId.is_valid(user_uid):
                                result = await self.emit(json_data["api"], data)
                                if result == None:
                                    result = {}
                                self.send_message(
                                    mto=from_jid,
                                    mbody=json.dumps({**result, "mid": json_data.get("mid")})
                                )
                        else:
                            await self.emit("message", {"from": from_jid, "body": body, "itsme": itsme, "itsbro": itsbro, "is_app":is_app})
                    except json.JSONDecodeError:
                        pass
                else:
                    await self.emit("message", {"from": from_jid, "body": body, "itsme": itsme, "itsbro": itsbro, "is_app":is_app})



class App:
    def __init__(self, *, app:str, resource:str, securekey:str, image:str, public:bool=False):
        self.app = app
        self.resource = resource
        self.securekey = securekey
        self.image = image
        self.public = public
        
        json = r.post("https://qepal.com/api/bridge/worker/init", json={
            "app":app, "resource":resource, "securekey":securekey, "image":image, "public":public}).json()
        
        self.uid = json["uid"]
        self.myjid = self.app + "-" + str(self.uid) + "@qepal.com/" + self.resource
        self.password = json["password"]
        self.xmpp = __WebSocketXMPP(self.myjid, self.password)

    def on(self, api:str, cb:callable):
        self.xmpp.on(api, cb)
    
        
    async def loop(self):
        # print("[🔄] Initializing connection...")
        ssl_ctx = ssl.create_default_context()
        ssl_ctx.check_hostname = False  # Disable hostname verification
        ssl_ctx.verify_mode = ssl.CERT_NONE  # Ignore SSL certificate validation
        self.xmpp.ssl_context = ssl_ctx
    
        self.xmpp.connect(address=("direct.qepal.com", 5222), disable_starttls=False, force_starttls=True)
        self.xmpp.process(forever=True)  # Keep the connection alive



