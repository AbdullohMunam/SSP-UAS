import os

# Nama file output
output_file = "output.txt"

# Nama file Python itu sendiri
current_script = "merge_files.py"

# Daftar file yang tidak perlu
excluded_files = {
    current_script,
    output_file,
    ".gitignore",
    "README.md",
}

def write_all_files(base_dir, out):
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if (
                filename not in excluded_files
                and not filename.endswith(".pyc")
            ):
                filepath = os.path.join(root, filename)
                out.write(f"{filepath}\n")  # Nama file dengan path relatif
                try:
                    with open(filepath, "r") as f:
                        out.write(f.read())
                except Exception as e:
                    out.write(f"[Tidak bisa membaca file: {e}]\n")
                out.write("\n")  # Baris kosong pemisah

with open(output_file, "w") as out:
    write_all_files(".", out)