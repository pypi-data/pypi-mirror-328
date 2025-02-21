import numpy as np
from astropy.table import Table
import pandas as pd
import matplotlib.pyplot as plt
from astropy.io import fits

hdul = fits.open('output.fits')
print(hdul[7].data)