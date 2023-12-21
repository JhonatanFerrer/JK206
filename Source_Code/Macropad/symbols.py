from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence

class SymbolsLinux:
    
    enie = simple_key_sequence(
        (      
                KC.TILDE,
                KC.N,
        )
    )

    abrirpregunta = simple_key_sequence(
        (      
                KC.LCTRL(no_release=True),
                KC.LSHIFT(no_release=True),
                KC.U,
                KC.B,
                KC.F,
        )
    )


    grado = simple_key_sequence(
        (      
                KC.LCTRL(no_release=True),
                KC.LSHIFT(no_release=True),
                KC.U,
                KC.B,
                KC.N0,
        )
    )
