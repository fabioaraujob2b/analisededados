lista =  ['a', 'b', 'c', 'a', 'b', 'c']
#Verificando duplicatas na lista e removendo sem perder a ordem
lista_sem_duplicatas = []
for item in lista:
    if item not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(item)
print(lista_sem_duplicatas) 
lista_usando_set = list(set(lista))
print(lista_usando_set) #Perde a ordem original

