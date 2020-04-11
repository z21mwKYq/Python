k = int(input('Кол-во предприятий'))
enter = {}
for i in range(1, k + 1):
    name = input('Название предприятия ')
    enter[name] = [float(input('План ')), float(input('Факт'))]
    # print(enter)

    enter[name].append(enter[name][1] / enter[name][0])

print(enter)

for key,value in enter.items():
    if value [1] > 10 and value[2] < 1:
        print(f'{key}')
