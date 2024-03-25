#!/bin/env python3
import os
import sys
from wayfire_socket import WayfireSocket, get_msg_template

def move_to_workspace(output_id, workspace_x, workspace_y):
    addr = os.getenv('WAYFIRE_SOCKET')
    sock = WayfireSocket(addr)
    
    msg = get_msg_template('vswitch/set-workspace')
    msg['data']['x'] = workspace_x
    msg['data']['y'] = workspace_y
    msg['data']['output-id'] = output_id
    sock.send_json(msg)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 move_workspace.py <output_id> <workspace_x> <workspace_y>")
        sys.exit(1)

    output_id = int(sys.argv[1])
    workspace_x = int(sys.argv[2])
    workspace_y = int(sys.argv[3])

    move_to_workspace(output_id, workspace_x, workspace_y)
