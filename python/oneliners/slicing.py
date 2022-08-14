import numpy as np

inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

#get second value of second index where first value is above 100
superstars = inst[inst[:,0].astype(float) > 100, 1]
print(superstars)

a = np.array([4]*16)
a[8::] = [42]*8
a[1:8:2] = 16
print(a)
