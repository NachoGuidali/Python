
"""import ejercicios_v4
from ejercicios_v4 import menu_principal

menu_principal()"""
import csv
import os
import requests


def opcion0():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        barrios = {}
        for row in csv_reader:
            if row[4] == "CABA" and row[9] == "confirmado":
                if row[5] in barrios:
                    barrios[row[5]] += 1
                else:
                    barrios[row[5]] = 1   
        maximo, max_barrio = max(barrios.items(), key=lambda x : x[1]) 

        print("el barrio con mas cantidad de casos es ", maximo, max_barrio)    

def opcion1():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        barrios = {}
        for row in csv_reader:
            if row[4] == "CABA" and row[9] == "confirmado":
                if row[5] in barrios:
                    barrios[row[5]] += 1
                else:
                    barrios[row[5]] = 1
                        
        print(barrios)

def opcion2():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        barrio = input("ingrese un barrio: ")
        casos = 0
        for row in csv_reader:           
            for cell in row:
                if row[5].lower() == barrio.lower() and row[4] == "CABA":
                    casos +=  cell.count("confirmado")
        print("cantidad de casos: ", casos)     
        
def opcion3():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        gba = 0
        caba = 0
        for row in csv_reader:
            for cell in row:
                if row[4] == "CABA":
                    caba += cell.count("CABA")
                elif row[4] == "Buenos Aires":
                    gba += cell.count("Buenos Aires")

        print ("en Gran buenos Aires hay un total de: ", gba, "casos","y en CABa hay un total de: ", caba, "casos")  

def opcion4():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        lugar = input("ingrese el lugar a analizar (total/CABA/Buenos Aires): ")
        total_m = 0
        total_f = 0
        gba_m = 0
        gba_f = 0
        caba_m = 0
        caba_f = 0
        
        for row in csv_reader:
            if lugar == row[4] or lugar == "total":
                if row[7] == "masculino":
                    caba_m += row.count("masculino") 
                    gba_m += row.count("masculino")                             #como hacer para que el parametro gba responda tambien con buenos aires
                    total_m += row.count("masculino")

                elif row[7] == "femenino":
                    caba_f += row.count("femenino")
                    gba_f += row.count("femenino")  
                    total_f += row.count("femenino")
        if lugar == "CABA":
            print("masculinos en CABA",caba_m,"femeninos en CABA", caba_f)
        elif lugar == "Buenos Aires":

            print("masculinos en GBA", gba_m, "femeninos en GBA", gba_f)
        elif lugar == "total":
            print("masculinos totales", total_m, "femeninos totales", total_f)                        


def opcion5():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        #CASOS_DE_COVID = {}
        for row in csv_reader:
            valores_casos = {
                "" : row[1],
                "" : row[2],
                "columna3" : row[3],
                "columna4" : row[4],
                "columna5" : row[5],
                "columna6" : row[6],
                "columna7" : row[7],                                             #el diccionario se hace asi? no logro poner el que un solo key tenga varios valores
                "columna8" : row[8],
                "columna9" : row[9],
                "columna10" : row[10],
                "columna11" : row[11],
                "columna12" : row[12],
                "columna13" : row[13],
            
        }
            
            #CASOS_DE_COVID[row[0]] = valores_casos
            for x in valores_casos:
                print(row[0], valores_casos[x])
    #print(CASOS_DE_COVID)    

def opcion6():
    url_archivo = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ministerio-de-salud/casos-covid-19/casos_covid19.csv"
    nombre_archivo = "casos_covid19.csv"
    pedido = requests.get(url_archivo)
    if os.path.exists("casos_covid19.csv"):
        print("el archivo casos_covid19.csv ya existe en la carpeta actual")
    else:     
        with open(nombre_archivo, "wb") as archivo:
            archivo.write(pedido.content)

def opcion7():
    with open("casos_covid19.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")
        barrios = {}
        for row in csv_reader:
            if row[4] == "CABA" and row[9] == "confirmado":
                if row[5] in barrios:
                    barrios[row[5]] += 1
                else:
                    barrios[row[5]] = 1  

        for key, value in barrios.items():
            if value > 10000:
                print("los barrios con mas de 10000 casos son: ", key, value)      

def salir():
    print("saliendo")

#-------estructura del menu--------

opciones = { 
    0 : ("opcion 0", opcion0),
    1 : ("opcion 1", opcion1),
    2 : ("opcion 2", opcion2),
    3 : ("opcion 3", opcion3),
    4 : ("opcion 4", opcion4),
    5 : ("opcion 5", opcion5),
    6 : ("opcion 6", opcion6),        
    7 : ("opcion 7", opcion7),
    8 : ("Salir", salir)
}


def menu_principal():
    opciones = { 
    0 : ("opcion 0", opcion0),
    1 : ("opcion 1", opcion1),
    2 : ("opcion 2", opcion2),
    3 : ("opcion 3", opcion3),
    4 : ("opcion 4", opcion4),
    5 : ("opcion 5", opcion5),
    6 : ("opcion 6", opcion6),        
    7 : ("opcion 7", opcion7),
    8 : ("Salir", salir)
    }
    generar_menu(opciones, 8)

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def mostrar_menu(opciones):
    print("seleccione una opcion: ")
    for key in sorted(opciones):
        print(f" {key}) {opciones[key][0]}") 

def leer_opcion(opciones):
    a = int(input('Opción: '))
    while a not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    else:
        return a
        

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

menu_principal()                                        