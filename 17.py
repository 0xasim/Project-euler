nletters =  [
            0, 3, 3, 5, 4, 4, 3, 5, 5, 4, # 0-9
            3, 6, 6, 8, 8, 7, 7, 9, 8, 8  # 10-19
            ]
ty = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6] # 0, 10, 20, 30, ...90
hundred, thousand, AND = (7, 8, 3)

for i in range(20, 100):
  if int(str(i)[1]) == 0: nletters.append(ty[int(str(i)[0])])
  else: nletters.append(ty[int(str(i)[0])] + nletters[int(str(i)[1])])
   
for j in range(100, 1000):
  upto_100 = nletters[int(str(j)[0])] + hundred
  if str(j)[1:] == "00": nletters.append(upto_100)
  else: nletters.append(upto_100 + AND + nletters[int(str(j)[1:])])
nletters.append(nletters[1] + thousand)
   
print(nletters)
print(sum(nletters))
#print(len(nletters))
