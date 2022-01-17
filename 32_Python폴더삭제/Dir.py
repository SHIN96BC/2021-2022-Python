
# 디렉토리가 존재하면 디렉토리안에 파일들을 출력

import os


def listing():  # 리스팅 옵션
    while True:
        terget = input("\n리스팅할 디렉토리를 입력해주세요.(종료는 exit, 메뉴선택은 menu):")
        if terget.lower() == "exit":
            exit()
        if terget.lower() == "menu":
            return
        if os.path.exists(terget):
            kids = os.listdir(terget)
            for kid in kids:
                    if os.path.isfile(terget +"\\"+ kid):   # (terget +"\\"+ kid) 이거 대신에 os.path.join(terget,kid) 
                        print("[F]",kid)                    # 이렇게 join을 쓰면 자동으로 \\ 가 붙어서 절대경로가 만들어진다.
                    elif os.path.isdir(terget +"\\"+ kid): 
                        print("[D]",kid)
                    else:
                        print("[else]",kid)
        else:
            print("존재하지 않는 디렉토리입니다.")
            while True:
                msg = input("\n생성하시겠습니까?(y/n):")
                if msg.lower() == "y":
                    os.makedirs(terget)
                    print("해당 디렉토리를 생성했습니다.")
                    break
                elif msg.lower() == "n":
                    print("생성하지 않았습니다")
                    break;
                else:
                    print("y,n 중에 하나만 입력하세요.")
                
def delete():    # 삭제 옵션
    while True:
        terget = input("\n삭제할 디렉토리를 입력해주세요.(종료는 exit, 메뉴선택은 menu):")
        if terget.lower() == "exit":
            exit()
        if terget.lower() == "menu":
            return
        if os.path.exists(terget):
            if os.path.isdir(terget):
                while True:
                    msg = input("폴더안에 파일이 존재합니다. 삭제하시겠습니까?(y,n):")
                    if msg.lower() == "y":
                        recursiveCall(terget)
                        os.rmdir(terget)
                        print("디렉토리가 삭제되었습니다.")
                        break
                    elif msg.lower() == "n":
                        return
                    else:
                        print("y 와 n 중에 하나만 입력해주세요.")
            else:
                print("디렉토리만 입력해주세요.")
        else:
            print("디렉토리가 존재하지 않습니다.")
            
def recursiveCall(dir):    # 디렉토리 삭제를 위한 재귀 호출(recursive call)
    if os.listdir(dir):
        dirK = os.listdir(dir)
        for dk in dirK:
            if os.path.isfile(dir +"\\"+ dk):
                os.remove(dir +"\\"+ dk)
                print(dk,"파일이 삭제되었습니다.")
            elif os.path.isdir(dir +"\\"+ dk): 
                recursiveCall(dir +"\\"+ dk)
                os.rmdir(dir +"\\"+ dk)
                print(dk,"디렉토리가 삭제되었습니다.")

# 실행 되는 메인
while True:
    msg = input("\n1.리스팅\t2.삭제 (메뉴를 골라주세요(번호입력):")
    if msg.lower() == "exit":
        exit()
    if msg == "1":
        listing()
    elif msg == "2":
        delete()
    else:
        print("메뉴에 존재하는 번호만 입력해주세요.")
