ss = int(input())
d = ss // 86400
h = (ss - d * 86400) // 3600
m = (ss - d * 86400 - h * 3600) // 60
s = (ss - d * 86400 - h * 3600 - m * 60)

print(ss, 's = ', d, 'd :', h, 'h :', m, 'm :', s, 's')
