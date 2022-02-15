per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Введите вкладываемую сумму денег '))
deposit = []
deposit.append(int(money/100*(per_cent['ТКБ']))),
deposit.append(int(money/100*float(per_cent['СКБ']))),
deposit.append(int(money/100*float(per_cent['ВТБ']))),
deposit.append(int(money/100*float(per_cent['СБЕР']))),
print(deposit)
print('Максимальная сумма, которую вы сможете заработать — ', max(deposit))