import random

def getRandNotEqualTo(start,stop,notEqual):
  x = random.randint(start,stop)
  while x == notEqual:
    x = random.randint(start,stop)
  return x

def randGo(string, totalClumps, goIndex, i):
  clumpsize = 15
  if string != "infect":
    return f"{string} {range(0, totalClumps * clumpsize, clumpsize)[random.randint(0,totalClumps - 1)] + goIndex if random.randint(0,1) else clumpsize * i + goIndex}"
  else:
    return f"{string} {range(0, totalClumps * clumpsize, clumpsize)[random.randint(0,totalClumps - 1)] +goIndex if random.randint(0,1) else clumpsize * i + goIndex}"
    
def initClumps(totalClumps, i):
    right_or_left = ["right", "left"]
    actions = ["right", "left", "hop"]
    #clump_check = lambda : 
    return [randGo("ifenemy", totalClumps, 12,i), randGo("ifwall", totalClumps, 6,i), randGo("ifsame", totalClumps, 6,i),actions[random.randint(0,2)],randGo("go", totalClumps, 1, i),randGo("go",totalClumps,10,i),randGo("go",totalClumps,10,i) if random.randint(0,1) else randGo("ifrandom",totalClumps,14,i),"left",randGo("go", totalClumps,1, i), right_or_left[random.randint(0,1)],randGo("go",totalClumps,1,i),randGo("infect", totalClumps,1, i), randGo("go", totalClumps,1,i),"right", randGo("go", totalClumps,1,i)]

def writeRandom():
  dict1 = {'hop':False, 'left':False, 'right':False, 'infect':True, 'ifempty':True, 'ifwall':True, 'ifsame':True, 'ifenemy':True, 'ifrandom':True, 'go':True}
  f = open("texts/oliver.txt", "w")
  randomRange = random.randint(8,1400)
  chunks = []
  for i in range(randomRange):
    chunk = initClumps(randomRange, i)
    chunks.append(chunk)
  for i in chunks:
    for j in i:
      f.write(j + "\n")
  f.write("go 1")
  f.close()
