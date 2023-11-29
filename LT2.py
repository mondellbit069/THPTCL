k, n = map(int, input().split())
print('Moi hoc sinh nhan duoc so man la: ', k // n)
print('So man thua la: ', k - n * (k // n))