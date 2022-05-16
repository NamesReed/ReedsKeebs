
#ifndef KB_H
#define KB_H

#include "quantum.h"

#define KEYMAP( \
	K000, K001, K002, K003, K004, K005,       K007, K008, K009, K010, K011, K012,       \
	K100, K101, K102, K103, K104, K105, K106, K107, K108, K109, K110, K111, K112,       \
	K200, K201, K202, K203, K204, K205, K206, K207, K208, K209, K210, K211, K212,       \
	                        K304, K305, K306, K307, K308  \
) { \
	{ K000,  K001,  K002,  K003,  K004,  K005,  KC_NO, K007,  K008,  K009,  K010,  K011,  K012 }, \
	{ K100,  K101,  K102,  K103,  K104,  K105,  K106,  K107,  K108,  K109,  K110,  K111,  K112 }, \
	{ K200,  K201,  K202,  K203,  K204,  K205,  K206,  K207,  K208,  K209,  K210,  K211,  K212 }, \
	{ KC_NO, KC_NO, KC_NO, KC_NO, K304,  K305,  K306,  K307,  K308,  KC_NO, KC_NO, KC_NO, KC_NO }  \
}

#endif