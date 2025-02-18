import time

from kevinbotlib.comm import AnyListSendable, BooleanSendable, IntegerSendable, KevinbotCommClient
from kevinbotlib.logger import Logger, LoggerConfiguration

logger = Logger()
logger.configure(LoggerConfiguration())

client = KevinbotCommClient(on_update=None)
client.connect()
client.wait_until_connected()

try:
    while True:
        print(client.get("joysticks/0/buttons", AnyListSendable))
        print(client.get("joysticks/0/axes", AnyListSendable))
        print(client.get("joysticks/0/pov", IntegerSendable))
        print(client.get("joysticks/0/connected", BooleanSendable))
        time.sleep(0.1)
except KeyboardInterrupt:
    client.disconnect()
