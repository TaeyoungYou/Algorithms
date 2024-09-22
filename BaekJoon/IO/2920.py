import sys



def asc(music: list):
    for i in range(1,9):
        if i != music[i-1]:
            return False
    print("ascending")
    return True

def des(music: list):
    for i in range(8,0,-1):
        if i != music[8-i]:
            return False
    print("descending")
    return True

def mix():
    print("mixed")

if __name__=="__main__":
    music = list(map(int, sys.stdin.readline().split()))
    if asc(music):
        pass
    elif des(music):
        pass
    else:
        mix()
#다른 풀이
sorted(music)
sorted(music, reverse=True)
#로 기존 리스트와 비교