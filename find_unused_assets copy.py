import os
import re
import shutil

# === CONFIGURACIÓN ===
ASSETS_DIR = "public/assets"
CODE_DIRS = ["src", "public"]
BACKUP_DIR = "used_assets_backup"
CODE_EXTENSIONS = {".js", ".ts", ".jsx", ".tsx", ".html", ".css", ".scss", ".svelte"}

def get_assets_files():
    asset_files = []
    for root, _, files in os.walk(ASSETS_DIR):
        for f in files:
            if f.startswith(".") or f.endswith(".DS_Store"):
                continue
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, ASSETS_DIR).replace("\\", "/")
            asset_files.append((rel_path, full_path))  # (rel_path, full_path)
    return asset_files

def get_code_files():
    contents = []
    for code_dir in CODE_DIRS:
        for root, _, files in os.walk(code_dir):
            for f in files:
                if any(f.endswith(ext) for ext in CODE_EXTENSIONS):
                    try:
                        with open(os.path.join(root, f), "r", encoding="utf-8") as file:
                            contents.append(file.read())
                    except Exception as e:
                        print(f"Error leyendo {f}: {e}")
    return "\n".join(contents)

def find_used_assets():
    assets = get_assets_files()
    code = get_code_files()
    used = []

    for rel_path, full_path in assets:
        if re.search(re.escape(rel_path), code):
            used.append((rel_path, full_path))

    return used

def backup_used_files(used_files):
    for rel_path, full_path in used_files:
        dest_path = os.path.join(BACKUP_DIR, rel_path)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        shutil.copy2(full_path, dest_path)

if __name__ == "__main__":
    used = find_used_assets()

    print(f"\nArchivos utilizados en '{ASSETS_DIR}':\n")
    for rel_path, _ in used:
        print(f" - {rel_path}")

    print(f"\nTotal: {len(used)} archivos usados.")

    if used:
        print(f"\nCopiando archivos usados a '{BACKUP_DIR}'...")
        backup_used_files(used)
        print("Copia completada.")
