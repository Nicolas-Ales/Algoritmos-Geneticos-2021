from collections import namedtuple

Capital = namedtuple('Capital', ['id', 'Nombre', 'Distancias'])

capitales = [
    Capital(0, 'Cdad. Bs. As.', [0, 646, 792, 933, 53, 986, 985, 989, 375, 834, 1127, 794, 2082, 979, 1080, 1334, 1282,
                                 1005, 749, 393, 579, 939, 2373, 799]),
    Capital(1, 'Córdoba', [646, 0, 677, 824, 698, 340, 466, 907, 348, 919, 1321, 669, 2281, 362, 517, 809, 745, 412,
                           293, 330, 577, 401, 2618, 1047]),
    Capital(2, 'Corrientes',
            [792, 677, 0, 157, 830, 814, 1131, 1534, 500, 291, 1845, 13, 2819, 691, 633, 742, 719, 1039, 969, 498,
             1136, 535, 3131, 1527]),
    Capital(3, 'Formosa',
            [933, 824, 157, 0, 968, 927, 1269, 1690, 656, 263, 1999, 161, 2974, 793, 703, 750, 741, 1169, 1117, 654,
             1293, 629, 3284, 1681]),
    Capital(4, 'La Plata',
            [53, 698, 830, 968, 0, 1038, 1029, 1005, 427, 857, 1116, 833, 2064, 1030, 1132, 1385, 1333, 1053, 795, 444,
             602, 991, 2350, 789]),
    Capital(5, 'La Rioja',
            [986, 340, 814, 927, 1038, 0, 427, 1063, 659, 1098, 1548, 802, 2473, 149, 330, 600, 533, 283, 435, 640,
             834, 311, 2821, 1311]),
    Capital(6, 'Mendoza',
            [985, 466, 1131, 1269, 1029, 427, 0, 676, 790, 1384, 1201, 1121, 2081, 569, 756, 1023, 957, 152, 235, 775,
             586, 713, 2435, 1019]),
    Capital(7, 'Neuquén',
            [989, 907, 1534, 1690, 1005, 1063, 676, 0, 1053, 1709, 543, 1529, 1410, 1182, 1370, 1658, 1591, 824, 643,
             1049, 422, 1286, 1762, 479]),
    Capital(8, 'Paraná',
            [375, 348, 500, 656, 427, 659, 790, 1053, 0, 658, 1345, 498, 2320, 622, 707, 959, 906, 757, 574, 19, 642,
             566, 2635, 1030]),
    Capital(9, 'Posadas',
            [834, 919, 291, 263, 857, 1098, 1384, 1709, 658, 0, 1951, 305, 2914, 980, 924, 1007, 992, 1306, 1200, 664,
             1293, 827, 3207, 1624]),
    Capital(10, 'Rawson',
            [1127, 1321, 1845, 1999, 1116, 1548, 1201, 543, 1345, 1951, 0, 1843, 975, 1647, 1827, 2120, 2054, 1340,
             1113, 1349, 745, 1721, 1300, 327]),
    Capital(11, 'Resistencia',
            [794, 669, 13, 161, 833, 802, 1121, 1529, 498, 305, 1843, 0, 2818, 678, 620, 729, 706, 1029, 961, 495,
             1132, 523, 3130, 1526]),
    Capital(12, 'Rio Gallegos',
            [2082, 2281, 2819, 2974, 2064, 2473, 2081, 1410, 2320, 2914, 975, 2818, 0, 2587, 2773, 3063, 2997, 2231,
             2046, 2325, 1712, 2677, 359, 1294]),
    Capital(13, 'S.F.d.V.d. Catamarca',
            [979, 362, 691, 793, 1030, 149, 569, 1182, 622, 980, 1647, 678, 2587, 0, 189, 477, 410, 430, 540, 602, 915,
             166, 2931, 1391]),
    Capital(14, 'S.M. de Tucumán',
            [1080, 517, 633, 703, 1132, 330, 756, 1370, 707, 924, 1827, 620, 2773, 189, 0, 293, 228, 612, 727, 689,
             1088, 141, 3116, 1562]),
    Capital(15, 'S.S de Jujuy',
            [1334, 809, 742, 750, 1385, 600, 1023, 1658, 959, 1007, 2120, 729, 3063, 477, 293, 0, 67, 874, 1017, 942,
             1382, 414, 3408, 1855]),
    Capital(16, 'Salta',
            [1282, 745, 719, 741, 1333, 533, 957, 1591, 906, 992, 2054, 706, 2997, 410, 228, 67, 0, 808, 950, 889,
             1316, 353, 3341, 1790]),
    Capital(17, 'San Juan',
            [1005, 412, 1039, 1169, 1053, 283, 152, 824, 757, 1306, 1340, 1029, 2231, 430, 612, 874, 808, 0, 284, 740,
             686, 583, 2585, 1141]),
    Capital(18, 'San Luis',
            [749, 293, 969, 1117, 795, 435, 235, 643, 574, 1200, 1113, 961, 2046, 540, 727, 1017, 950, 284, 0, 560,
             412, 643, 2392, 882]),
    Capital(19, 'Santa Fe',
            [393, 330, 498, 654, 444, 640, 775, 1049, 19, 664, 1349, 495, 2325, 602, 689, 742, 889, 740, 560, 0, 641,
             547, 2641, 1035]),
    Capital(20, 'Santa Rosa',
            [579, 577, 1136, 1293, 602, 834, 586, 422, 642, 1293, 745, 1132, 1712, 915, 1088, 1382, 1316, 686, 412, 641,
             0, 977, 2044, 477]),
    Capital(21, 'Sgo. Del Estero',
            [939, 401, 535, 629, 991, 311, 713, 1286, 566, 827, 1721, 523, 2677, 166, 141, 414, 353, 583, 643, 547, 977,
             0, 3016, 1446]),
    Capital(22, 'Ushuaia',
            [2373, 2618, 3131, 3284, 2350, 2821, 2435, 1762, 2635, 3207, 1300, 3130, 359, 2931, 3116, 3408, 3341, 2585,
             2392, 2641, 2044, 3016, 0, 1605]),
    Capital(23, 'Viedma',
            [799, 1047, 1527, 1681, 789, 1311, 1019, 479, 1030, 1624, 327, 1526, 1294, 1391, 1562, 1855, 1790, 1141,
             882, 1035, 477, 1446, 1605, 0])
]
