import numpy as np
# import essentia.standard as esst
# import essentia.pool
from os import listdir, walk
import soundAnalysis_mod as SA
import json
import parseJSONkeys as newClustering

# def featureExtraction(soundfiles):
#     # extractor = esst.LowLevelSpectralExtractor()
#     extractor = esst.Extractor(dynamics = False,
#                                                 dynamicsFrameSize = 88200,
#                                                 dynamicsHopSize = 44100,
#                                                 highLevel = False,
#         			         lowLevel = True,
#         			         lowLevelFrameSize = 2048,
#         			         lowLevelHopSize = 1024,
#         			         midLevel = True,
#         			         namespace = "",
#         			         relativeIoi = False,
#         			         rhythm = False,
#         			         sampleRate  = 44100,
#         			         tonalFrameSize  = 4096,
#         			         tonalHopSize = 2048,
# 			         tuning = True)
#
# 	#soundfiles = listdir(inputPath)
#     for file in soundfiles:
#
#         path1= '/Users/helena/Desktop/SMC/ASP/sms-tools/workspace/A10/code/downloaded/'
#         name=file[70:-4] + '_features.json'
#         outPath = path1 + 'features/' + name
#         print file
#         audioLoader = esst.MonoLoader(filename=file)
#         audio = audioLoader()
#         pool = essentia.Pool()
#         pool = extractor(audio)
#         aggPool = esst.PoolAggregator()(pool)
#         output = esst.YamlOutput(filename = outPath, format='json')
#         output(aggPool)
#         print (outPath + ' exported')



path = '/Users/helena/Desktop/SMC/ASP/sms-tools/workspace/A10/code/downloaded/'

instruments_ = listdir(path)
instruments=[]
for i in instruments_:
    if i == 'features': continue
    instruments.append(i)

soundfilesList = []
for instrument in instruments:
    if '.DS'  not in instrument and 'txt' not in instrument:
	sounds = listdir(path+instrument+'/')
	for sound in sounds:
		if '.txt'  not in sound and  '.DS' not in sound:

			files = listdir(path+instrument+'/'+sound)
			audio=''
			for file in files:
				if '.mp3' in file: audio=file

			soundfilesList.append(path+instrument+'/'+sound+'/'+audio)

#print (soundfilesList)

# featureExtraction(soundfilesList)

# Clustetring

# see descriptors
# path = '/Users/helena/Desktop/SMC/ASP/sms-tools/workspace/A10/code/downloaded/features/cello_note/247485/247485_6552981-lq_features.json'
# fDict = json.load(open(path,'r'))
# descriptors = fDict.keys()
# print descriptors


newClustering.clusterSounds('downloaded/features/', nCluster=10, descInput=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])




