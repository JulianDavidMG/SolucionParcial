import re

texto = "Ciao! Nel 2025, 25 programmatori sviluppano insieme. Lista: tastiera, schermo, mouse. Il prezzo è €100,80. Le stelle (★) brillano sopra il computer. 19 gatti scrivono, 18 cani testano. Il codice #7788 è speciale. 22 giorni di sviluppo, 18 di riposo. @tutti sviluppano. Il numero magico è 1636. Cosa faresti con 63,90€? La risposta è nella lista: scrivere, testare, creare. Sviluppa il tuo futuro! 100 parole, 22 interi, 3 decimales, 2 listas."
                                                                                                                          
patron_enteros = r"-?\b\d+\b"
enteros = re.findall(patron_enteros, texto) 
print("Total:", len(enteros),"| Enteros hallados:", enteros)


patron_decimales = r"-?\b\d+\,\d+\b"
decimales = re.findall(patron_decimales, texto) 
print("Total:", len(decimales),"| Decimales hallados:", decimales)


patron_lista = r"[Ll]ista:\s*(?:\w+\s*(?:,\s*\w+)+)"
listas = re.findall(patron_lista, texto)
print("Total:", len(listas),"| Listas halladas:",listas)


patron_palabras = r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ]+\b|è"
palabras = re.findall(patron_palabras, texto)
print("Total:", len(palabras), "| Palabras halladas:", palabras)