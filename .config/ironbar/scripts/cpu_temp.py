#!/usr/bin/env python3
import psutil
import argparse

# --- CONFIG ---
ICON = ""
SEP = "│"  # Using the same separator you chose for CPU usage

def get_temp_data():
    temps = psutil.sensors_temperatures()
    
    # Common keys for CPU temp are 'coretemp' (Intel) or 'k10temp' (AMD)
    cpu_key = next((k for k in temps.keys() if k in ['coretemp', 'k10temp', 'cpu_thermal']), None)
    
    if not cpu_key:
        return 0, []
        
    data = temps[cpu_key]
    
    # Overall temp is usually the first entry (Package)
    overall = int(data[0].current)
    
    # Per-core temps
    per_core = []
    for entry in data:
        # Avoid repeating the 'Package' or 'Composite' temp in the list
        if "Core" in entry.label:
            per_core.append((entry.label, int(entry.current)))
            
    return overall, per_core

parser = argparse.ArgumentParser()
parser.add_argument("--text", action="store_true")
parser.add_argument("--tooltip", action="store_true")
args = parser.parse_args()

overall, core_temps = get_temp_data()

if args.text:
    # Matches your 09% style with 39°C
    print(f"{ICON} {overall:02d}°C")
elif args.tooltip:
    if not core_temps:
        print("No per-core sensors found.")
    else:
        print("CPU Temperature:")
        for label, temp in core_temps:
            # Cleans up "Core 0" to "Core 1" to match your CPU module
            core_num = label.replace("Core ", "")
            print(f"CPU{int(core_num)+1:<1}  {temp:02d}°C")
else:
    print(f"{ICON} {overall:02d}°C")
