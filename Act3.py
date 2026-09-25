# act03_types.py
#Crea una variable de cada tipo: int, float, str, bool, None
v_entero="10"
v_decimal="3.14"
v_text="hi"
v_boleano="True"
v_resultado="none"


print(f"{v_entero} -> {type(v_entero)}")
print(f"{v_decimal} -> {type(v_decimal)}")
print(f"{v_text} -> {type(v_text)}")
print(f"{v_boleano} -> {type(v_boleano)}")
print(f"{v_resultado} -> {type(v_resultado)}")

 #Muestra valor + type() en una tabla formateada
print(f"{'Valor':<15} | {'Tipo'}")
print("-" * 35)
print(f"{str(v_entero):<15} | {type(v_entero)}")
print(f"{str(v_decimal):<15} | {type(v_decimal)}")
print(f"{str(v_text):<15} | {type(v_text)}")
print(f"{str(v_boleano):<15} | {type(v_boleano)}")
print(f"{str(v_resultado):<15} | {type(v_resultado)}")


 #Prueba 0.1 + 0.2 == 0.3 y explica el resultado

print(0.1 + 0.2 == 0.3)
 #Prueba "3" + 3 y copia el TypeError 

print("3" + 3)



 