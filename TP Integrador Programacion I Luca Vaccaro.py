# Consigna 1
nombre = ""
while not nombre.isalpha():
    nombre = input("Cliente: ")

cantidad_str = ""
while not cantidad_str.isdigit() or int(cantidad_str) <= 0:
    cantidad_str = input("Cantidad de productos: ")
cantidad = int(cantidad_str)

total_sin_desc = 0
total_con_desc = 0.0

for i in range(1, cantidad + 1):
    print(f"Producto {i}")
    precio_str = ""
    while not precio_str.isdigit() or int(precio_str) <= 0:
        precio_str = input("Precio: ")
    precio = int(precio_str)
    
    desc = ""
    while desc.lower() not in ["s", "n"]:
        desc = input("Descuento (S/N): ").lower()
    
    total_sin_desc += precio
    if desc.lower() == "s":
        total_con_desc += precio * 0.9
    else:
        total_con_desc += precio

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# Consigna 2
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
ingresado = False

while intentos < 3 and not ingresado:
    intentos += 1
    print(f"Intento {intentos}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        ingresado = True
    else:
        print("Error: credenciales inválidas.")

if not ingresado:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")
        
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error: ingrese un número válido o fuera de rango.")
        else:
            if opcion == "1":
                print("Inscripto")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                else:
                    confirmacion = input("Confirmar clave: ")
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave actualizada correctamente.")
                    else:
                        print("Error: las claves no coinciden.")
            elif opcion == "3":
                print("¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!")

# Consigna 3 
operador = ""
while not operador.isalpha():
    operador = input("Nombre del operador: ")

l1, l2, l3, l4 = "", "", "", ""
m1, m2, m3 = "", "", ""

opcion = ""
while opcion != "5":
    print("1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema")
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        dia = ""
        while dia not in ["1", "2"]:
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")
            
        if dia == "1":
            if paciente in [l1, l2, l3, l4] and paciente != "":
                print("Paciente ya tiene turno el Lunes.")
            elif l1 == "": l1 = paciente
            elif l2 == "": l2 = paciente
            elif l3 == "": l3 = paciente
            elif l4 == "": l4 = paciente
            else: print("No hay cupos el Lunes.")
        elif dia == "2":
            if paciente in [m1, m2, m3] and paciente != "":
                print("Paciente ya tiene turno el Martes.")
            elif m1 == "": m1 = paciente
            elif m2 == "": m2 = paciente
            elif m3 == "": m3 = paciente
            else: print("No hay cupos el Martes.")
            
    elif opcion == "2":
        dia = ""
        while dia not in ["1", "2"]:
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente a cancelar: ")
            
        if dia == "1":
            if l1 == paciente: l1 = ""
            elif l2 == paciente: l2 = ""
            elif l3 == paciente: l3 = ""
            elif l4 == paciente: l4 = ""
            else: print("Paciente no encontrado.")
        elif dia == "2":
            if m1 == paciente: m1 = ""
            elif m2 == paciente: m2 = ""
            elif m3 == paciente: m3 = ""
            else: print("Paciente no encontrado.")
            
    elif opcion == "3":
        dia = ""
        while dia not in ["1", "2"]:
            dia = input("Elegir día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Turno 1: {l1 if l1 else '(libre)'}")
            print(f"Turno 2: {l2 if l2 else '(libre)'}")
            print(f"Turno 3: {l3 if l3 else '(libre)'}")
            print(f"Turno 4: {l4 if l4 else '(libre)'}")
        else:
            print(f"Turno 1: {m1 if m1 else '(libre)'}")
            print(f"Turno 2: {m2 if m2 else '(libre)'}")
            print(f"Turno 3: {m3 if m3 else '(libre)'}")
            
    elif opcion == "4":
        ocupados_lunes = 0
        if l1 != "": ocupados_lunes += 1
        if l2 != "": ocupados_lunes += 1
        if l3 != "": ocupados_lunes += 1
        if l4 != "": ocupados_lunes += 1
        
        ocupados_martes = 0
        if m1 != "": ocupados_martes += 1
        if m2 != "": ocupados_martes += 1
        if m3 != "": ocupados_martes += 1
        
        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres.")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres.")
        
        if ocupados_lunes > ocupados_martes: print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes: print("Día con más turnos: Martes")
        else: print("Ambos días tienen la misma cantidad de turnos ocupados.")

# Consigna 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del agente: ")

racha_forzar = 0

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print(f"\nEstado: Energía {energia} | Tiempo {tiempo} | Cerraduras abiertas {cerraduras_abiertas}")
    print("1. Forzar cerradura\n2. Hackear panel\n3. Descansar")
    
    opcion = input("Acción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        opcion = input("Acción (1-3): ")
        
    if opcion == "1":
        racha_forzar += 1
        energia -= 20
        tiempo -= 2
        
        if racha_forzar == 3:
            alarma = True
            print("¡Alarma activada! La cerradura se trabó por forzar repetidamente.")
        else:
            if energia < 40:
                riesgo = ""
                while not riesgo.isdigit() or riesgo not in ["1", "2", "3"]:
                    riesgo = input("Riesgo de alarma, ingrese un número (1-3): ")
                if riesgo == "3":
                    alarma = True
                    print("¡Alarma activada!")
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")
                
    elif opcion == "2":
        racha_forzar = 0
        energia -= 10
        tiempo -= 3
        print("Hackeando panel...")
        for _ in range(4):
            codigo_parcial += "A"
            print(f"Progreso... código actual: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = "" 
            print("¡Panel hackeado, cerradura abierta!")
            
    elif opcion == "3":
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
        print("Descansando para recuperar energía...")

if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA. Sistema bloqueado por alarma.")
elif cerraduras_abiertas == 3:
    print("VICTORIA. ¡Has abierto la bóveda!")
else:
    print("DERROTA. Te quedaste sin energía o sin tiempo.")

# Consigna 5
nombre = ""
while not nombre.isalpha():
    nombre = input("Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("Error: Solo se permiten letras.")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")
    
    opcion = input("Opción: ")
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")
        
    if opcion == "1":
        dano_final = float(dano_pesado)
        if vida_enemigo < 20:
            dano_final = dano_pesado * 1.5
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {int(dano_final)} puntos de daño!")
        
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for _ in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion == "3":
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
            print("¡Te has curado!")
        else:
            print("¡No quedan pociones!")
            
    if vida_enemigo > 0:
        vida_gladiador -= dano_enemigo
        print(f"¡El enemigo te atacó por {dano_enemigo} puntos de daño!")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")


