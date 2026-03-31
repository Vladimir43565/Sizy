import os

def get_item_size(path):
    """Calculates size of a file or a folder (iteratively)."""
    if os.path.isfile(path):
        try:
            return os.path.getsize(path)
        except OSError:
            return 0
    
    total_size = 0
    stack = [path]
    while stack:
        current = stack.pop()
        try:
            with os.scandir(current) as it:
                for entry in it:
                    try:
                        if entry.is_file(follow_symlinks=False):
                            total_size += entry.stat().st_size
                        elif entry.is_dir(follow_symlinks=False):
                            stack.append(entry.path)
                    except (PermissionError, OSError):
                        continue
        except (PermissionError, OSError):
            continue
    return total_size

def format_size(size_bytes):
    if size_bytes == 0: return "0 B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = 0
    while size_bytes >= 1024 and i < len(units) - 1:
        size_bytes /= 1024
        i += 1
    return f"{size_bytes:.2f} {units[i]}"

# --- Main App ---
target_path = input("Paste folder location to find biggest items: ").strip().strip('"')

if os.path.exists(target_path):
    print(f"\nAnalyzing items inside: {target_path}...")
    
    report = []
    
    # We look at the immediate children of the folder you pasted
    try:
        with os.scandir(target_path) as entries:
            for entry in entries:
                print(f"Checking: {entry.name}...")
                size = get_item_size(entry.path)
                report.append((entry.name, size))
    except Exception as e:
        print(f"Error accessing folder: {e}")

    # Sort items by size (largest first)
    report.sort(key=lambda x: x[1], reverse=True)

    print("\n--- SIZY TOP 10 LARGEST ITEMS ---")
    for name, size in report[:10]:
        print(f"{format_size(size)} -> {name}")

else:
    print("Invalid path!")

input("\nScan complete. Press Enter to exit.")