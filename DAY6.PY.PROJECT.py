Q1='''who won the first ipl trophy?
a.ee saala cup namde
b.chennai super kings
c.mumbai indians
d.rajasthan royals'''
Q2='''which team was banned for matchfixing?
a.sunrises
b.chennai
c.rajasthan
d.both b&c'''
Q3='''best indian film,over the world?
a.dangal
b.bahubali
c.kgf 2
d.rrr'''
Q4='''Indian who is proud of the nation?
a.APJ Abdul kalam
b.ms dhoni
c.sundar pichai
d.all of above''' 
Q5='''no.1 all format player for indian cricket team ever?
a.virat kohli
b.sachin
c.sehwag
d.vijay shankar'''
questions={Q1:"d",Q2:"d",Q3:"b",Q4:"d",Q5:"a"}
name=input("hi whats ur name")
print("hello",name,"welcome to quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("do you want to skip this question(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow!you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("ur current score is",score)
    flag2=input("do you want to quit?type(yes/no)")
    if flag2=="yes":
        break
    print("your total score is:",score)
