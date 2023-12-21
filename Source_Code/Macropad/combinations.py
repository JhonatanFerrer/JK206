from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence

class Combinations:
    Copy = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True),
            KC.C,
        )
    )

    Paste = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True),
            KC.V,
        )
    )

    Cut = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True),
            KC.X,
        )
    )

    Save = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True),
            KC.S,
        )
    )

    Undo = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True),
            KC.Z,
        )
    )

    Redo = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True),
            KC.Y,
        )
    )

    AltTab = simple_key_sequence(
        (      
            KC.LALT(no_release=True), 
            KC.TAB,

        )
    )

    CtrlAltDel = simple_key_sequence(
        (      
            KC.LCTRL(no_release=True), 
            KC.LALT(no_release=True), 
            KC.DELETE,
        )
    )