'''
Main Body of script.

in input_file variable we introduce the file to change from crx to rnx.

This file has to be in the same folder as decompress_rinex.py

Use in Terminal:

    python decompress_rinex.py

to launch script

'''


from pathlib import Path
import hatanaka


# 0. File to convert inside the same folder as decompress_rinex
file_crx = "BIRG00ITA_R_20232060000_01D_30S_MO.crx"

# 1. Folder where the script is
folder = Path(__file__).resolve().parent

# 2. Compact RINEX file of the station
#input_file = folder / "TLSG00FRA_R_20221480000_01D_30S_MO.crx" --> ORIGINAL
input_file = folder / file_crx

# 3. Check that the file exists
if not input_file.is_file():
    raise FileNotFoundError(
        f"File not found: {input_file}"
    )

# 4. Uncompress Hatanaka
print("Uncompressing RINEX file...")

output_file = hatanaka.decompress_on_disk(input_file)

# 5. Show result
print("¡Uncompression completed!")
print(f"File generated: {output_file}")