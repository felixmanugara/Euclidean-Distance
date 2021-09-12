import matplotlib.pyplot as plt
import numpy as np
import math

# koordinat_mod from gps module reading
def koordinat_GPS():
    gps_data =[[-5.3741278,105.2514637],
               [-5.3727553,105.2522518],
               [-5.3732140,105.2508992],
               [-5.3704840,105.2496747],
               [-5.3728913,105.2455960],
               [-5.3635015,105.2456365],
               [-5.3656357,105.2443033]]
    
    return gps_data
    
# koordinat_ref being use for calculate error distance
def koordinat_referensi():
    data_ref = [[-5.3741387,105.2514740],
                [-5.3727958,105.2522109],
                [-5.3732511,105.2508500],
                [-5.3702449,105.2497647],
                [-5.3729377,105.2456338],
                [-5.3634703,105.2455758],
                [-5.3657855,105.2442934]]
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
print(f"jarak error rata-rata adalah: {average:.2f} Meter")

def data_plot(source):
    bins = [1.5, 3.5, 5.5, 7.5, 9.5, 11.5, 13.5, 15.5, 17.5]
    xlab = 'Selisih jarak error dalam meter'
    ylab = 'Jumlah Data'
    color = "#ff7f50"

    # plot customizations
    plt.title('Jarak Error GPS')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.yticks(range(1,4))
    
    plt.hist(source,bins=bins,edgecolor="black")
    plt.axvline(average,color=color,label="nilai rata-rata",linewidth=2)
    plt.legend(loc="best")
    plt.show()

data_plot(data_stored)
