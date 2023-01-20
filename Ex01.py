# # создать список гостей и вывести пригласительное сообщение каждаму
# guests=['Ann','Sam','Kate','Stoyn']
# print(guests)
# print(f"{guests[1]} won't be able to come")
# print('Dear Jack, I invite you to lunch')
# # print(f'Dear {guests[0]}, I invite you to lunch')
# # print(f'Dear {guests[1]}, I invite you to lunch')
# # изменить список гостей, который прийти не сможет на нового гостя
# guests[1]= 'Jack'
# print(f'New list guests {guests}') 
# # расширить список, добавить гостей в конец, середину и начало списка
# guests.append('Mary')
# print(guests)
# guests.insert(1,'Max')
# print(guests)
# guests.insert(0,'Jim')
# print(guests)
# # сокращение списка гостей
# new_list= guests.pop(-1)
# print(new_list)
# print(guests)
# guests.remove('Ann')
# print(guests)
# del guests[0]
# print(guests)
# print(len(guests))

# сортировка
countries=['Turkie', 'Africa', 'Russia', 'Cyprus', 'Chaina']
print(countries)
print(sorted(countries))
countries.reverse()
print(countries)
countries.sort(reverse=True)
print(countries)
print(len(countries))