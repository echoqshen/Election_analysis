lstname = ["Dex", "Chico", "Julia", "Doug"]
lstage = [16, 17, 15, 18]
lstMarks=[89, 90, 78, 59]
numstudents=len((lstname))

lststudents = [lstname, lstage,lstMarks]
# print(lststudents[1][0])

# for i in range(numstudents):
#     # print(f"{lststudents[0][i]} age is {lststudents[1][i]} and their exam score is {lststudents[2][i]}")
#     print(f"{lstname[i]} age is {lstage[i]} and score is {lstMarks[i]}  ")

# dictResults = {"name":lstname, "age": lstage, "marks": lstMarks}
# print(dictResults["name"][2])

listofdict=[]
dictnewstud={}
for i in range(numstudents):
    dictnewstud["name"]=lstname[i]
    dictnewstud["age"]=lstage[i]
    dictnewstud["marks"]=lstMarks[i]
    # print(dictnewstud)
    listofdict.append(dictnewstud)
    dictnewstud={}
    # print(dictnewstud)
print(listofdict)