import matplotlib.pyplot as plt
import numpy as np
import math

# koordinat_mod from gps module reading
koordinat_mod =[[-5.3721453,105.2501265],
                [-5.3721573,105.2500973],
                [-5.3721093,105.2501245],
                [-5.3721382,105.2500378],
                [-5.3721327,105.2500537],
                [-5.3721107,105.2500453],
                [-5.3721357,105.2500975],
                [-5.3721415,105.2501023],
                [-5.3721390,105.2500798],
                [-5.3721660,105.2500765]]

# koordinat_ref being use for calculate error distance
koordinat_ref = [-5.3723438,105.2500923]

# numpy array
np_koor_mod = np.array(koordinat_mod)
np_koor_ref = np.array(koordinat_ref)

# euclidean distance formula
formula = np.linalg.norm(np_koor_mod - np_koor_ref, axis=-1)

# loop for storing calculations result
new_arr = []
for i in formula:
    result = i * 111.322
    km = result * 1000
    m = round(km,2)
    new_arr.append(m)

np_new_arr = np.array(new_arr)
print(np_new_arr)

average = np.mean(np_new_arr)
print(f"jarak error rata-rata adalah: {average:.2f} Meter")

frequency = [1,2,3,4]
tick_val = [20,21,22,23,24,25,26]
tick_lab = ['20m','21m','22m','23m','24m','25m','26m']
xlab = 'Error Distance'
ylab = 'Frequency'

plt.hist(np_new_arr,bins=6)

# plot customizations
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.xticks(tick_val,tick_lab)
plt.yticks(frequency)

plt.show()