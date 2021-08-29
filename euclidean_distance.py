import matplotlib.pyplot as plt
import numpy as np
import math

# koordinat_mod from gps module reading
def koordinat_GPS():
    gps_data =[[-5.3721453,105.2501265],
               [-5.3721573,105.2500973],
               [-5.3721093,105.2501245],
               [-5.3721382,105.2500378],
               [-5.3721327,105.2500537],
               [-5.3721107,105.2500453],
               [-5.3721357,105.2500975],
               [-5.3721415,105.2501023],
               [-5.3721390,105.2500798],
               [-5.3721660,105.2500765]]
    
    return gps_data
    
# koordinat_ref being use for calculate error distance
def koordinat_referensi():
    data_ref = [-5.3723438,105.2500923]
    return data_ref

gps_data = koordinat_GPS()
data_ref = koordinat_referensi()

# numpy array
def array(gps_array,ref_array):
    np_gps_arr = np.array(gps_array)
    np_ref_arr = np.array(ref_array)
    
    return np_gps_arr, np_ref_arr

np_gps_arr, np_ref_arr = array(gps_data,data_ref)

# euclidean distance formula
def counting_process():
    formula = np.linalg.norm(np_gps_arr - np_ref_arr, axis=-1)
    return formula

formula = counting_process()

# loop for storing calculations result
def store_data():
    new_arr = []
    for i in formula:
        result = i * 111.322
        km = result * 1000
        m = round(km,2)
        new_arr.append(m)

    np_new_arr = np.array(new_arr)
    print(np_new_arr)
    return np_new_arr

data_stored = store_data()

average = np.mean(data_stored)
print(f"jarak error rata-rata adalah: {average:.2f} Meter")

def data_plot(source):
    frequency = [1,2,3,4]
    tick_val = [20,21,22,23,24,25,26]
    tick_lab = ['20m','21m','22m','23m','24m','25m','26m']
    xlab = 'Error Distance'
    ylab = 'Frequency'

    # plot customizations
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xticks(tick_val,tick_lab)
    plt.yticks(frequency)
    
    plt.hist(source,bins=6)
    plt.show()

data_plot(data_stored)