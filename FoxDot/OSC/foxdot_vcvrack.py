# This is an OSC proxy server that receives FoxDot OSC bundles,
# serializes them into a dictionary and sends to VCV Rack cvOSCcv module.

import argparse
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

# Client will send OSC messages to VCV Rack
client = udp_client.SimpleUDPClient("127.0.0.1", 7002)

def foxdot_handler(addr, *args):
    # 'play1' is the name of FoxDot's sample player, but you can use any synth name here, like "pluck"
    if args[0] != 'play1':
        return

    # OSC bundle looks like this: ["/s_new", "play1", 1001, 1, 0, "freq", 440, "amp", 1, "pan", -1, "sus", 1] 
    args = args[6:] # strip first six elements, we won't need them

    # Parse attributes from the OSC bundle into a dictionary for easier use
    args_dict = {}
    for i in range(0, len(args), 2):
        args_dict[args[i]] = args[i + 1]

    # We will send to two separate VCV Rack OSC addresses,
    # so we need a way to tell which player goes to which address.
    # In this case, sample number decides which address to use.
    if args_dict['sample'] == 0:
        client.send_message("/kick_rate", args_dict['rate'])
        client.send_message("/kick_sus", args_dict['sus'])
    elif args_dict['sample'] == 1:
        client.send_message("/hihat_rate", args_dict['rate'])
        client.send_message("/hihat_sus", args_dict['sus'])

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1", help="The ip to listen on")
  parser.add_argument("--port", type=int, default=7001, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/s_new", foxdot_handler)

  # Server will receive messages from FoxDot and decode them using "foxdot_handler" function
  server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)

  print("Serving on {}".format(server.server_address))
  server.serve_forever()

