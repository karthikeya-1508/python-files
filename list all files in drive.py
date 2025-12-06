import os

path = "D:/"

for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))

def print_tree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = "│   " * level
        folder = os.path.basename(root)
        print(f"{indent}├── {folder}")

        subindent = "│   " * (level + 1)
        for f in files:
            print(f"{subindent}├── {f}")

print_tree(path)
