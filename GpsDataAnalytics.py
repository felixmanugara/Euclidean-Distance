import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import tabulate

class ReadDataFromCSV:

    def __init__(self, gpsDataFromCsv):
        self.data = pd.read_csv(gpsDataFromCsv, engine='python', parse_dates=['Dates'], dtype={"Latitude modul": np.float64, "Longitude modul": np.float64})
        self.dataset = pd.DataFrame(self.data, index= range(1,len(self.data)))
        self.dataset.drop_duplicates(subset=['Latitude modul','Longitude modul','Sat count','Speed','Alt'], keep= False,inplace= True)
        self.dataset.index = range(1,40)
        #method call
        self.extractData(self.dataset)
        #print(dataset)


    def extractData(self,datasetFromCsv):
        self.moduleArray = pd.DataFrame(datasetFromCsv).loc[:,['Latitude modul','Longitude modul']].to_numpy(dtype=np.float32)
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
        
    
    def finalDataTable(self, errorDistanceData, gpsReferenceData, datasetFromCsv):
        index = list(range(1,40))
        referenceCoordinate = pd.DataFrame(gpsReferenceData.reshape(1,2),columns=['Latitude Referensi','Longitude Referensi'],index = [1], dtype= np.float64)
        errorDistance = pd.DataFrame(errorDistanceData, columns=['Jarak Error (Meter)'], index= index)
        mergeData = pd.concat([referenceCoordinate,datasetFromCsv,errorDistance], axis=1)
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
    

class DataFromList:
     __gpsModuleData = [[-5.3741278,105.2514637],
                        [-5.3727553,105.2522518],
                        [-5.3732140,105.2508992],
                        [-5.3704840,105.2496747],
                        [-5.3728913,105.2455960],
                        [-5.3635015,105.2456365],
                        [-5.3656357,105.2443033]]
    
     __gpsReferenceData = [[-5.3741387,105.2514740],
                           [-5.3727958,105.2522109],
                           [-5.3732511,105.2508500],
                           [-5.3702449,105.2497647],
                           [-5.3729377,105.2456338],
                           [-5.3634703,105.2455758],
                           [-5.3657855,105.2442934]]
    
     def __init__(self):
         self.gpsModuleArray = np.array(DataFromList.__gpsModuleData)
         self.gpsReferenceArray = np.array(DataFromList.__gpsReferenceData)

         self.counting_process(self.gpsModuleArray,self.gpsReferenceArray)


     def counting_process(self, gpsModuleArray, gpsReferenceArray):
        self.dataProc = np.linalg.norm(gpsModuleArray - gpsReferenceArray, axis=1)
        self.storeData(self.dataProc)
            
     def storeData(self, dataProcessed):
        dataResult = []
        for i in dataProcessed:
            result = i * 111.322
            km = result * 1000
            m = round(km,2)
            dataResult.append(round(m))

        self.dataCounted = np.array(dataResult)
        self.dataframe(self.gpsModuleArray,self.gpsReferenceArray,self.dataCounted)
        
        
     def dataframe(self, gpsModuleArray, gpsReferenceArray, dataCounted):
        index = list(range(1,8))
        referenceData = pd.DataFrame(gpsReferenceArray,index= index, columns=['Latitude (ref)', 'Longitude (ref)'], dtype=np.float64)
        gpsData = pd.DataFrame(gpsModuleArray, index= index, columns=['Latitude (GPS)', 'Longitude (GPS)'], dtype=np.float64)
        resultData = pd.DataFrame(dataCounted, index= index, columns=['Jarak Error (Meter)'])
        self.df = pd.concat([referenceData,gpsData,resultData], axis= 1, join='outer')
        print(tabulate.tabulate(self.df, tablefmt='psql', showindex=True, headers='keys'))


     def dataPlot(self):
        average = np.median(self.dataCounted)
        xlab = 'Selisih jarak error dalam meter'
        ylab = 'Jumlah Data'
        color = "#ff7f50"

        # plot customizations
        plt.title('Jarak Error GPS')
        plt.xlabel(xlab)
        plt.ylabel(ylab)
        plt.yticks(range(1,4))
    
        plt.hist(self.dataCounted,edgecolor="black")
        plt.axvline(average,color=color,label="nilai rata-rata",linewidth=2)
        plt.legend(loc="best")
        plt.show()

Analytics1 = ReadDataFromCSV('gpsdat.csv')
Analytics2 = DataFromList()
#Analytics.dataPlot()
#GpsDataAnalytics.dataPlot()
