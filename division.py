def dividor(arreglo, izquierda, derecha):  
  # El valor del pivote pasa a ser el valor del último indice del arreglo
  pivote = arreglo[derecha]
  
  # El valor de i pasa a ser un valor menor al primer valor del arreglo
  i = izquierda - 1
  for j in range(izquierda, derecha):
    if arreglo[j] <= pivote:
      # Avanzo al siguiente indice sumando 1
      i = i + 1
      # Intercambio los elementos
      (arreglo[i], arreglo[j]) = (arreglo[j], arreglo[i])
  
  # Al final intercambio el pivote
  (arreglo[i + 1], arreglo[derecha]) = (arreglo[derecha], arreglo[i + 1])
  
  return i + 1
