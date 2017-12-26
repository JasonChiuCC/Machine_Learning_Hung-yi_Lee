idx     = 0
resDict = {}
rList   = open("words.txt", "r").read().split(" ")

for i, elem in enumerate(rList):
    if elem in resDict.keys():
      tmp = resDict.get(elem)
      tmp[1] += 1
      resDict[elem] = tmp
    else:
      resDict.update( { elem: [idx,1] } )
      idx+=1
