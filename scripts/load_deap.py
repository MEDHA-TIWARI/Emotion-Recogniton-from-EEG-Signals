# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:33:28 2019

@author: Akshat
"""


import os
import sys
import numpy as np
import scipy.io as sio


chan = ['Fp1','AF3','F3','F7','FC5','FC1','C3','T7','CP5','CP1','P3','P7','PO3','O1','Oz','Pz','Fp2','AF4','Fz','F4','F8','FC6','FC2','Cz','C4','T8','CP6','CP2','P4','P8','PO4','O2']
nLabel, nTrial, nUser, nChannel, nTime  = 4, 40, 2, 32, 8064
print ("Program started \n")
fout_labels0 = open("labels_0.dat",'w')
fout_labels1 = open("labels_1.dat",'w')
fout_labels2 = open("labels_2.dat",'w')
fout_labels3 = open("labels_3.dat",'w')


for i in range(nUser):#4, 40, 32, 32, 8064
	if i < 10:
		name = '%0*d' % (2,i+1)
	else:
		name = i+1
	fname = "s"+str(name)+".mat"
	x = sio.loadmat(fname)
	print (fname)
	for tr in range(nTrial):
		fout_data = open("features_raw.csv",'w')
		for ch in chan:
				if ch!= 'O2':
						fout_data.write(ch+",")
				else:
						fout_data.write(ch)
		fout_data.write("\n")
		for dat in range(nTime):
			for ch in range(nChannel):
				if ch <32:
					if ch == 31:
						fout_data.write(str(x['data'][tr][ch][dat]));	
					else:					
						fout_data.write(str(x['data'][tr][ch][dat])+",");
			fout_data.write("\n");
		fout_labels0.write(str(x['labels'][tr][0]) + "\n");
		fout_labels1.write(str(x['labels'][tr][1]) + "\n");
		fout_labels2.write(str(x['labels'][tr][2]) + "\n");
		fout_labels3.write(str(x['labels'][tr][3]) + "\n");
		fout_data.close()
        #Normalizing the data between [0,1]
		array = np.genfromtxt('features_raw.csv',delimiter=',',skip_header=1)
		maximum=array[:, 1:].max()
		minimum=array[:, 1:].min()
		#normalise all data in the array except the first value of each row
		a = (array[:,1:] - minimum)/(maximum - minimum)
		np.savetxt("features_raw.csv", a, delimiter=",", fmt='%s')
		#os.system('python entropy1.py')
		print ("user "+ str(i+1)+" trail"+ str(tr+1))
fout_labels0.close()
fout_labels1.close()
fout_labels2.close()
fout_labels3.close()
print ("\n"+"Print Successful")