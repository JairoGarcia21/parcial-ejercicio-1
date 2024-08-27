def registrar_compras():
    compras = []
    while True:
        producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
        if producto.lower() == 'fin':
            break
        try:
            precio = float(input(f"Ingrese el precio de {producto}: "))
        except ValueError:
            print("El precio debe ser un número. Inténtelo de nuevo.")
            continue
        
        compras.append((producto, precio))
    return compras

def calcular_total(compras):
    total = sum(precio for _, precio in compras)
    return total

def calcular_cambio(total, billete):
    if billete < total:
        print("El billete no es suficiente para cubrir el total.")
        return None
    return billete - total

def main():
    print("Registro de compras")
    compras = registrar_compras()
    total = calcular_total(compras)
    
    print("\nResumen de compras:")
    for producto, precio in compras:
        print(f"{producto}: ${precio:.2f}")
    
    print(f"\nTotal a pagar: ${total:.2f}")
    
    try:
        billete = float(input("Ingrese el valor del billete con el que va a pagar: "))
    except ValueError:
        print("El valor del billete debe ser un número.")
        return
    
    cambio = calcular_cambio(total, billete)
    
    if cambio is not None:
        print(f"El cambio a devolver es: ${cambio:.2f}")

if __name__ == "__main__":
    main()
