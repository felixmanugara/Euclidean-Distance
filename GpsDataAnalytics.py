import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tabulate

class GpsDatafromsameLocation:

    def __init__(self, datafromcsv):
        self.dataset = pd.read_csv(datafromcsv)
        self.df = pd.DataFrame(self.dataset)
        # convert data to numpy array
        self.moduleArray = self.dataset.loc[:,['Latitude modul','Longitude modul']].to_numpy()
        self.referenceArray = self.dataset.loc[:,['Latitude referensi','Longitude referensi']].to_numpy()
       
    
class GpsDatafromdifferentLocation:
     
     def __init__(self,datafromCsv):
        self.dataset = pd.read_csv(datafromCsv)
        # convert data to numpy array
        self.moduleArray = self.data.loc[:,['Latitude modul','Longitude modul']].to_numpy()
        self.referenceArray = self.data.loc[:,['Latitude referensi','Longitude referensi']].to_numpy()
        

class DataProcess(GpsDatafromsameLocation,GpsDatafromdifferentLocation):

    def __init__(self, datafromcsv):
        super().__init__(datafromcsv)
        self.dataproc = np.linalg.norm(self.moduleArray - self.referenceArray, axis=1)
        # function call
        self.storeData(self.dataproc)
            
    def storeData(self, dataProcessed):
        data = dataProcessed * 111.322
        converttoMeters = data * 1000
        datainMeters = np.around(converttoMeters,2)
        self.dataCounted = datainMeters
        self.dataframe(self.dataCounted)

    def dataframe(self,errordistancedata):
        self.errordistance = pd.DataFrame(errordistancedata, columns=['Jarak Error (Meter)'])
        self.dataset = pd.concat([self.df,self.errordistance], axis=1)
        print(tabulate.tabulate(self.dataset, tablefmt='psql', showindex=True, headers='keys'))
        self.dataPlot()
    
    def dataPlot(self):
        self.dataplot = sns.displot(self.dataCounted, kde=True)
        self.dataplot.set(title ="Jarak Error sama Lokasi",
                          ylabel ="Frekuensi Data",
                          xlabel ="Jarak Error (Meter)")
        plt.grid(axis="y")
        plt.show()
    

DatasameLoc = DataProcess("newdata.csv")
DatadifferentLoc = DataProcess("DifferentLocation.csv")
#print(DataProcess.__dict__)