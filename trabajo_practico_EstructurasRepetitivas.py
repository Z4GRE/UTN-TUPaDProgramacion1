while True:
    nombre_cliente = input("Introduzca su nombre: ")
    if nombre_cliente.isalpha():
        break
    else:
        print("El nombre que introdujo es incorrecto")

while True:
    cantidad_productos = (input("Cuantos productos desea comprar?: "))
    if  not cantidad_productos.isdigit():
        print("La cantidad que fue introducida no es posible")
        continue
    cantidad_productos = int(cantidad_productos)
    if not cantidad_productos > 0:
        print("La cantidad que fue introducida no es posible")
        continue
    break    

total = 0
total_descuentos = 0         

for i in range(cantidad_productos):
    while True:
        precio = (input(f"Cual es precio del producto numero {i + 1}?: "))
        if not precio.isdigit():
            print("El precio que fue introducida no es posible")
            continue
        precio = int(precio)
        if not precio > 0:
            print("El precio que fue introducida no es posible")
            continue
        total += precio
        break

    while True:
        descuento = input(f"El producto numero {i + 1} tiene descuento?(responda con s/n): ")
        descuento = descuento.lower()

        if "s" == descuento:
            total_descuentos += (precio * 0.9)
            break
        elif "n" == descuento:
            total_descuentos += precio
            break
        else:
            print("No ingreso una do las opciones correctas.")  

ahorro = total - total_descuentos          
promedio_productos = (total_descuentos / cantidad_productos)  
print(f"El total sin descuentos es de:         {total}$")              
print(f"El total con descuentos es de:         {total_descuentos:.2f}$")         
print(f"El ahorro total es de:                 {ahorro:.2f}$")
print(f"El precio promedio por producto es de: {promedio_productos:.2f}$")

#Ejercicio 2

usuario_correcto = "alumno"
contrasena_correcta = "python123"
intentos = 0
usuario_logueado = False
while True:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        usuario_logueado = True
        print("Acceso concedido")
        break
    else:
        if intentos == 1 or intentos == 2:    
          print("Datos incorrectos, intentelo nuevamente")
        if intentos >= 3:
          print("Demasiados intentos fallidos; Cuenta bloqueda")    
          break

if usuario_logueado:
   print("""*Menu de Opciones*
    1. *Ver estado de inscripción* 
    2. *Cambiar clave* 
    3. *Mostrar mensaje motivacional*
    4. *Salir* """)
   while True:
      opciones_numero = input("Opcion: ")

      if not opciones_numero.isdigit(): 
         print("Esa opcion no es un digito positivo.")
         continue
      
      opciones_numero = int(opciones_numero)

      if opciones_numero < 1 or opciones_numero > 4:
         print("Opcion fuera de rango.")
         continue

      if opciones_numero == 1:
         print("Usted esta inscripto.")

      if opciones_numero == 2:
         contrasena_antigua = contrasena_correcta
         contrasena_correcta = input("Nueva Clave: ")

         if len(contrasena_correcta) < 6:
            print("Error: Minimo 6 caracteres")
            contrasena_correcta = contrasena_antigua
            continue
         confirmacion = input("Confimarcion de contraseña: ")

         if confirmacion != contrasena_correcta:
            print("La contraseña y la confimacion no coinciden.")
            contrasena_correcta = contrasena_antigua
            continue

         print("Datos guardados correctamente.")

      if opciones_numero == 3:
         print("""      En las montañas de la verdad nunca escalarás en vano:
      o bien llegarás hoy más arriba, o bien ejercitarás tus fuerzas
      para poder subir más arriba mañana.""")

      if opciones_numero == 4:
         print("Saliendo...")   
         break
#Ejercio 3
while True:
  operador = input("Digame su nombre de operador: ")      

  if not operador.isalpha():
     print("---Nombre invalido---")
     continue
  break
lunes_uno    = ""
lunes_dos    = ""
lunes_tres   = ""
lunes_cuatro = ""
martes_uno   = ""
martes_dos   = ""
martes_tres  = ""

while True:
   print("""1. *Reservar turno*
2. *Cancelar turno*
3. *Ver agenda del día*
4. *Ver resumen general*
5. *Cerrar sistema* """)
   opciones_numero_turno = input("Opcion: ")

   if not opciones_numero_turno.isdigit(): 
      print("---Esa opcion no es un digito positivo---")
      continue
         
   opciones_numero_turno = int(opciones_numero_turno)
   
   if opciones_numero_turno < 1 or opciones_numero_turno > 5:
      print("---Opcion fuera de rango---")
      continue

   if opciones_numero_turno == 1:
      dia_reserva = (input("Que dia quiere reservar?(Lunes=1 Martes=2): "))
      if not dia_reserva.isdigit() or (dia_reserva != "1" and dia_reserva != "2"): 
         print("---Esa opcion no es un digito positivo o dentro del rango aceptado---")
         continue   
      paciente = input("Digame su nombre como paciente: ")
      if not paciente.isalpha():
         print("---Nombre invalido---")
         continue

      if dia_reserva == "1" and (paciente == lunes_uno or paciente == lunes_dos or
      paciente == lunes_tres or paciente == lunes_cuatro):
         print("---El paciente ya saco un turno este día---")
         continue

      if dia_reserva == "2" and (paciente == martes_uno or paciente == martes_dos or
      paciente == martes_tres):
         print("---El paciente ya saco un turno este día---")
         continue   

      if dia_reserva == "1" and lunes_uno == "": 
         lunes_uno = paciente
      elif dia_reserva == "1" and lunes_dos == "": 
         lunes_dos = paciente
      elif dia_reserva == "1" and lunes_tres == "": 
         lunes_tres = paciente
      elif dia_reserva == "1" and lunes_cuatro == "": 
         lunes_cuatro = paciente
      elif dia_reserva == "2" and martes_uno== "":
         martes_uno = paciente
      elif dia_reserva == "2" and martes_dos == "":
         martes_dos = paciente
      elif dia_reserva == "2" and martes_tres == "":
         martes_tres = paciente
      else:
         print("---No quedan reservas disponibles este dia---")
         continue  

      print("---Reserva guardada---") 
      continue  

   if opciones_numero_turno == 2: 
      dia_reserva = (input("De que dia quiere cancelar un turno?(Lunes=1 Martes=2): "))
      if not dia_reserva.isdigit() or (dia_reserva != "1" and dia_reserva != "2"): 
         print("---Esa opcion no es un digito positivo o dentro del rango aceptado---")
         continue   
      paciente = input("Digame su nombre como paciente: ")
      if not paciente.isalpha():
         print("---Nombre invalido---")
         continue

      if dia_reserva == "1" and paciente == lunes_uno:    lunes_uno      = ""
      elif dia_reserva == "1" and paciente == lunes_dos:    lunes_dos    = ""   
      elif dia_reserva == "1" and paciente == lunes_tres:   lunes_tres   = ""   
      elif dia_reserva == "1" and paciente == lunes_cuatro: lunes_cuatro = ""  
      elif dia_reserva == "2" and paciente == martes_uno:   martes_uno   = "" 
      elif dia_reserva == "2" and paciente == martes_dos:   martes_dos   = "" 
      elif dia_reserva == "2" and paciente == martes_tres:  martes_tres  = "" 
      else: print("---No se encontro ninguna reserva a ese nombre---"); continue
      print("---Reserva cancelada con exito---")

   if opciones_numero_turno == 3:  
      dia_reserva = (input("De que dia le gustaria ver la agenda?(Lunes=1 Martes=2): "))
      if not dia_reserva.isdigit() or (dia_reserva != "1" and dia_reserva != "2"): 
         print("---Esa opcion no es un digito positivo o dentro del rango aceptado---")
         continue   

      if dia_reserva == "1":
         print("---Turnos del dia Lunes---")
         if lunes_uno == "": print(f"Turno 1: *Libre*")
         else: print(f"Turno 1: *{lunes_uno}*")
         if lunes_dos == "": print(f"Turno 2: *Libre*")
         else: print(f"Turno 2: *{lunes_dos}*")
         if lunes_tres == "": print(f"Turno 3: *Libre*")
         else: print(f"Turno 3: *{lunes_tres}*")
         if lunes_cuatro == "": print(f"Turno 4: *Libre*")
         else: print(f"Turno 4: *{lunes_cuatro}*")

      if dia_reserva == "2":
         print("---Turnos del dia Martes---")   
         if martes_uno == "": print(f"Turno 1: *Libre*")
         else: print(f"Turno 1: *{martes_uno}*")
         if martes_dos == "": print(f"Turno 2: *Libre*")
         else: print(f"Turno 2: *{martes_dos}*")
         if martes_tres == "": print(f"Turno 3: *Libre*")
         else: print(f"Turno 3: *{martes_tres}*")

   if opciones_numero_turno == 4:
      turnos_libres_lunes = 0
      turnos_libres_martes = 0
   
      if lunes_uno == "":    turnos_libres_lunes  += 1
      if lunes_dos == "":    turnos_libres_lunes  += 1
      if lunes_tres == "":   turnos_libres_lunes  += 1
      if lunes_cuatro == "": turnos_libres_lunes  += 1
      if martes_uno == "":   turnos_libres_martes += 1
      if martes_dos == "":   turnos_libres_martes += 1
      if martes_tres == "":  turnos_libres_martes += 1

      print(f"El dia Lunes tiene {4 - turnos_libres_lunes} turnos ocupados y {turnos_libres_lunes} libres.")
      print(f"El dia Martes tiene {3 - turnos_libres_martes} turnos ocupados y {turnos_libres_martes} libres.")
      
      if turnos_libres_lunes > turnos_libres_martes:
         print("---El dia Lunes tiene mas turnos libres que el Martes---")
      elif turnos_libres_martes > turnos_libres_lunes:
         print("---El dia Martes tiene mas turnos libres que el Lunes---")
      else:
         print("---Tienen la misma cantidad de turnos libres---")   

   if opciones_numero_turno == 5:
      print("---Saliendo de la reserva de turnos...---")   
      break        

#Ejercicio 4  
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
contador_forzar = 0
numero_alarma = 0

while True:
    nombre_agente = input("Introduzca su nombre de agente: ")
    if nombre_agente.isalpha():
        break
    else:
        print("---El nombre que introdujo es incorrecto, solo puede contener letras---")

print(f"""---Hola {nombre_agente}, tiene que intentar abrir suficientes
cerraduras a tiempo y llegar a la boveda a tiempo---""")

while True:
   
    if cerraduras_abiertas >= 3:
        print("---Felicidades, lograste abrir las tres cerraduras y tenes acceso a la boveda---")  
        break
        
    if energia <= 0 or tiempo <= 0:
        print("---Te quedaste sin energia o tiempo para poder terminar---")
        break
    if alarma == True and tiempo <= 3:
        print("---Debido a la alarma, el sistema se a bloqueado antes de tiempo---")        
        break       

    print(f"""1. *Forzar cerradura*
2. *Hackear panel*    
3. *Descansar*
Energia restante:    |{energia}%|
Tiempo restantes:    |{tiempo} minutos|
Cerraduras abiertas: |{cerraduras_abiertas} de 3| 
""")
    
    opciones_numero_room = (input("Que accion quiere realizar?: "))
    if not opciones_numero_room.isdigit() or (opciones_numero_room != "1" and opciones_numero_room != "2" and opciones_numero_room != "3"): 
        print("---Esa opcion no es un digito positivo o dentro del rango aceptado---")
        continue  

    if opciones_numero_room == "1":
        contador_forzar += 1
        energia -= 20
        tiempo -= 2

        if contador_forzar >= 3:
            print("""---Muchos intentos seguidos de forzar cerradura
    han provocado que la cerradura se trabe---""")
            alarma = True
            print("---La alarma se ha activado---")
            continue

        if energia < 40:
            numero_alarma = input("Hay riesgo de alarma, eliga un numero de el 1 al 3: ")
            if not numero_alarma.isdigit() or (numero_alarma != "1" and numero_alarma != "2" and numero_alarma != "3"): 
                print("---Esa opcion no es un digito positivo o dentro del rango aceptado---")
                continue

        if numero_alarma == "3":
                numero_alarma = 0
                alarma = True
                print("---Elegiste el número incorrecto y se activó la alarma---")
                continue        
        numero_alarma = 0        

        cerraduras_abiertas += 1       
        print("---Se ha abierto una cerradura---")

    if opciones_numero_room == "2":
        contador_forzar = 0
        energia -= 10
        tiempo -= 3
        for i in range(4):
            letra_codigo_parcial = input("Introduzca una letra: ")

            if len(letra_codigo_parcial) != 1 :
                print("---Solo una letra es permitida---")
                continue
            if letra_codigo_parcial.isalpha() == False:
                print("---No ha introducido una letra---")
                continue

            codigo_parcial += letra_codigo_parcial

            if len(codigo_parcial) >= 8:
                print
                cerraduras_abiertas += 1
                print("---Se ha abierto una cerradura---")
                codigo_parcial = ""

    if opciones_numero_room == "3":
        contador_forzar = 0
        tiempo -= 1
        if alarma == True: energia += 5 ; print("---Se ha descansado menos debido a la alarma---")
        else: energia += 15 ; print("---Se ha descansado correctamente---")
        
        if energia > 100:
            energia = 100

#Ejercicio 5
print("/// BIENVENIDO A LA ARENA DE COMBATE \\\\\\")
while True:
    nombre_gladiador = input("Digame su nombre de Gladiador: ")
    if nombre_gladiador.isalpha():
        break
    else:
        print("---Error: Solo se permiten letras y no se permiten espacios---")

Vida_gladiador = 100   
Vida_enemigo = 100   
Pociones_vida = 3   
Daño_base_AtaquePesado = 15   
Daño_base_enemigo = 12   
Turno_gladiador = True  

while Vida_gladiador > 0 and Vida_enemigo > 0:
    print("*** NUEVO TURNO ***")
    print(f"{nombre_gladiador} (HP: {Vida_gladiador}) vs Enemigo (HP: {Vida_enemigo}) || Pociones: {Pociones_vida}")    
    while Turno_gladiador == True:
        print("""1. Ataque Pesado
2. Ráfaga Veloz
3. Curar""") 
        opciones_numero_gladiador = (input("Que accion quiere realizar?: "))
        if not opciones_numero_gladiador.isdigit() or (opciones_numero_gladiador != "1" and opciones_numero_gladiador != "2" and opciones_numero_gladiador != "3"): 
            print("---Esa opcion no es un digito positivo o dentro del rango aceptado---")
            continue

        if opciones_numero_gladiador == "1":
            if Vida_enemigo >= 20:
                Vida_enemigo -= Daño_base_AtaquePesado
                print(f"¡Atacaste al enemigo por {Daño_base_AtaquePesado} puntos de daño!")
            else:
                Vida_enemigo -= (Daño_base_AtaquePesado * 1.5)
                print(f"¡Atacaste al enemigo por {Daño_base_AtaquePesado * 1.5} puntos de daño!")
        if opciones_numero_gladiador == "2":
            print("¡Inicias una ráfaga de golpes!")
            for i in range(3):
                Vida_enemigo -= 5
                print("Golpe conectado por 5 de daño")
        if opciones_numero_gladiador == "3":
            if Pociones_vida > 0:
                Pociones_vida -= 1
                Vida_gladiador += 30
                print("¡Has recuperado 30 puntos de salud!")
                if Vida_gladiador > 100:
                    Vida_gladiador = 100
            else:
                print("¡No quedan pociones!")

        Turno_gladiador = False
        continue
    if Vida_enemigo <= 0:
        continue    
    Vida_gladiador -= Daño_base_enemigo
    print("¡El enemigo contrataca por 12 puntos de daño!")
    Turno_gladiador = True
                
if Vida_gladiador > 0:
    print("¡VICTORIA!")
    print("/// Final del Combate \\\\\\")

if Vida_gladiador <= 0:
    print("¡DERROTA!")
    print("/// Final del Combate \\\\\\")     