from division import(dividor)

def quicksort(arreglo, izquierda, derecha):
  if izquierda < derecha:
    # Divido el arreglo y acomodo los  valores
    pi = dividor(arreglo, izquierda, derecha)
  
    quicksort(arreglo, izquierda, pi - 1)
    quicksort(arreglo, pi + 1, derecha)

arr = [7, 4, 6, 2, 10, 3, 8, 9, 5, 1, 0]
print(arr)
if(len(arr) <= 1):
  print("El arreglo debe tener como mínimo 2 elementos")
else:
  quicksort(arr, 0, len(arr)-1)
  print(arr)