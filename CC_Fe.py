# Import required libraries
#import scipy.stats as stats
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics
#from scipy.stats import shapiro
import os

class AnomalyDetector: 

 def loadData():
    dirname = os.path.dirname(os.path.realpath(__file__))
    root_path = os.path.join(dirname, 'datos/dataset_Fe.xlsx')
    df = pd.read_excel(root_path)
    return df

 if __name__ == '__main__':
    
 
    cantidad = int(input("¿Cuanto valores son de calibración?: "))
    print(cantidad )
    
    df = loadData()
    print('\nSample data loaded.')
    
    df = df.drop('day', axis = 1)

    trainIndexLimit = cantidad
    trainSet = df[:trainIndexLimit]
    testSet = df[trainIndexLimit:]
    print(trainSet)
    

    
    mean = statistics.mean(trainSet['amount'])
    sigma = trainSet['amount'].std()
  
    
    
    print(f"Mean(𝑥̅): {mean}")
    print(f"Std(𝜎):  {sigma}")
   

    x=df['amount']
    rango_movil=df['Rm']
    
    # Get and append moving ranges
    
 MR_cal= trainSet['Rm'] 
 x_cal= trainSet['amount']

 data_cal = pd.concat([x_cal,MR_cal], axis=1)
#print(data_cal)




# Plot x and mR charts
 fig, axs = plt.subplots(2, figsize=(15,15), sharex=True)




# x chart
 axs[0].plot(x, linestyle='-', marker='o', color='black')
 axs[0].axhline(mean, color='blue')

 axs[0].axhline(mean + 3*statistics.mean(data_cal ['Rm'][1:len(data_cal ['Rm'])])/1.128, color = 'red', linestyle = 'dashed')
 axs[0].axhline(mean - 3*statistics.mean(data_cal['Rm'][1:len(data_cal['Rm'])])/1.128, color = 'red', linestyle = 'dashed')
 axs[0].axhline(mean + 2*statistics.mean(data_cal['Rm'][1:len(data_cal['Rm'])])/1.128, color = 'green', linestyle = 'dashed')
 axs[0].axhline(mean - 2*statistics.mean(data_cal['Rm'][1:len(data_cal['Rm'])])/1.128, color = 'green', linestyle = 'dashed')
 axs[0].axhline(mean + 1*statistics.mean(data_cal['Rm'][1:len(data_cal['Rm'])])/1.128, color = 'yellow', linestyle = 'dashed')
 axs[0].axhline(mean - 1*statistics.mean(data_cal['Rm'][1:len(data_cal['Rm'])])/1.128, color = 'yellow', linestyle = 'dashed')
 axs[0].set_title('Individual Chart - Fe')
 axs[0].set(xlabel='Unit', ylabel='Value')


 



# mR chart
 axs[1].plot(rango_movil, linestyle='-', marker='o', color='black')
 axs[1].axhline(statistics.mean(data_cal['Rm']), color='blue')
 axs[1].axhline(statistics.mean(data_cal['Rm'])* 3.267, color='red', linestyle ='dashed')
#  axs[1].axhline(statistics.mean(data_cal['Rm'])* 1.628, color='green', linestyle ='dashed')
# axs[1].axhline(1*3.267, color='yellow', linestyle ='dashed')
 axs[1].set_ylim(bottom=0)
 axs[1].set_title('mR Chart - Fe')
 axs[1].set(xlabel='Unit', ylabel='Range')
 
 
 
 



 plt.savefig('datos/Fe-Xi-Rm')
 
 
    