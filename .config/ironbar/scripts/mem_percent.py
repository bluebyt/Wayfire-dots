#!/usr/bin/env python3
import psutil

# Get virtual memory stats
mem = psutil.virtual_memory()
percent = int(mem.percent)

# Format as two digits (e.g., 09%) to match your CPU module
print(f"{percent:02d}%")
