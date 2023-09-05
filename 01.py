a = list(map(int, input().split()))
revolvers = list(map(int, input().split()))

c = (i for i in range(a[0]))

revolver_max = 0
for i in c:
    if revolvers[i] > revolver_max and revolvers[i] <= a[1]:
        revolver_max = revolvers[i]
    if revolver_max == a[1]:
        break
print(revolver_max)