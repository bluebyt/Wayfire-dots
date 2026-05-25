#!/usr/bin/env python3
import psutil
import argparse

# --- CONFIG ---
ICON = ""

def get_cpu_data():
    # Adding an interval (0.1s) allows psutil to calculate real usage
    # instead of just a snapshot of the current clock cycle.
    overall = int(psutil.cpu_percent(interval=0.5))
    per_core = psutil.cpu_percent(interval=None, percpu=True)
    return overall, per_core

# CLI Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--text", action="store_true", help="Output only the bar label")
parser.add_argument("--tooltip", action="store_true", help="Output only the tooltip text")
args = parser.parse_args()

overall, per_core = get_cpu_data()

if args.text:
    print(f"{ICON} {overall:02d}%")
elif args.tooltip:
    print("CPU Load per Core:")
    for i, percentage in enumerate(per_core):
        # Displays "Core 1" instead of "Core 0" to match your screenshot
        print(f"CPU{i+1:<1}  {int(percentage):02d}%")
else:
    print(f"{ICON} {overall:02d}%")
