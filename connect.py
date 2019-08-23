USERNAME = "Asquedril"
LOGIN_COMMANDS = ["/login skylo", "/go"]
SERVER = "ns3035424.ip-149-202-89.eu"
#SERVER = "neocrash.tk"
PORT = 25565

from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound, PositionAndLookPacket
import time

from log import log

global minecraft_bots
minecraft_bots = {}

class MinecraftBot():
	def __init__(self, username, server, port, commands):
		self.username = username
		self.server = server
		self.port = port
		self.commands = commands
		self.bot = Connection(server, port, username=username, allowed_versions=[47])
		self.bot.register_packet_listener(self.handle_join_game, clientbound.play.JoinGamePacket)
		log("INFO", "Trying to connect {0} to {1}:{2}.".format(username, server, port))
		self.bot.connect()

	def handle_join_game(self, join_game_packet):
		log("INFO", "{0} is connected to {1}:{2}.".format(self.username, self.server, self.port))
		time.sleep(1)
		for command in self.commands:
			packet = serverbound.play.ChatPacket()
			packet.message = command
			self.bot.write_packet(packet)
			time.sleep(10)

	def disconnect(self):
		log("INFO", "Disconnecting {0} from {1}:{2}.".format(self.username, self.server, self.port))
		self.bot.disconnect()
		log("INFO", "{0} is disconnected of {1}:{2}.".format(self.username, self.server, self.port))

def minecraft_connect(username, server, port, commands):
	global minecraft_bots
	try:
		minecraft_bots[username]

	except KeyError:
		minecraft_bots[username] = MinecraftBot(username, server, port, commands)
		return True

def minecraft_disconnect(username):
	global minecraft_bots
	try:
		minecraft_bots[username].disconnect()
		del minecraft_bots[username]
		return True
	except:
		return False



#minecraft_connect("Asquedril", SERVER, PORT, LOGIN_COMMANDS)
#time.sleep(10)
#minecraft_disconnect("Asquedril")
#minecraft_connect("test", SERVER, PORT, LOGIN_COMMANDS)