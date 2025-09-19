from datetime import datetime
hora_actual = datetime.now().hour
if hora_actual < 12:
    print("¡Buenos días pepe!")
elif hora_actual <22:
    print("¡Buenas tardes pepe!")
else: 
    print("¡Buenas noches pepe!")