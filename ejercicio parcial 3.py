# Definir precios de servicios
PRECIO_NOCHE = 100  # Precio por noche de estadía
PRECIO_PISCINA = 20  # Precio por uso de piscina por día
PRECIO_GOLF = 50     # Precio por uso de la cancha de golf por día

# Diccionario para almacenar los registros de clientes
registros_clientes = {}

def registrar_cliente():
    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre in registros_clientes:
            print("El cliente ya está registrado. Ingrese un nombre diferente.")
            continue
        
        try:
            noches = int(input("Ingrese el número de noches que se quedará: "))
            if noches <= 0:
                print("El número de noches debe ser mayor que cero.")
                continue
        except ValueError:
            print("El número de noches debe ser un número entero. Inténtelo de nuevo.")
            continue
        
        piscina = input("¿Desea usar la piscina? (si/no): ").lower() == 'si'
        golf = input("¿Desea usar la cancha de golf? (si/no): ").lower() == 'si'
        
        registros_clientes[nombre] = {
            'noches': noches,
            'piscina': piscina,
            'golf': golf
        }
        print(f"Cliente {nombre} registrado con éxito.")
        break

def calcular_total(noches, piscina, golf):
    costo_noche = noches * PRECIO_NOCHE
    costo_piscina = (PRECIO_PISCINA if piscina else 0) * noches
    costo_golf = (PRECIO_GOLF if golf else 0) * noches
    total = costo_noche + costo_piscina + costo_golf
    return total

def mostrar_registros():
    if not registros_clientes:
        print("No hay registros de clientes.")
        return
    
    print("\nRegistro de Clientes:")
    for cliente, datos in registros_clientes.items():
        total = calcular_total(datos['noches'], datos['piscina'], datos['golf'])
        print(f"\nCliente: {cliente}")
        print(f"Noches: {datos['noches']}")
        print(f"Uso de piscina: {'Si' if datos['piscina'] else 'si'}")
        print(f"Uso de cancha de golf: {'Si' if datos['golf'] else 'No'}")
        print(f"Total a pagar: ${total:.2f}")

def main():
    print("Sistema de Registro de Clientes para Hotel de Playa")
    while True:
        print("\nOpciones:")
        print("1. Registrar cliente")
        print("2. Mostrar registros")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            mostrar_registros()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
