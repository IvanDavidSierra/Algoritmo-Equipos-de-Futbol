"""
Desarrollar un algoritmo lea: los partidos ganados, los partidos empatados y los partidos perdidos para cuatro equipos de futbol. Una vez leidos, determine:
    1. Los puntos para cada equipo
    2. El equipo ganador

Ivan Sierra. 

"""

print("\n-- Algoritmo para calcular al equipo ganador --\n")
print("Digite la cantidad de partidos ganados, empatados y perdidos de cada equipo junto su respectivo nombre")

print("*****************************************")
nombreEquipoUno = input("Ingrese el nombre del primer equipo: ")
print("Ingrese los partidos ganados, perdidos y empatados del equipo --",nombreEquipoUno,"--")


partidoGanadoEquipoUno = int(input("Ingrese cantidad de partidos ganados: "))
partidoEmpatadoEquipoUno = int(input("Ingrese cantidad de partidos empatados: "))
partidoPerdidoEquipoUno = int(input("Ingrese cantidad de partidos perdidos: "))

print("*****************************************")

nombreEquipoDos = input("Ingrese el nombre del segundo equipo: ")
print("Ingrese los partidos ganados, perdidos y empatados del equipo --",nombreEquipoDos,"--")

partidoGanadoEquipoDos = int(input("Ingrese cantidad de partidos ganados: "))
partidoEmpatadoEquipoDos = int(input("Ingrese cantidad de partidos empatados: "))
partidoPerdidoEquipoDos = int(input("Ingrese cantidad de partidos perdidos: "))

print("*****************************************")

nombreEquipoTres = input("Ingrese el nombre del tercer equipo: ")
print("Ingrese los partidos ganados, perdidos y empatados del equipo --",nombreEquipoTres,"--")

partidoGanadoEquipoTres = int(input("Ingrese cantidad de partidos ganados: "))
partidoEmpatadoEquipoTres = int(input("Ingrese cantidad de partidos empatados: "))
partidoPerdidoEquipoTres = int(input("Ingrese cantidad de partidos perdidos: "))

print("*****************************************")


nombreEquipoCuatro = input("Ingrese el nombre del cuarto equipo: ")
print("Ingrese los partidos ganados, perdidos y empatados del equipo --",nombreEquipoCuatro,"--")

partidoGanadoEquipoCuatro = int(input("Ingrese cantidad de partidos ganados: "))
partidoEmpatadoEquipoCuatro = int(input("Ingrese cantidad de partidos empatados: "))
partidoPerdidoEquipoCuatro = int(input("Ingrese cantidad de partidos perdidos: "))

print("*****************************************")

#Para calcular al ganador, se le asignan 3 puntos a los partidos ganados, 1 punto a los partidos empatados y se les resta 3 puntos por cada partido perdido
resultadoEquipoUno = (partidoGanadoEquipoUno * 3 ) + partidoEmpatadoEquipoUno - (partidoPerdidoEquipoUno * 3)
resultadoEquipoDos = (partidoGanadoEquipoDos * 3 ) + partidoEmpatadoEquipoDos - (partidoPerdidoEquipoDos * 3)
resultadoEquipoTres = (partidoGanadoEquipoTres * 3 ) + partidoEmpatadoEquipoTres - (partidoPerdidoEquipoTres * 3)
resultadoEquipoCuatro = (partidoGanadoEquipoCuatro * 3 ) + partidoEmpatadoEquipoCuatro - (partidoPerdidoEquipoCuatro * 3)



#Se guardan los resultados con su respectivo equipo dentro de un diccionario para ser ordenados
tablaResultado = {
    nombreEquipoUno : resultadoEquipoUno,
    nombreEquipoDos : resultadoEquipoDos, 
    nombreEquipoTres : resultadoEquipoTres,
    nombreEquipoCuatro : resultadoEquipoCuatro
    }

#Se ordenan los resultados de mayor a menor
resultados = dict(sorted(tablaResultado.items(), key=lambda item: item[1], reverse=True))

#Tabla de resultados
print("----------------------------------------")
for equipo, resultado in resultados.items():
    print(f"Puntuacion del equipo -- {equipo} --: {resultado}")
print("----------------------------------------")


#Determinar cual es el ganandor 
if resultadoEquipoUno > resultadoEquipoDos and resultadoEquipoUno > resultadoEquipoTres and resultadoEquipoUno > resultadoEquipoCuatro:
    print("¡El equipo ganador es:",nombreEquipoUno,"!")
elif resultadoEquipoDos > resultadoEquipoUno and resultadoEquipoDos > resultadoEquipoTres and resultadoEquipoDos > resultadoEquipoCuatro:
    print("¡El equipo ganador es:",nombreEquipoDos,"!")
elif resultadoEquipoTres > resultadoEquipoUno and resultadoEquipoTres > resultadoEquipoDos and resultadoEquipoTres > resultadoEquipoCuatro:
    print("¡El equipo ganador es:",nombreEquipoTres,"!")
elif resultadoEquipoCuatro > resultadoEquipoUno and resultadoEquipoCuatro > resultadoEquipoDos and resultadoEquipoCuatro > resultadoEquipoTres:
    print("¡El equipo ganador es: ",nombreEquipoCuatro,"!")
else:
    print("No hay equipos ganadores")