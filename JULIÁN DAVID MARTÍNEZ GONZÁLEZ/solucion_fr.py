import re

texto = "Salut! En 2025, 24 programmeurs codent ensemble. Liste: clavier, écran, souris. Le prix est de 103,40€. Les étoiles (★) brillent la nuit. 20 chats codent, 19 chiens testent. Le code #5566 est spécial. 23 jours de développement, 17 jours de repos. @tous codent. Le numéro magique est 1626. Que feriez-vous avec 69,70€? La réponse est dans la liste: écrire, tester, créer. Développez votre avenir! 100 mots, 23 entiers, 3 decimales, 2 listas."

                                                                                                                          
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto) 
print("Total:", len(enteros),"| Enteros hallados:", enteros)


patron_decimales = r"-?\b\d+\,\d+\b"
decimales = re.findall(patron_decimales, texto) 
print("Total:", len(decimales),"| Decimales hallados:", decimales)


patron_lista = r"[Ll]iste:\s*(?:\w+\s*(?:,\s*\w+)+)"
listas = re.findall(patron_lista, texto)
print("Total:", len(listas),"| Listas halladas:",listas)


patron_palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚ]+\b"
palabras = re.findall(patron_palabras, texto)
print("Total:", len(palabras), "| Palabras halladas:", palabras)