import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def table():
    # create dataframe from .csv
    data = pd.read_csv('gpsdat.csv',engine='python')
    #print(data)
    return data


def koordinat_GPS(df):
    np_gps_arr = pd.DataFrame(df).loc[:,['Latitude','Longitude']].to_numpy(dtype=np.float32)
    #print(np_gps_arr)
    np_ref_arr = np.array([-5.3723438,105.2500923]) 
    #print(np_ref_arr)
    
    return np_gps_arr, np_ref_arr
    
np_gps_arr, np_ref_arr = koordinat_GPS(table())


# euclidean distance formula
def counting_process(gps_data,ref_data):
    data_count = np.linalg.norm(gps_data - ref_data, axis=1)    
    return data_count

# loop for storing calculation result
def store_data(data_counted):
    new_arr = []
    for i in data_counted:
        result = i * 111.322
        km = result * 1000
        m = round(km,2)
        new_arr.append(m)

    np_new_arr = np.array(new_arr)
    #print(np_new_arr)
    return np_new_arr

data_stored = store_data(counting_process(np_gps_arr, np_ref_arr))

average = np.mean(data_stored)
average_value = (f"jarak error rata-rata adalah: {average:.2f} Meter")
print(average_value)

def data_plot(source):
    bins = 20
    xlab = 'Nilai Error Dalam Meter'
    ylab = 'Jumlah Data'
    color = '#ff7f50'

    # plot customizations
    plt.title("Selisih Jarak Error GPS")
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    plt.hist(source,bins=bins,edgecolor="black", alpha=0.8)
    plt.axvline(average,color=color,label='Nilai rata-rata',linewidth=2)
    plt.legend(loc='best')
    plt.show()
                        
data_plot(data_stored) 