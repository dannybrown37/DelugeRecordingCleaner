import glob
import os

# Simple but effective bulk renaming tool 


# Rename files based on patterns below
for filename in glob.glob( "*.wav"):
    os.rename(filename, filename.replace("OOT_", ""))

# Rename directories based on patterns below
for dn in os.listdir():
    os.rename(dn, dn.replace("OOT_", ""))
