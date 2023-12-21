from kb import KMKKeyboard 
from symbols import Symbols
from combinations import Combinations
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

Keyboard = KMKKeyboard()
Keyboard.modules.append(Layers())
Keyboard.extensions.append(MediaKeys()) 

Keyboard.unicode_mode = Symbols.UnicodeMode

OledConfiguration = Oled(
      OledData(image={0:OledReactionType.LAYER,1:["logo.bmp","logo.bmp","KBNums.bmp","FNKeys.bmp","KeyComb.bmp"]}),
      oWidth=128,oHeight=32,toDisplay=OledDisplayMode.IMG,flip=True
    )
Keyboard.extensions.append(OledConfiguration)

encoder_handler = EncoderHandler() 
encoder_handler.pins = Keyboard.encoderPins

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU,),(KC.UP, KC.DOWN,),(KC.LEFT, KC.RIGHT,),(KC.TO(4), KC.TO(2),),),  # Layer 0
    ((KC.VOLD, KC.VOLU,),(KC.UP, KC.DOWN,),(KC.LEFT, KC.RIGHT,),(KC.NO, KC.NO,),),        # Layer 1
    ((KC.VOLD, KC.VOLU,),(KC.UP, KC.DOWN,),(KC.LEFT, KC.RIGHT,),(KC.TO(0), KC.TO(3)),),   # Layer 2
    ((KC.VOLD, KC.VOLU,),(KC.UP, KC.DOWN,),(KC.LEFT, KC.RIGHT,),(KC.TO(2), KC.TO(4)),),   # Layer 3
    ((KC.VOLD, KC.VOLU,),(KC.UP, KC.DOWN,),(KC.LEFT, KC.RIGHT,),(KC.TO(3), KC.TO(0),),),  # Layer 4
)
Keyboard.modules.append(encoder_handler)

Keyboard.keymap = [
    # Layer 0 NUMPAD
   [
     KC.MEDIA_PLAY_PAUSE,  KC.HOME,           KC.END,           KC.ESCAPE,
     Symbols.abrirpregunta,                KC.P8,             KC.P9,            KC.KP_SLASH,
     KC.P4,                KC.P5,             KC.P6,            KC.KP_ASTERISK,
     KC.P1,                KC.P2,             KC.P3,            KC.KP_MINUS,
     KC.P0,                KC.PDOT,           KC.KP_PLUS,       KC.MO(1),
   ], 
   # Layer 1 NUMPAD Extras
   [  
     KC.MEDIA_PLAY_PAUSE,  KC.HOME,           KC.END,           KC.ESCAPE,
     KC.P7,                KC.P8,             KC.P9,            KC.KP_SLASH,
     KC.P4,                KC.UP,             KC.P6,            KC.KP_ASTERISK,
     KC.LEFT,              KC.DOWN,           KC.RIGHT,         KC.BSPACE,
     KC.P0,                KC.PENT,           KC.KP_EQUAL,      KC.NO,
   ],
   # Layer 2 Main keyboard numbers (if you need them in specific)
   [  
     KC.MEDIA_PLAY_PAUSE,  KC.HOME,           KC.END,           KC.ESCAPE,
     KC.N7,                KC.N8,             KC.N9,            KC.KP_SLASH,
     KC.N4,                KC.N5,             KC.N6,            KC.KP_ASTERISK,
     KC.N1,                KC.N2,             KC.N3,            KC.KP_MINUS,
     KC.N0,                KC.PDOT,           KC.KP_PLUS,       KC.MO(1),
   ],
   # Layer 3 Function keys
   [  
     KC.MEDIA_PLAY_PAUSE,  KC.HOME,           KC.END,           KC.ESCAPE,
     KC.F9,                KC.F10,            KC.F11,           KC.F12,
     KC.F5,                KC.F6,             KC.F7,            KC.F8,
     KC.F1,                KC.F2,             KC.F3,            KC.F4,
     KC.PSCREEN,           KC.DELETE,         KC.INSERT,        KC.APPLICATION,
   ],
   # Layer 4 Common keys combination
   [  
     KC.MEDIA_PLAY_PAUSE,  KC.HOME,           KC.END,           KC.ESCAPE,
     KC.P7,                KC.P8,             KC.P9,            KC.KP_SLASH,
     KC.P4,                KC.UP,             KC.P6,            KC.KP_ASTERISK,
     Combinations.Save,    Combinations.Undo, Combinations.Redo,Combinations.CtrlAltDel,
     Combinations.Copy,    Combinations.Paste,Combinations.Cut, Combinations.AltTab,
   ]
]




if __name__ == '__main__':
    Keyboard.go()

 #
