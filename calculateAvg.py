calAvg=lambda score,multy: score*multy
run=True
scoreList=[]
while(run):
    score=int(input('please enter score: '))
    multy=int(input('please enter multy: '))
    scoreList.append(calAvg(score,multy))
    answer=int(input('do you want to add another? yes(1) or no(0)'))
    if answer==0: run=False