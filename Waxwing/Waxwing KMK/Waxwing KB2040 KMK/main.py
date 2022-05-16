import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers



keyboard = KMKKeyboard()
layers_ext = Layers()

keyboard.modules = [layers_ext]


from kmk.extensions.rgb import RGB


rgb_ext = RGB(pixel_pin=board.A3, num_pixels=4)
keyboard.extensions.append(rgb_ext)


#Waxwing Pins for KB2040
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D7, board.D8, board.D9, board.A2, board.D10, board.MOSI, board.MISO, board.SCK, board.A0, board.A1)
keyboard.row_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [#QWERTY
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.NO, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.BSPC, 
	    KC.MO(2), KC.A, KC.S, KC.D, KC.F, KC.G, KC.B, KC.H, KC.J, KC.K, KC.L, KC.QUOT, KC.ENT, 
	    KC.LSFT, KC.LCTRL, KC.Z, KC.X, KC.C, KC.V, KC.MO(1), KC.N, KC.M, KC.COMM, KC.DOT, KC.SLASH, KC.RSFT, 
	    KC.NO, KC.NO, KC.NO, KC.NO, KC.LCTRL, KC.LALT, KC.MO(1), KC.SPC, KC.RCTRL, KC.NO, KC.NO, KC.NO, KC.NO
    ],
    [#Number Layer
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.NO, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.BSPC, 
	    KC.DEL, KC.RGB_TOG, KC.RGB_HUI, KC.RGB_HUD, KC.RGB_VAI, KC.RGB_VAD, KC.TRNS, KC.LBRC, KC.RBRC, KC.MINUS, KC.EQUAL, KC.QUOT, KC.SCLN, 
	    KC.TRNS, KC.TRNS, KC.RGB_SAI, KC.RGB_SAD, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
	    KC.NO, KC.NO, KC.NO, KC.NO, KC.LCTRL, KC.LALT, KC.SPC, KC.RALT, KC.RCTRL, KC.NO, KC.NO, KC.NO, KC.NO
    ],

    [#Function Layer
        KC.ESC, KC.F1, KC.UP, KC.F3, KC.F4, KC.F5, KC.NO, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.BSPC, 
	    KC.TRNS, KC.LEFT, KC.DOWN, KC.RIGHT, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.QUOT, KC.ENT, 
	    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
	    KC.NO, KC.NO, KC.NO, KC.NO, KC.LCTRL, KC.LALT, KC.SPC, KC.VOLD, KC.VOLU, KC.NO, KC.NO, KC.NO, KC.NO
    ],
]

if __name__ == '__main__':
    keyboard.go() 