
<h1 align="Left"> Armado </h1>

<h2 align="Left"> 1. Materiales </h2>

Para poder armar tu propio JK206, sea en su versión de macropad o de teclado 50%, necesitas los siguientes materiales:

|                           | Macropad                                    | Teclado                                     |
| ------------------------- | ------------------------------------------- | ------------------------------------------- |
| Switches mx               | 15 - 20 (dependiendo el número de encoders) | 57 - 60 (dependiendo el número de encoders) |
| Sockets hotswap kailh     | 15 - 20 (dependiendo el número de encoders) | 57 - 60 (dependiendo el número de encoders) |
| Encoders EC11             | 0 - 5                                       | 0 - 3                                       |
| Diodos 1n4148             | 20                                          | 60                                          |
| PCB JK206                 | 1                                           | 3                                           |
| Raspberry Pi Pico         | 1                                           | 1                                           |
| Pantalla OLED SSD1306 (0.91 o 0.96 pulgadas)  | 1 (opcional pero recomendada)               | 1 (opcional pero recomendada)               |
| Case                      | A preferencia                               | A preferencia                               |
| Keycaps                   | A preferencia                               | A preferencia                               |

Mas a continuación hablaremos de los tipos de case y que materiales en particular necesitan estos

Además de lo anterior, para poder realizar el montaje necesitarás de cautín/soldador y estaño, el flux de soldadura es opcional pero nunca viene mal para soldar

<h2 align="Left"> 2. Obtener la PCB </h2>

Para obtener las PCBs basta con tomar los gerbers de la PCB (son un .zip) y mandarlos a hacer un una pagina de fabricación de PCBs. Solo hay que tener en cuenta que el número minimo de PCBs que se pueden mandar a hacer generalmente es de 5

<h2 align="Left"> 3. Soldar piezas </h2>

Una vez tengas todos los materiales necesarios, toca empezar a soldar. Antes de empezar a soldar las piezas ten en cuenta lo siguiente según quieras montar un macropad o un teclado.

<h3 align="Left"> Para el macropad </h3>

Si estas montando el macropad, tienes que "habilitar" la opción de usar mas encoders en la PCB, para esto basta con unir los puntos de la PCB que se ven en la imagen, de forma que cada uno quede unido con quien tenga a sud derecha o izquierda

![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/57addb74-b026-4cfa-8451-b28f55c42d1b)


De forma que queden unidos de la siguiente manere

![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/20f61c4c-638f-4485-a3b4-19ebd36d7ff5)

Esto se puede hacer tanto con cable UTP como con un jumper o uniendo directamente ambos puntos con estaño, basta con que la corriente fluya entre ambos puntos

<h3 align="Left"> Para el teclado </h3>

Si estas montando el teclado, tienes que unir las 3 PCBs, para esto hay que unir filas y columnas; las columnas se unen en la parte superior de las PCBs de la siguiente forma:


![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/8d986f73-baac-420b-a798-1e904f3f9116)

Las filas se unen puenteando los puntos que se encuentran a los lados de la PCB junto al punto que le quede inmediatamente al lado de la otra PCB. Esto se hace en ambas intersecciones entre PCBs

![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/734ff414-ec16-4648-906f-d32c0567a64a)

Ya con los preparativos listos, queda soldar los componentes en sus sitios correspondientes. Comienza colocando los diodos, estos van posicionados de forma que la parte que tiene una linea va hacia abajo, como se puede observar en la misma PCB

------Aquí debe ir una foto ------

Lo siguiente sería soldar los sockets hotswap y los encoders, ten en cuenta que donde vayas a colocar enconders no hay que colocar sockets. Dependiendo de si estás armando un teclado o un macropad debes tener en cuenta las siguientes consideraciones:

<h3 align="Left"> Para el macropad </h3>

Los encoders se pueden colocar en el macropad de la siguiente forma

![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/261219ae-7fc7-40b2-8a4f-46c7caaa28a1)

Las zonas verdes en el diagrama representan los puntos donde puenden colocarse los encoders. No es recomendable colocar dos encoders en posiciones que compartan el mismo número, pues por limitaciones del Raspberry Pi Pico y del diseño de la PCB estos serían reconocidos como un solo encoder; por lo que la formas recomendables de colocar los encoders serían las siguientes


![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/15c20124-f5a1-4b04-b754-f72da8c0276f)
![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/4c740b88-ffe2-471d-b411-18dfd2f6fb84)

<h3 align="Left"> Para el teclado </h3>

A pesar de tecnicamente poder poner encoders en la pcb de la izquierda en las posiciones 1, 2 y 3 mostradas en la sección anterior. Por cuestiones de usabilidad del teclado se recomienda solo poner un encoder en el extremo superior izquierdo.

Teniendo en cuenta lo anterior, empieza a soldar los sockets hotswap y los encoders que vayas a colocar. Puede que tengas problemas con los sockets, pero si eres generoso con el estaño no habrán mayores dificultades

-----Aquí deben haber 2 imagenes-------

Ahora solo faltaría soldar el Raspberry Pi Pico y la pantalla OLED. Es necesario que la Raspberry tenga pines soldados para poderla poner en la PCB, así que en caso de que tu Raspberry no los tenga de antemano tendrás que soldarle tu mismo unas regletas Antes de colocarla en la PCB.


![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/e1d4df5e-f2e3-4f1a-a8f8-0bd331d9776c)


-----Aquí debe haber una imagen--------



En cuanto a la pantalla OLED, su posicionamiento varía dependiendo de cual pantalla vayas a usar. En caso de tener una pantalla rectangular de 0.91 pulgadas esta quedaría sobre la Raspberry, mientras que una pantalla cuadrada de 0.96 pulgadas quedaría a la derecha.

Nota: para el montaje del teclado, tanto la Raspberry como la pantalla van únicamente en la PCB de la izquierda. El diseño de la PCB no está pensado para que tomen ninguna otra posición.

<h2 align="Left"> 4. Montaje </h2>

Aquí el proceso cambia según el tipo de montaje que se quiera realizar:

<h3 align="Left"> Para el montaje sandwich-case </h3>
