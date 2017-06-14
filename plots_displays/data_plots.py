# -*- coding: utf-8 -*-
"""
Created on Thu May 2 15:33:00 2017

@author: p.cretu
"""

from matplotlib import pyplot
from scipy import signal
from comtypes.npsupport import numpy


class Plots():
    '''
    object to custom plot different data structures
    has as main attribute a matplotlib.pyplot object
    '''
    def __init__(self):
        self.plot = pyplot.plot


    def plotTwoArraySubplots(self, fileName, array1, array2):
        fig, ax = pyplot.subplots(nrows=2, ncols=1)
        pyplot.subplot(2, 1, 1)
        pyplot.plot(array1)
        pyplot.title('Data for file: '+ fileName)
        pyplot.subplot(2, 1, 2)
        pyplot.plot(array2)
        
        pyplot.show()

    def plotSpectrogramScipy(self, fileName, *args):
        f, t, Sxx = signal.spectrogram(*args)
#         f = numpy.log(f)
        Sxx = numpy.log(Sxx)
        max = numpy.amax(Sxx)
        min = numpy.amin(Sxx)
        pyplot.pcolormesh(t, f, Sxx)
#         pyplot.ylabel('Frequency [Hz]')
#         pyplot.xlabel('Time [sec]')
        pyplot.title('Spectogram, logarithmic, file: ' + fileName + '\n parameter: Acceleration')
#         pyplot.yscale('log')
#         pyplot.annotate(
#             "samplig rate 52 kHz, \nsegment length = sampling rate", xy=(1,1))
        pyplot.text(0, 0, 'samplig rate 52 kHz, \nsegment length = sampling rate', style='italic',
                    bbox={'facecolor':'white', 'alpha':0.8, 'pad':10})
        pyplot.colorbar()

        pyplot.show()
    
    def plotSpectrogramMplib(self, fileName, arrayData, sampligRate = None, param = ''):
        fft = numpy.fft.fft(arrayData)
        pyplot.subplot(3, 1, 1)
        pyplot.plot(arrayData)
        pyplot.title( param + ' from file: '+ fileName)
        pyplot.subplot(3, 1, 2)
        try:
            Pxx, freqs, t, im = pyplot.specgram(arrayData, NFFT= int(sampligRate[0]), Fs = int(sampligRate[0]), noverlap = 0)
        except TypeError:
            Pxx, freqs, t, im = pyplot.specgram(arrayData,  noverlap = 0)
        finally:    
            pyplot.title( param + ' Spectogram from file: '+ fileName + '\n with sampling rate '+ str(sampligRate) + ' and overlap ' + str(sampligRate))
            pyplot.colorbar()
            pyplot.subplot(3, 1, 3)
            pyplot.plot(freqs)
            pyplot.show()
            
    def plotmesh(self, data, name):
        fig, ax = self.plot.subplots()
        self.pcolormesh(numpy.flipud(data))
        self.colorbar()
#         self.winter()
        self.title('Gear Noise Matrix (Measure: Order Cut ' + name + ')\n\n')
        self.xticks( (numpy.arange(1.5, len(data[0])) ) , ['LR %i'%w for w in range(1,len(data[0])) ] )
        self.yticks( numpy.arange(0.5, len(data)), ['FR %i'%w for w in range(len(data) - 1, 0, -1) ] ) 
        self.ylabel('Festrad (FR)')
        self.xlabel('Losrad (LR)')
        ax.xaxis.tick_top()
        self.savefig('OrderCut' + name + '.png', dpi=300)
        self.show()
        

    def areKeys(self, hdf5File):
        try:
            listOfKeys = list(hdf5File.keys())
            return listOfKeys
        except AttributeError as e:
            print(self.plotOneGear.__qualname__)
            print(e)
            return 0

    def plotOneGear(self, hdf5File, gear):
        listOfKeys = self.areKeys(hdf5File)
        if listOfKeys != 0:
            if gear.find('FR') > -1:
                length = 6 # nr of FR gears
            else:
                length = 11 #nr of LR gears
            
            for j in range(1, length):
                legend = list()
                self.figure(j-1)
                for i in range(0, len(listOfKeys), 2):
                    if listOfKeys[i].find(gear + str(j)) > 0:
                        legend.append(listOfKeys[i+1])
                        self.plot(hdf5File[listOfKeys[i+1]].value, hdf5File[listOfKeys[i]].value, hold = True)
                        self.legend(legend, fontsize=12, loc='best')
                        self.title('Order Cuts for Gear ' + gear + str(j))
                        self.xlabel('Speed[rpm]')
                        self.ylabel('L[dB]')
                    
                    
            self.show()
            
            
    def plotOneGearSecond(self, hdf5File, gears):
        listOfKeys = self.areKeys(hdf5File)
        count = 0
        if listOfKeys != 0:
            for gear in gears:
                legend = list()
                self.figure(count)
                for i in range(0, len(listOfKeys), 2):
                    if listOfKeys[i].find(gear) > 0:
                        legend.append(listOfKeys[i+1])
                        self.plot(hdf5File[listOfKeys[i+1]].value, hdf5File[listOfKeys[i]].value, hold = True)
                        self.legend(legend, fontsize=12, loc='best')
                        self.title('Order Cuts for Gear ' + gear )
                        self.xlabel('Speed[rpm]')
                        self.ylabel('L[dB]')
                count += 1
                    
            self.plot.show()

    def plotOneOrderCut(self, hdf5File, orderCuts):
        listOfKeys = self.areKeys(hdf5File)
        if listOfKeys != 0:
            j = 0
            for oc in orderCuts:
                legend = list()
                self.figure(j)
                for i in range(0, len(listOfKeys), 2):
                    if listOfKeys[i].find(oc) > 0 and listOfKeys[i].find('PH1') > 0 :
                        legend.append(listOfKeys[i+1])
                        self.plot(hdf5File[listOfKeys[i+1]].value, hdf5File[listOfKeys[i]].value, hold = True)
                        self.legend(legend, fontsize=12, loc='best')
                        self.title('Order Cut ' + oc + ' for Gear ' + listOfKeys[0].split(' ')[0])
                        self.xlabel('Speed[rpm]')
                        self.ylabel('L[dB]')
                j += 1
                    
            self.show()
            
    def plotOneOrderCutSecond(self, hdf5File, orderCuts):
        listOfKeys = self.areKeys(hdf5File)
        if listOfKeys != 0:
            j = 0
            for oc in orderCuts:
                legend = list()
                self.figure(j)
                for i in range(0, len(listOfKeys), 2):
                    if listOfKeys[i].find(oc) > 0 and listOfKeys[i].find('PH1') > 0 :
                        legend.append(listOfKeys[i+1])
                        self.plot(hdf5File[listOfKeys[i+1]].value, hdf5File[listOfKeys[i]].value, hold = True)
                        self.legend(legend, fontsize=12, loc='best')
                        self.title('Order Cut ' + oc + ' for Gear ' + listOfKeys[0].split(' ')[0])
                        self.xlabel('Speed[rpm]')
                        self.ylabel('L[dB]')
                j += 1
                    
            self.show()

