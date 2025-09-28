#1 Crear un diccionario con información personal ficticia

informacion_personal = {
    "nombre": "Yuribeth Chamba",
    "edad": 28,
    "ciudad": "Cuenca",
    "profesion": "Diseñadora Gráfica"
}

#2 Modificar el valor de la clave "ciudad"

informacion_personal ["ciudad"] = "Guayaquil" 

#3 Agregar o actualizar la clave "profesion"

informacion_personal ["profesion"] = "Ingenieria de software"

#4 Verificar si existe la clave "telefono", y agregarla si no

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0963258840"

#5 Eliminar la clave "edad"

del informacion_personal["edad"]

#6 Imprimir el diccionario final

print("Diccionario final:")
print(informacion_personal)

