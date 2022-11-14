print(f.readline())   # leer linea por linea - unicamente la primera linea del fichero

modo = w - write # escritura
modo = a - append # escribir a partir del ultimo punto del archivo
modo = r - read  # lectura
modo = x         # creacion del fichero

r+: Abre el archivo en modo lectura y escritura. Pudiendo así no solo obtener y usar su contenido, sino modificarlo si se desea.

w: Abre el archivo en solo modo escritura. Va a sustituir el archivo original si existe antes o crear uno nuevo si no existe. Quiere decir entonces, que el contenido original que tenga ese archivo se perderá una vez escribas en él.
a: Abre el archivo para escritura, pero permitiendo agregar contenido al existente. Esto quiere decir que el contenido original se conserva y lo que escribas se agregará al final del archivo. Si el archivo no existe, se crea uno nuevo.

a+: Abre el archivo en modo de escritura para agregar contenido y lectura, permitiendo así agregar contenido al final y leerlo también.





archivo.writelines(["hola", "Mundo"])  # holaMundo   escribe todo junto en una sola linea

# recorre linea por linea
for line in archivo
    print(line)


# eliminar un fichero -- hay que importar os (modulo)    import os
os.remove(archivo)


#crear un archivo
path = archivo.dat
f = open(path, modo = "x")
f.close

# eliminar un archivo - primero hay que verificar que exista ( para que no salte un error )
if os.path.existe(path)
    os.remove(path)
else: 
    print("el archivo que se quiere eliminar no existe ")



## para trabajar con ficheros csv hay que importar un modulo

import csv

abrir el archivo en modo r

reader = csv.reader(archivo) # estan separados por coma , -- devuelve un objeto iterable del tipo reader
for linea in reader:
    print(linea)    [, , , , ] ## lista que tiene n elementos


## leer datos de un archivo linea por linea
archivo = open("archivo.dat", "r")
while(True):
    linea = archivo.readline()
    print(linea)
    if not linea:   #llega al final de la linea y no hay nada (sale) (las lineas son vacias )
        break
archivo.close()




set() # para remover los duplicados


## buscar un texto y modificar
# def recibeTexto():
#     texto = input("ingrese texto a buscar:")
#     print("el texto a buscar sera: ", texto)

#     textoReemplaza = input(f"Ingrese el texto que reemplazará a '{texto}' : " )
#     print("el texto que se reemplazará : ", textoReemplaza)

# recibeTexto()

def recibeTexto():
    # def lista
    listaBuscar = list()
    listaReemplazar = list()
    texto = input("ingrese texto a buscar:")

    listaBuscar.append(texto)
    textoReemplaza = input(f"Ingrese el texto que reemplazará a '{texto}' : " )
    listaReemplazar.append(textoReemplaza)

    print(dict(zip(listaBuscar, listaReemplazar)))  # obtenemos un diccionario

recibeTexto()



for p in doc.paragraphs:
    inline=p.runs
    len_inline=len(inline)
    for item in dict_texto:
        print(dict_texto)
        if p.text.find(item)>=0:     # find - buscar
            for i in range(len_inline):
                if item in inline[i].text:
                    nuevo_texto=inline[i].text.replace(item,dict_texto[item])   ## replace - reemplazar
                    inline[i].text=nuevo_texto
# doc.save(path_doc)
print("se realizó el cambio con exito!") 



## 
archivo = open("archivo.dat")
linea = archivo.readline()    ## lee una linea  (guarda un punto que leyo por ultima vez)
print(linea)

linea = archivo.readline()    
print(linea)

linea = archivo.readline.rstrip()   # rstrip quita el salto de linea   
print(linea)

#imprime las tres primera lineas













