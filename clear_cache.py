import os
import shutil


def clear_python_cache(root="."):
    removed = {"pycache_dirs": 0, "pyc_files": 0}

    for dirpath, dirnames, filenames in os.walk(root):
        # Remove __pycache__ directories
        if "__pycache__" in dirnames:
            pycache_path = os.path.join(dirpath, "__pycache__")
            shutil.rmtree(pycache_path)
            removed["pycache_dirs"] += 1

        # Remove .pyc files
        for file in filenames:
            if file.endswith(".pyc"):
                pyc_path = os.path.join(dirpath, file)
                os.remove(pyc_path)
                removed["pyc_files"] += 1

    return removed


if __name__ == "__main__":
    result = clear_python_cache(".")
    print(f"Removed {result['pycache_dirs']} __pycache__ directories")
    print(f"Removed {result['pyc_files']} .pyc files")
