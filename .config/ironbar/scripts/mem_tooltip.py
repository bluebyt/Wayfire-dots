#!/usr/bin/env python3
import sys
import psutil
import argparse

# --- CONFIG ---
ICON = ""

# Mapping for cleaner names (sums them up if multiple exist)
MAPPING = {
    "isolated web co": "Firefox",
    "privileg": "Firefox",
    "firefox": "Firefox",
    "helium-browser": "Helium",
    "vesktop.bin": "Discord",
    "element-desktop": "Element",
    "codium": "VS Code"
}

def get_data():
    # Overall Percent
    percent = int(psutil.virtual_memory().percent)
    
    # Process Memory
    procs = {}
    for p in psutil.process_iter(['name', 'memory_info']):
        try:
            name = p.info['name'].lower()
            # Match replacements
            for key, val in MAPPING.items():
                if key in name:
                    name = val
                    break
            else:
                # If not in list, just capitalize the first letter
                name = name.capitalize()
            
            mem = p.info['memory_info'].rss
            procs[name] = procs.get(name, 0) + mem
        except:
            continue
    
    # Sort and take Top 5
    top = sorted(procs.items(), key=lambda x: x[1], reverse=True)[:5]
    return percent, top

def format_mb(b):
    return f"{int(b / (1024*1024))} MB"

# CLI Arguments
parser = argparse.ArgumentParser()
parser.add_argument("--text", action="store_true", help="Output only the bar label")
parser.add_argument("--tooltip", action="store_true", help="Output only the tooltip text")
args = parser.parse_args()

percent, top = get_data()

if args.text:
    # Outputs formatted percentage (e.g., 09%)
    print(f"{ICON} {percent:02d}%")
elif args.tooltip:
    # Outputs plain text for the tooltip
    print("Top Memory Usage:")
    for name, mem in top:
        print(f"{name} / {format_mb(mem)}")
else:
    # Default fallback
    print(f"{ICON} {percent:02d}%")
