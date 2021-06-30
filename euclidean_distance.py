import numpy as np
import math

# koordinat_mod merupakan koordinat hasil pembacaan modul GPS

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

# koordinat_ref merupakan koordinat referensi
# yang digunakan untuk mengukur selisih jarak error dari GPS

koordinat_ref = [-5.3723438,105.2500923]

np_koor_mod = np.array(koordinat_mod)
np_koor_ref = np.array(koordinat_ref)

formula = np.linalg.norm(np_koor_mod - np_koor_ref, axis=-1)

new_arr = []
for i in formula:
    result = i * 111.322
    km = result * 1000
    m = round(km,2)
    new_arr.append(m)

np_new_arr = np.array(new_arr)
print(np_new_arr)

# menghasilkan rata - rata dari jarak error
average = np.mean(np_new_arr)
print("jarak error rata-rata adalah: " + str(round(average,2)) + " meter")
