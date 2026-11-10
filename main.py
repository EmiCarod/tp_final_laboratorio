import os
from fpdf import FPDF
from modelo_base import CuentaCorriente, CajaAhorro

def main():
    # Arreglo para almacenar las cuentas creadas
    cuentas = []

    print("-------- Bienvenido al menú de opciones del Banco ---------")
    
    while True:
        print("\n--- MENU ---")
        print("1. Crear Cuenta Corriente")
        print("2. Crear Caja de Ahorro")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Listar cuentas")
        print("6. Generar reporte PDF")
        print("7. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            continue

        match opcion:
            case 1:
                print("\n--- Crear Cuenta Corriente ---")
                nro = input("Ingrese numero de cuenta: ")
                titular = input("Ingrese nombre del titular: ")
                try:
                    saldo_inicial = float(input("Ingrese saldo inicial: "))
                    # Crear instancia y guardar en el arreglo en memoria
                    nueva_cc = CuentaCorriente(nro, titular, saldo_inicial)
                    cuentas.append(nueva_cc)
                    print("Cuenta Corriente creada con exito.")
                except ValueError as e:
                    print(f"Error en los datos ingresados: {e}")

            case 2:
                print("\n--- Crear Caja de Ahorro ---")
                nro = input("Ingrese numero de cuenta: ")
                titular = input("Ingrese nombre del titular: ")
                try:
                    saldo_inicial = float(input("Ingrese saldo inicial: "))
                    # Crear instancia y guardar en el arreglo en memoria
                    nueva_ca = CajaAhorro(nro, titular, saldo_inicial)
                    cuentas.append(nueva_ca)
                    print("Caja de Ahorro creada con exito.")
                except ValueError as e:
                    print(f"Error en los datos ingresados: {e}")

            case 3:
                if not cuentas:
                    print("No hay cuentas registradas en el sistema.")
                    continue
                
                nro = input("Ingrese el numero de cuenta para depositar: ")
                cuenta_encontrada = next((c for c in cuentas if c.get_numero_cuenta() == nro), None)
                
                if cuenta_encontrada:
                    try:
                        monto = float(input("Ingrese el monto a depositar: "))
                        cuenta_encontrada.depositar(monto)
                        print(f"Deposito exitoso. Nuevo saldo: {cuenta_encontrada.get_saldo()}")
                    except ValueError as e:
                        print(f"Error: {e}")
                else:
                    print("Cuenta no encontrada.")

            case 4:
                if not cuentas:
                    print("No hay cuentas registradas en el sistema.")
                    continue
                
                nro = input("Ingrese el número de cuenta para retirar: ")
                cuenta_encontrada = next((c for c in cuentas if c.get_numero_cuenta() == nro), None)
                
                if cuenta_encontrada:
                    try:
                        monto = float(input("Ingrese el monto a retirar: "))
                        cuenta_encontrada.retirar(monto)
                        print(f"Retiro exitoso. Nuevo saldo: {cuenta_encontrada.get_saldo()}")
                    except ValueError as e:
                        print(f"Error al retirar: {e}")
                else:
                    print("Cuenta no encontrada.")

            case 5:
                if not cuentas:
                    print("No hay cuentas registradas en el sistema.")
                else:
                    print("\n--- LISTADO DE CUENTAS ---")
                    for c in cuentas:
                        tipo = "Cuenta Corriente" if isinstance(c, CuentaCorriente) else "Caja de Ahorro"
                        print(f"Tipo: {tipo} | Nro: {c.get_numero_cuenta()} | Titular: {c.get_titular()} | Saldo: ${c.get_saldo()}")

            case 6:
                if not cuentas:
                    print("No hay cuentas para generar el reporte.")
                else:
                    print("Generando PDF...")
                    try:
                        pdf = FPDF(orientation="P", unit="mm", format="A4")
                        pdf.add_page()
                        pdf.set_font("Helvetica", "B", 16)
                        pdf.cell(0, 10, "Reporte General - Sistema Bancario", border=0, new_x="LMARGIN", new_y="NEXT", align="C")
                        pdf.ln(10)

                        pdf.set_font("Helvetica", "", 12)
                        for c in cuentas:
                            tipo = "Cuenta Corriente" if isinstance(c, CuentaCorriente) else "Caja de Ahorro"
                            texto = f"Tipo: {tipo} | Nro: {c.get_numero_cuenta()} | Titular: {c.get_titular()} | Saldo: ${c.get_saldo()}"
                            pdf.cell(0, 8, texto, border=0, new_x="LMARGIN", new_y="NEXT")

                        nombre_pdf = "reporte_banco.pdf"
                        pdf.output(nombre_pdf)
                        print(f"PDF generado: {os.path.abspath(nombre_pdf)}")
                    except Exception as e:
                        print(f"Error al generar el PDF: {e}")

            case 7:
                print("Saliendo del sistema.")
                break
            case _:
                print("Opcion invalida. Elija un numero del 1 al 7.")

if __name__ == "__main__":
    main()