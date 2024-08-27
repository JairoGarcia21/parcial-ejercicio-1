import datetime

# Diccionario para almacenar los registros de asistencia
registros_asistencia = {}

def registrar_asistencia():
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        
        tipo_asistencia = input("Ingrese el tipo de asistencia (asistencia/permiso/inasistencia): ").lower()
        
        if tipo_asistencia == "permiso":
            razon = input("Ingrese la razón del permiso: ")
            registros_asistencia[nombre] = {
                'fecha': datetime.date.today().strftime("%Y-%m-%d"),
                'tipo': tipo_asistencia,
                'razon': razon
            }
        elif tipo_asistencia in ["asistencia", "inasistencia"]:
            registros_asistencia[nombre] = {
                'fecha': datetime.date.today().strftime("%Y-%m-%d"),
                'tipo': tipo_asistencia
            }
        else:
            print("Tipo de asistencia no válido. Inténtelo de nuevo.")
            continue

def mostrar_registros():
    if not registros_asistencia:
        print("No hay registros de asistencia.")
        return
    
    print("\nRegistro de Asistencia:")
    for estudiante, datos in registros_asistencia.items():
        if datos['tipo'] == 'permiso':
            print(f"{estudiante}: {datos['tipo'].capitalize()} - Razón: {datos['razon']} - Fecha: {datos['fecha']}")
        else:
            print(f"{estudiante}: {datos['tipo'].capitalize()} - Fecha: {datos['fecha']}")

def main():
    print("Registro de Asistencia de Estudiantes")
    while True:
        print("\nOpciones:")
        print("1. Registrar asistencia")
        print("2. Mostrar registros")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            registrar_asistencia()
        elif opcion == '2':
            mostrar_registros()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()