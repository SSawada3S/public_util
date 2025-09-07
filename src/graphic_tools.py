import numpy as np

def round_sig(x, sig=2):
    if x == 0:
        return 0
    return np.round(x, sig - int(np.floor(np.log10(abs(x)))) - 1)

def get_bins(list_of_numbers:list) -> list:
  array=np.array(list_of_numbers)
  diff=np.percentile(array, 95) - np.percentile(array, 5) 
  scale=10**np.round( np.log10(np.abs( diff )) - 1) 
  min = 10*round(np.percentile(array, 10) / scale)
  max = 10*round(np.percentile(array, 90) / scale)
  for i in range(1,100):
    bins=[v* (scale*0.1) for v in range(min, max, 5*i)]
    if len(bins) > 10:
      i+=1
    else:
      break
  return np.vectorize(round_sig)(bins, sig=2)

def ratio_in_range(arr, low, high):
  arr = np.asarray(arr)
  mask = (arr >= low) & (arr < high)
  return mask.mean()

def array_to_prob_distribution(array):
  bins=get_bins(arr)
  di={}
  for high, low in zip(bins[1:], bins[:-1]):
    di[low, high]=ratio_in_range(arr, low, high) 
  return di
