import json
with open('text1.txt', 'r', encoding='utf-8') as file:
    companies = file.read().split('\n')
ls = []
companies_profit = {}
mean_profit = {}
summa = 0
plus_companies = 0
for c in companies:
    info = c.split()
    name = info[0]
    profit = float(info[-2]) - float(info[-1])
    if profit >= 0:
        summa += profit
        plus_companies += 1
    companies_profit[name] = profit
ls.append(companies_profit)
mean_profit['mean_profitt'] = summa / plus_companies
ls.append(mean_profit)

with open('profit.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(ls))