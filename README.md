# Hatanaka2Rinex

Hatanaka2Rinex is a little Python script (ver 3.14.3) to transform a GNSS .crx file into a .rnx file

Script language: English
Help documents languages: English, Spanish

## Previous considerations

Used Visual Studio Code (VS) in Windows 11 to write the script and Python version 3.14.3.

Need Python version 3.6 or above.

It is used the hatanaka package in the script. No need of previous install of hatanaka at first.

If this happens, use in Terminal (bash or VS):

```bash
pip install hatanaka
```

## Usage

1. Download folder "Hatanaka2Rinex_CRX2RNX".
2. Place the .crx file to transform in the same folder as the Python script "decompress_rinex.py".
3. Open "decompress_rinex.py" in any compiler (VS Code, for example).
4. Change the value of the variable "file_crx" as a string with the complete name of the .crx file (that is, including the .crx extension)

```python
# 0. File to convert inside the same folder as decompress_rinex
file_crx = "BIRG00ITA_R_20232060000_01D_30S_MO.crx"
```
5. In Terminal, run:

```python
python decompress_rinex.py
```

If the file if generated properly you will see a message in Terminal "¡Uncompression completed!".


## Notes

If using Linux I am not familiarize with process but is quite similar.

There is an example made with "BIRG00ITA_R_20232060000_01D_30S_MO.crx" file


## Help

- If needed to install the package, write in Terminal:

```bash
pip install hatanaka
```

To check it, use in Terminal:

```bash
pytest --pyargs hatanaka
```

- If, after using the script there is a Warning in the compiler but still you can execute it, sometimes you have to restart the analysis in VS code or to select the correct interpreter. Take a look to the next fast guides to solve it

See:

"Help_Hatanaka_Import_Warning_VSCode_Guide_EN.pdf"

for English version.

See
"Ayuda_Guia_Aviso_Hatanaka_VSCode_ES.pdf"

for Spanish version.
