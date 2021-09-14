import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def table():
    # create dataframe from .csv
    data = pd.read_csv('gpsdat.csv',engine='python', header=None, names=['Latitude','Longitude','Sat count','Speed','Altitude','Date'], parse_dates=True)
   
    return data

df = table()

def koordinat_GPS():
    np_gps_arr = pd.DataFrame(df).iloc[:,[0,1]].to_numpy(dtype=np.float64)
    np_ref_arr = np.array([-5.3723438,105.2500923]) 
    #print(np_ref_arr)
    
    return np_gps_arr, np_ref_arr
    
np_gps_arr, np_ref_arr = koordinat_GPS()


# euclidean distance formula
def counting_process():
    formula = np.linalg.norm(np_gps_arr - np_ref_arr, axis=1)    
    return formula

formula = counting_process()

# loop for storing calculation result
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