""" СПИСОК СУЩНОСТЕЙ ДАННЫХ """
import pandas as pd
import json
""" 1. ссылка на сайт соревнований
2. ссылка на сплиты 
3. ссылка на стартовые протоколы
4. список координат
5. контакты оргов
6. записи о потерянных вещах
7. ссылка на заявку
8. ссылка на gps трансляцию
8. кол-во дней
"""

# print([i.strip() for i in s.split('\n')])
""" БАЗА 1. ИНФОРМАЦИЯ ОТ ОРГАНИЗАТОРОВ"""
columns1 = ['СПЛИТЫ', 'СТАРТОВЫЕ ПРОТОКОЛЫ',
            'ЛОКАЦИЯ', 'GPS ТРАНСЛЯЦИЯ', 'ОНЛАЙН РЕЗУЛЬТАТЫ']
ind1 = ['day1', 'day2', 'day3', 'dayN']
base1 = pd.DataFrame(columns=columns1,index=ind1)
# base1.to_csv('base1.csv')
""" БАЗА 2. ИНФОРМАЦИЯ ОБ УЧАСТНИКАХ """

columns2 = ['ИНФОРМАЦИОННЫЙ БЮЛЛЕТЕНЬ', "САЙТ СОРЕВНОВАНИЙ", "КОНТАКТЫ ОРГАНИЗАТОРОВ", "СПОНСОРЫ", "ДОКУМЕНТЫ"]
base2 = pd.DataFrame(columns=columns1)
base2.to_csv('base2.csv')


""" БАЗА 3. ИНФОРМАЦИЯ ОБ УЧАСТНИКАХ """

columns3 = ['ID', 'NAME', 'LASTNAME', 'GROUP', 'CONTACT']
ind3 = ['id1', 'id2', 'id3', 'id4']
base3 = pd.DataFrame(columns=columns3, index=ind3)
# print(base1.columns)

# df = pd.read_csv('base1.csv', index_col=0)
# df.loc[ind1[0]]['СПЛИТЫ'] = 893449
# s1:pd.Series = df.loc[ind1[0]]
# print(df.loc[i"nd1[0]].dropna().index.values[0])
d = "{'sdsds':2543,'sdaass':2233,'sd,v,s':212,'sdies':24}"
# print(pd.Series(d))
# print(dict(str(d)))
a = json.loads(d.replace("'",'"'))
print(type(a))