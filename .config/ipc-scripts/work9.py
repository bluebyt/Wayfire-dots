#!/bin/env python3
from wayfire_socket import WayfireSocket, get_msg_template
import os

addr = os.getenv('WAYFIRE_SOCKET')
sock = WayfireSocket(addr)

msg = get_msg_template('vswitch/set-workspace')
msg['data']['x'] = 2
msg['data']['y'] = 2
msg['data']['output-id'] = 1
sock.send_json(msg)
