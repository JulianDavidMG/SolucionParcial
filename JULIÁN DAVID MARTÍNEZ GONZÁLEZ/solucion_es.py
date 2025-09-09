import re

texto = "En el año 2025, 26 programadores desarrollan juntos. ¡Hola! ¿Te gusta programar? El cielo digital, las estrellas (★) brillan. 22 niños codifican, 21.50 horas de trabajo. Lista: teclado, monitor, mouse. El costo es $105.20. ¿Sabías que el código #3344 es especial? La vida es código, @todos participan. El tiempo pasa, 23 días de desarrollo. ¡Programa! El número especial es 1616. ¿Qué harías con 66.90 pesos? La respuesta está en la lista: escribir, depurar, crear. ¡Desarrolla tu futuro! 100 palabras, 23 enteros, 3 decimales, 2 listas."
                                                                                                                          
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto) 
print("Total:", len(enteros),"| Enteros hallados:", enteros)


patron_decimales = r"-?\b\d+\.\d+\b"
decimales = re.findall(patron_decimales, texto) 
print("Total:", len(decimales),"| Decimales hallados:", decimales)


patron_lista = r"[Ll]ista:\s*(?:\w+\s*(?:,\s*\w+)+)"
listas = re.findall(patron_lista, texto)
print("Total:", len(listas),"| Listas halladas:",listas)


patron_palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b"
palabras = re.findall(patron_palabras, texto)
print("Total:", len(palabras), "| Palabras halladas:", palabras)