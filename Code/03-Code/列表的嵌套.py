import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
rooms = [[], [], []]

# for teacher in teachers:
#     room = random.choice(rooms)
#     room.append(teacher)

# for teacher in teachers:
#     room_index = random.randint(0, 2)
#     rooms[room_index].append(teacher)
#
# print(rooms)
# print('第一个房间的人数是',len(rooms[0]))
# i = 0
# for p in rooms[0]:
#     if i < len(rooms[0]):
#         print(p)
#         i += 1


for teacher in teachers:
    room_num = random.randint(0, 2)
    rooms[room_num].append(teacher)

for i, room in enumerate(rooms):
    print(f"Room {i} has length {len(room)}")
    for teacher in room:
        print(f"Teacher: {teacher}")
