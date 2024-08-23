import json
from os import system
import time

def readlist():
    system("cls")
    print("Escriba la ruta de la lista")
    path = input("Ruta: ")
    _file = open(path,"r")
    _data = json.loads(_file.read())

    print(f"Clase: {_data['class']}")

    _std = _data['stud']
    for i in range(_data['stdnum']):
        print(f"Nombre: {_std[i]['name']}")
        print(f"Notas: {json.dumps(_std[i]['notes'])}")
        print(f"Promedio: {_std[i]['promd']}")
        print("=========================================")

def createlist():
    system("cls")

    print("Coloque la clase")
    _class = input()

    print("Indique cuantos alumnos tiene")
    _std = int(input())

    _stds = {
        'class' : _class,
        'stdnum': _std,
        'stud' : []
    }
    for i in range(_std):
        _name = input("Ingrese el nombre del alumno: ")
        _notesnum = int(input("Ingrese la cantidad de notas: "))
        _notes = []
        for x in range(_notesnum):
            print("=============================")
            _notes.append(int(input(f"Ingrese la nota numero {x}: ")))

        _stds['stud'].append({
            'name' : _name,
            'notes' : _notes,
            'promd' : sum(_notes) / len(_notes)
            })
        
    print("Con que nombre deseas guardar el archivo")
    _filename = input()

    print("Coloque la direccion en donde deseas guardar el archivo.")
    _path = input()

    _file = open(f"{_path}{_filename}","w")

    _file.write(json.dumps(_stds))
    _file.close()
    


def init():
    print("Coloque 1 para leer una lista")
    print("Coloque 2 para hacer una lista nueva")
    op = int(input("Opcion: "))

    if op == 1:
        print("Elegiste leer lista")
        readlist()
    elif op == 2:
        print("Elegiste crear lista")
        createlist()
    else:
        print("No seleccionaste nada")
        system("cls")

system("cls")
init()
        