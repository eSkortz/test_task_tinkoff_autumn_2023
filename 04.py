# sum_to_find, count_nominals = map(int, input().split())
# bank_nominals = list(map(int, input().split()))
    

# if len(bank_nominals) < count_nominals:
#     print(-1)
# else:

n, m = map(int, input().split())
s = list(map(int, input().split()))

s.sort(reverse=True)

s_count = {}

for i in s:
    if i not in s_count:
        s_count[i] = 0
        
stolen_money = []

for i in s:
    while n >= i and s_count[i] < 2:
        n -= i
        stolen_money.append(i)
        s_count[i] += 1

if n == 0:
    print(len(stolen_money))
    print(*stolen_money)
else:
    print(-1)

