import numpy as np
import essentia.standard as esst
import essentia.pool
from os import listdir

def featureExtraction(soundfiles):

	#extractor = esst.LowLevelSpectralExtractor()
	extractor = esst.Extractor(dynamics = True,
    					dynamicsFrameSize = 88200,
        				dynamicsHopSize = 44100,
        				highLevel = True,
        				lowLevel = True,
        				lowLevelFrameSize = 2048,
        				lowLevelHopSize = 1024,
        				midLevel = True,
        				namespace = "",
        				relativeIoi = False,
        				rhythm = True,
        				sampleRate  = 44100,
        				tonalFrameSize  = 4096,
        				tonalHopSize = 2048,
						tuning = True)
	
	#soundfiles = listdir(inputPath)

	for file, outPath in soundfiles:

		audioLoader = esst.MonoLoader(filename=file)
		audio = audioLoader()
		pool = essentia.Pool()
		pool = extractor(audio)
		aggPool = esst.PoolAggregator()(pool)
		esst.YamlOutput(filename = outPath + 'features.json', format='json')(aggPool)
		print (file + ' exported')


path = '/home/aspma/Desktop/ASPMA_A10/downloaded/'

instruments = listdir(path)

soundfilesList = []
for instrument in instruments:
	sounds = listdir(path+instrument+'/')
	for sound in sounds:
		if '.txt' not in sound:

			files = listdir(path+instrument+'/'+sound)
			audio=''
			for file in files:
				if '.mp3' in file: audio=file

			soundfilesList.append([path+instrument+'/'+sound+'/'+audio,path+instrument+'/'+sound+'/features/'])

#print (soundfilesList)

featureExtraction(soundfilesList)
