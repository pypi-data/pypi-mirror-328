import sys
import os
import glob

bins = [f for f in sorted(glob.glob(f'CHANTER/Miles_Atlas/Chabrier_IMF/*ised'))]


for i in bins:
    os.system('$bc03/ascii_ised ~/Desktop/research/' + i)