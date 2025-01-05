#Modulo donde se encuentran las funciones de la DBA y funciones secundarias para validaciones e importaciones de modulos 
import os
import time

import sqlite3
import re
from colorama import init,Fore,Style,Back
init(autoreset=True)

categorias = {  # diccionario de categorias a mostrar en mi programa 

    1: 'acero',

    2: 'vidrio',

    3: 'isotermico'

    }


numero_columna= {  # en la funcion de busqueda se puede buscar por columna. diccionario de columnas 
    1: "Codigounico",
    2: "Nombre",
    3: "FechadeAlta",
    4: "Categoria"
    }

dic_campos= {

    1: 'Nombre',
    2: 'Descripcion',
    3: 'Cantidad',
    4: 'Precio',
    5: 'Categoria'
    }



def limpiar_pantalla(): #limpiar consola por tiempo 5 segundos 
    print(Style.DIM + Fore.CYAN + "Enter para continuar")

    while input() is None:
        pass
    if os.name == "nt":

        os.system("cls")

    else:

        os.system("clear")


def limpiar_pantalla1(): #limpiar consola por tiempo 2 segundos

    time.sleep(2)

    if os.name == "nt":

        os.system("cls")

    else:

        os.system("clear")


def Bienvenido(): #funcion se saludo incial al programa que se muestra al usuario

    print(Style.BRIGHT+ Fore.CYAN + Back.LIGHTBLACK_EX+"Lumilagro S.A".center(40, " "))

    print("\n"+ Style.BRIGHT + Fore.CYAN + Back.LIGHTCYAN_EX+ "Sistema de control del inventorio".center(40, " ") + "\n")

    limpiar_pantalla()

                #saludo de ingreso, se utilizo una funcion para incializar con el nombre del usuario

    name = input(Fore.CYAN + "Bienvenido,cual es tu nombre: ")

    limpiar_pantalla() 

    if len(name)>0:

        print (Fore.CYAN +"\nBienvenido " + str(name) + "," + " seleccione una opcion:  \n ") 

    else:

        print(Fore.CYAN + "\nBienvenido, Seleccione una opcion:\n") 


def validacion_minus(palabra): #Funciona de ayuda para realizar validacion sencilla de si una palabra esa en minuscula

    if palabra.islower()==True:

        palabra=palabra

    else:

        palabra= palabra.lower()

    print(palabra)

    return palabra


def registrar_datos():  #Funcion principal de mi programa donde se tiene input solicitando data al usuario para el registro de producto- Cada input tiene sus correspondientes validaciones para que la app no crashee


    while True:

        try:

            codigouni=int(input(Fore.CYAN + "Ingrese un código único asociado al producto: "))

            numeros_validos1= list(range(1,100))

            if codigouni in numeros_validos1:

                codigouni=codigouni

                break

            else:

                print(Fore.RED + "El campo código  único no puede estar vacío, ni contenter letras y tampoco números negativos")            


        except (ValueError, TypeError):
            

            print(Fore.RED + "El campo código  único  no puede estar vacío, ni contenter letras y tampoco números negativos")


        finally:

            limpiar_pantalla()

    while True:    

        nombre_producto=str(input(Fore.CYAN + "Ingrese el nombre del producto:  ")).strip().lower() 

        x= re.search("[0-9]",nombre_producto) is None

        if x ==False or len(nombre_producto)<=1:

                print(Fore.RED + "El nombre del producto no puede contener números y tampoco puede estar vacío")

                limpiar_pantalla()

        else:

            nombre_producto=nombre_producto   

            limpiar_pantalla()  

            break
            
                    

    while True:

        descripcion=str(input(Fore.CYAN + "Ingrese la descripcion del producto: ")).strip().lower() 

        x= re.search("[0-9]",descripcion) is None

        if x ==False:

                print(Fore.RED + "La descripcion del producto no puede contener números")     

                limpiar_pantalla()       

        else: 

            descripcion=descripcion

            limpiar_pantalla()

            break
            
        

    while True:

        try:

            cantidad=int(input(Fore.CYAN + "Ingrese la cantidad del producto a registrar: "))

            numeros_validos= list(range(1,100))


            if cantidad in numeros_validos:

                cantidad=cantidad

                limpiar_pantalla()

                break
                


            else:

                print(Fore.RED + "El campo cantidad no puede estar vacío , ni contenter letras y tampoco números  negativos")
                limpiar_pantalla

        except ValueError:

                print(Fore.RED + "El campo cantidad no puede estar vacío , ni contenter letras y tampoco números  negativos")
                limpiar_pantalla


    while True:

        try:

            precio=float(input(Fore.CYAN + "Ingrese el precio del producto: "))

            if precio>0:

                precio=precio

                limpiar_pantalla()

                break

            else:

                print(Fore.RED + "El campo precio no puede estar vacío, ni contenter letras y tampoco números negativos")

        except ValueError:

            print(Fore.RED + "El campo precio no puede estar vacío, ni contenter letras y tampoco números negativos")
            limpiar_pantalla

    while True:

        try:

            FechadeAlta=str(input(Fore.CYAN + "Ingrese la fecha de alta del producto: "))

            if len(FechadeAlta)>0:

                FechadeAlta=FechadeAlta

                limpiar_pantalla()

                break

            else:

                print(Fore.RED + "El campo Fecha de alta cio no puede estar vacio")
                limpiar_pantalla

        except ValueError:

            print(Fore.RED + "El campo precio no puede estar vacio")
            limpiar_pantalla


    while True:

        print(Style.BRIGHT + Fore.CYAN + Back.LIGHTCYAN_EX + "Las Categorías válidas a seleccionar son: ")

        for k, v in categorias.items():

            print(k, ':' ,v)

        categoria = int(input(Fore.CYAN + "Ingrese nombre de Categoría que desea seleccionar: "))

        if categoria in categorias.keys():

            categoria=categorias.get(categoria, "")

            limpiar_pantalla()

            break

        else:

            print(Fore.RED + "La categoría ingresada no corresponde a ninguna de las mencionadas, ingrese una opción valida")

            limpiar_pantalla()


    try:

        registrar_productos_dba(codigouni,nombre_producto,descripcion,cantidad,precio,FechadeAlta,categoria)

        print(Fore.GREEN + "El registro se realizo correctamente")

    except:

        print(Fore.RED + "Ocurrio un error al guardar los datos en la base, intentar nuevamente")

        
def buscar_prod_(): #busqueda de producto seleccionando campo de busqueda, que seria la columna de mi DB y ingresando el valor de busqueda
    while True:
        print(Style.BRIGHT + Fore.CYAN + Back.LIGHTCYAN_EX + "Los campos validos para realizar la busqueda son: ")

        for k, v in numero_columna.items():

            print(k, ':' ,v)

        campo = int(input(Fore.CYAN + "Ingrese el codigo del campos que desea seleccionar: "))
        if campo in numero_columna.keys():
            print(Fore.CYAN + "El campo ingresado para la busqueda es: "+ str (campo))
            campo=campo

                        
            break
        else:

            print(Fore.RED + "El campo ingresado no corresponde a ninguna de las opciones disponibles en sistema, debe estar identico que en la lista impresa. ingrese una opción valida")

    while True: 
        
        try:
            if campo  == 1:
                pregunta=int(input(Fore.CYAN + "Detalle el código único producto a buscar: "))
                print(Fore.CYAN + "El dato ingresado es: "+ str (pregunta))
                

                break 
            else:
                pregunta=str(input(Fore.CYAN + "Detalle el dato del producto buscado: ")).strip().lower() 
                print(Fore.CYAN + "El dato ingresado es: "+ str (pregunta))

                break
        except Exception as e:
            #print(e)
            print(Fore.RED + "No se pudo ejecutar la consulta del campo y el dato del producto ingresado")

    try:
        consultar_campo(campo,pregunta)
    except Exception as e:
        #print(e)
        print(Fore.RED + "Ocurrio un error al realizar la busqueda en el sistema. Vuelva a intentarlo")    


def actualizar_producto():  #funcion de actualizar datos del producto. 
    while True: #pide un codigo unico con un ciclo hasta que el usuario lo ingrese correctamente 
        try:
            id_producto = int(input(Fore.CYAN + "Ingrese el codigo unico del producto a actualizar: "))
            
            numeros_validos1= list(range(1,100))

            if id_producto in numeros_validos1:

                id_producto=id_producto
                
                break

            else:

                print(Fore.RED + "El campo código único no puede estar vacío, ni contenter letras y tampoco números negativos")   
        except ValueError:

                print(Fore.RED + "El campo código único no puede estar vacío, ni contenter letras y tampoco números negativos")
    while True:
        print(Fore.CYAN + "Los campos que puede modificar son: ")

        for k, v in dic_campos.items():

            print(k, ':' ,v)

        campos = int(input(Fore.CYAN + "Ingrese el campo que desea modificar: "))

        if campos in dic_campos.keys():

            campos=campos

            limpiar_pantalla()

            break

        else:

            print(Fore.RED + "El campo ingresada no corresponde a ninguna de las opciones disponibles en sistema, ingrese una opción valida")

            limpiar_pantalla()
    while True:
        try:
            if campos  == 1:
                try:
                    nuevo_valor=str(input (Fore.CYAN + "Ingrese el nuevo nombre del producto: ")).strip().lower() 

                    x= re.search("[0-9]",nuevo_valor) is None 

                    if x ==False or len(nuevo_valor)<=1:
                            print(Fore.RED + "El nombre no puede estar vacio, ingreselo nuevamente ni contener numeros")
                            limpiar_pantalla()     

                    else: 
                        nuevo_valor=nuevo_valor

                        limpiar_pantalla()

                        break
                    
                except:
                    print(Fore.RED  + "Ocurrio un error al ingresar el nombre del producto")
            elif campos==2:
                try:
                    nuevo_valor=str(input (Fore.CYAN + "Ingrese la nueva descripcion del producto: ")).strip().lower() 
                    x= re.search("[0-9]",nuevo_valor) is None 

                    if x ==False: 
                        print(Fore.RED + "La descripcion del producto no puede contener números") 
                        limpiar_pantalla()
                        
                    else:
                        nuevo_valor=nuevo_valor
                        break
                except:
                    print(Fore.RED + "Ocurrio un error al ingresar la descripcion del producto")

            elif campos ==3:
                try:
                    nuevo_valor=int(input(Fore.CYAN + "Ingrese la nueva cantidad del producto: "))
                    numeros_validos1= list(range(1,1000))

                    if nuevo_valor in numeros_validos1:

                        nuevo_valor=nuevo_valor             
                        limpiar_pantalla()
                        break

                except:
                    print(Fore.RED + "Ocurrio un problema al ingresar la nueva cantidad del producto")

            elif campos == 4 :
                try:
                    nuevo_valor=float(input(Fore.CYAN + "Ingrese el nuevo precio del producto: "))

                    if nuevo_valor > 0:

                        nuevo_valor=nuevo_valor

                        limpiar_pantalla()

                        break
                    
                    else:
                        print(Fore.RED + "El campo precio no puede estar vacío, ni contenter letras y tampoco números negativos")
                        limpiar_pantalla()
                except ValueError:

                    print(Fore.RED + "El campo precio no puede estar vacío, ni contenter letras y tampoco números negativos")

            else:
                try:
                    print(Style.BRIGHT + Fore.CYAN + Back.LIGHTCYAN_EX + "Las Categorías válidas a seleccionar son: ")

                    for k, v in categorias.items():

                        print(k, ':' ,v)

                    nuevo_valor= int(input(Fore.CYAN + "Ingrese la nueva de Categoría que desea asociada al producto: "))

                    if nuevo_valor in categorias.keys():

                        nuevo_valor=categorias.get(nuevo_valor, "")

                        limpiar_pantalla()
                        break
                    else:

                        print(Fore.RED + "La categoría ingresada no corresponde a ninguna de las disponibles en sistema, ingrese una opción valida")
                        limpiar_pantalla()
                except:
                    print("Ocurrio un error al ingresar la nueva categoria, intentelo nuevamente")
        except:
            print(Fore.RED + "Ocurrio un problema, no se pudo ingresar el nuevo valor")
            limpiar_pantalla()

    try:
        x= consulta_id(id_producto)
        if x is None:
            print(Fore.RED + "El producto que esta buscando no se encuentra en el sistema")
        
        else:
            modificacion_db(id_producto,campos,nuevo_valor)
            print(Fore.GREEN + "El producto con codigo unico " + str (id_producto) +" se modifico correctamente")
        
            consulta_id2(id_producto)
            
    except:
        print(Fore.RED + "No se pudo realizar la modificacion de los datos")

def eliminardatos_producto(): #funion del main donde pide en dato al usuario y ejecuta la funcion de la DB
    while True: #pide un codigo unico con un ciclo hasta que el usuario lo ingrese correctamente 
        try:
            id_producto = int(input(Fore.CYAN + "Ingrese codigo unico del producto a Eliminar: "))

            numeros_validos1= list(range(1,1000))

            if id_producto in numeros_validos1:

                id_producto=id_producto
                break

            else:

                print(Fore.RED + "El campo código  único no puede estar vacío, ni contenter letras y tampoco números negativos")   
        except ValueError:

                print(Fore.RED + "El campo código  único no puede estar vacío, ni contenter letras y tampoco números negativos")
    try:
        eliminar_producto(id_producto)
        print(Fore.GREEN + "El producto con codigo unico" +" " + str( id_producto ) +" se elimino correctamente del sistema")
    except:
        print(Fore.RED + "Ocurrio un error, no se pudo realizar la eliminacion del producto, vuelva a intentarlo")

def reporte_ejecucion(): #funcion del main que imprime los registros 
    x = reporte()

    if x is None:
        print(Fore.RED + "\n","No existen productos creados en el sistema".center(60,"*"),"\n")

    else:
        texto=""
        print(Fore.CYAN + "\n","REPORTE DE PRODUCTOS EN STOCK" .center(60,"*"),"\n")
        print(Fore.CYAN + "ID COD    NOMBRE    DESCRIPCION    CANTIDAD    PRECIO    FECHA DE ALTA    CATEGORIA".center(60,"*"))
        print(Fore.CYAN + "\n== ===    ======    ===========    ========    ======    =============    =========".center(60,"*"),"\n")
        for campo in x:
            texto = texto + str(campo)+ " -  "
        
        print(Fore.CYAN + texto)
    

def reporteeje_bajastock(): #funcion del main que imprime los registros 
    while True:

        try:
            
            limite=int(input(Fore.CYAN + "Ingrese un valor de stock minimo: "))

            numeros_validos1= list(range(1,1000))

            if limite in numeros_validos1:

                limite=limite
                
            else:

                print(Fore.RED + "El campo limite no puede estar vacíos")
                limpiar_pantalla()

        except (ValueError, TypeError):
            

            print(Fore.RED + "El campo código  único  no puede estar vacío, ni contenter letras y tampoco números negativos")
            limpiar_pantalla()
            

        try:
            x=reporte_bajo_stock(limite)
            if x is None:
                print(Fore.RED + "\n","No existen productos con menos stock que el indicado".center(60,"*"),"\n")
                limpiar_pantalla()


            else:
                print(Fore.CYAN + "\n","REPORTE DE PRODUCTOS EN STOCK" .center(60,"*"),"\n")
                print(Fore.CYAN + "ID COD    NOMBRE    DESCRIPCION    CANTIDAD    PRECIO    FECHA DE ALTA    CATEGORIA".center(60,"*"))
                print(Fore.CYAN + "\n== ===    ======    ===========    ========    ======    =============    =========".center(60,"*"),"\n")
                for producto in x:
                    print(producto)

            break

        except:
            print("Ocurrio un error, vuelva a intentarlo")
            limpiar_pantalla()

#Apartado de base datos ###

#Funciones para manipular  la DBA de SQLITE3 # MI dba es: inventariolumilagro.db y mi tabla: productos

def inicializar_bd(): #intruccion de crear la DB de inventariolumilagro y su tabla productos. Si la misma no esta creada la funciona la crea si no, no se ejecuta accion 

        conexion = sqlite3.connect('inventariolumilagro.db')

        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS productos (

                    id INTEGER PRIMARY KEY AUTOINCREMENT, 

                    Codigounico INTEGER NOT NULL,

                    Nombre TEXT NOT NULL,

                    Descripcion TEXT,

                    Cantidad INTEGER NOT NULL,

                    Precio  REAL NOT NULL,

                    FechadeAlta TEXT NOT NULL,

                    Categoria TEXT NOT NULL)''')

        conexion.commit()

        conexion.close()

def registrar_productos_dba(Codigounico, Nombre, Descripcion, Cantidad,Precio, FechadeAlta,Categoria):  #Se solicita los siguientes datos para ingresar registros nuevos a la DBA, la funcion requiere de parametros para ejecurtarse. 

    conexion = sqlite3.connect('inventariolumilagro.db')

    cursor = conexion.cursor()

    query = """ INSERT INTO productos (`Codigounico`, `Nombre`, `Descripcion`, `Cantidad`, `Precio`, `FechadeAlta`, `Categoria`)

        VALUES (?, ?, ?, ?, ?, ?, ?) 
    """    
    jls_extract_var = Precio
    cursor.execute(query, (Codigounico, Nombre, Descripcion, Cantidad, Precio, FechadeAlta, Categoria))

    conexion.commit()

    conexion.close()

def consultar_nombrel(Nombre): # Funcion donde se evalua un valor ingresado como parametro y se busca dentro de la tabla en la columna nombre, si el valor esta, devuelve los resultados encontrados y si no esta devuelve ese msj 

    conexion = sqlite3.connect('inventariolumilagro.db')

    cursor = conexion.cursor()

    query = f"SELECT * FROM productos WHERE Nombre = '{Nombre}'"

    cursor.execute(query)

    fila = cursor.fetchone()

    if fila != None: 

        print(fila)

    else:

        print(Fore.RED + "El producto que esta buscando no se encuentra en el sistema")
    

    return fila

    conexion.close()

def consultar_campo(campo,pregunta): #funcion que busca en la DB dentro de una columna definida por el usuario y el valor o parametro ingresado por el usuario 
    conexion = sqlite3.connect('inventariolumilagro.db')

    cursor = conexion.cursor()

    opcion = numero_columna.get(campo, "")

    query = f"SELECT * FROM productos WHERE {opcion} =  ?"

    cursor.execute(query,(pregunta,))

    fila = cursor.fetchone()

    if fila != None: 
        texto=""
        print(Fore.CYAN + "\n","REPORTE DE PRODUCTOS EN STOCK" .center(60,"*"),"\n")
        print(Fore.CYAN + "ID COD    NOMBRE    DESCRIPCION    CANTIDAD    PRECIO    FECHA DE ALTA    CATEGORIA".center(60,"*"))
        print(Fore.CYAN + "\n== ===    ======    ===========    ========    ======    =============    =========".center(60,"*"),"\n")
        for campo in fila:
            texto = texto + str(campo)+ " -  "
        #texto = texto[:]
        
        print(Fore.CYAN + texto)

    else:

        print(Fore.RED + "El producto que esta buscando no se encuentra en el sistema")
    

    return fila

    conexion.close()

def consulta_id(codigouni): #Funciona que buscar en la tabla, columna codigounico, por el valor indicado por el usuario

    conexion = sqlite3.connect('inventariolumilagro.db')

    cursor = conexion.cursor()

    query = f"SELECT * FROM productos WHERE Codigounico = '{codigouni}'"

    cursor.execute(query)

    fila = cursor.fetchone()

    if fila != None: 
        fila=fila
    else:
        print(Fore.RED + "El producto que esta buscando no se encuentra en el sistema")
    
    return fila
    conexion.close()

def consulta_id2(codigouni): #Funciona que buscar en la tabla, columna codigounico, por el valor indicado por el usuario

    conexion = sqlite3.connect('inventariolumilagro.db')

    cursor = conexion.cursor()

    query = f"SELECT * FROM productos WHERE Codigounico = '{codigouni}'"

    cursor.execute(query)

    fila = cursor.fetchone()
    
    filalist=[]

    while (len(fila)):
        filalist.append([i])
   


"""   if fila != None: 
        texto=""
        print(Fore.CYAN + "\n","REPORTE DE PRODUCTOS EN STOCK" .center(60,"*"),"\n")
        print(Fore.CYAN + "ID COD    NOMBRE    DESCRIPCION    CANTIDAD    PRECIO    FECHA DE ALTA    CATEGORIA".center(60,"*"))
        print(Fore.CYAN + "\n== ===    ======    ===========    ========    ======    =============    =========".center(60,"*"),"\n")
        for campo in fila:
            texto = texto + str(campo)+ " -  "
        
        print(Fore.CYAN + texto)
    else:

        print(Fore.RED + "El producto que esta buscando no se encuentra en el sistema")
    conexion.close()"""



def modificacion_db(Codigounico,campos,nuevo_valor): #funcion de update, modificacion de datos que el usuario indique por medio de un input 
    conexion = sqlite3.connect('inventariolumilagro.db')
    cursor = conexion.cursor()
    opcion = dic_campos.get(campos, "")

    query = f'UPDATE productos SET {opcion} = ? WHERE Codigounico = ?'
    cursor.execute(query, (nuevo_valor,Codigounico))
    conexion.commit()
    conexion.close()

def eliminar_producto(id_producto): #se elimina el registro del producto de la db ingresando el CODIGO UNICO 
    conexion = sqlite3.connect('inventariolumilagro.db')
    cursor = conexion.cursor()
    query = '''DELETE FROM productos WHERE Codigounico = ?'''
    query2= '''ALTER TABLE productos id = 1 '''
    cursor.execute(query, (id_producto, ))

    conexion.commit()
    conexion.close()



def reporte(): #consulta general de la db y tabla para funicion de reportes 
    conexion = sqlite3.connect('inventariolumilagro.db')
    cursor = conexion.cursor()
    query = f"SELECT * FROM productos"
    cursor.execute(query)
    resultados = cursor.fetchall()
    
    conexion.close()
    return resultados


def reporte_bajo_stock(limite): #consulta general de la db y tabla para funicion de reportes con un limite de stock ingresando por el usuario 
    conexion = sqlite3.connect('inventariolumilagro.db')
    cursor = conexion.cursor()
    query = f"SELECT * FROM productos productos WHERE cantidad <= ?"
    cursor.execute(query, (limite, ))
    resultados = cursor.fetchall()

    conexion.close()

    return resultados



"""
if __name__ == "__main__":

    #inicializar_bd()

    #registrar_productos(110, "Tango", "Rojo", 10, 1550.2, "10/02/2016", "Vidrio")

    #consultar_nombrel("tango")

    #validacion_minus("TABLA")

    #registrar_datos()

    #registrar_productos_dba(23,"jarra","verde",45,1087.52,"27/10/2020","vidrio")
    #buscar_prod_()
    #onsultar_campo("Nombre","tango"
    #consulta_id(23)
    #modificacion_db(codigounico,campo,nuevo_valor)
    #actualizar_producto()
    #eliminardatos_producto()
    #reporte_ejecucion()
    #reporte_bajo_stock(10)
    #reporte_ejecucion()
    #reporte_bajo_stock(10)"""