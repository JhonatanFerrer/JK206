import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
       board.GP0,
       board.GP1,
       board.GP2,
       board.GP3,
       board.GP4,
       board.GP5,
       board.GP6,
       board.GP7,
       board.GP8,
       board.GP9,
       board.GP10,
       board.GP11,
    )

    row_pins = (
       board.GP18,
       board.GP19,
       board.GP20,
       board.GP21,
       board.GP22,
    )

    encoderPins = (      
        (board.GP12, board.GP13, None), # encoder0
    )

    SCL=board.GP17
    SDA=board.GP16

    diode_orientation = DiodeOrientation.COL2ROW

    
    
