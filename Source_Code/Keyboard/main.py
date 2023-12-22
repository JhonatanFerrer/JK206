from kb import KMKKeyboard
from symbols import SymbolsLinux as Symbols
from combinations import Combinations
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

Keyboard = KMKKeyboard()
Keyboard.modules.append(Layers())
Keyboard.extensions.append(MediaKeys())



OledConfiguration = Oled(
      OledData(image={0:OledReactionType.LAYER,1:["Logo.bmp","Fn.bmp","Extras.bmp", "Game.bmp"]}),
      oWidth=128,oHeight=64,toDisplay=OledDisplayMode.IMG,
    )
Keyboard.extensions.append(OledConfiguration)

encoder_handler = EncoderHandler()
encoder_handler.pins = Keyboard.encoderPins

encoder_handler.map = (
    ((KC.VOLD, KC.VOLU,),),  # Layer 0
    ((KC.VOLD, KC.VOLU,),),  # Layer 1
    ((KC.VOLD, KC.VOLU,),),  # Layer 2
    ((KC.VOLD, KC.VOLU,),),  # Layer 3¿¿¿¿¿¿¿
)

Keyboard.modules.append(encoder_handler)

Keyboard.keymap = [
    # Layer 0 BASE
   [
     KC.MEDIA_PLAY_PAUSE, KC.N1,        KC.N2,      KC.N3,       KC.N4,        KC.N5,      KC.N6,         KC.N7,        KC.N8,      KC.N9,      KC.N0,                KC.BSPC,
     KC.ESC,              KC.Q,         KC.W,       KC.E,        KC.R,         KC.T,       KC.Y,          KC.U,         KC.I,       KC.O,       KC.P,                 KC.QUOTE,
     KC.TAB,              KC.A,         KC.S,       KC.D,        KC.F,         KC.G,       KC.H,          KC.J,         KC.K,       KC.L,       KC.SCOLON,            KC.ENTER,
     KC.LSHIFT,           KC.Z,         KC.X,       KC.C,        KC.V,         KC.B,       KC.N,          KC.M,         KC.COMMA,   KC.DOT,     KC.SLASH,             KC.RSHIFT,
     KC.LCTRL ,           KC.LGUI,      KC.PGUP,   KC.LALT,      KC.MO(2),     KC.SPACE,   KC.SPACE,      KC.MO(2),    KC.RALT,    KC.PGDOWN,   KC.RCTRL,             KC.MO(1),
   ],
   # Layer 1 FN
   [ 
     KC.F1,               KC.F2,        KC.F3,      KC.F4,       KC.F5,        KC.F6,      KC.F7,         KC.F8,        KC.F9,      KC.F10,      KC.F11,              KC.F12,
     KC.ESC,              KC.Q,         KC.W,       KC.E,        KC.R,         KC.T,       KC.Y,          KC.U,         KC.I,       KC.O,       KC.P,                 KC.QUOTE,
     KC.TAB,              KC.A,         KC.S,       KC.D,        KC.F,         KC.G,       KC.H,          KC.J,         KC.K,       KC.L,       KC.SCOLON,            KC.ENTER,
     KC.LSHIFT,           KC.Z,         KC.X,       KC.C,        KC.V,         KC.B,       Symbols.enie,  KC.M,         KC.COMMA,   KC.UP ,     KC.SLASH,             KC.RSHIFT,
     KC.LCTRL ,           KC.LGUI,      KC.PGUP,    KC.LALT,     KC.NO,        KC.SPACE,   KC.SPACE,      KC.NO,        KC.LEFT,    KC.DOWN,    KC.RIGHT,             KC.NO,
   ],
     # Layer 2 extra Simbols / Delete, printscreen and caps lock
   [
     KC.TO(3),            KC.N1,        KC.N2,      KC.N3,       KC.N4,        KC.N5,      KC.N6,         KC.N7,        KC.N8,      KC.N9,      KC.N0,                KC.DELETE,
     Symbols.grado,       KC.PLUS,      KC.MINUS,   KC.EQUAL,    KC.UNDERSCORE,KC.T,       KC.Y,          KC.U,         KC.I,       KC.O,       KC.P,                 KC.PSCREEN,
     KC.TAB,              KC.LCBR,      KC.RCBR,    KC.PIPE,     KC.BACKSLASH, KC.G,       KC.H,          KC.J,         KC.K,       KC.L,       KC.SCOLON,            KC.ENTER,
     KC.CAPS,             KC.LBRACKET,  KC.RBRACKET,KC.C,        KC.V,         KC.B,       KC.N,          KC.M,         KC.COMMA,   KC.DOT,     Symbols.abrirpregunta,KC.RSHIFT,
     KC.LCTRL ,           KC.LGUI,      KC.PGUP,    KC.LALT,     KC.NO,        KC.SPACE,   KC.SPACE,      KC.NO,        KC.RALT,    KC.PGDOWN,  KC.RCTRL,             KC.NO,
   ],
    # Layer 3 Game: permanents arrows and extended space
   [
     KC.TO(0),            KC.N1,        KC.N2,      KC.N3,       KC.N4,        KC.N5,      KC.N6,         KC.N7,        KC.N8,      KC.N9,      KC.N0,                KC.BSPC,
     KC.ESC,              KC.Q,         KC.W,       KC.E,        KC.R,         KC.T,       KC.Y,          KC.U,         KC.I,       KC.O,       KC.P,                 KC.QUOTE,
     KC.TAB,              KC.A,         KC.S,       KC.D,        KC.F,         KC.G,       KC.H,          KC.J,         KC.K,       KC.L,       KC.SCOLON,            KC.ENTER,
     KC.LSHIFT,           KC.Z,         KC.X,       KC.C,        KC.V,         KC.B,       KC.N,          KC.M,         KC.COMMA,   KC.UP,      KC.SLASH,             KC.RSHIFT,
     KC.LCTRL ,           KC.LGUI,      KC.PGUP,    KC.LALT,     KC.SPACE,     KC.SPACE,   KC.SPACE,      KC.SPACE,     KC.LEFT,    KC.DOWN,    KC.RIGHT,             KC.MO(1),
   ]
]



if __name__ == '__main__':
    Keyboard.go()

 #
