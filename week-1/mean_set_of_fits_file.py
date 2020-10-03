from astropy.io import fits
import numpy as np

def mean_fits(fitsfiles):
  count = 0
  
  for fitsfile in fitsfiles:
    hdulist = fits.open(fitsfile)
    newdata = hdulist[0].data
    
    if count == 0:
      data = newdata
    else:
     data = data + newdata 
    count = count + 1

  data = data/count

  return data


if __name__ == '__main__':
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
