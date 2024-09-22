import sys

room=int(sys.stdin.readline())

max_room_num = 1
count = 1
while True:
    if room <= max_room_num:
        break
    max_room_num += (6*count)
    count += 1
print(count)