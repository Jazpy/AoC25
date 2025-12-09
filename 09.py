with open('inputs/09.txt') as in_f:
    rectangles = [tuple((int(l.split(',')[0]), int(l.split(',')[1]))) for l in in_f]

hlines, vlines = [], []
for i in range(len(rectangles) - 1):
    r0, r1 = rectangles[i], rectangles[i + 1]
    if r0[0] == r1[0]:
        vlines.append((r0, r1))
    else:
        hlines.append((r0, r1))
if rectangles[0][0] == rectangles[-1][0]:
    vlines.append((rectangles[0], rectangles[-1]))
else:
    hlines.append((rectangles[0], rectangles[-1]))

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersects(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def outer(c0, c1):
    middle_x = min(c0[0], c1[0]) + ((max(c0[0], c1[0]) - min(c0[0], c1[0])) / 2)
    middle_y = min(c0[1], c1[1]) + ((max(c0[1], c1[1]) - min(c0[1], c1[1])) / 2)

    new_c0_x = c0[0] + .1 if middle_x > c0[0] else c0[0] - .1
    new_c0_y = c0[1] + .1 if middle_y > c0[1] else c0[1] - .1
    new_c1_x = c1[0] + .1 if middle_x > c1[0] else c1[0] - .1
    new_c1_y = c1[1] + .1 if middle_y > c1[1] else c1[1] - .1
    nc0, nc1 = (new_c0_x, new_c0_y), (new_c1_x, new_c1_y)

    segments = [(nc0, (nc0[0], nc1[1])), ((nc0[0], nc1[1]), nc1),
                (nc1, (nc1[0], nc0[1])), ((nc1[0], nc0[1]), nc0)]

    for a, b in segments:
        ls = hlines if a[0] == b[0] else vlines
        for l in ls:
            if intersects(a, b, l[0], l[1]):
                return True
    return False

silver = 0
gold = 0
for i in range(len(rectangles) - 1):
    for j in range(i + 1, len(rectangles)):
        r0, r1 = rectangles[i], rectangles[j]
        area = (abs(r0[0] - r1[0]) + 1) * (abs(r0[1] - r1[1]) + 1)
        if area > silver:
            silver = area
        if area > gold and not outer(r0, r1):
            gold = area

print(silver)
print(gold)
