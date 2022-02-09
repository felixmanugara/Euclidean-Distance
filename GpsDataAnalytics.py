import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tabulate

class GpsDatafromsameLocation:

    def __init__(self, gpsDataFromCsv):
        self.data = pd.read_csv(gpsDataFromCsv, engine='python', parse_dates=['Dates'], dtype={"Latitude modul": np.float64, "Longitude modul": np.float64})
        #self.dataset = pd.DataFrame(self.data, index= range(1,len(self.data)))
        self.data.drop_duplicates(subset=['Latitude modul','Longitude modul','Sat count','Speed','Alt'], keep= False,inplace= True)
        self.data.index = range(1,40)
        # convert data to numpy array
        self.moduleArray = self.data.loc[:,['Latitude modul','Longitude modul']].to_numpy()
        self.referenceArray = np.array([-5.3721512,105.2500960],dtype=np.float64)
        #method call
        self.countingProcess(self.moduleArray,self.referenceArray)
        #print(self.data)

    def countingProcess(self,gpsModuleArray, gpsReferenceArray):
        self.dataProc = np.linalg.norm(gpsModuleArray - gpsReferenceArray , axis=1)
        #method call
        self.dataResult(self.dataProc)

    def dataResult(self, dataProcessed):
        data = dataProcessed * 111.322
        converttoMeters = data * 1000
        datainMeters = np.around(converttoMeters,2)

        self.dataCounted = datainMeters#.astype(np.int32)

        #print(self.dataCounted)
        self.finalDataTable(self.dataCounted,self.referenceArray,self.data)
        
    
    def finalDataTable(self, errorDistanceData, gpsReferenceData, datasetFromCsv):
        referenceCoordinate = pd.DataFrame(gpsReferenceData.reshape(1,2),columns=['Latitude Referensi','Longitude Referensi'],index = [1], dtype= np.float64)
        errorDistance = pd.DataFrame(errorDistanceData, columns=['Jarak Error (Meter)'], index= range(1,40))
        mergeData = pd.concat([referenceCoordinate,datasetFromCsv,errorDistance], axis=1)
        finalDataset = mergeData.fillna(method='ffill') # fill missing value 
        finalDataset.drop(columns=['Sat count','Speed','Dates','Alt'], inplace=True)
        print(tabulate.tabulate(finalDataset, tablefmt='psql', showindex=True, headers='keys'))
    
    def dataPlot(self):
        self.dataplot = sns.displot(self.dataCounted[:10], kde=True)
        self.dataplot.set(title ="Jarak Error sama Lokasi",
                          ylabel ="Frekuensi Data",
                          xlabel ="Jarak Error (Meter)")
        plt.grid(axis="y")
        plt.show()
    

class GpsDataFromDifferentLocation:
     
    
     def __init__(self,gpsDatafromCsv):
        self.data = pd.read_csv(gpsDatafromCsv, engine='python',dtype={"Latitude modul": np.float64, "Longitude modul": np.float64})
        self.data.index = range(1,11)
        # convert data to numpy array
        self.moduleArray = self.data.loc[:,['Latitude modul','Longitude modul']].to_numpy()
        self.referenceArray = self.data.loc[:,['Latitude referensi','Longitude referensi']].to_numpy()
        #print(self.data)
        #method call
        self.counting_process(self.moduleArray,self.referenceArray)

     def counting_process(self, gpsModuleArray, gpsReferenceArray):
        self.dataProc = np.linalg.norm(gpsModuleArray - gpsReferenceArray, axis=1)
        self.storeData(self.dataProc)
            
     def storeData(self, dataProcessed):
        data = dataProcessed * 111.322
        converttoMeters = data * 1000
        datainMeters = np.around(converttoMeters,2)
        self.dataCounted = datainMeters#.astype(np.int32)
        #print(self.dataCounted)
        self.dataframe(self.data,self.dataCounted)
        
        
     def dataframe(self, dataFrame, dataCounted):
        resultData = pd.DataFrame(dataCounted, index=range(1,11), columns=['Jarak Error (Meter)'])
        self.df = pd.concat([dataFrame,resultData], axis= 1, join='outer')
        print(tabulate.tabulate(self.df, tablefmt='psql', showindex=True, headers='keys'))

     
     def dataPlot(self):
        self.dataplot = sns.displot(self.dataCounted, kde=True)
        self.dataplot.set(title ="Perbandingan jarak error berbeda lokasi",
                          #yticks= range(5),
                          #xticks= range(1,30,5),
                          ylabel ="Frekuensi Data",
                          xlabel ="Jarak Error (Meter)")
        plt.grid(axis="y")
        plt.show()


def run(InputNumber:int):
    if InputNumber > 2:
        raise Exception("masukkan angka 1 atau 2")
    else:
        if InputNumber == 1:
            Analytics = GpsDatafromsameLocation('gpsdat.csv')
            Analytics.dataPlot()
        elif InputNumber == 2:
            Analytics = GpsDataFromDifferentLocation("DifferentLocation.csv")
            Analytics.dataPlot()

run(2)
