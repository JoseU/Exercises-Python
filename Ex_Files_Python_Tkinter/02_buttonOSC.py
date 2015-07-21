#!/usr/bin/python3
# button.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com
import argparse

from pythonosc import osc_message_builder
from pythonosc import udp_client


from tkinter import *
from tkinter import ttk  

"""osc"""

parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
  help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=8000,
  help="The port the OSC server is listening on")
args = parser.parse_args()

client = udp_client.UDPClient(args.ip, args.port)


def osc():
	msg = osc_message_builder.OscMessageBuilder(address = "/click")
	msg.add_arg(3)
	msg = msg.build()
	client.send(msg)



""" interfaz grafica """      
    
root = Tk()

button = ttk.Button(root, text = "Click Me")
button.pack()

def callback():
    print('Clicked!')
    osc()


button.config(command = callback)
button.invoke()


root.mainloop()
