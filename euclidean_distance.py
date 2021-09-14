import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

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
    formula = np.linalg.norm(np_gps_arr - np_ref_arr, axis=1)
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
average_value = (f"jarak error rata-rata adalah: {average:.2f} Meter")
print(average_value)

def dictionary():
    d = dict(enumerate(np_gps_arr.flatten(),1))
    print(d)

#dictionary()

def data_plot(source):
    bins = [20.5,22.5,24.5,26.5]
    xlab = 'Nilai Error [dalam Meter]'
    ylab = 'Jumlah Data'
    color = '#ff7f50'

    # plot customizations
    plt.title("Selisih Jarak Error GPS")
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    plt.hist(source, bins=bins, edgecolor="black", alpha=0.8)
    plt.axvline(average,color=color,label='Nilai rata-rata',linewidth=2)
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

data_plot(data_stored)