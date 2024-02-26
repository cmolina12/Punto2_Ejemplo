

import pulp as pl

problem = pl.LpProblem("Punto 2", pl.LpMinimize)

"""Popti es una empresa dedicada a la producción de
helados con sabores innovadores y atractivos para
nuevos consumidores. La empresa se destaca por su
compromiso con la calidad nutricional y lo orgánico,
utilizando ingredientes naturales adquiridos
directamente de agricultores. Actualmente, dispone de
cinco fábricas de producción ubicadas en diferentes
ciudades del país: Armenia, Bogotá, Neiva, Cali, y
Medellín. Cada una de las fábricas produce 4 sabores de
helado diferentes: Uchuva, Pomarrosa, Borojó y Kiwi. La
Tabla 1 presenta la capacidad mensual de producción de
cada sabor de helado en cada fabrica.
Tabla 1. Capacidad de producción de helado por fábrica y sabor (litros/mes).
Fábrica
Sabor de Helado
Uchuva Pomarrosa Borojó Kiwi
Armenia 1,200 730 700 900
Bogotá 2,300 895 815 110
Neiva 5,000 920 600 500
Cali 2,500 1,140 570 1,990
Medellín 4,100 315 1,315 1,500
Las cinco (5) fábricas deben abastecer de helado a nueve (9) heladerías importantes del
país: CreamLicious, IceCamp, SkyCream, IceDream, OptiCream, MFCream, BajoZero,
SnowFlakes y Selva Helada. Cada una de las heladerías estableció la mínima cantidad de
litros de helado que necesitan de cada sabor para suplir la demanda de un mes. Esta
información se encuentra en la Tabla 2.
Tabla 2. Demanda mensual de helado por heladería y sabor (litros/mes).
Heladería
Sabor de Helado
Uchuva Pomarrosa Borojó Kiwi
CreamLicious 1,420 364 527 408
IceCamp 1,794 495 596 646
SkyCream 1,930 374 452 584
IceDream 1,717 339 484 621
OptiCream 1,712 335 486 594
MFCream 1,606 380 320 352
BajoZero 1,903 415 594 482
SnowFlakes 1,958 370 300 407
Selva Helada 960 428 81 296
El costo de transportar un litro de helado (independiente del sabor) desde cada fábrica a
cada heladería se presenta en la Tabla 3. Para este transporte, cada fabrica tiene disponibles
4 camiones, cada uno con una capacidad de 1,625 litros. Esto significa que Popti sólo puede
enviar hasta 6,500 litros de helado (en total) desde cada fábrica hacia los clientes. La
empresa ha acudido a usted para determinar la distribución óptima de helado desde las
fábricas hasta las heladerías, minimizando el costo total de transporte y satisfaciendo la
demanda de las heladerías.
Tabla 3. Costo de transportar un litro de helado de cualquier sabor ($ COP/litro).
Heladería
Fábrica
Armenia Bogotá Neiva Cali Medellín
CreamLicious 800 876 977 751 630
IceCamp 1,200 722 835 1,056 740
SkyCream 1,000 801 758 624 604
IceDream 1,150 945 1,004 1,038 560
OptiCream 700 736 715 977 561
MFCream 950 200 500 894 562
BajoZero 750 1,056 603 1,035 563
SnowFlakes 1,100 731 900 681 564
Selva Helada 400 500 300 600 400
    """


fabricas = ["Armenia", "Bogotá", "Neiva", "Cali", "Medellín"]
heladerias = ["CreamLicious", "IceCamp", "SkyCream", "IceDream", "OptiCream", "MFCream", "BajoZero", "SnowFlakes", "Selva Helada"]
sabores = ["Uchuva", "Pomarrosa", "Borojó", "Kiwi"]

costo_transporte = {"Armenia": {"CreamLicious": 800, "IceCamp": 1200, "SkyCream": 1000, "IceDream": 1150, "OptiCream": 700, "MFCream": 950, "BajoZero": 750, "SnowFlakes": 1100, "Selva Helada": 400},
                                "Bogotá": {"CreamLicious": 876, "IceCamp": 722, "SkyCream": 801, "IceDream": 945, "OptiCream": 736, "MFCream": 200, "BajoZero": 1056, "SnowFlakes": 731, "Selva Helada": 500},
                                "Neiva": {"CreamLicious": 977, "IceCamp": 835, "SkyCream": 758, "IceDream": 1004, "OptiCream": 715, "MFCream": 500, "BajoZero": 603, "SnowFlakes": 900, "Selva Helada": 300},
                                "Cali": {"CreamLicious": 751, "IceCamp": 1056, "SkyCream": 624, "IceDream": 1038, "OptiCream": 977, "MFCream": 894, "BajoZero": 1035, "SnowFlakes": 681, "Selva Helada": 600},
                                "Medellín": {"CreamLicious": 630, "IceCamp": 740, "SkyCream": 604, "IceDream": 560, "OptiCream": 561, "MFCream": 562, "BajoZero": 563, "SnowFlakes": 564, "Selva Helada": 400}}
demanda = {"CreamLicious": {"Uchuva": 1420, "Pomarrosa": 364, "Borojó": 527, "Kiwi": 408},
                "IceCamp": {"Uchuva": 1794, "Pomarrosa": 495, "Borojó": 596, "Kiwi": 646},
                "SkyCream": {"Uchuva": 1930, "Pomarrosa": 374, "Borojó": 452, "Kiwi": 584},
                "IceDream": {"Uchuva": 1717, "Pomarrosa": 339, "Borojó": 484, "Kiwi": 621},
                "OptiCream": {"Uchuva": 1712, "Pomarrosa": 335, "Borojó": 486, "Kiwi": 594},
                "MFCream": {"Uchuva": 1606, "Pomarrosa": 380, "Borojó": 320, "Kiwi": 352},
                "BajoZero": {"Uchuva": 1903, "Pomarrosa": 415, "Borojó": 594, "Kiwi": 482},
                "SnowFlakes": {"Uchuva": 1958, "Pomarrosa": 370, "Borojó": 300, "Kiwi": 407},
                "Selva Helada": {"Uchuva": 960, "Pomarrosa": 428, "Borojó": 81, "Kiwi": 296}}
capacidad_produccion = {"Armenia": {"Uchuva": 1200, "Pomarrosa": 730, "Borojó": 700, "Kiwi": 900},
                                    "Bogotá": {"Uchuva": 2300, "Pomarrosa": 895, "Borojó": 815, "Kiwi": 110},
                                    "Neiva": {"Uchuva": 5000, "Pomarrosa": 920, "Borojó": 600, "Kiwi": 500},
                                    "Cali": {"Uchuva": 2500, "Pomarrosa": 1140, "Borojó": 570, "Kiwi": 1990},
                                    "Medellín": {"Uchuva": 4100, "Pomarrosa": 315, "Borojó": 1315, "Kiwi": 1500}}
# Variables de decisión
x = pl.LpVariable.dicts("x", ((fabricas, heladerias, sabores)), lowBound=0, cat='Continuous')

# Función objetivo
problem += pl.lpSum([x[f][h][s] * costo_transporte[f][h] for f in fabricas for h in heladerias for s in sabores]) #Costo total de transporte

#Restricciones

#Satisfacción de la demanda para cada heladeria y sabor
for h in heladerias:
    for s in sabores:
        problem += pl.lpSum([x[f][h][s] for f in fabricas]) == demanda[h][s]

#No exceder la capacidad de produccion por fabrica y sabor
for f in fabricas:
    for s in sabores:
        problem += pl.lpSum([x[f][h][s] for h in heladerias]) <= capacidad_produccion[f][s]
        
#No exceder la capacidad de transporte por fabrica

for f in fabricas:
    problem += pl.lpSum([x[f][h][s] for h in heladerias for s in sabores]) <= 6500
    
status = problem.solve()
print(pl.LpStatus[status])

if status == pl.LpStatusOptimal:
    print(f"El costo total de transporte es: ${pl.value(problem.objective)} COP")
    for f in fabricas:
        for h in heladerias:
            for s in sabores:
                if x[f][h][s].varValue > 0:
                    print(f"Se enviarán {x[f][h][s].varValue} litros de helado de {s} desde {f} a {h}")
                    