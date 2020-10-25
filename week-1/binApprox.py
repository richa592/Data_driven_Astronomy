import numpy as np

def median_bins(values, B):
  mean = np.mean(values)
  std = np.std(values)
  left_bin = 0
  bins = np.zeros(B)
  bin_width = 2*std/B
  for value in values:
    if value < mean - std:
      left_bin += 1
    elif value < mean + std:
      bin = int((value - (mean - std))/bin_width)
      bins[bin] += 1

  return mean, std, left_bin, bins

