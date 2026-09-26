# ==========================================
# GUÍA DE ERRORES Y EXCEPCIONES EN PYTHON
# Archivo de consulta rápida: errores.py
# ==========================================

lista_materias = ["Programación", "Bases de Datos"]

try:
    print("1. 🟢 Inicio de la operación...")

    # Descomentá UNA sola línea para probar distintas situaciones:
    # print(materia_inexistente)        # Provoca NameError
    # resultado = "Año " + 2026          # Provoca TypeError
    # print(lista_materias[5])          # Provoca IndexError
    #eval("if True print('Hola')")     # Provoca SyntaxError (en texto dinámico)

    print("2. 🟢 Todo funcionó correctamente en el try.")

# -----------------------------------------------------------------
# RED DE CONTENCIÓN (Atrapamos cada error específico)
# -----------------------------------------------------------------
except NameError:
    print("❌ NameError: Usaste una variable o función no definida.")

except TypeError:
    print("❌ TypeError: Mezclaste tipos de datos incompatibles.")

except IndexError:
    print("❌ IndexError: Te pasaste del límite de la lista.")

except SyntaxError:
    print("❌ SyntaxError: El código tiene un error de estructura o sintaxis.")

except Exception as e:
    print(f"❌ Error inesperado no contemplado: {e}")

# -----------------------------------------------------------------
# LIMPIEZA / CIERRE (Se ejecuta SIEMPRE)
# -----------------------------------------------------------------
finally:
    print("3. 🧹 FINALLY: Cerramos procesos y liberamos memoria. (Corre SIEMPRE).")