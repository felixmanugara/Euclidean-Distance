import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

class GpsDataAnalytics:

    def __init__(self, GPSData):
        self.data = pd.read_csv(GPSData, engine='python', parse_dates=['Dates'])
        self.dataset = pd.DataFrame(self.data, index= range(1,len(self.data)))
        self.dataset.drop_duplicates(subset=['Latitude modul','Longitude modul','Sat count','Speed','Alt'], keep= False,inplace= True)
        self.dataset.index = range(1, len(self.dataset)+1)
        #print(dataset)

    def extractData(self):
        self.npGpsModuleArray = pd.DataFrame(self.dataset).loc[:,['Latitude modul','Longitude modul']].to_numpy(dtype=np.float32)
        self.npGpsReferenceArray = np.array([-5.3721512,105.2500960])
        #print(self.npGpsModuleArray)
        #print(self.npGpsReferenceArray)

    def countingProcess(self):
        self.dataProc = np.linalg.norm(self.npGpsModuleArray - self.npGpsReferenceArray, axis=1)
        #print(self.dataProc)

    def dataResult(self):
        resultArray = []
        for i in self.dataProc:
            multiplication = i * 111.322
            km = multiplication * 1000
            m = round(km, 2)
            resultArray.append(m)

        self.resultArrayData = np.array(resultArray, dtype=np.int32)
        #print(self.resultArrayData)
    
    def finalDataTable(self):
        referenceCoordinate = pd.DataFrame(self.npGpsReferenceArray.reshape(1,2),columns=['Latitude Referensi','Longitude Referensi'])
        referenceCoordinate.index= range(1,len(referenceCoordinate)+1)
        # index using data length
        self.errorDistanceData = pd.DataFrame(self.resultArrayData, columns=['Jarak Error (Meter)'], index= range(1,len(self.resultArrayData)+1))
        mergeData = pd.concat([referenceCoordinate,self.dataset,self.errorDistanceData], axis=1)
        finalDataset = mergeData.fillna(method='ffill') # fill missing value 
        finalDataset.drop(columns=['Sat count','Speed','Dates','Alt'], inplace=True)
        #print(finalDataset)
    
    def dataPlot(self):
        dataValue = self.resultArrayData
        minVal = min(self.resultArrayData)
        maxVal = max(self.resultArrayData)
        average = np.median(self.resultArrayData)
        binCount = math.ceil((maxVal - minVal) / 3)
        xLabel = "Nilai error dalam Meter"
        yLabel = "Jumlah Data"
        color = "#ff7f50"

        #plot customizations
        plt.title("Selisih Jarak Error GPS")
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.yticks(np.arange(0,22,2))

        plt.hist(dataValue,bins=binCount,edgecolor="black", alpha=0.8)
        plt.axvline(average,color=color,label='Nilai rata-rata',linewidth=2)
        plt.grid(color='grey',alpha=0.4)
        plt.legend(loc='best')
        plt.show()
    
    def run(self):
        self.extractData()
        self.countingProcess()
        self.dataResult()
        self.finalDataTable()
        self.dataPlot()



Analytics = GpsDataAnalytics('gpsdat.csv')
Analytics.run()

