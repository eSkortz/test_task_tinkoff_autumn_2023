a = int(input())
jo_order = list(map(int, input().split()))
correct_order = list(map(int, input().split()))

c = (i for i in range(a))
d = (i for i in range(a-1, -1, -1))

first_marker = 0
second_marker = a-1

for i in c:
    if jo_order[i] == correct_order[i]:
        first_marker += 1
    else:
        break

for j in d:
    if jo_order[j] == correct_order[j]:
        second_marker -= 1
    else:
        break

sorted_jo = sorted(jo_order[first_marker:second_marker+1])

if sorted_jo == correct_order[first_marker:second_marker+1]:
    print('YES')
else:
    print('NO')