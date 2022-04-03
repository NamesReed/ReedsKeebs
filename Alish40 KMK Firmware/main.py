import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()

keyboard = KMKKeyboard()

layers_ext = Layers()

keyboard.modules = [layers_ext, encoder_handler]

#Alish Pins for KB2040
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4, board.D5, board.D10, board.MOSI, board.D9, board.D8, board.D7, board.D6)
keyboard.row_pins = (board.A1, board.A0, board.SCK, board.MISO)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#Alish Encoder Pins for KB2040
encoder_handler.pins = ((board.A3, board.A2, board.SDA, False),)


keyboard.keymap = [
    [#QWERTY
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, 
	    KC.MO(2), KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT, 
	    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.RSFT, 
	    KC.LCTL, KC.TG(3), KC.LALT, KC.NO, KC.MO(1), KC.NO, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    [#Number Layer
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC, 
	    KC.DEL, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.EQL, KC.MINS, KC.LBRC, KC.RBRC, KC.SCLN, 
	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.SLASH, KC.TRNS, 
	    KC.LCTL, KC.TRNS, KC.LALT, KC.NO, KC.TRNS, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    [#Function Layer
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, 
	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
	    KC.LCTL, KC.TRNS, KC.LALT, KC.NO, KC.TRNS, KC.NO, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ],
    [#Gaming Layer (Left and right space)
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, 
	    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT, 
	    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.RSFT, 
	    KC.LCTL, KC.TRNS, KC.LALT, KC.NO, KC.SPC, KC.NO, KC.NO, KC.SPC, KC.NO, KC.LCTL, KC.LEFT, KC.RGHT,
    ]
]

encoder_handler.map = ( ((KC.VOLD, KC.VOLU, KC.MUTE),), 
                        ((KC.DOWN, KC.UP, KC.MUTE),), 
                        ((KC.VOLD, KC.VOLU, KC.N1),), 
                        ((KC.VOLD, KC.VOLU, KC.N1),), 
                        )

if __name__ == '__main__':
    keyboard.go()
