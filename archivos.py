    #abrir open 
    #procesar read/write
    #cerrar close()
    #with nos perimite agrupar trabajo con archivos 

def leer_archivo(file_name):
    print("intentas abrir este archivo ", file_name)
    with open(file_name,  'r') as file:
        lineas=file.readlines()
        for linea in lineas:
            print(linea) 

def agregar_equipo(file_name, equipo):
    with open(file_name, 'a') as file:
        file.write(equipo)
    print("equipo guardado")
    
def eliminar_equipo(file_name, equipo):
    with open(file_name, 'r') as file:
        lista_equipos=file.readlines()
    try:
        lista_equipos.remove(equipo)
        print("equipo eliminado")
        with open(file_name, 'w') as file:#si ocurre guarda los cambios 
            file.writelines(lista_equipos)
    except ValueError:
        print("El equipo que deseas eliminar no existe")
        
def actualizar_equipo(file_name, equipo, new_equipo):
    with open(file_name, 'r')as file:
        lista_equipos=file.readlines()
    try:
        index_equipo=lista_equipos.index(f'{equipo}')#busca el equipo para despues actualizar el equipo 
        lista_equipos[index_equipo]=new_equipo
        with open(file_name, 'w') as file:#si ocurre guarda los cambios 
            file.writelines(lista_equipos)
    except ValueError:
        print("El equipo no se encuentra")