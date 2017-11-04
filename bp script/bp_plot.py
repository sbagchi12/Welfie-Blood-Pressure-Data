import matplotlib.pyplot as plt
import numpy as np
import time,csv,sys,os

bpFolder = sys.argv[1]
rate = sys.argv[2]
outputFolder = sys.argv[3]

txtFormat = ".txt"	

for bp in os.listdir(bpFolder):

        if bp.find(txtFormat) == -1 :
        	continue

        with open(bpFolder+bp, 'r') as f:
              reader = csv.reader(f)
              pressure_series = list(reader)

        blood_pressure = []

        with open(outputFolder+'/'+os.path.splitext(bp)[0]+'.csv', 'w') as f2:
                                f2.write('timestamp(seconds)' + ',' + 'value' + os.linesep)
                                
        for i in range(len(pressure_series)):

                try:
                        pressure = float(pressure_series[i][0])
                        blood_pressure.append(pressure)
                        time = float(i)/float(rate)
                        with open(outputFolder+'/'+os.path.splitext(bp)[0]+'.csv', 'a') as f2:
                                f2.write(str(time)+','+ str(pressure) + os.linesep)
                except:
                        print "Incorrect pressure data ", pressure_series[i][0]
                        continue
                
        plt.plot(blood_pressure)
        plt.xlabel('Samples')
        plt.ylabel('Pressure in mmHg')
        plt.savefig(outputFolder+'/'+os.path.splitext(bp)[0]+'.jpg')
        plt.clf()
