
<h1 align="Left"> Guía ensamble </h1>

<h2 align="Left"> 1. Materiales Base</h2>

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

Para obtener las PCBs basta con tomar el gerber de la PCB (es un .zip) y mandarlo a hacer un una pagina de fabricación de PCBs. Solo hay que tener en cuenta que el número minimo de PCBs que se pueden mandar a hacer generalmente es de 5

<h2 align="Left"> 3. Preparar la PCB </h2>

Una vez tengas todos los materiales necesarios, toca empezar a soldar. Antes de empezar a soldar las piezas ten en cuenta lo siguiente según quieras montar un macropad o un teclado.

<h3 align="Left"> Para el macropad </h3>

Si estas montando el macropad, tienes que "habilitar" la opción de usar mas encoders en la PCB, para esto basta con unir los puntos de la PCB que se ven en la imagen, de forma que cada uno quede unido con quien tenga a sud derecha o izquierda

![292385655-57addb74-b026-4cfa-8451-b28f55c42d1b](https://github.com/JhonatanFerrer/JK206/assets/111335841/2189e91f-a64e-4447-abd9-0322da5fcc75)



De forma que queden unidos de la siguiente manere

![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/20f61c4c-638f-4485-a3b4-19ebd36d7ff5)

Esto se puede hacer tanto con cable UTP como con un jumper o uniendo directamente ambos puntos con estaño, basta con que haya continuidad entre ambos puntos

<h3 align="Left"> Para el teclado </h3>

Si estas montando el teclado, tienes que unir las 3 PCBs, para esto hay que unir filas y columnas; las columnas se unen en la parte superior de las PCBs de la siguiente forma:


![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/8d986f73-baac-420b-a798-1e904f3f9116)

Las filas se unen puenteando los puntos que se encuentran a los lados de la PCB junto al punto que le quede inmediatamente al lado de la otra PCB. Esto se hace en ambas intersecciones entre PCBs

![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/734ff414-ec16-4648-906f-d32c0567a64a)

No olvides que para evitar problemas posteriores con el montaje del teclado las 3 PCBs deben quedar completamente juntas y alineadas


<h2 align="Left"> 4. Soldar piezas </h2>

Ya con los preparativos listos, queda soldar los componentes en sus sitios correspondientes. Comienza colocando los diodos, estos van posicionados de forma que la parte que tiene una linea va hacia abajo, como se puede observar en la misma PCB

![IMG_20250111_233957](https://github.com/user-attachments/assets/0deebb8a-1d8a-4c98-a9b5-f40d03befae3)

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

![IMG_20250111_234158](https://github.com/user-attachments/assets/2b18d638-62e7-41cd-bf09-768f42581df7)
![IMG_20250111_234228](https://github.com/user-attachments/assets/5e3aa1e8-e9ce-46b1-a27d-408516879857)
![IMG_20250111_234041](https://github.com/user-attachments/assets/7c991923-5355-49ad-b558-d8e15f57497c)

Ahora solo faltaría soldar el Raspberry Pi Pico y la pantalla OLED. Es necesario que la Raspberry tenga pines soldados para poderla poner en la PCB, así que en caso de que tu Raspberry no los tenga de antemano tendrás que soldarle tu mismo unas regletas Antes de colocarla en la PCB.


![image](https://github.com/JhonatanFerrer/JK206/assets/111335841/e1d4df5e-f2e3-4f1a-a8f8-0bd331d9776c)

![IMG_20250111_225725](https://github.com/user-attachments/assets/9943f2f9-16a2-4e09-a465-cdd6062bb180)


En cuanto a la pantalla OLED, su posicionamiento varía dependiendo de cual pantalla vayas a usar. En caso de tener una pantalla rectangular de 0.91 pulgadas esta quedaría sobre la Raspberry, mientras que una pantalla cuadrada de 0.96 pulgadas quedaría a la derecha.

![IMG_20250111_231447](https://github.com/user-attachments/assets/ea0b8b9f-d76f-4f5e-8f8c-35bf3330b7b8)
![IMG_20250111_231349](https://github.com/user-attachments/assets/3840b839-e131-4758-8a00-a087cf327e41)


Nota: para el montaje del teclado, tanto la Raspberry como la pantalla van únicamente en la PCB de la izquierda. El diseño de la PCB no está pensado para que tomen ninguna otra posición.

<h2 align="Left"> 5. Montaje </h2>

Aquí el proceso cambia según el tipo de montaje que se quiera realizar:

<h3 align="Left"> Para el montaje sandwich-case </h3>

Para este montaje relativamente sencillo vas a necesitar de estos materiales:

|                           | Macropad                                    | Teclado                                     |
| ------------------------- | ------------------------------------------- | ------------------------------------------- |
| Separadores de latón M2 10mm| 4                                         | 4                                           |
| Tornillos M2 cabeza plana 6mm| 8                                        | 8                                           |
| Plate acrílico superior (1.5mm de grosor)   | 1 (de macropad)                             | 1 (de teclado completo                      |
| Plate acrílico inferior (1.5mm de grosor)   | 1 (de macropad)                             | 1 (de teclado completo                      |

Esta guía de montaje estará enfocada principalmente para el macropad, pero el montaje del JK206 en modo teclado es muy similar y la guía debería servir igualmente.

Para realizar el montaje del teclado o macropado lo primero será tomar el plate inferior y colocarle pies antideslizantes bajo preferencia del usuario.

![IMG_20250121_221636](https://github.com/user-attachments/assets/42427d16-c144-42f8-98af-191288188648)


Una vez hecho esto seguiría atornillar a éste los separadores

![IMG_20250122_213610](https://github.com/user-attachments/assets/f56cbecc-82e8-456f-b305-00ac5f930a01)

![IMG_20250122_213600](https://github.com/user-attachments/assets/be4fccbe-bb4c-45c6-b4b4-591005383395)


Nota: Los plates superior e inferior de la versión de teclado completo del JK206 tienen huecos para 12 separadores, aunque yo recomiendo usar solo 4 (2 al extremo derecho y 2 al extremo izquierdo),pero queda la opción de colocar mas separadores si se desea una sensación mas rígida al escribir

Ya teniendo nuestro plate inferior ahora vamos a sujetar nuestra PCB al plate superior con los switches, para esto basta con colocar un par de switches en el plate para luego colocarlos juntos en la PCB

![IMG_20250121_222020](https://github.com/user-attachments/assets/b1b5b28b-8e55-47af-9ecc-ea8817459f2a)

![IMG_20250121_222112](https://github.com/user-attachments/assets/64c44b68-a08f-4113-85d3-3a0e4d27aa3d)

Despues de esto quedaría colocar los switches faltantes

![IMG_20250121_222300](https://github.com/user-attachments/assets/a2773ded-38ee-4008-80bd-7a5d7aeb76ee)

Ya teniendo unidos plate, pcb y switches podemos atornillar el plate superior a los separadores que habíamos colocado anteriormente en el plate inferior

![IMG_20250121_222456](https://github.com/user-attachments/assets/43fd86f2-b0a6-45bd-934f-476f111d68de)

Y con esto ya tenemos nuestro teclado o macropad listo, solo faltaría colocar keycaps a nuestro gusto y disfrutar.

![IMG_20250121_222836](https://github.com/user-attachments/assets/a5e6be41-453b-48a2-ab99-7aa1fcc90356)

<h4 align="Left"> Mods recomendados: </h4>
En general el tape mod funciona bien con el montaje, fuera de eso no hay mucho mas que se pueda hacer.


<h2 align="Left"> 5. Instalación del firmware </h2>

Ésta es la parte más fácil, para esto solo debes instalar [KMK](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/Getting_Started.md) y sobre este colocar los archivos de configuración, sean los del [macropad](https://github.com/JhonatanFerrer/JK206/tree/main/Source_Code/Macropad) o el [teclado completo](https://github.com/JhonatanFerrer/JK206/tree/main/Source_Code/Keyboard).


Y con ésto ya deberías tener completamente funcional tu JK206 :D
