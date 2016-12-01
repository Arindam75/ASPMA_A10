import soundDownload as SD

queryText = ["violin","cello note","bassoon","flute","trumpet note", "snare hit", "naobo", "daluo","mridangam stroke","clarinet"]
tag=["single-note","good-sounds","tenuto","good-sounds","single-note","one-shot","qmul","qmul","sm-58","single-note"]
duration=(0,5)
API_Key='oRDjiagAmLlrlxnxwKs6MOqDCIlCa0Xi5H5mu1VH'
outputDir='testDownload/'



SD.downloadSoundsFreesound(queryText = queryText, tag=tag, duration=duration, API_Key = API_Key, outputDir = outputDir, topNResults = 20, featureExt = '.json')
