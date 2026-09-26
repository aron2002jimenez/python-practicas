#===========================================
# EXECEPCIONES PERSONALIZADAS EN PYTHON
# Archivo: errores_personalizdos.py
#===========================================

#1. Definimos la función con la regla de negocio
def transferir_dinero(monto, saldo_disponibles):

    # La condición (formula) de lo que no puede pasar
    if monto> saldo_disponibles:
        # Usamos 'raise' para lanzar nuestro error con su mensje
        raise Exception("Saldo insuficiente para realizar la transferencia.")

    print(f"✅Transferencia de {monto} realizada con exito.")


# 2 robramos la función 
try:
    print("Inciando transferencia...")
    # '1000' y '500' son los ARGUMENTOS (los valores que toman estas variables)
    transferir_dinero(1000, 500)

except Exception as e:
    print(f"❌ Error capturado: {e}")

finally:
    print("🔒 Operación finalizada.")