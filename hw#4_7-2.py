import operator

'''2019038062'''

## 변수 선언 부분 ##

TrainTuple = [('토마스',5),('헨리',8),('에드워드',9),('에밀리',5), ('토마스',4), ('헨리',7),('토마스',3),('에밀리',8),('퍼시',5),('고든',13)]
Train_Weight={}
TrainList=[]
Tname=''
Tweight=0
Rank=1

## 메인 코드 부분 ##

for i in range(0,10) :
    Tname=TrainTuple[i][0]
    Tweight=TrainTuple[i][1]
    if Tname in Train_Weight:
        Tweight+=Train_Weight[Tname]

    Train_Weight[Tname]=Tweight
    
print("기차 수송량 목록 ===> ", TrainTuple)

print("---------------------------")

TrainList=sorted(Train_Weight.items(),key=operator.itemgetter(1),reverse=True)
print("기차     \t총수송량  순위")
print("---------------------------")
print(TrainList[0][0],"   \t",TrainList[0][1],"\t",Rank)
for i in range(1,len(TrainList)):
    Rank+=1
    if TrainList[i][1]== TrainList[i-1][1]:
        SameRank=Rank-1
        print(TrainList[i][0],"   \t",TrainList[i][1],"\t",SameRank)
    else:
        print(TrainList[i][0],"   \t",TrainList[i][1],"\t",Rank)
