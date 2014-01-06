#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2013-2014 ankostis@gmail.com
#
# This file is part of wltc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
'''wltc.cycles.class1 module: WLTC class data for gear-shift calculator.

Data below extracted from the specs and prepared with the followinf python scripts
found inside the source-distribution:

* ``./util/printwltcclass.py``

* ``./util/csvcolumns8to2.py``
'''

def class_data():
    data = {
        'parts': [[0, 589], [590, 1022]],
        'downscale': {
            'phases': [[651, 847], [849, 906]],
            'max_p_values': [764, 61.4, 0.22],         ## t, V(Km/h), Accel(m/s2)
            'factor_coeffs': [1, 0.54, -0.54],  ## r0, a1, b1
        },
        'cycle': [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 5, 8,
            10, 12, 13, 15, 16, 17, 18, 18, 18, 18, 16, 14, 10, 7, 4, 0,
            0, 0, 0, 1, 3, 5, 7, 9, 10, 12, 13, 15, 16, 17, 18, 18,
            19, 20, 20, 21, 22, 23, 23, 24, 25, 25, 25, 23, 21, 19, 17, 14,
            12, 9, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2,
            3, 4, 6, 7, 9, 11, 12, 14, 16, 18, 20, 21, 23, 25, 26, 28,
            30, 31, 32, 33, 33, 33, 33, 34, 34, 34, 34, 35, 35, 35, 35, 36,
            37, 38, 39, 40, 40, 41, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42,
            42, 43, 43, 43, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 43,
            43, 43, 43, 43, 43, 43, 43, 42, 42, 42, 42, 42, 42, 42, 42, 42,
            42, 42, 42, 43, 43, 43, 43, 43, 43, 42, 42, 42, 41, 41, 41, 40,
            39, 39, 38, 38, 37, 36, 36, 35, 35, 34, 33, 33, 33, 33, 33, 34,
            34, 35, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39, 39, 39, 39, 40,
            40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 39, 38, 37, 35, 33, 31,
            29, 27, 26, 26, 26, 26, 27, 28, 29, 30, 31, 31, 32, 33, 33, 33,
            34, 34, 34, 33, 33, 32, 31, 30, 29, 28, 27, 27, 26, 25, 25, 24,
            24, 24, 24, 23, 23, 23, 23, 23, 23, 23, 23, 23, 22, 22, 22, 21,
            21, 20, 19, 18, 17, 16, 15, 14, 14, 14, 14, 13, 13, 13, 13, 13,
            13, 13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 14,
            14, 14, 13, 11, 10, 8, 7, 6, 5, 5, 4, 4, 3, 3, 2, 2,
            1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 10, 12, 14,
            16, 17, 19, 19, 20, 20, 20, 21, 21, 22, 23, 24, 25, 26, 26, 26,
            26, 26, 26, 26, 26, 27, 27, 28, 28, 29, 31, 31, 32, 32, 32, 32,
            31, 30, 28, 27, 24, 22, 19, 17, 14, 12, 9, 7, 4, 2, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 3, 4, 6, 7, 9, 11, 13, 15, 16, 18, 20, 21, 23, 24,
            26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 40, 41, 41, 42, 43, 44,
            44, 45, 45, 45, 45, 44, 44, 43, 43, 42, 42, 42, 43, 43, 44, 45,
            46, 47, 47, 48, 48, 48, 48, 49, 49, 49, 48, 48, 48, 48, 48, 48,
            48, 47, 46, 45, 44, 42, 40, 38, 35, 31, 28, 25, 22, 20, 17, 15,
            12, 10, 7, 6, 4, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 7, 9, 11, 14,
            15, 18, 19, 21, 23, 24, 25, 26, 27, 27, 28, 28, 28, 29, 29, 29,
            29, 29, 28, 28, 28, 27, 26, 26, 24, 22, 21, 19, 18, 18, 19, 20,
            21, 23, 24, 26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 43, 44, 44, 44, 45, 45, 46, 46, 47, 47, 48, 48, 49,
            49, 50, 50, 51, 51, 52, 52, 53, 54, 54, 55, 55, 56, 56, 57, 57,
            58, 58, 58, 58, 58, 57, 56, 56, 55, 55, 55, 54, 54, 54, 54, 54,
            54, 53, 53, 53, 52, 52, 51, 51, 51, 51, 52, 52, 52, 52, 53, 53,
            53, 53, 53, 53, 53, 54, 54, 54, 55, 56, 57, 57, 58, 59, 60, 60,
            61, 61, 61, 61, 61, 61, 60, 60, 59, 59, 58, 58, 58, 57, 57, 57,
            57, 57, 56, 56, 56, 56, 57, 57, 58, 59, 59, 60, 61, 62, 62, 63,
            64, 64, 64, 64, 63, 62, 62, 62, 61, 61, 61, 61, 60, 60, 59, 58,
            58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43,
            42, 40, 39, 38, 38, 37, 37, 36, 37, 37, 37, 38, 38, 39, 39, 40,
            40, 41, 41, 42, 43, 44, 45, 45, 46, 47, 48, 49, 50, 51, 52, 53,
            54, 54, 55, 55, 56, 56, 56, 57, 57, 58, 58, 59, 60, 60, 61, 61,
            61, 61, 61, 60, 60, 59, 58, 58, 57, 57, 57, 56, 56, 56, 55, 55,
            55, 55, 54, 54, 54, 54, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53,
            53, 53, 53, 53, 52, 52, 51, 51, 50, 49, 48, 47, 46, 45, 45, 44,
            43, 43, 42, 42, 42, 41, 41, 40, 39, 38, 37, 36, 36, 36, 36, 37,
            38, 39, 39, 40, 40, 41, 41, 42, 42, 43, 43, 44, 44, 44, 44, 44,
            44, 44, 44, 44, 44, 44, 43, 43, 42, 42, 41, 40, 39, 38, 37, 36,
            36, 35, 35, 34, 34, 34, 33, 33, 33, 33, 32, 32, 31, 31, 31, 30,
            30, 29, 29, 28, 27, 26, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17,
            16, 14, 13, 11, 9, 7, 5, 3, 1, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        ],
    }

    return data