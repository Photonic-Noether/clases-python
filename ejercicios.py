# Ejercicios propuestos - Clase 4
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Jerarquía de empleados con herencia múltiple
# Crea una clase base Empleado(nombre, salario) con un método calcular_bonus()
# que devuelva el 10% del salario. Hereda dos clases:
# - Programador(lenguajes: list): el bonus es un 20% del salario.
# - Manager(equipo: list[Empleado]): el bonus es un 30% del salario + 5% por miembro del equipo.
# Implementa __str__ en la clase base mostrando nombre, salario y bonus calculado.
# Usa super() correctamente en todos los constructores.


# Ejercicio 2: Contexto de base de datos simulada (context manager)
# Implementa una clase ConexionDB con __enter__ y __exit__ que simule una conexión.
# Al entrar: imprime "Conectando a la base de datos..."
# Al salir sin error: imprime "Commit realizado. Conexión cerrada."
# Al salir con error: imprime "Rollback realizado: [mensaje_error]. Conexión cerrada."
# El __exit__ debe suprimir el error (devolver True) para que el programa no se detenga.
# Pruébala con un bloque with normal y otro que lance una excepción.


# Ejercicio 3: Sistema de excepciones para una cuenta bancaria
# Crea la clase CuentaBancaria con saldo, limite_credito y lista de transacciones.
# Define excepciones personalizadas: SaldoInsuficiente, MontoInvalido (monto <= 0).
# Implementa: depositar(monto), retirar(monto) y transferir(destino, monto).
# Cada operación añade un registro a la lista de transacciones con el tipo y monto.
# Si retirar pone el saldo por debajo de -limite_credito, lanza SaldoInsuficiente.
