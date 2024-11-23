#!/usr/bin/python3
from wayfire import WayfireSocket
from wayfire.extra.ipc_utils import WayfireUtils
import itertools
sock = WayfireSocket()
utils = WayfireUtils(sock) 
utils.go_next_workspace()
