# 1. 파일(original.txt)을 열어서 읽는다 
fname = "original.txt"
f = open(fname, "r")
#print(f.readline()) # 한 라인을 읽어옴 
#print(f.readlines()) # 전체를 읽어옴 ( 줄바꿈 기호를 포함해서 )
#print(f.read()) # 전체를 읽어옴


# 2. 중복문제를 제거한다 
# s = {} # 기본값이 dict로 인식 
s = set()
while True:
    line = f.readline()
    if not line: break
    line = line.strip()
    s.add(line)
f.close()

# 3. 필터링된 문제들을 컬렉션에 옮긴다
li = []
for x in s:
    li.append(x)
#print(li)

# 4. 게임시작을 알리는 Enter을 입력받으면, 램덤한 문제를 출력한다
import random
q = random.choice(li)
#print(q)

print("[타자 게임!! 준비되면 엔터!!]")
input()

import time
start = time.time()
print("시작시간:", start)

# 5. 사용자의 입력을 받고 -> 문제의 내용과 비교 -> 통과 or 재도전 

# 6. 게임시간을 체킹하여 걸린시간을 출력한다 
# end = time.time()