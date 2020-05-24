#coding=utf-8
import csv

print("=========读取CSV=============")

csvFile=open("csvData.csv","r",encoding='utf-8')
reader=csv.reader(csvFile)
data=[]
for item in reader:
    print(item)
    data.append(item)

print(data)
csvFile.close()

print("=========读取CSV2=============")
with open("csvData.csv","r",encoding='utf-8') as csvfile:
    reader2=csv.reader(csvfile)
    for item2 in reader2:
        print(item2)

print("=======从列表写入csv文件==========")
csvFile2=open("csvData2.csv","w",newline='',encoding='utf-8')
writer=csv.writer(csvFile2)
m=len(data)
for i in range(m):
    writer.writerow(data[i])
csvFile2.close()

print("=======从字典写入csv=========")
dic={"a1":123,"a2":321,"a3":456}
csvFile3=open("csvData3.csv","w",newline='',encoding='utf-8')
writer2=csv.writer(csvFile3)
for key in dic:
    writer2.writerow([key,dic[key]])
csvFile3.close()