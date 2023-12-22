
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
| Pantalla SSD1306          | 1 (opcional pero recomendada)               | 1 (opcional pero recomendada)               |
| Case                      | A preferencia                               | A preferencia                               |
| Keycaps                   | A preferencia                               | A preferencia                               |

Mas a continuación hablaremos de los tipos de case y que materiales en particular necesitan estos

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

Ya con los preparativos listos, queda soldar los componentes en sus sitios correspondientes. A excepción de los diodos es dificil colocar algo mal (e incluso estos tienen marcada la orientación correcta en la PCB), por lo que no hay pierde.

<h2 align="Left"> 4. Montaje </h2>

Aquí el proceso cambia según el tipo de montaje que se quiera realizar:

<h3 align="Left"> Para el montaje sandwich-case </h3>
