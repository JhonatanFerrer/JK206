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

class SymbolsWindows:
    #ñ
    enie = simple_key_sequence( 
        (      
                KC.TILDE,
                KC.N,
        )
    )
    #¿
    abrirpregunta = simple_key_sequence( 
         (      
                KC.LALT(no_release=True),
                KC.KP_1,
                KC.KP_6,
                KC.KP_8,
        )
    )

    #°
    grado = simple_key_sequence( 
        (      
                KC.LALT(no_release=True),
                KC.KP_0,
                KC.KP_1,
                KC.KP_7,
                KC.KP_6,
        )
    )

