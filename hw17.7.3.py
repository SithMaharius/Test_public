

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
vklad=input('Введите сумму вклада:')
deposit=[]
v1=(int(vklad)*per_cent['ТКБ']*(365/365))/100  #накопления в первом банке
deposit.append(int(v1))
v2=(int(vklad)*per_cent['СКБ']*(365/365))/100 #накопления во втором банке
deposit.append(int(v2))
v3=(int(vklad)*per_cent['ВТБ']*(365/365))/100 #накопления во третьем банке
deposit.append(int(v3))
v4=(int(vklad)*per_cent['СБЕР']*(365/365))/100 #накопления во четвёртом банке
deposit.append(int(v4))

print('Депозиты в банке ',deposit)

print('Максимальная сумма, которую вы можете заработать :', max(deposit))
