import os

# Nama file output
output_file = "output.txt"

# Nama file Python itu sendiri
current_script = "merge_files.py"

# Membuka file output untuk menulis
with open(output_file, "w") as out:
    for filename in os.listdir("."):
        # Mengecualikan file Python itu sendiri dan file output
        if os.path.isfile(filename) and filename not in {current_script, output_file}:
            out.write(f"{filename}\n")  # Menulis nama file
            with open(filename, "r") as f:
                out.write(f.read())  # Menulis isi file
            out.write("\n")  # Baris kosong pemisah
