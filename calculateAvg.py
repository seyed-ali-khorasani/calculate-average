from tokenize import Double


calAvg=lambda score,multy: score*multy
run=True
scoreList=[]
multyList=[]
total=0
mulTotal=0
while(run):
    score=float(input('please enter score: '))
    multy=int(input('please enter multy: '))
    scoreList.append(calAvg(score,multy))
    multyList.append(multy)
    answer=int(input('do you want to add another? yes(1) or no(0): '))
    if answer==0: run=False
for i in scoreList:
    total+=i
for i in multyList:
    mulTotal+=i
print(f'your average is: {total/mulTotal}')