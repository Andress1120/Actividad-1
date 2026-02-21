# Titulo
print("=== SISTEMA DE ACCESO ===")

# Variabale principal
contrasena_correcta = "HolaMundo"

# Crear variables de control
intentos = 0
acceso = False

# Bucle
while intentos < 3 and acceso == False:
    
# Pedido de datos la user    
    contrasena = input("Ingresa la contraseña: ")

# Condional por si se cumple o no    
    if contrasena == contrasena_correcta:
        print("Acceso concedido.")
        acceso = True
    else:
        print("Contraseña incorrecta.")
        intentos = intentos + 1

# Verificar si se bloqueó
if acceso == False:
    print("Cuenta bloqueada. Demasiados intentos.")

# Mensaje final
print("Fin del programa.")

