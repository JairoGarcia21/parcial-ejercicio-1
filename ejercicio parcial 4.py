from datetime import datetime

# Definir precios y tarifas
BONO_ADICIONAL = 500  # Bono adicional para empleados con más de 5 años de antigüedad

# Diccionario para almacenar los registros de empleados
registros_empleados = {}

def calcular_antiguedad(fecha_ingreso):
    hoy = datetime.now()
    antiguedad = hoy.year - fecha_ingreso.year - ((hoy.month, hoy.day) < (fecha_ingreso.month, fecha_ingreso.day))
    return antiguedad

def registrar_empleado():
    while True:
        tipo = input("Ingrese el tipo de empleado (fijo/por horas): ").lower()
        
        if tipo not in ['fijo', 'por horas']:
            print("Tipo de empleado no válido. Inténtelo de nuevo.")
            continue
        
        nombre = input("Ingrese el nombre del empleado: ")
        fecha_ingreso = input("Ingrese la fecha de ingreso (YYYY-MM-DD): ")
        try:
            fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        except ValueError:
            print("Formato de fecha no válido. Inténtelo de nuevo.")
            continue
        
        if tipo == 'fijo':
            salario_base = float(input("Ingrese el salario base mensual: "))
            comisiones = float(input("Ingrese el total de comisiones: "))
            salario_total = salario_base + comisiones
        elif tipo == 'por horas':
            horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
            tarifa_hora = float(input("Ingrese la tarifa por hora: "))
            salario_total = horas_trabajadas * tarifa_hora
        
        antiguedad = calcular_antiguedad(fecha_ingreso)
        bono = BONO_ADICIONAL if antiguedad > 5 else 0
        
        registros_empleados[nombre] = {
            'tipo': tipo,
            'salario_total': salario_total,
            'antiguedad': antiguedad,
            'bono': bono
        }
        print(f"Empleado {nombre} registrado con éxito.")
        break

def mostrar_planilla():
    if not registros_empleados:
        print("No hay registros de empleados.")
        return
    
    print("\nPlanilla de Pago de Empleados:")
    for empleado, datos in registros_empleados.items():
        total_pago = datos['salario_total'] + datos['bono']
        print(f"\nEmpleado: {empleado}")
        print(f"Tipo: {datos['tipo'].capitalize()}")
        print(f"Salario Total: ${datos['salario_total']:.2f}")
        print(f"Antigüedad: {datos['antiguedad']} años")
        print(f"Bono Adicional: ${datos['bono']:.2f}")
        print(f"Total a Pagar: ${total_pago:.2f}")

def main():
    print("Sistema de Planilla de Pago de Empleados")
    while True:
        print("\nOpciones:")
        print("1. Registrar empleado")
        print("2. Mostrar planilla de pago")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1/2/3): ")
        
        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            mostrar_planilla()
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
