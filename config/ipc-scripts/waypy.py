#!/bin/env python3
from wayfire import sock
# focused_view_id = sock.get_focused_view()["id"]
# sock.set_workspace({"x":1, "y":1}, focused_view_id)

# or not moving the view and yet going to the workspace
# sock.set_workspace({"x":2, "y":2})

# sock.get_focused_view()

sock.go_next_workspace()
# sock.go_previous_workspace()

# sock.get_active_workspace_number()
# sock.get_active_workspace_number()
# workspace_number = 2
# sock.set_workspace(workspace_number)



