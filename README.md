# SemanaTecProgra-Reto
AUTHORS: Ximena Flores, Luis Javier Alonso, Daniel Montero

Games included:
- snake.py
- cannon.py

Descripcion cambios realizados:

Cambios Ximena: 
- snake.py - cambio del tamaño del display del juego modificando los valores de las siguientes lineas inside head: -240 <head.x < 230 and -240 <head.y < 230  
"setup values "(500, 500, 370,0) 
- cannon.py - cambio de colores para la varible de target y para la variable de ball dot(20, 'green')
dot(6, 'yellow')

Cambios Luis Javier:
- snake.py: se modificó el comportamiento de la comida para que con cada paso de la serpiente, esta se moviera en una dirección aleatoria 1 paso. (food.x = randrange(-1, 1) * 10, food.y = randrange(-1, 1) * 10).
- cannon.py: se modificaron los valores de la velocidad de los targets como del proyectil. En los targets se cambió la velocidad en el eje "x" y en el proyectil en el eje "y". (speed.y, target.x)

Cambios Daniel: 
- snake.py: se añadió una función que permite cambiar, cada vez que se corre el juego y de manera aleatoria, los colores de la víbora y la comida (variables 'snakecolor' y 'foodcolor'). De momento se cuentan con 5 colores, la adición de más colores se puede realizar mediante la matriz 'colors'.
- cannon.py - Se añadio un sistema de vidas personalizable. Por el momento esta configrado a tres pero se puede modificar al gusto mediante la variable 'lifes' dentro del def 'move'.



Enlace a la presentación: https://docs.google.com/presentation/d/1lhlmWNVv3bE_G5KVLbdgTw7jkLKEZ3iZu0yKkbu9jEg/edit?usp=sharing
