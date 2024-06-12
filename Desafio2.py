lista = []
while len(lista) < 3:
 item = input()
 lista.append(item)
print("Lista de Equipamentos:")  
for item in lista:
  print(f"- {item}")