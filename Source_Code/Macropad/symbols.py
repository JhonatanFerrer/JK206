from kmk.keys import KC
from kmk.consts import UnicodeMode
from kmk.handlers.sequences import simple_key_sequence
from kmk.handlers.sequences import unicode_string_sequence

class Symbols:
    UnicodeMode = UnicodeMode.LINUX
    
    enie = simple_key_sequence(
        (      
                KC.TILDE,
                KC.N,
        )
    )

    abrirpregunta = unicode_string_sequence('¿')


    grado = unicode_string_sequence('°')

