"""
This program sends 10 random values between 0.0 and 1.0 to the /filter address,
waiting for 1 seconds between each value.
"""
import argparse

from pythonosc import osc_message_builder
from pythonosc import udp_client


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="172.16.162.169",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=8000,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.UDPClient(args.ip, args.port)

  keyA = input("tecla A :")

  if keyA == 'a' :

    msg = osc_message_builder.OscMessageBuilder(address = "/tecla")
    msg.add_arg(3)
    msg = msg.build()
    client.send(msg)
    #time.sleep(1)