import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import tabulate

class GpsDataAnalytics:

    def __init__(self, gpsData):
        self.data = pd.read_csv(gpsData, engine='python', parse_dates=['Dates'])
        self.dataset = pd.DataFrame(self.data, index= range(1,len(self.data)))
        self.dataset.drop_duplicates(subset=['Latitude modul','Longitude modul','Sat count','Speed','Alt'], keep= False,inplace= True)
        self.dataset.index = range(1, len(self.dataset)+1)
        #method call
        self.extractData(self.dataset)
        #print(dataset)


    def extractData(self,dataFrame):
        self.moduleArray = pd.DataFrame(dataFrame).loc[:,['Latitude modul','Longitude modul']].to_numpy(dtype=np.float32)
        self.referenceArray = np.array([-5.3721512,105.2500960])
        #print(self.npGpsModuleArray)
        #print(self.npGpsReferenceArray)
        #method call
        self.countingProcess(self.moduleArray,self.referenceArray)

    def countingProcess(self,gpsModuleArray, gpsReferenceArray):
        self.dataProc = np.linalg.norm(gpsModuleArray - gpsReferenceArray , axis=1)
        #method call
        self.dataResult(self.dataProc)

    def dataResult(self, processedData):
        _resultArray = []
        for i in processedData:
            _multiplication = i * 111.322
            _km = _multiplication * 1000
            _m = round(_km, 2)
            _resultArray.append(round(_m))

        self.resultArrayData = np.array(_resultArray)
        #print(self.resultArrayData)
        self.finalDataTable(self.resultArrayData,self.referenceArray,self.dataset)
        
    
    def finalDataTable(self, errorDistanceData, gpsReferenceData, dataFrame):
        referenceCoordinate = pd.DataFrame(gpsReferenceData.reshape(1,2),columns=['Latitude Referensi','Longitude Referensi'])
        referenceCoordinate.index= range(1,len(referenceCoordinate)+1)
        # index using data length
        self.errorDistanceData = pd.DataFrame(errorDistanceData, columns=['Jarak Error (Meter)'], index= range(1,len(errorDistanceData)+1))
        mergeData = pd.concat([referenceCoordinate,dataFrame,self.errorDistanceData], axis=1)
        finalDataset = mergeData.fillna(method='ffill') # fill missing value 
        finalDataset.drop(columns=['Sat count','Speed','Dates','Alt'], inplace=True)
        print(tabulate.tabulate(finalDataset, tablefmt='psql', showindex=True, headers='keys'))
    
    def dataPlot(self):
        dataValue = self.resultArrayData
        minVal = min(self.resultArrayData)
        maxVal = max(self.resultArrayData)
        average = np.median(self.resultArrayData)
        _binCount = math.ceil((maxVal - minVal) / 3)
        _xLabel = "Nilai error dalam Meter"
        _yLabel = "Frekuensi Data"
        color = "#ff7f50"

        #plot customizations
        plt.title("Selisih Jarak Error GPS")
        plt.xlabel(_xLabel)
        plt.ylabel(_yLabel)
        #plt.yticks(np.arange(0,22,2))

        plt.hist(dataValue,bins=_binCount,edgecolor="black", alpha=0.8)
        plt.axvline(average,color=color,label='Nilai rata-rata',linewidth=2)
        plt.grid(color='grey',alpha=0.4)
        plt.legend(loc='best')
        plt.show()
    
    #def run(self):
        #self.extractData()
        #self.countingProcess()
        #self.dataResult()
        #self.finalDataTable()
        #self.dataPlot()


Analytics = GpsDataAnalytics('gpsdat.csv')
#Analytics.dataPlot()

