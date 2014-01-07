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
'''wltc.cycles.class3a module: WLTC class data for gear-shift calculator.

Data below extracted from the specs and prepared with the followinf python scripts
found inside the source-distribution:

* ``./util/printwltcclass.py``

* ``./util/csvcolumns8to2.py``
'''
def class_data_a():
    data = {
        'parts': [[0, 589], [590, 1022], [1023, 1477], [1478, 1800]],
        'downscale': {
            'phases': [1532, 1724, 1763],           ## Note: Start end end +1 from specs.
            'p_max_values': [1566, 111.9, 0.50],    ## t, V(Km/h), Accel(m/s2)
            'factor_coeffs': [[1.3, .65, -.65],     ## r0, a1, b1 x 2
                              [1.0, .65, -.65]],
            'v_max_split': 112,                     ## V (Km/h), >
        },
        'cycle': [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 9,
            13, 16, 21, 26, 27, 28, 28, 28, 29, 30, 31, 34, 36, 39, 41, 42,
            43, 43, 44, 44, 44, 42, 39, 37, 34, 32, 29, 25, 22, 20, 20, 19,
            18, 17, 17, 17, 15, 13, 12, 12, 12, 12, 12, 12, 14, 15, 15, 16,
            17, 17, 18, 18, 20, 23, 26, 29, 32, 34, 35, 36, 37, 38, 39, 39,
            39, 38, 37, 37, 36, 35, 35, 34, 34, 31, 27, 22, 17, 14, 12, 9,
            5, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 11, 16, 18,
            19, 20, 22, 25, 27, 29, 29, 29, 27, 22, 17, 13, 12, 12, 14, 17,
            20, 23, 25, 27, 29, 31, 32, 33, 35, 37, 38, 37, 35, 31, 27, 25,
            25, 25, 27, 29, 29, 29, 29, 28, 26, 23, 21, 18, 17, 15, 14, 13,
            12, 12, 12, 12, 12, 12, 12, 12, 13, 14, 15, 16, 19, 21, 23, 26,
            29, 32, 35, 37, 39, 40, 41, 43, 45, 47, 49, 50, 51, 52, 53, 53,
            53, 54, 54, 55, 55, 56, 56, 56, 56, 54, 52, 51, 49, 49, 48, 46,
            44, 41, 39, 37, 34, 32, 29, 25, 22, 20, 20, 19, 18, 17, 17, 17,
            15, 14, 15, 17, 20, 23, 25, 28, 32, 36, 39, 40, 42, 44, 45, 46,
            45, 45, 43, 40, 38, 34, 30, 25, 21, 20, 22, 26, 30, 34, 37, 40,
            44, 47, 49, 49, 49, 48, 47, 46, 46, 46, 47, 47, 47, 47, 46, 45,
            44, 43, 41, 40, 40, 40, 39, 39, 38, 37, 36, 34, 33, 31, 30, 28,
            26, 25, 24, 24, 24, 23, 23, 23, 23, 20, 17, 16, 16, 15, 15, 15,
            14, 14, 14, 15, 17, 21, 24, 25, 25, 25, 26, 26, 27, 27, 28, 28,
            28, 28, 27, 27, 28, 28, 28, 26, 25, 23, 21, 21, 20, 20, 20, 21,
            22, 23, 24, 24, 23, 21, 17, 14, 11, 10, 8, 8, 7, 6, 4, 3,
            2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 8, 12, 16, 20, 24,
            25, 25, 24, 23, 21, 20, 18, 17, 15, 14, 13, 14, 14, 14, 14, 15,
            17, 18, 19, 18, 17, 16, 16, 16, 17, 19, 22, 27, 31, 33, 33, 32,
            31, 31, 31, 30, 29, 26, 23, 18, 12, 7, 3, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 2, 6, 11, 16, 20, 21, 21, 21, 20, 19, 17, 15, 11, 7, 4,
            2, 1, 0, 0, 0, 0, 1, 3, 5, 8, 13, 18, 23, 24, 24, 24,
            23, 22, 20, 18, 17, 16, 15, 14, 14, 13, 13, 13, 13, 13, 13, 14,
            16, 17, 17, 17, 15, 10, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 5, 9, 13, 18, 22,
            26, 29, 32, 36, 39, 42, 45, 48, 48, 48, 47, 47, 45, 44, 44, 44,
            44, 45, 45, 46, 46, 46, 46, 46, 47, 48, 50, 51, 52, 53, 53, 52,
            52, 52, 53, 54, 55, 55, 55, 56, 56, 56, 56, 56, 54, 52, 50, 47,
            43, 39, 36, 34, 31, 26, 20, 15, 13, 12, 12, 14, 19, 23, 28, 32,
            34, 36, 38, 40, 40, 40, 39, 35, 31, 27, 22, 21, 18, 18, 21, 23,
            25, 28, 30, 30, 31, 31, 32, 33, 32, 28, 25, 23, 21, 21, 21, 21,
            20, 19, 17, 15, 12, 12, 13, 17, 21, 21, 21, 18, 13, 12, 12, 13,
            16, 20, 23, 26, 28, 31, 33, 36, 37, 40, 41, 41, 42, 42, 42, 42,
            43, 43, 44, 44, 45, 46, 47, 47, 47, 47, 47, 47, 48, 49, 49, 49,
            49, 49, 48, 47, 46, 43, 39, 34, 29, 23, 18, 14, 12, 12, 16, 20,
            24, 29, 32, 36, 39, 43, 45, 49, 51, 54, 56, 58, 59, 61, 62, 63,
            63, 64, 64, 65, 65, 65, 65, 65, 66, 65, 63, 59, 54, 49, 44, 42,
            41, 41, 43, 45, 46, 48, 49, 51, 52, 51, 49, 47, 43, 39, 35, 31,
            26, 21, 18, 17, 18, 21, 24, 27, 30, 33, 35, 37, 38, 41, 44, 46,
            47, 48, 48, 49, 49, 50, 50, 51, 52, 53, 54, 55, 56, 56, 57, 57,
            57, 58, 60, 61, 61, 62, 62, 63, 63, 63, 63, 64, 65, 65, 66, 67,
            68, 69, 70, 70, 71, 72, 73, 73, 74, 74, 75, 75, 75, 76, 76, 76,
            75, 75, 74, 73, 72, 71, 70, 70, 70, 69, 68, 67, 66, 64, 63, 62,
            62, 61, 61, 61, 61, 60, 59, 54, 49, 44, 42, 41, 41, 42, 44, 46,
            48, 50, 51, 54, 55, 56, 56, 56, 56, 57, 59, 60, 61, 62, 62, 62,
            61, 60, 60, 60, 59, 59, 58, 57, 56, 56, 55, 55, 54, 54, 54, 53,
            53, 54, 54, 55, 55, 56, 56, 55, 52, 48, 43, 37, 32, 27, 25, 27,
            29, 33, 37, 40, 43, 45, 46, 47, 46, 46, 45, 44, 41, 36, 31, 27,
            24, 19, 16, 13, 10, 8, 7, 5, 3, 1, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 8, 14, 20, 24, 28, 31, 35, 37, 39, 41, 43,
            46, 48, 50, 51, 52, 52, 52, 53, 53, 53, 52, 50, 48, 46, 43, 40,
            36, 30, 25, 21, 16, 13, 12, 12, 12, 15, 19, 23, 24, 27, 29, 32,
            34, 37, 40, 43, 46, 48, 50, 52, 54, 55, 57, 58, 58, 58, 58, 58,
            58, 58, 58, 58, 59, 60, 61, 63, 63, 63, 63, 62, 60, 58, 58, 58,
            60, 62, 63, 64, 64, 63, 62, 61, 61, 61, 62, 64, 66, 66, 65, 64,
            63, 62, 62, 61, 60, 57, 55, 50, 45, 40, 36, 32, 29, 26, 23, 19,
            16, 14, 14, 14, 14, 15, 16, 19, 22, 24, 24, 22, 17, 13, 12, 12,
            12, 13, 17, 22, 27, 31, 35, 39, 42, 45, 48, 50, 52, 54, 56, 58,
            60, 61, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 74, 75, 76,
            77, 77, 78, 79, 79, 80, 81, 81, 82, 82, 83, 83, 84, 84, 85, 85,
            86, 86, 87, 88, 88, 88, 89, 89, 89, 90, 90, 91, 91, 91, 91, 92,
            92, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95,
            95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 97,
            97, 97, 97, 97, 97, 97, 97, 97, 96, 96, 96, 96, 95, 95, 95, 95,
            95, 94, 94, 94, 94, 94, 94, 94, 94, 93, 93, 92, 92, 91, 90, 90,
            89, 88, 88, 87, 86, 86, 85, 84, 84, 83, 82, 82, 81, 81, 80, 79,
            79, 79, 78, 78, 78, 77, 77, 77, 77, 76, 76, 76, 76, 75, 76, 76,
            76, 76, 76, 76, 76, 77, 77, 77, 77, 77, 78, 78, 78, 79, 80, 80,
            81, 81, 81, 81, 81, 80, 80, 80, 80, 79, 79, 79, 79, 79, 80, 80,
            80, 81, 81, 81, 81, 81, 80, 79, 78, 76, 75, 73, 72, 70, 68, 66,
            63, 61, 60, 59, 60, 61, 62, 62, 61, 60, 58, 57, 57, 57, 57, 56,
            54, 50, 45, 40, 34, 29, 28, 29, 30, 31, 32, 35, 38, 40, 42, 45,
            47, 48, 49, 49, 49, 48, 47, 46, 45, 44, 42, 40, 37, 33, 30, 28,
            27, 27, 27, 27, 27, 26, 26, 28, 31, 34, 38, 40, 41, 40, 38, 35,
            34, 34, 36, 39, 41, 42, 41, 40, 36, 31, 26, 20, 19, 19, 21, 22,
            22, 21, 19, 18, 18, 18, 18, 17, 15, 9, 4, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 7, 9, 10, 11, 12, 14,
            17, 19, 23, 26, 30, 34, 37, 40, 43, 45, 47, 49, 50, 51, 52, 52,
            53, 54, 54, 55, 55, 56, 57, 58, 60, 62, 64, 67, 69, 70, 71, 72,
            73, 73, 74, 74, 73, 72, 70, 68, 66, 64, 62, 60, 60, 60, 60, 61,
            63, 65, 68, 71, 74, 78, 81, 84, 87, 89, 90, 90, 91, 91, 92, 92,
            93, 94, 94, 95, 96, 97, 98, 100, 102, 103, 105, 106, 108, 110, 111, 113,
            115, 116, 118, 119, 120, 121, 122, 123, 123, 123, 123, 123, 123, 122, 122, 121,
            120, 120, 119, 118, 117, 116, 115, 114, 114, 114, 113, 113, 113, 112, 112, 111,
            110, 109, 108, 107, 107, 106, 106, 106, 106, 106, 106, 106, 106, 107, 107, 108,
            109, 110, 111, 113, 114, 115, 115, 116, 116, 116, 116, 115, 113, 112, 110, 108,
            107, 106, 105, 105, 105, 105, 105, 104, 104, 104, 103, 103, 104, 105, 106, 107,
            108, 109, 111, 112, 113, 115, 116, 116, 117, 118, 119, 120, 120, 121, 122, 123,
            123, 124, 125, 125, 125, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126,
            126, 125, 125, 125, 125, 126, 126, 127, 127, 127, 127, 127, 128, 128, 128, 128,
            128, 128, 128, 128, 128, 128, 128, 127, 127, 127, 127, 127, 126, 126, 126, 126,
            126, 127, 127, 127, 128, 128, 129, 129, 130, 130, 131, 131, 131, 131, 130, 129,
            128, 126, 124, 121, 119, 116, 114, 111, 109, 107, 104, 102, 100, 98, 97, 95,
            94, 93, 92, 91, 91, 90, 89, 89, 88, 88, 87, 87, 86, 86, 85, 85,
            84, 83, 83, 82, 82, 81, 80, 79, 77, 75, 72, 69, 65, 62, 59, 57,
            54, 52, 49, 46, 43, 39, 36, 33, 30, 28, 26, 24, 22, 20, 18, 15,
            12, 8, 5, 0, 0, 0, 0, 0, 0,
        ],
    }

    return data


def class_data_b():
    cycle = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 9,
        13, 16, 21, 26, 27, 28, 28, 28, 29, 30, 31, 34, 36, 39, 41, 42,
        43, 43, 44, 44, 44, 42, 39, 37, 34, 32, 29, 25, 22, 20, 20, 19,
        18, 17, 17, 17, 15, 13, 12, 12, 12, 12, 12, 12, 14, 15, 15, 16,
        17, 17, 18, 18, 20, 23, 26, 29, 32, 34, 35, 36, 37, 38, 39, 39,
        39, 38, 37, 37, 36, 35, 35, 34, 34, 31, 27, 22, 17, 14, 12, 9,
        5, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 11, 16, 18,
        19, 20, 22, 25, 27, 29, 29, 29, 27, 22, 17, 13, 12, 12, 14, 17,
        20, 23, 25, 27, 29, 31, 32, 33, 35, 37, 38, 37, 35, 31, 27, 25,
        25, 25, 27, 29, 29, 29, 29, 28, 26, 23, 21, 18, 17, 15, 14, 13,
        12, 12, 12, 12, 12, 12, 12, 12, 13, 14, 15, 16, 19, 21, 23, 26,
        29, 32, 35, 37, 39, 40, 41, 43, 45, 47, 49, 50, 51, 52, 53, 53,
        53, 54, 54, 55, 55, 56, 56, 56, 56, 54, 52, 51, 49, 49, 48, 46,
        44, 41, 39, 37, 34, 32, 29, 25, 22, 20, 20, 19, 18, 17, 17, 17,
        15, 14, 15, 17, 20, 23, 25, 28, 32, 36, 39, 40, 42, 44, 45, 46,
        45, 45, 43, 40, 38, 34, 30, 25, 21, 20, 22, 26, 30, 34, 37, 40,
        44, 47, 49, 49, 49, 48, 47, 46, 46, 46, 47, 47, 47, 47, 46, 45,
        44, 43, 41, 40, 40, 40, 39, 39, 38, 37, 36, 34, 33, 31, 30, 28,
        26, 25, 24, 24, 24, 23, 23, 23, 23, 20, 17, 16, 16, 15, 15, 15,
        14, 14, 14, 15, 17, 21, 24, 25, 25, 25, 26, 26, 27, 27, 28, 28,
        28, 28, 27, 27, 28, 28, 28, 26, 25, 23, 21, 21, 20, 20, 20, 21,
        22, 23, 24, 24, 23, 21, 17, 14, 11, 10, 8, 8, 7, 6, 4, 3,
        2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 4, 8, 12, 16, 20, 24,
        25, 25, 24, 23, 21, 20, 18, 17, 15, 14, 13, 14, 14, 14, 14, 15,
        17, 18, 19, 18, 17, 16, 16, 16, 17, 19, 22, 27, 31, 33, 33, 32,
        31, 31, 31, 30, 29, 26, 23, 18, 12, 7, 3, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 2, 6, 11, 16, 20, 21, 21, 21, 20, 19, 17, 15, 11, 7, 4,
        2, 1, 0, 0, 0, 0, 1, 3, 5, 8, 13, 18, 23, 24, 24, 24,
        23, 22, 20, 18, 17, 16, 15, 14, 14, 13, 13, 13, 13, 13, 13, 14,
        16, 17, 17, 17, 15, 10, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 9, 14, 19, 25,
        30, 34, 38, 42, 46, 48, 48, 48, 48, 48, 47, 47, 45, 44, 44, 44,
        44, 45, 45, 46, 46, 46, 46, 46, 47, 48, 50, 51, 52, 53, 53, 52,
        52, 52, 53, 54, 55, 55, 55, 56, 56, 56, 56, 56, 54, 52, 50, 47,
        43, 39, 36, 34, 31, 26, 20, 15, 13, 12, 12, 14, 19, 23, 28, 32,
        34, 36, 38, 40, 40, 40, 39, 35, 31, 27, 22, 21, 18, 18, 21, 23,
        25, 28, 30, 30, 31, 31, 32, 33, 32, 28, 25, 23, 21, 21, 21, 21,
        20, 19, 17, 15, 12, 12, 13, 17, 21, 21, 21, 18, 13, 12, 12, 13,
        16, 18, 20, 22, 24, 26, 29, 34, 37, 40, 41, 41, 42, 42, 42, 42,
        43, 43, 44, 44, 45, 46, 47, 47, 47, 47, 47, 47, 48, 49, 49, 49,
        49, 49, 48, 47, 46, 43, 39, 34, 29, 23, 18, 14, 12, 12, 16, 19,
        22, 25, 30, 35, 39, 44, 47, 50, 54, 56, 58, 59, 61, 62, 62, 63,
        63, 64, 64, 65, 65, 65, 65, 65, 66, 65, 63, 59, 54, 49, 44, 42,
        41, 41, 42, 44, 48, 51, 52, 53, 52, 51, 49, 47, 43, 39, 35, 31,
        26, 21, 18, 17, 18, 21, 24, 27, 30, 33, 35, 37, 38, 41, 44, 46,
        47, 48, 48, 49, 49, 50, 50, 51, 52, 53, 54, 55, 56, 56, 57, 57,
        57, 58, 60, 61, 61, 62, 62, 63, 63, 63, 64, 65, 66, 67, 68, 71,
        72, 72, 73, 74, 76, 76, 76, 76, 75, 75, 74, 73, 72, 71, 70, 70,
        70, 69, 68, 68, 68, 68, 68, 68, 68, 68, 68, 67, 66, 64, 63, 62,
        62, 61, 61, 61, 61, 60, 59, 54, 49, 44, 42, 41, 41, 42, 44, 48,
        51, 52, 54, 57, 58, 59, 59, 59, 59, 60, 62, 63, 65, 64, 62, 62,
        61, 60, 60, 60, 59, 59, 58, 57, 56, 56, 55, 55, 54, 54, 54, 53,
        53, 54, 54, 55, 55, 56, 56, 55, 52, 48, 43, 37, 32, 27, 25, 26,
        29, 34, 40, 45, 49, 51, 52, 52, 52, 51, 50, 49, 45, 40, 35, 30,
        24, 19, 16, 13, 10, 8, 7, 5, 3, 1, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 3, 8, 14, 20, 24, 28, 31, 35, 37, 39, 41, 43,
        46, 48, 50, 51, 52, 52, 52, 53, 53, 53, 52, 50, 48, 46, 43, 40,
        36, 30, 25, 21, 16, 13, 12, 12, 12, 15, 19, 23, 24, 25, 26, 28,
        31, 35, 39, 44, 49, 53, 56, 58, 61, 62, 63, 62, 60, 59, 58, 58,
        58, 58, 58, 58, 59, 60, 61, 63, 63, 63, 63, 62, 60, 58, 58, 58,
        60, 62, 63, 64, 64, 63, 62, 61, 61, 62, 65, 68, 69, 69, 69, 68,
        66, 66, 65, 64, 63, 60, 55, 50, 45, 40, 36, 32, 29, 26, 23, 19,
        16, 14, 14, 14, 14, 15, 16, 19, 22, 24, 24, 22, 17, 13, 12, 12,
        12, 13, 17, 22, 27, 31, 35, 39, 42, 45, 48, 50, 52, 54, 56, 58,
        60, 61, 63, 64, 65, 67, 68, 69, 70, 71, 72, 73, 74, 74, 75, 76,
        77, 77, 78, 79, 79, 80, 81, 81, 82, 82, 83, 83, 84, 84, 85, 85,
        86, 86, 87, 88, 88, 88, 89, 89, 89, 90, 90, 91, 91, 91, 91, 92,
        92, 93, 93, 93, 93, 93, 94, 94, 94, 94, 94, 94, 94, 95, 95, 95,
        95, 95, 95, 95, 96, 96, 96, 96, 96, 96, 97, 97, 97, 97, 97, 97,
        97, 97, 97, 97, 97, 97, 97, 97, 96, 96, 96, 96, 95, 95, 95, 95,
        95, 94, 94, 94, 94, 94, 94, 94, 94, 93, 93, 92, 92, 91, 90, 90,
        89, 88, 88, 87, 86, 86, 85, 84, 84, 83, 82, 82, 81, 81, 80, 79,
        79, 79, 78, 78, 78, 77, 77, 77, 77, 76, 76, 76, 76, 75, 75, 75,
        75, 75, 75, 75, 74, 74, 73, 73, 73, 74, 74, 76, 77, 79, 80, 80,
        81, 81, 81, 81, 81, 80, 80, 80, 80, 79, 79, 79, 79, 79, 80, 80,
        80, 81, 81, 81, 81, 81, 80, 79, 78, 76, 75, 73, 72, 70, 68, 66,
        63, 61, 60, 59, 60, 61, 62, 62, 61, 60, 58, 57, 57, 57, 57, 56,
        54, 50, 45, 40, 34, 29, 27, 29, 32, 35, 36, 37, 39, 42, 46, 50,
        52, 54, 54, 54, 54, 54, 53, 52, 50, 49, 47, 45, 41, 36, 31, 27,
        26, 27, 27, 27, 27, 26, 26, 28, 31, 34, 38, 40, 41, 40, 38, 35,
        34, 34, 36, 39, 41, 42, 41, 40, 36, 31, 26, 20, 19, 19, 21, 22,
        22, 21, 19, 18, 18, 18, 18, 17, 15, 9, 4, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 7, 9, 10, 11, 12, 14,
        17, 19, 23, 26, 30, 34, 37, 40, 43, 45, 47, 49, 50, 51, 52, 52,
        53, 54, 54, 55, 55, 56, 57, 58, 60, 62, 64, 67, 69, 70, 71, 72,
        73, 73, 74, 74, 73, 72, 70, 68, 66, 64, 62, 60, 60, 60, 60, 61,
        63, 65, 68, 71, 74, 78, 81, 84, 87, 89, 90, 90, 91, 91, 92, 92,
        93, 94, 94, 95, 96, 97, 98, 100, 102, 103, 105, 106, 108, 110, 111, 113,
        115, 116, 118, 119, 120, 121, 122, 123, 123, 123, 123, 123, 123, 122, 122, 121,
        120, 120, 119, 118, 117, 116, 115, 114, 114, 114, 113, 113, 113, 112, 112, 111,
        110, 109, 108, 107, 107, 106, 106, 106, 106, 106, 106, 106, 106, 107, 107, 108,
        109, 110, 111, 113, 114, 115, 115, 116, 116, 116, 116, 115, 113, 112, 110, 108,
        107, 106, 105, 105, 105, 105, 105, 104, 104, 104, 103, 103, 104, 105, 106, 107,
        108, 109, 111, 112, 113, 115, 116, 116, 117, 118, 119, 120, 120, 121, 122, 123,
        123, 124, 125, 125, 125, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126, 126,
        126, 125, 125, 125, 125, 126, 126, 127, 127, 127, 127, 127, 128, 128, 128, 128,
        128, 128, 128, 128, 128, 128, 128, 127, 127, 127, 127, 127, 126, 126, 126, 126,
        126, 127, 127, 127, 128, 128, 129, 129, 130, 130, 131, 131, 131, 131, 130, 129,
        128, 126, 124, 121, 119, 116, 114, 111, 109, 107, 104, 102, 100, 98, 97, 95,
        94, 93, 92, 91, 91, 90, 89, 89, 88, 88, 87, 87, 86, 86, 85, 85,
        84, 83, 83, 82, 82, 81, 80, 79, 77, 75, 72, 69, 65, 62, 59, 57,
        54, 52, 49, 46, 43, 39, 36, 33, 30, 28, 26, 24, 22, 20, 18, 15,
        12, 8, 5, 0, 0, 0, 0, 0, 0,
    ]


    data = class_data_a()
    data['cycle'] = cycle

    return data

