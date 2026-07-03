import os
import sys
from collections import defaultdict
from pathlib import Path

def audit_physical_disk(target_path):
    root = Path(target_path).resolve()
    
    total_files = 0
    ext_counts = defaultdict(int)
    
    # Explicitly blind the auditor to Git noise and your output telemetry
    IGNORED_DIRS = {'.git', 'raw output', 'tools', 'telemetry'}
    
    for dirpath, dirnames, filenames in os.walk(root):
        # In-place modification to instantly prune ignored directories from the walk
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]
        
        for file in filenames:
            total_files += 1
            
            # Extract extension, grouping extensionless files explicitly
            ext = Path(file).suffix.lower()
            if not ext:
                ext = '<no_extension>'
                
            ext_counts[ext] += 1
            
    return total_files, ext_counts

if __name__ == "__main__":
    # Smart Path Resolution
    script_dir = Path(__file__).parent.resolve()
    
    # 1. Did the user provide a specific path?
    if len(sys.argv) > 1:
        target = Path(sys.argv[1]).resolve()
    # 2. Is the script being run from inside the 'tools' directory?
    elif script_dir.name == "tools":
        target = script_dir.parent / "data"
    # 3. Otherwise, look for the 'data' folder in the current directory
    else:
        target = Path.cwd() / "data"
        if not target.exists():
            target = Path.cwd()
    
    print(f"=== PHYSICAL DISK AUDIT: {target} ===\n")
    
    if not target.exists():
        print(f"Error: Target path '{target}' does not exist.")
        sys.exit(1)
        
    total, exts = audit_physical_disk(target)
    
    print(f"--- ABSOLUTE TOTAL FILES: {total} ---\n")
    
    print("--- COMPOSITION BY EXTENSION (Complete) ---")
    sorted_exts = sorted(exts.items(), key=lambda x: x[1], reverse=True)
    for ext, count in sorted_exts:
        print(f"{count:>7}  {ext}")