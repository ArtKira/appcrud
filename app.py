
lista_elements=[
    {
        "id":1,
        "nombre":"Fabuloso",
        "Precio": 20,
        "cantidad": 5
    },
    {
        "id": 2,
        "nombre":"Galletas",
        "Precio": 10,
        "cantidad": 2
    }
]


def add_element():
    #agrega los elementos
    id = int(input("Ingresa el ID "))
    nombre= input("Ingresa el nombre ")
    precio= int(input("ingresa el precio "))
    cantidad= int(input("Ingresa la cantidad "))#pedimos los valores 
    product = {#creamos el objeto 
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad#pasamos los parametros 
    }
    lista_elements.append(product)#agregamos los parametros a la lista 
    pass

def remove_element():
    #for buscar
    id=int(input("Ingresa el id a ELIMINAR "))
    found = find_element(id)
    print(found)
    aceptar=input("Estas seguro de eliminar S/N")
    if aceptar == "s":
        lista_elements.remove(found)
        print("Elemento elminado")
    pass

def find_element(id):
    #for para buscar
    found =()
    for element in lista_elements:
        if element['id'] == id:
            found=element
        else:
            print("NO SE ENCUENTRA EL PRODUCTO")
    return found

def show_elements():
    #for para iterar y mostrar 
    for element in lista_elements:#iterar todos los elementos de la lista 
        for key, value in element.items():#mostramos todos los elementos 
            print(f"{key} -> {value}")#lo imprime 

def edit_element():
    #for a find para buscar
    #editar
    
    id=int(input("Ingresa el id a editar "))
    found = find_element(id)#busca los elementos 
    print(found)#lo imprime 
    nombre= input("Ingresa el nuevo nombre ")
    precio= int(input("ingresa el nuevo precio "))
    cantidad= int(input("Ingresa la cantidad nueva "))#pedimos los valores
    product = {#creamos el objeto 
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad#pasamos los parametros 
    }
    lista_elements.remove(found)#elimina lo que contiene 
    lista_elements.append(product)#agrega los nuevos elemntos 

    


if __name__ == '__main__':
     message=f"Tienda de abarrotes DU:\n  Elige la opcion\n1=Agregar Producto\n2=Mostar Producto\n3=Buscar Producto\n4=Editar Producto\n5=eliminar\n6=salir\n"
     while True:
        option=int(input(message))
        #compara cada opcion y llama a la funcion correspondiente 
        if option == 1:
            print("Inserta un producto")
            add_element()
        elif option==2:
            print("Mostar todos los productos")
            show_elements()
        elif option==3:
            print("Buscar productos")
            id =int(input("Agrega el id a buscar "))
            found = find_element(id)
            print(found)
            
        elif option==4:
            print("Editar producto")
            edit_element()
        elif option==5:
            print("Eliminar producto")
            remove_element()
        elif option == 6:
            print("BYE")
            break
        else:
            print("OPCION INCORRECTA ")
