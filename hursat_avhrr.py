#Appendix: A list of color tables courtesy Deelan Jariwale, Elliot Fossier and "Adam" you can use in place of the other IR tables: RUN THIS FIRST!
from matplotlib.colors import LinearSegmentedColormap
def bd():
    newcmp = LinearSegmentedColormap.from_list("", [
        (0/120, "#a8d1ff"), (11/120, "#000000"),
        (12/120, "#000000"), (12/120, "#1d1d1d"),
        (21/120, "#fafafa"), (21/120, "#3a3a3a"),
        (60/120, "#d2d2d2"), (60/120, "#5b5b5b"),
        (71/120, "#5b5b5b"), (71/120, "#9a9a9a"),
        (83/120, "#9a9a9a"), (83/120, "#b7b7b7"),
        (93/120, "#b7b7b7"), (93/120, "#000000"),
        (99/120, "#000000"), (99/120, "#f9f9f9"),
        (105/120, "#f9f9f9"), (105/120, "#9e9e9e"),
        (110/120, "#9e9e9e"), (110/120, "#424242"),
        (120/120, "#424242")
    ])
    vmax = 30 + 273.15  # 30°C to Kelvin
    vmin = -90 + 273.15  # -90°C to Kelvin
    return newcmp.reversed(), vmax, vmin

def rammb():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#b55555"),
    (10/150, "#000000"),
    (25/150, "#000000"),
    (80/150, "#fefefe"),
    (80/150, "#a8fdfd"),
    (100/150, "#545454"),
    (100/150, "#000067"),
    (110/150, "#0000fe"),
    (110/150, "#00600d"),
    (120/150, "#00fc00"),
    (120/150, "#4d0d00"),
    (130/150, "#fb0000"),
    (130/150, "#fcfc00"),
    (140/150, "#000000"),
    (140/150, "#FFFFFF"),
    (150/150, "#040404")])

    vmax = 50  + 273.15
    vmin = -100  + 273.15
    return newcmp.reversed(), vmax, vmin

def ca():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, '#000000'),
    (19/130, "#626466"),
    (21/130, "#1c2a7a"),
    (30/130, "#0b3a54"),
    (40/130, "#15476b"),
    (60/130, "#098292"),
    (70/130, "#18bc71"),
    (80/130, "#61ec22"),
    (87.5/130, "#e8ed29"),
    (95/130, "#f88d1e"),
    (105/130, "#ce221c"),
    (110/130, "#ac61ce"),
    (115/130, "#563ab4"),
    (120/130, "#cbcbfe"),
    (130/130, "#FFFFFF")])

    vmax = 30 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def rainbow():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/145, '#110112'),
    (15/145, '#ff09fd'),
    (32.5/145, '#00007d'),
    (50/145, "#06fefe"),
    (70/145, "#007d0c"),
    (87/145, "#ffff2d"),
    (123/145, "#7d0706"),
    (135/145, "#ff1a18"),
    (145/145, "#FFFFFF")])

    vmax = 55 + 273.15
    vmin = -90 + 273.15

    return newcmp.reversed(), vmax, vmin

def avn():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/131, "#000000"),
    (80/131, "#FFFFFF"),
    (80/131, "#0096FF"),
    (100/131, "#006e96"),
    (100/131, "#a0a000"),
    (110/131, "#fafa00"),
    (110/131, "#fafa00"),
    (120/131, "#c87800"),
    (120/131, "#fa0000"),
    (130/131, "#c80000"),
    (131/131, "#585858")])

    vmax = 50 + 273.15
    vmin = -81 + 273.15

    return newcmp.reversed(), vmax, vmin

def funktop():
    newcmp=LinearSegmentedColormap.from_list("",[
    (0/128, "#000000"),
    (1/128, "#141414"),
    (54/128, "#d8d8d8"),
    (55/128, "#646400"),
    (74/128, "#f8f800"),
    (75/128, "#000078"),
    (94/128, "#00fcfc"),
    (95/128, "#540000"),
    (106/128,"#fc0000"),
    (107/128,"#fc5050"),
    (114/128,"#fc8c8c"),
    (115/128,"#00fc00"),
    (127/128,"#fcfcfc"),
    (128/128,"#fcfcfc")])

    vmax = 36 + 273.15
    vmin = -92 + 273.15

    return newcmp.reversed(), vmax, vmin

def jsl():
    newcmp=LinearSegmentedColormap.from_list("",[
    (0/167, "#000000"),
    (1.5/167, "#000000"),
    (2/167, "#1C001C"),
    (3.5/167, "#1C001C"),
    (4/167, "#3C003C"),
    (5.5/167, "#3C003C"),
    (6/167, "#5C005C"),
    (7.5/167, "#5C005C"),
    (8/167, "#7C007C"),
    (9.5/167, "#7C007C"),
    (10/167, "#9C009C"),
    (11.5/167, "#9C009C"),
    (12/167, "#BC00BC"),
    (13.5/167, "#BC00BC"),
    (14/167, "#DC00DC"),
    (15.5/167, "#DC00DC"),
    (16/167, "#FC00FC"),
    (17.5/167, "#FC00FC"),
    (18/167, "#E000EC"),
    (19.5/167, "#E000EC"),
    (20/167, "#C400DC"),
    (21.5/167, "#C400DC"),
    (22/167, "#A800D0"),
    (23.5/167, "#A800D0"),
    (24/167, "#8C00C0"),
    (25.5/167, "#8C00C0"),
    (26/167, "#7000B4"),
    (27.5/167, "#7000B4"),
    (28/167, "#5400A4"),
    (29.5/167, "#5400A4"),
    (30/167, "#380098"),
    (31.5/167, "#380098"),
    (32/167, "#1C0088"),
    (33.5/167, "#1C0088"),
    (34/167, "#00007C"),
    (35.5/167, "#00007C"),
    (36/167, "#001C88"),
    (37.5/167, "#001C88"),
    (38/167, "#003898"),
    (39.5/167, "#003898"),
    (40/167, "#0054A4"),
    (41.5/167, "#0054A4"),
    (42/167, "#0070B4"),
    (43.5/167, "#0070B4"),
    (44/167, "#008CC0"),
    (45.5/167, "#008CC0"),
    (46/167, "#00A8D0"),
    (47.5/167, "#00A8D0"),
    (48/167, "#00C4DC"),
    (49.5/167, "#00C4DC"),
    (50/167, "#00E0EC"),
    (51.5/167, "#00E0EC"),
    (52/167, "#00FCFC"),
    (53.5/167, "#00FCFC"),
    (54/167, "#00ECE0"),
    (55.5/167, "#00ECE0"),
    (56/167, "#00DCC4"),
    (57.5/167, "#00DCC4"),
    (58/167, "#5C5C5C"),
    (65.5/167, "#686868"),
    (66/167, "#707070"),
    (71.5/167, "#787878"),
    (72/167, "#808080"),
    (77.5/167, "#888888"),
    (78/167, "#909090"),
    (83.5/167, "#989898"),
    (84/167, "#A0A0A0"),
    (91/167, "#A8A8A8"),
    (92/167, "#B0B0B0"),
    (95/167, "#B0B0B0"),
    (96/167, "#B8B8B8"),
    (99/167, "#B8B8B8"),
    (100/167, "#C0C0C0"),
    (103/167, "#C0C0C0"),
    (104/167, "#C8C8C8"),
    (107/167, "#C8C8C8"),
    (108/167, "#D0D0D0"),
    (111/167, "#D0D0D0"),
    (112/167, "#D8D8D8"),
    (113/167, "#D8D8D8"),
    (114/167, "#3C0000"),
    (126/167, "#FF3C3C"),
    (127/167, "#FF4747"),
    (137/167, "#FFBEBE"),
    (138/167, "#650065"),
    (157/167, "#DEC9DE"),
    (158/167, "#000000"),
    (167/167, "#000000")])

    vmax = 57 + 273.15
    vmin = -110 + 273.15

    return newcmp.reversed(), vmax, vmin

def bd05():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#000000"),
    (21/120, "#fafafa"),
    (21/120, "#3a3a3a"),
    (60/120, "#d2d2d2"),
    (60/120, "#5b5b5b"),
    (71/120, "#5b5b5b"),
    (71/120, "#9a9a9a"),
    (83/120, "#9a9a9a"),
    (83/120, "#b7b7b7"),
    (93/120, "#b7b7b7"),
    (93/120, "#000000"),
    (99/120, "#000000"),
    (99/120, "#f9f9f9"),
    (105/120, "#f9f9f9"),
    (105/120, "#9e9e9e"),
    (110/120, "#9e9e9e"),
    (110/120, "#424242"),
    (120/120, "#424242")])

    vmax = 30 + 273.15
    vmin = -90 + 273.15

    return newcmp.reversed(), vmax, vmin

def bd2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#b58555"),
    (12/120, "#090926"),

    (21/120, "#ffffff"),
    (21/120, "#fefefe"),
    (60/120, "#4c8032"),

    (60/120, "#ffff29"),
    (71/120, "#ffff29"),

    (71/120, "#ff8129"),
    (83/120, "#ff8129"),

    (83/120, "#ff2929"),
    (93/120, "#ff2929"),

    (93/120, "#000000"),
    (99/120, "#000000"),

    (99/120, "#e6dada"),
    (105/120, "#e6dada"),

    (105/120, "#261940"),
    (110/120, "#261940"),

    (110/120, "#990f97"),
    (120/120, "#990f97")])

    vmax = 30 + 273.15
    vmin = -90 + 273.15

    return newcmp.reversed(), vmax, vmin

def bd3():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#b58555"),
    (22/130, "#090926"),
    (22/130, "#000000"),

    (31/130, "#ffffff"),
    (31/130, "#fefefe"),
    (70/130, "#404080"),

    (70/130, "#ffe329"),
    (81/130, "#ffe329"),

    (81/130, "#de7022"),
    (93/130, "#de7022"),

    (93/130, "#b31b1b"),
    (103/130, "#b31b1b"),

    (103/130, "#2e0202"),
    (109/130, "#2e0202"),

    (109/130, "#e6dada"),
    (115/130, "#e6dada"),

    (115/130, "#bc67b7"),
    (120/130, "#bc67b7"),

    (120/130, "#990f97"),
    (125/130, "#990f97"),

    (125/130, "#601f60"),
    (130/130, "#601f60")])

    vmax = 40 + 273.15
    vmin = -90 + 273.15

    return newcmp.reversed(), vmax, vmin

def ibtracs():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#000000"),
    (12/120, "#b881a1"),
    (12/120, "#000000"),
    (12/120, "#1d1d1d"),
    (21/120, "#fafafa"),
    (21/120, "#664848"),
    (60/120, "#ffe1e1"),
    (60/120, "#9f2323"),
    (71/120, "#9f2323"),

    (71/120, "#ff6e1c"),
    (83/120, "#ff6e1c"),

    (83/120, "#ffe132"),
    (93/120, "#ffe132"),

    (93/120, "#a0d2fe"),
    (99/120, "#a0d2fe"),

    (99/120, "#02bffd"),
    (105/120, "#02bffd"),

    (105/120, "#4169e1"),
    (110/120, "#4169e1"),

    (110/120, "#000096"),
    (115/120, "#000096"),

    (115/120, "#FFFFFF"),
    (120/120, "#FFFFFF")])

    vmax = 30 + 273.15
    vmin = -90 + 273.15

    return newcmp.reversed(), vmax, vmin

def ibtracs2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#000000"),
    (21/120, "#fafafa"),
    (21/120, "#664848"),
    (60/120, "#ffe1e1"),
    (60/120, "#9f2323"),
    (71/120, "#9f2323"),

    (71/120, "#ff6e1c"),
    (83/120, "#ff6e1c"),

    (83/120, "#ffe132"),
    (93/120, "#ffe132"),

    (93/120, "#a0d2fe"),
    (99/120, "#a0d2fe"),

    (99/120, "#02bffd"),
    (105/120, "#02bffd"),

    (105/120, "#4169e1"),
    (110/120, "#4169e1"),

    (110/120, "#000096"),
    (115/120, "#000096"),

    (115/120, "#FFFFFF"),
    (120/120, "#FFFFFF")])

    vmax = 30 + 273.15
    vmin = -90 + 273.15

    return newcmp.reversed(), vmax, vmin

def nhc():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/136, "#000000"),   #26C
    (1/136, "#000018"),   #25C
    (16/136, "#0000FC"),  #10C
    (36/136, "#00FC00"),  #-10C
    (56/136, "#FC0000"),  #-30C
    (96/136, "#FCF8F8"),  #-70C
    (96/136, "#D8D8D8"),  #-70C
    (136/136, "#FCFCFC")])#To end

    vmax = 25 + 273.15
    vmin = -110 + 273.15

    return newcmp.reversed(), vmax, vmin

def rbtop4():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (50/150, "#00c3c3"),
    (70/150, "#04fcfc"),
    (80/150, "#000073"),
    (90/150, "#1cff24"),
    (100/150, "#ffff2d"),
    (110/150, "#ff1a18"),
    (120/150, "#000000"),
    (130/150, "#f1f1f1"),
    (130/150, "#f272c3"),
    (140/150, "#7f027f"),
    (140/150, "#ffff2d"),
    (145/150, "#000000"),
    (145/150, "#ff1a18"),
    (150/150, "#ffffff")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def rbtop3():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/140, "#000000"),
    (60/140, "#fffdfd"),
    (60/140, "#05fcfe"),
    (70/140, "#010071"),
    (80/140, "#00fe24"),
    (90/140, "#fbff2d"),
    (100/140, "#fd1917"),
    (110/140, "#000300"),
    (120/140, "#e1e4e5"),
    (120/140, "#eb6fc0"),
    (130/140, "#9b1f94"),
    (140/140, "#330f2f")])

    vmax = 40 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def rbtop2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/160, "#000000"),
    (82.5/160, "#ffffff"),
    (82.5/160, "#00ffff"),
    (95/160, "#001ee1"),
    (109/160, "#4bff00"),
    (115/160, "#e1ff00"),
    (125/160, "#c84d0e"),
    (134/160, "#521f05"),
    (136/160, "#32261E"),
    (140/160, "#908C89"),
    (145/160, "#ffffff"),
    (155/160, "#8D2392"),
    (155/160, "#ffffff"),
    (160/160, "#ffffff")])

    vmax = 57 + 273.15
    vmin = -103 + 273.15

    return newcmp.reversed(), vmax, vmin

def rbtop25():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/160, "#000000"),
    (3.75/160, "#262626"),
    (35/160, "#7f7f7f"),
    (60/160, "#c6c6c6"),
    (78.75/160, "#fbfbfb"),
    (85/160, "#2dbfde"),
    (91.25/160, "#2365b4"),
    (97.5/160, "#36877a"),
    (103.75/160, "#55e039"),
    (110/160, "#9cfc22"),
    (116.25/160, "#e6e91f"),
    (122.5/160, "#f9801f"),
    (128.75/160, "#b44a1f"),
    (135/160, "#4a2b1f"),
    (141.25/160, "#8a8483"),
    (147.5/160, "#eadbe9"),
    (153.75/160, "#ab55ab"),
    (160/160, "#ffffff")])

    vmax = 57 + 273.15
    vmin = -103 + 273.15

    return newcmp.reversed(), vmax, vmin

def rbtop():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/157, "#000000"),
    (30/157, "#787878"),
    (30.5/157, "#030303"),
    (45/157, "#5A5A5A"),
    (45.5/157, "#5B5B5B"),
    (50/157, "#646464"),
    (50.5/157, "#676767"),
    (72/157, "#F8F8F8"),
    (72.5/157, "#FAFAFA"),
    (77/157, "#BF00FF"),
    (77.5/157, "#BF00FF"),
    (85/157, "#0000FF"),
    (85.5/157, "#000CF2"),
    (102/157, "#00FF00"),
    (103/157, "#19FF00"),
    (112/157, "#FFFF00"),
    (113/157, "#FFE500"),
    (122/157, "#FF0000"),
    (123/157, "#E50000"),
    (132/157, "#000000"),
    (133/157, "#141414"),
    (157/157, "#FFFFFF")])

    vmax = 57 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def shrek():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"),

    (70/130, "#590a02"),

    (80/130, "#d99d4e"),
    (85/130, "#cfb629"),
    (90/130, "#dbdbdb"),
    (100/130, "#6dab43"),
    (110/130, "#328078"),
    (120/130, "#191d40"),
    (130/130, "#FFFFFF")])

    vmax = 30 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def cody():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#000000"),
    (10/130, "#091543"),
    (20/130, "#545b7a"),
    (30/130, "#9fa2b2"),
    (40/130, "#e6e6e7"),
    (50/130, "#29a6d5"),
    (60/130, "#50bb27"),
    (70/130, "#f5fb73"),
    (80/130, "#dc972a"),
    (90/130, "#c9122a"),
    (100/130, "#ffffff"),
    (110/130, "#8baff3"),
    (120/130, "#2675fe"),
    (130/130, "#025172")])

    vmax = 30 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def irg():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#b55555"),
    (10/150, "#b58555"),
    (30/150, "#090926"),
    (60/150, "#ffffff"),

    (80/150, "#4c8032"),
    (90/150, "#ffff29"),

    (105/150, "#ff2929"),
    (120/150, "#000000"),
    (130/150, "#e6dada"),
    (140/150, "#261940"),
    (141/150, "#990f97"),
    (150/150, "#e6dada")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def mw89():
  newcmp = LinearSegmentedColormap.from_list("", [
    (0/100, '#0507b4'),
    (10/100, "#0457cf"),
    (20/100, "#06a5eb"),
    (26/100, "#0ad5c2"),
    (26/100, "#0bb617"),
    (30/100, "#20bc01"),
    (40/100, "#4fd200"),
    (50/100, "#80ec02"),
    (52/100, "#8ef101"),
    (52/100, "#f1e400"),
    (60/100, "#f2de01"),
    (68/100, "#f8c30d"),
    (68/100, "#f90602"),
    (70/100, "#f40a03"),
    (80/100, "#da280a"),
    (90/100, "#be4411"),
    (100/100, "#a36319"),])

  vmax = 280
  vmin = 180

  return newcmp.reversed(), vmax, vmin

def mw37():
  newcmp = LinearSegmentedColormap.from_list("", [
    (0/115, '#7f0102'),
    (5/115, '#9a1a02'),
    (15/115, "#d05102"),
    (25/115, "#fd8608"),
    (35/115, "#f5c141"),
    (45/115, "#e0c66e"),
    (55/115, "#98f68c"),
    (65/115, "#9fe4c9"),
    (75/115, "#60e0fe"),
    (85/115, "#24a4fe"),
    (95/115, "#106dee"),
    (105/115, "#4c33b3"),
    (115/115, "#7f017e"),])

  vmax = 280
  vmin = 165

  return newcmp.reversed(), vmax, vmin

def ir89():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (20/150, "#000000"),
    (50/150, "#0000ff"),
    (70/150, "#00ffff"),
    (70/150, "#00c800"),
    (90/150, "#00fa00"),
    (90/150, "#fffa00"),
    (110/150, "#ffc800"),
    (120/150, "#ff0000"),
    (150/150, "#000000")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def fozbd():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#997373"),
    (30/150, "#e6bfbf"),
    (30/150, "#a6a6a6"),
    (41/150, "#e6e6e6"),
    (41/150, "#7e9898"),
    (80/150, "#cce6e6"),
    (80/150, "#0c4c8c"),
    (91/150, "#73b2f2"),
    (91/150, "#097222"),
    (103/150, "#25ff3f"),
    (103/150, "#a3a302"),
    (113/150, "#ffff19"),
    (113/150, "#7f3f0c"),
    (119/150, "#ff7f19"),
    (119/150, "#7f1906"),
    (125/150, "#ff330c"),
    (125/150, "#650f33"),
    (130/150, "#ff1965"),
    (130/150, "#6d356d"),
    (150/150, "#ff65ff")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def fozir():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (20/150, "#603030"),
    (30/150, "#804040"),
    (35/150, "#a08080"),
    (41/150, "#d0d0d0"),
    (50/150, "#80a0a0"),
    (60/150, "#407070"),
    (70/150, "#204040"),
    (80/150, "#206020"),
    (91/150, "#30a030"),
    (97/150, "#80c030"),
    (103/150, "#d0e030"),
    (108/150, "#e08020"),
    (113/150, "#f02010"),
    (116/150, "#7f1906"),
    (119/150, "#000000"),
    (125/150, "#a0a0a0"),
    (130/150, "#ffffff"),
    (135/150, "#306090"),
    (140/150, "#403070"),
    (145/150, "#a05090"),
    (150/150, "#f050a0")])
    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def scumsat():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#7f7f7f"),
    (41/150, "#e8e8e8"),
    (41/150, "#2d1b0f"),
    (80/150, "#bf4c19"),
    (80/150, "#947f0c"),
    (113/150, "#42a614"),
    (113/150, "#a37000"),
    (150/150, "#ffcc08")])

    vmax = 50
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def crys1():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (20/150, "#ff80ff"),
    (30/150, "#ffb3ff"),
    (35/150, "#ffe6ff"),
    (41/150, "#f9e6ff"),
    (50/150, "#d1b3ff"),
    (60/150, "#b380ff"),
    (70/150, "#944dff"),
    (80/150, "#ff4d4d"),
    (91/150, "#ff8080"),
    (97/150, "#ffcccc"),
    (103/150, "#ccf5ff"),
    (108/150, "#ccffff"),
    (113/150, "#ccd9ff"),
    (116/150, "#3366ff"),
    (119/150, "#400080"),
    (125/150, "#8c1aff"),
    (130/150, "#d9b3ff"),
    (135/150, "#000099"),
    (140/150, "#000066"),
    (145/150, "#1a1aff"),
    (150/150, "#8080ff")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def crys2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (20/150, "#330033"),
    (30/150, "#ff00ff"),
    (35/150, "#f9e6ff"),
    (41/150, "#f0e6ff"),
    (50/150, "#d1b3ff"),
    (60/150, "#b380ff"),
    (70/150, "#944dff"),
    (80/150, "#ff4d4d"),
    (91/150, "#ff8080"),
    (97/150, "#ffcccc"),
    (103/150, "#ccd9ff"),
    (108/150, "#ccffff"),
    (113/150, "#1a53ff"),
    (116/150, "#002db3"),
    (119/150, "#400080"),
    (125/150, "#8c1aff"),
    (130/150, "#d9b3ff"),
    (135/150, "#000099"),
    (140/150, "#000066"),
    (145/150, "#1a1aff"),
    (150/150, "#8080ff")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin

def crys3():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (20/150, "#000000"),
    (28/150, "#33ccff"),
    (35/150, "#f9e6ff"),
    (41/150, "#f0e6ff"),
    (50/150, "#d1b3ff"),
    (60/150, "#b380ff"),
    (70/150, "#944dff"),
    (80/150, "#ff4d4d"),
    (91/150, "#ff8080"),
    (97/150, "#ffcccc"),
    (103/150, "#668aff"),
    (108/150, "#3366ff"),
    (113/150, "#0039e6"),
    (116/150, "#002699"),
    (119/150, "#400080"),
    (125/150, "#8c1aff"),
    (130/150, "#b366ff"),
    (135/150, "#d9b3ff"),
    (140/150, "#FFFFFF"),
    (145/150, "#FFFFFF"),
    (150/150, "#FFFFFF")])

    vmax = 50 + 273.15
    vmin = -100 + 273.15

    return newcmp.reversed(), vmax, vmin


import subprocess, sys, datetime, requests
packages = ["cartopy", "numpy", "xarray", "datetime", "glob"]
for package in packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import LinearSegmentedColormap
from datetime import datetime, timedelta
import glob

# Custom colormap function with corrected vmin/vmax in Kelvin is present in the Appendix; feel free to add to the collection!
# Ensure you run the second code first

#-------------------USER INPUT HERE--------------------------------------------------------------
# Load netCDF data here =
nc_paths = sorted(glob.glob(r"C:\Users\USER\Downloads\Archived_NOAA_CLASS_Downloads\1986 WPAC\Forrest 1986\AVHRR\*.nc")) #No need to touch this anymore, it automatically loads the files once uploaded

# Generate colormap, vmin, and vmax depending on which one you want
cmap, vmax, vmin = ibtracs2() # Name of the colorscale should be same as name of the colormap function; refer to appendix

idl_flag = True #If the storm is expected to cross the IDL, set this to True
#-------------------USER INPUT ENDS---------------------------------------------------------------
for nc_path in nc_paths:
  ds = xr.open_dataset(nc_path)

  # Extracting variables from netCDF file
  ch4_temp = ds["CH4_TEMP"].values  # Brightness temperature data in Kelvin
  lat = ds["lat"].values
  lon = ds["lon"].values
  bt_lat = ds["CentLat"].values  # Best track latitude
  bt_lon = ds["CentLon"].values  # Best track longitude
  satellite_name = ds.attrs.get("Satellite_Name")  # Satellite name

  # Handling NaN values if present
  ch4_temp = np.ma.masked_invalid(ch4_temp)

  # Extracting and converting satellite time to datetime
  sat_time_days = ds["sat_time"].values  # Days since 1970-01-01
  base_time = datetime(1970, 1, 1)
  sat_time = base_time + timedelta(days=float(sat_time_days))

  # Setting up the plot with Cartopy
  fig = plt.figure(figsize=(10, 8))
  if idl_flag:
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    ax.set_extent([lon[-1], lon[0], lat[-1], lat[0]], crs=ccrs.PlateCarree())
  else:
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([lon[-1], lon[0], lat[-1], lat[0]], crs=ccrs.PlateCarree())

  # Addding map features
  ax.add_feature(cfeature.COASTLINE, linewidth=1, color='magenta')
  ax.add_feature(cfeature.BORDERS, linestyle=':', linewidth=0.5)
  gls = ax.gridlines(draw_labels=True, linewidth=0.5, linestyle='--', color='gray')
  gls.top_labels = False
  gls.right_labels = False

  # Plotting the CH4 brightness temperature data
  temp_plot = ax.pcolormesh(lon, lat, ch4_temp, cmap=cmap,
                            vmin=vmin, vmax=vmax, transform=ccrs.PlateCarree())

  # Adding the colorbar
  cbar = plt.colorbar(temp_plot, ax=ax, orientation="vertical", shrink=0.7, pad=0.05)
  cbar.set_label("Brightness Temperature (°C)")

  # Set custom ticks in Celsius with intervals of 10°C
  celsius_tick_values = np.arange(-100, 60, 10)  # Adjust the range if needed
  kelvin_tick_values = celsius_tick_values + 273.15  # Convert Celsius ticks to Kelvin

  # Update the colorbar ticks and labels
  cbar.set_ticks(kelvin_tick_values)  # Set the ticks in Kelvin
  cbar.set_ticklabels([f"{int(temp)}°C" for temp in celsius_tick_values])  # Label them in Celsius

  # Algorithm to find the max eye temperature
  max_temp_celsius_list = []  # To store max temperatures for both latitude/longitude pairs

  # Defining the range for latitude and longitude (1 degree north/south and east/west)
  lat_range = (bt_lat - 0.5, bt_lat + 0.5)  # (min_lat, max_lat)
  lon_range = (bt_lon - 0.5, bt_lon + 0.5)  # (min_lon, max_lon)

  # Creating a mask for the selected latitude and longitude range
  lat_mask = (lat >= lat_range[0]) & (lat <= lat_range[1])  # 1D mask for latitude
  lon_mask = (lon >= lon_range[0]) & (lon <= lon_range[1])  # 1D mask for longitude

  # Combining masks into a 2D mask
  combined_mask = lat_mask[:, None] & lon_mask  # Broadcasting lon_mask to 2D

  # Getting the brightness temperature values that correspond to the valid indices
  valid_temp = ch4_temp[combined_mask]  # Applying the 2D mask to ch4_temp

  # if valid temperatures
  if valid_temp.size > 0:  # Ensure valid_temp is not empty
      max_temp_kelvin = np.max(valid_temp)
      max_temp_celsius = max_temp_kelvin - 273.15  # Convert Kelvin to Celsius

      # Append to the list of max temperatures
      max_temp_celsius_list.append(max_temp_celsius)

  if max_temp_celsius_list:
      overall_max_temp_celsius = max(max_temp_celsius_list)
  else:
      overall_max_temp_celsius = float('nan')
  #plt.scatter(bt_lon, bt_lat, color='#ffff00', marker='^', zorder=93)
  # Title
  plt.title(
      f"AVHRR Brightness Temperature IR"+
      f" At {sat_time.strftime('%Y-%m-%d %H:%M:%S UTC')}\n"+
      f"Satellite: {satellite_name}\n"
      f"Max Eye Temperature recorded: {overall_max_temp_celsius:.2f} °C" if not np.isnan(overall_max_temp_celsius) else "Max Temp: Not Available",
      fontsize=16
  )

  # Display
  plt.savefig(nc_path[:-3] + '.png', format='png', bbox_inches='tight')
plt.close()

