#!/usr/bin/env python3

import os
import time

# Paths to the workspace script and style file
workspace_script = os.path.expanduser("~/.config/ipc-scripts/active_workspace_number.py")
style_file = os.path.expanduser("~/.config/waybar/style_wayfire_now.css")

def get_active_workspace():
    """Get the active workspace number from the workspace script."""
    try:
        result = os.popen(f"{workspace_script}").read().strip()
        if result.isdigit() and 1 <= int(result) <= 9:
            return int(result)
        else:
            raise ValueError(f"Unexpected output from {workspace_script}: {result}")
    except Exception as e:
        print(f"Error reading active workspace: {e}")
        return None

def update_specific_line(active_workspace):
    """Update `.workX` at line 280 in the style file while preserving trailing characters."""
    try:
        with open(style_file, "r") as file:
            lines = file.readlines()

        # Ensure line 280 exists
        if len(lines) < 320:
            print(f"Error: {style_file} has fewer than 280 lines.")
            return

        # Update line 280 directly
        target_line = lines[319]  # Line 280 (zero-based index is 279)
        # Replace `.workX` while preserving the rest of the line
        updated_line = target_line.replace(
            target_line.split()[0], f"#custom-work{active_workspace}"
        )
        if updated_line != target_line:  # Only update if there's a change
            lines[319] = updated_line

            # Write back the modified lines to the file
            with open(style_file, "w") as file:
                file.writelines(lines)

            print(f"Updated {style_file}: Set line 280 to `.work{active_workspace}` with preserved content.")
        else:
            print(f"No changes needed; line 280 is already `.work{active_workspace}`.")

    except Exception as e:
        print(f"Error updating style file: {e}")

if __name__ == "__main__":
    previous_workspace = None
    try:
        while True:
            active_workspace = get_active_workspace()
            if active_workspace and active_workspace != previous_workspace:
                update_specific_line(active_workspace)
                previous_workspace = active_workspace

            time.sleep(1)  # Check every second
    except KeyboardInterrupt:
        print("Script stopped.")

