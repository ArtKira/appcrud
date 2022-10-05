lista_elements=[]


def add_element():
    pass
def remove_element():
    pass
def show_element():
    pass
def show_elements():
    pass
def edit_element():
    pass


if __name__ == '__main__':
     message=f"Tienda de abarrotes:\n  Elige la opcion\n 1=Buscar Producto\n  2=Editar Producto\n  3=Elimina Producto\n 4=Registrar Producto\n 5=Salir"
     while True:
        option=int(input(message))
        #compara cada opcion y llama a la funcion correspondiente 
        if option == 1:
            #pedir numeros al usuario 
            ##numeros=return_values()
            
        elif option== 2:
            #pedir numeros al usuario 
            ##numeros=return_values()
            
        elif option==3:
            #pedir numeros al usuario
            ##numeros=return_values() 
           
        elif option==4:
            #pedir numeros al usuario
            ##numeros=return_values() 
            
        elif option == 5:
            print("BYE")
            break
        else:
            print ("Opcion incorrecta")