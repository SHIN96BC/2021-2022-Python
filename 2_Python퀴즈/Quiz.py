import random
import time

# 타자게임
def SetTypingQ():
    f = open("original.txt", "r", encoding="ANSI")
    s = set()
    qs = []
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        s.add(line)
    if len(s) == 0:
        print("텍스트파일이 비었습니다.")
    else:
        for x in s:
            qs.append(x)
    f.close()
    TypingGame(qs)
    
def TypingGame(qs):
    print("[타자게임!! 시작하려면 엔터를, 게임 선택창으로 돌아가려면 back 을 입력하세요.]")
    msg = input()
    msg = msg.strip()
    if msg == "back":
        return
    elif len(msg) == 0:
        start = time.time()
        xQ = []
        for x in range(5,11,1):  #문제 갯수를 5~10 까지 숫자중에 랜덤으로 뽑기
            xQ.append(x)
        r = random.choice(xQ)
        answer=0
        while answer < r:
            q = random.choice(qs)
            print("< "+q+" >")
            while True:
                A = input("정답을 입력하세요:")
                A = A.strip()
                if q.lower() == A.lower():
                    answer += 1
                    break
        end = time.time()
        print("\n정답 맞춘 갯수: ", answer, "개")
        print("걸린시간: ", (end-start))

# 나이맞추기 게임 
def setAgeQ():
    f = open("kosmoAge.txt", "r", encoding="ANSI")
    d = {}
    while True:
        fkv = f.readline()
        if not fkv:
            break
        fkv = fkv.strip()
        if len(fkv) == 0:
            continue
        fkvis = fkv.split(" ")
        fk = fkvis[0]
        fv = fkvis[1]
        d.update({fk:fv})
    AgeGame(d)

def AgeGame(d):
    dli = []
    for k in d:
        dli.append(k)
    msg = input("[나이 맞추기 게임!! 시작하려면 엔터, 게임 선택창으로 돌아가려면 back 을 입력하세요.]")
    msg = msg.strip();
    if msg.lower() == "back":
        return
    if len(msg) == 0:
        start = time.time()
        aQ = []
        for x in range(5,11,1):   #문제 갯수를 5~10 까지 숫자중에 랜덤으로 뽑기
            aQ.append(x)
        r = random.choice(aQ)
        answer=0
        while answer < r:
            q = random.choice(dli)
            print("< "+q+" >")
            while True:
                A = input("정답을 입력하세요:")
                A = A.strip()
                if d[q] == A:
                    answer += 1
                    break
        end = time.time()
		tt = end-start         # 타임을 tm = time.localtime(start) 이런식으로 주고 
		tt = format(tt,"2f")   # starting =  time.strftime('%Y-%m-%d %H:%M:%S %p', tm) 이렇게 적어주면 년도, 날짜까지 다 나온다
        print("\n정답 맞춘 갯수: ", answer, "개")
        print("걸린시간: ", tt, "초")

#실행
while True:
    msg = input("\n게임을 선택해주세요(종료하려면 exit).\n(1.타자게임, 2.나이맞추기):")
    if msg == "1":
        SetTypingQ()
    elif msg == "2":
        setAgeQ()
    elif msg.lower() == "exit":
        exit()
    else:
        print("메뉴에 있는 게임만 선택해주세요.")