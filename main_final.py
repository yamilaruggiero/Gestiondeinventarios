#------Proyecto integrador Final - Pre entrega----- \
#------Mi sistema de control de inventarios, se armo en base a la empresa Lumilagro SA la cual fabrica y comercializa termos de vidrio y acero----- \

from os import system, name
import os
import funciones
from colorama import init,Fore,Style,Back
init(autoreset=True)




def saludo(): #Funcion que muestra en pantalla saludo incial al usuario 
    funciones.Bienvenido()


def menu_interactivo():  ##muestra opciones del menu interactivo, con sus opciones, para que el usuario seleccione y comience a usar el programa
    while True: 
            print("\n"+ "*" *40)     
            print(Style.BRIGHT+ Fore.CYAN + Back.WHITE+ "Menu Principal".center(40, " "))
            print("\n"+ "*" *40)               
            print(Style.BRIGHT + Fore.BLUE + "(1) Registrar producto")
            print(Style.BRIGHT + Fore.BLUE + "(2) Consultar datos de un producto")
            print(Style.BRIGHT + Fore.BLUE + "(3) Actualizar información del producto ")
            print(Style.BRIGHT + Fore.BLUE + "(4) Eliminar producto")
            print(Style.BRIGHT + Fore.BLUE + "(5) Listar todos los productos")
            print(Style.BRIGHT + Fore.BLUE + "(6) Listo de productos con stock mínimo")
            print(Style.BRIGHT + Fore.BLUE + "(7) salir del sistema")
            print("\n"+ "*" *40)  
            
            
            try:
                respuesta=int(input(Fore.CYAN + "Ingrese la opcion deseada: "))  ##pregunta que opcion desea elegir para dar comienzo al sistema
                print(Style.DIM + Fore. CYAN + "La opcion seleccionada fue: "+ str (respuesta) )
                funciones.limpiar_pantalla()

            except:
                print(Fore.RED + "No se pudo ejecutar el menu principal, elija nuevamente la opcion deseada")
                funciones.limpiar_pantalla()

            else:

                if respuesta == 1:
                        pregunta=str(input(Fore.CYAN + "¿Cual es el producto que deseas agregar ? Detalle el nombre:  ")).strip().lower
                        busqueda = funciones.consultar_nombrel(pregunta) #Funcion que busca en la dba si exite el producto por nombre
                        if busqueda != None:
                            print(Fore.RED +  "El producto que desea registrar ya existe en el inventario")
                            funciones.limpiar_pantalla()
                        else:
                            funciones.registrar_datos()
                            funciones.limpiar_pantalla()

                elif respuesta==2:
                    try:
                        funciones.buscar_prod_()
                        
                        funciones.limpiar_pantalla()
                    except Exception as e:
                        #print(e)
                        print(Fore.RED + "No se pudo ejecutar la busqueda del producto, presione enter para continuar")
                        funciones.limpiar_pantalla()
                elif respuesta==3:
                    try:
                        funciones.actualizar_producto()
                        funciones.limpiar_pantalla()
                    except:
                        print(Fore.RED + "No se pudo ejecutar la actualizacion del producto")
                        funciones.limpiar_pantalla()
                elif respuesta==4:
                    try:
                        funciones.eliminardatos_producto()
                        funciones.limpiar_pantalla()
                    except:
                        print(Fore.RED + "No se pudo ejecutar la eliminacion del producto")
                        funciones.limpiar_pantalla()

                elif respuesta==5:
                    try:
                        funciones.reporte_ejecucion()
                        funciones.limpiar_pantalla()
                    except:
                        print(Fore.RED + "Ocurrio un error, no se puedo obtener el reporte de produtos")
                        funciones.limpiar_pantalla()    
                elif respuesta==6:
                    try:
                        funciones.reporteeje_bajastock()
                        funciones.limpiar_pantalla()
                    except:
                        print(Fore.RED + "Ocurrio un error, no se puedo obtener el reporte de produtos")
                        funciones.limpiar_pantalla() 

                elif respuesta==7:

                    print(Fore.CYAN + "Saliendo del programa")
                    print(Fore.CYAN + "!Hasta luego!")
                    break
                
                else:
                    print(Fore.RED + "Opcion invalida, ingrese nuevamente un opcion valida")
            


if __name__ == "__main__": 
    saludo()
    menu_interactivo()
    

