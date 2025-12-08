boxes = []
with open('inputs/08.txt') as in_f:
    for line in in_f:
        boxes.append(tuple(int(x) for x in line.split(',')))

def get_dist(b0, b1):
    return (b0[0] - b1[0]) ** 2 + (b0[1] - b1[1]) ** 2 + (b0[2] - b1[2]) ** 2

distances = []
for i in range(len(boxes) - 1):
    for j in range(i + 1, len(boxes)):
        distances.append((get_dist(boxes[i], boxes[j]), boxes[i], boxes[j]))
distances = sorted(distances, key=lambda x: x[0])

circuit_ctr = 0
connected = {}
box_dict = {}
for i, (d, b0, b1) in enumerate(distances):
    if b0 in box_dict and b1 not in box_dict:
        box_dict[b1] = box_dict[b0]
        connected[box_dict[b0]].add(b1)
        gold_key = box_dict[b0]
    elif b1 in box_dict and b0 not in box_dict:
        box_dict[b0] = box_dict[b1]
        connected[box_dict[b1]].add(b0)
        gold_key = box_dict[b1]
    elif b0 not in box_dict and b1 not in box_dict:
        box_dict[b0] = circuit_ctr
        box_dict[b1] = circuit_ctr
        connected[circuit_ctr] = set([b0, b1])
        gold_key = circuit_ctr
        circuit_ctr += 1
    else:
        to_change = []
        for key, val in box_dict.items():
            if val == box_dict[b1]:
                to_change.append(key)
        connected[box_dict[b0]].update(to_change)
        gold_key = box_dict[b0]
        for b in to_change:
            box_dict[b] = box_dict[b0]

    if i == 999:
        silver_dic = {}
        for b in boxes:
            if b in box_dict:
                silver_dic[box_dict[b]] = silver_dic.get(box_dict[b], 0) + 1
        silver = sorted([v for v in silver_dic.values()])[-3:]

        print(silver[0] * silver[1] * silver[2])

    if len(connected[gold_key]) == len(boxes):
        print(b0[0] * b1[0])
        break
