import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (
       board.GP0,
       board.GP1,
       board.GP2,
       board.GP3,
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
        (board.GP14, board.GP15, None), # encoder1
        (board.GP26, board.GP27, None), # encoder2
        (board.GP6,  board.GP7,  None), # encoder3
    )
    SCL=board.GP17
    SDA=board.GP16

    diode_orientation = DiodeOrientation.COL2ROW
    

