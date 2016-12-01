import soundDownload as SD
import numpy as np

queryText = ["violin","cello_note","bassoon","flute","trumpet_note", "snare_hit", "naobo", "daluo","mridangam_stroke","clarinet"]
tag=["single-note","good-sounds","tenuto","good-sounds","single-note","one-shot","qmul","qmul","sm-58","single-note"]
duration=(0,5)
API_Key='oRDjiagAmLlrlxnxwKs6MOqDCIlCa0Xi5H5mu1VH'
outputDir='downloaded/'

vec = np.arange(10)

for i in vec:
    SD.downloadSoundsFreesound(queryText = queryText[i], tag=tag[i], duration=duration, API_Key = API_Key, outputDir = outputDir, topNResults = 20, featureExt = '.json')
