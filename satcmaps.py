from netCDF4 import Dataset      # Read / Write NetCDF4 files
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace  # Plotting library
import cartopy, cartopy.crs as ccrs  # Plot maps
import numpy.ma as ma
import numpy as np
import pandas as pd
import xarray as xr
import datetime
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
#import goesRequest2 as goes2

# IR Color Tables
def swir():
    num1 = 15
    num2 = 55
    num3 = 40

    top = cm.get_cmap('Blues', num1)
    mid = cm.get_cmap('plasma', num2)
    bot = cm.get_cmap('bone_r', num3)

    newcolors = np.vstack((top(np.linspace(0, 1, num1)),
                           mid(np.linspace(0, 1, num2)),
                           bot(np.linspace(0, 1, num3))))
    newcmp = ListedColormap(newcolors, name='temp')
    return newcmp

def oldspooky():
    num1 = 20
    num2 = 85
    num3 = 30

    top = cm.get_cmap('Greys', num1)
    mid = cm.get_cmap('CMRmap', num2)
    bot = cm.get_cmap('Greys', num3)

    newcolors = np.vstack((top(np.linspace(0, 1, num1)),
                           mid(np.linspace(0, 1, num2)),
                           bot(np.linspace(0, 1, num3))))
    newcmp = ListedColormap(newcolors, name='temp')
    return newcmp

def santa():
    num1 = 20
    num2 = 30
    num3 = 40
    num4 = 50

    top = LinearSegmentedColormap.from_list("", [(0.0, "#cfcfcf"), (1, "#d9c548")])
    mid = cm.get_cmap('PiYG', num2)
    mid2 = cm.get_cmap('Reds_r', num3)
    bot = cm.get_cmap('Greys', num4)

    newcolors = np.vstack((top(np.linspace(0, 1, num1)),
                           mid(np.linspace(0.5, 1, num2)),
                           mid2(np.linspace(0.2, 0.8, num3)),
                           bot(np.linspace(0.1, 0.9, num4))))
    newcmp = ListedColormap(newcolors, name='temp')

    vmax = 40
    vmin = -100

    return newcmp, vmax, vmin

def gay():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, '#000000'),
    (20/130, '#cccccc'),
    (20/130, '#1c2a7a'),
    (60/130, "#56db58"), 
    (75/130, "#fcfa68"),
    (90/130, "#ed422f"),
    (95/130, "#c71e75"),
    (100/130, "#170824"),
    (110/130, "#a145ed"),
    (120/130, "#dce6f7"),
    (130/130, "#000000")])

    vmax = 30
    vmin = -100

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

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def ca2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, '#000000'),
    (19/130, "#626466"),
    (21/130, "#1c2a7a"),
    (30/130, "#0b3a54"),
    (40/130, "#15476b"),
    (50/130, "#098292"),
    (60/130, "#18bc71"),
    (70/130, "#61ec22"),
    (80/130, "#e8ed29"),
    (85/130, "#f88d1e"),
    (95/130, "#ce221c"),
    (100/130, "#ac61ce"),
    (105/130, "#563ab4"),
    (117.5/130, "#cbcbfe"),
    (122.5/130, "#FFFFFF"),
    (122.5/130, "#ffd919"),
    (130/130, "#292825")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def gaytestir():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, '#750000'),
    (40/150, "#decbbd"),
    (60/150, "#2c124a"),
    (70/150, "#2b27a3"),
    (80/150, "#65a87f"),
    (90/150, "#e0e64e"),
    (100/150, "#c26915"),
    (110/150, "#752a29"),
    (120/150, "#a60503"),
    (130/150, "#d599f7"),
    (150/150, "#000000")])

    return newcmp.reversed()

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

    vmax = 55
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def rammb():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#b55555"),
    (10/150, "#b58555"),
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

    vmax = 50
    vmin = -100

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

    vmax = 50
    vmin = -81

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

    vmax = 36
    vmin = -92

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

    vmax = 57
    vmin = -110

    return newcmp.reversed(), vmax, vmin

def bd():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#a8d1ff"),
    (11/120, "#011a36"), 
    (12/120, "#000000"),
    (12/120, "#1d1d1d"),
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

    vmax = 30
    vmin = -90

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

    vmax = 30
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def lavn():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#000000"),
    (80/150, "#FFFFFF"),
    (80/150, "#0096FF"),
    (100/150, "#006e96"),
    (100/150, "#a0a000"),
    (110/150, "#fafa00"),
    (110/150, "#fafa00"),
    (120/150, "#c87800"),
    (120/150, "#fa0000"),
    (130/150, "#660000"),
    (130/150, "#585858"),
    (150/150, "#FFFFFF")])

    return newcmp.reversed()

def candy():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#000000"), 
    (10/130, "#2a2a2a"),
    (20/130, "#535353"), 
    (30/130, "#7c7c7c"),
    (40/130, "#a3a3a3"),
    (50/130, "#cccccc"),
    (60/130, "#f3f3f3"),
    (70/130, "#96b9e0"),
    (80/130, "#3b7fcd"),
    (90/130, "#868bbc"),
    (95/130, "#ffb8b9"),
    (100/130, "#ff999b"),
    (110/130, "#e43a52"),
    (120/130, "#822049"),
    (130/130, "#250740")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def candy3():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"), 

    (70/130, "#254f80"),
    (75/130, "#298c6d"),
    (80/130, "#6fb334"),
    (85/130, '#cccc3b'),
    (90/130, "#e68743"),
    (100/130, "#ffb8b9"),
    (110/130, "#e43a52"),
    (120/130, "#822049"),
    (130/130, "#250740")])

    return newcmp.reversed() 

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

    vmax = 25
    vmin = -110

    return newcmp.reversed(), vmax, vmin

def oldirb():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#121212"),
    (20/130, "#787878"),
    (25/130, "#d7d9db"),
    (30/130, "#fcfcfc"),
    (45/130, "#2b39a1"),
    (50/130, "#fff957"),
    (55/130, "#e3c024"),
    (85/130, "#a6233f"),
    (85/130, "#a62353"),
    (100/130, "#b075ba"),
    (110/130, "#533c73"),
    (120/130, "#382c4f"),
    (125/130, "#19171c"),
    (130/130, "#000000")])

    return newcmp.reversed()

def irb():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#121212"),
    (20/130, "#787878"),
    (25/130, "#d7d9db"),
    (30/130, "#fcfcfc"),

    (40/130, "#2b39a1"),
    (50/130, "#3dad8f"),
    (65/130, "#fff957"),
    (70/130, "#e3c024"),
    (85/130, "#a6233f"),
    (90/130, "#4d0d07"),
    (100/130, "#9649c9"),
    (110/130, "#e0e0ff"),
    (130/130, "#000000")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def irc():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#b58d65"),
    (15/150, "#9c4c4c"),
    (25/150, "#000000"),
    (30/150, "#333333"),
    (70/150, "#ffffff"),
    (75/150, "#658ba3"),
    (107.5/150, "#112c3d"),
    (112.5/150, "#b53564"),
    (129/150, "#fae1ea"),
    (131/150, "#FFFFFF"),
    (140/150, "#787878"),
    (144/150, "#000000"),
    (145/150, "#2b2b2b"),
    (150/150, "#6f4c9c")])

    vmax = 50
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def oldirc():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (15/130, "#2b2b2b"),
    (50/130, "#ffffff"),
    (55/130, "#658ba3"),
    (75/130, "#112c3d"),
    (85/130, "#b53564"),
    (100/130, "#fae1ea"),
    (110/130, "#787878"),
    (130/130, "#0f0303")])

    return newcmp.reversed()

def blcold():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#000000"),
    (60/120, "#FFFFFF"),
    (60/120, "#666ad6"),
    (70/120, "#949cfd"),
    (70/120, "#0eb7e7"),
    (85/120, "#081a7a"),
    (95/120, "#f6f72b"),
    (100/120, "#fe3518"),
    ((106+(2/3))/120, "#110f0f"),
    ((113+(1/3))/120, "#f5f5f5"),
    (120/120, "#a60aa6")])

    vmax = 40
    vmin = -80

    return newcmp.reversed(), vmax, vmin

def blhot():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/140, "#000000"),
    (80/140, "#FFFFFF"),
    (80/140, "#0eb7e7"),
    (95/140, "#081a7a"),
    (105/140, "#f6f72b"),
    (110/140, "#fe3518"),
    (117.5/140, "#110f0f"),
    (125/140, "#f5f5f5"),
    (135/140, "#a60aa6"),
    (135/140, "#FFFFFF"),
    (140/140, "#FFFFFF")])

    vmax = 40
    vmin = -100

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

    vmax = 50
    vmin = -100

    return newcmp.reversed()

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

    vmax = 40
    vmin = -100

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

    vmax = 57
    vmin = -103

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

    vmax = 57
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def copperOld():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#07010a"), 
    (10/90, "#4a474a"),
    (30/90, "#ebd7f7"),
    (45/90, "#e88c6d"),
    (60/90, "#703030"),
    (75/90, "#79a2d4"),
    (90/90, "#25184a")])

    vmax = 30
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def coppert():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#549977"), 
    (15/90, "#07010a"),
    (30/90, "#f7f7f7"),
    (40/90, "#e88c6d"),
    (60/90, "#703030"),
    (75/90, "#79a2d4"),
    (90/90, "#25184a")])

    vmax = 30
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def copper():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#bfbfbf"),
    (15/90, "#4d1f1f"), 
    (22.5/90, "#e88c6d"),
    (30/90, "#f7f7f7"),
    (40/90, "#98bf8e"),
    (60/90, "#104020"),
    (75/90, "#79a2d4"),
    (90/90, "#25184a")])

    vmax = 30
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def ire():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#171717"),
    (50/130, "#ffffff"),
    (69/130, "#3f426b"),
    (71/130, "#711d82"),
    (85/130, "#eb7cbe"),
    (95/130, "#a12a2a"),
    (109/130, "#240404"),
    (111/130, "#16192e"),
    (125/130, "#e1e2e8"),
    (130/130, "#ffffff")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def irf():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"), #white
    (60/130, "#181557"), #blue
    (65/130, "#35db50"), #green
    (70/130, '#ffff29'), #yellow
    (80/130, "#db9335"), #orange
    (85/130, "#ff2929"), #red
    (95/130, "#541c1c"), #brown
    (100/130, "#000000"), #black
    (110/130, "#545454"), #grey
    (120/130, "#ffffff"), #white
    (130/130, "#261940")]) #purple

    vmax = 30
    vmin = -100

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

    vmax = 50
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def wu():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (40/130, "#7a7a7a"),
    (65/130, "#e2dfde"),
    (70/130, "#9febeb"),
    (75/130, "#7c9f9f"),
    (80/130, "#014bb4"),
    (85/130, "#189010"),
    (90/130, "#7abc1b"),
    (95/130, "#d6e026"),
    (100/130, "#d2951b"),
    (105/130, "#ad201d"),
    (110/130, "#7d0553"),
    (115/130, "#9139a4"),
    (120/130, "#b072be"),
    (125/130, "#d1add9"),
    (130/130, "#ece6ed")])

    vmax = 35
    vmin = -95
    
    return newcmp.reversed(), vmax, vmin

def spooky():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"),

    (50/130, "#f5e2c1"),
    (70/130, "#eb8415"),
    (95/130, "#590401"),

    (100/130, "#121010"),
    (110/130, "#fcf5f5"),
    (125/130, "#2a084d"),
    (125/130, "#ffffff"),
    (130/130, "#ffffff")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def testir():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/150, "#545454"),
    (40/130, "#ffffff"),

    (50/130, "#a8fdfd"),
    (70/130, "#2a084d"),

    (80/130, "#545454"),
    (90/130, "#ff9d1c"),
    
    (100/130, "#cc2e29"),
    (110/130, "#fad7e4"),
    (120/130, "#6e1428"),
    (125/130, "#6e3514"),
    (130/130, "#121011")])
    return newcmp.reversed()

def irh():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"), 
    (60/130, "#216beb"),
    (70/130, "#60c259"),
    (80/130, "#fff88f"),
    (90/130, "#c74c0e"),
    (100/130, "#630505"),
    (110/130, "#edbbbb"),
    (120/130, "#9444c7"),
    (130/130, "#FFFFFF")]) 

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def iri():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"), 
    (45/130, "#2c5f78"),
    (60/130, "#3e0f4d"),
    (60/130, "#1c4d2e"),
    (80/130, "#cbed5c"),
    (80/130, "#edab9a"),
    (85/130, "#eb4921"),
    (90/130, "#80082c"),
    (100/130, "#240a12"),
    (100/130, "#242424"),
    (130/130, "#FFFFFF")]) 

    vmax = 30
    vmin = -100
    
    return newcmp.reversed(), vmax, vmin

def irk():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#4f4f4f"), 
    (40/130, "#ffffff"),
    (60/130, "#397ae3"),
    (75/130, "#193263"),
    (90/130, "#d9c916"),
    (95/130, "#db770b"),
    (100/130, "#8f1111"),
    (110/130, "#db56b5"),
    (120/130, "#ffffff"),
    (127.5/130, "#8556db"),
    (127.5/130, "#e0bb00"),
    (130/130, "#e0bb00")])

    vmax = 30
    vmin = -100
    
    return newcmp.reversed(), vmax, vmin

def irj():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#545454"),
    (40/130, "#ffffff"), 
    (60/130, "#7ed1e6"),
    (75/130, "#564ba6"),
    (88.5/130, "#090b3b"),
    (91.5/130, "#3b090a"),
    (100/130, "#801315"),
    (110/130, "#c76f9b"),
    (120/130, "#f7e4e4"),
    (120/130, "#e8e8e8"),
    (125/130, "#b694ff"),
    (130/130, "#2d1c52")]) 

    vmax = 30
    vmin = -100
    
    return newcmp.reversed(), vmax, vmin

def ryglicki():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/110, "#fafafa"),
    (50/110, "#4f4c53"),
    (50/110, "#a2f5a4"),
    (60/110, "#08520a"),
    (60/110, "#1e1971"),
    (70/110, "#e9fafb"),
    (70/110, "#7a0906"),
    (80/110, "#f3f6dd"),
    (90/110, "#cf615d"),
    (90/110, "#d5bfd5"),
    (100/110, "#9235cb"),
    (100/110, "#04827d"),
    (110/110, "#60f1f0")]) 

    vmax = 20
    vmin = -90

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

    vmax = 30
    vmin = -100
    
    return newcmp.reversed(), vmax, vmin

def cody():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#000000"), 
    (10/130, "#2d2e32"),
    (20/130, "#5d5d5d"), 
    (30/130, "#a9abb0"),
    (40/130, "#f2f2f2"),
    (60/130, "#3bc1cc"),
    (70/130, "#e6db02"),
    (80/130, "#d47624"),
    (90/130, "#d14747"),
    (100/130, "#f2f2f2"),
    (110/130, "#82b0ff"),
    (120/130, "#2072ff"),
    (130/130, "#004f6a")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin
    
def ocody():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#000000"), 
    (10/130, "#2d2e32"),
    (20/130, "#5d5d5d"), 
    (30/130, "#a9abb0"),
    (40/130, "#f2f2f2"),
    (50/130, "#27c1cc"),
    (60/130, "#3bc1cc"),
    (70/130, "#e6db02"),
    (80/130, "#d47624"),
    (90/130, "#d14747"),
    (100/130, "#f2f2f2"),
    (110/130, "#82b0ff"),
    (120/130, "#2072ff"),
    (130/130, "#004f6a")])

    return newcmp.reversed()
    
def lava():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, '#2e271d'),
    (40/120, '#c4b7a3'),
    (45/120, '#f09c43'),
    (75/120, '#8a2727'),
    (90/120, '#f26555'),
    (100/120, '#f09246'),
    (110/120, '#eddb82'),
    (120/120, '#cfceca')])

    vmax = 30
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def oldira():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/120, "#2e3036"), 
    (50/120, '#c3b3f5'), 
    (50/120, '#d6d24f'),
    (62.5/120, '#f07951'),
    (80/120, '#a80295'), 
    (95/120, '#e3ddd8'), 
    (110/120, "#7b80c9"), 
    (120/120, "#3e47c7")])
    return newcmp.reversed()

def ira():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#000000"),
    (20/130, "#4f4f4f"), 
    (40/130, "#ffffff"),
    (60/130, "#397ae3"),
    (75/130, "#0a6930"),
    (85/130, "#96ad47"),
    (90/130, "#db770b"),
    (100/130, "#8f3d11"),
    (105/130, "#8f1111"),
    (115/130, "#db56b5"),
    (120/130, "#ffffff"),
    (130/130, "#8556db")])

    vmax = 30
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def test():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/150, "#7d3025"),
    (25/150, "#1a1a1a"),
    (75/150, "#ffffff"),
    (90/150, "#804080"),
    (100/150, "#61203f"),
    (110/150, "#bf3030"),
    (120/150, "#261919"),
    (135/150, "#e6e6f2"),
    (150/150, "#308fbf")])

    vmax = 50
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def irl():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/130, "#ad4747"),
    (15/130, "#604642"),
    (25/130, "#162c36"),
    (70/130, "#a3becc"),
    (75/130, "#FFFFFF"),
    (80/130, "#dae6cf"),
    (100/130, "#085024"),
    (110/130, "#bf9b30"),
    (115/130, "#cc1414"),
    (120/130, "#e65c5c"),
    (130/130, "#FFFFFF")])

    vmax = 40
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def irm():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/140, "#ad4747"),
    (15/140, "#604642"),
    (25/140, "#162c36"),
    (60/140, "#a3becc"),
    (65/140, "#FFFFFF"),
    (70/140, "#dae6cf"),
    (95/140, "#085024"),
    (105/140, "#bf9b30"),
    (110/140, "#cc1414"),
    (115/140, "#e65c5c"),
    (120/140, "#FFFFFF"),
    (130/140, "#323ca8"),
    (140/140, "#1a1a1a")])

    vmax = 40
    vmin = -100

    return newcmp.reversed(), vmax, vmin

def irn():
    print('next')

def nws():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/160, "#74d7ff"),
    (10/160, "#aefeff"),
    (20/160, "#32cec1"),
    (30/160, "#009996"),
    (40/160, "#115757"),
    (50/160, "#076d2c"),
    (60/160, "#30a355"),
    (70/160, "#73c475"),
    (80/160, "#a1d99a"),
    (90/160, "#d2ffbe"),
    (100/160, "#feffb3"),
    (105/160, "#8b2800"),
    (110/160, "#510100"),
    (115/160, "#cd313e"),
    (120/160, "#ff6669"),
    (125/160, "#eea8a7"),
    (130/160, "#f892d3"),
    (135/160, "#cf5caa"),
    (140/160, "#8c3b8a"),
    (145/160, "#5e2665"),
    (150/160, "#2d0041"),
    (155/160, "#01004c"),
    (160/160, "#74d7ff")])

    vmax = 50
    vmin = -110

    return newcmp.reversed(), vmax, vmin

def ird():
    color1 = 'twilight'
    num1 = 110
    color2 = 'Greys' 
    num2 = 40

    top = cm.get_cmap(color1, num1)
    bottom = cm.get_cmap(color2, num2)
    newcolors = np.vstack((top(np.linspace(0, 1, num1)),
                       bottom(np.linspace(0, 1, num2))))
    newcmp = ListedColormap(newcolors, name='temp')

    vmax = 40
    vmin = -110

    return newcmp.reversed(), vmax, vmin

def ir():
    num1 = 20
    num2 = 60
    num3 = 40
    num4 = 20
    num5 = 10
    top3 = cm.get_cmap('OrRd', num5)
    top2 = cm.get_cmap('BuPu_r', num4)
    top = cm.get_cmap('PuRd', num1)
    mid = cm.get_cmap('Spectral', num2)
    bot = cm.get_cmap('bone_r', num3)

    newcolors = np.vstack((top3(np.linspace(0, 1, num5)), top2(np.linspace(0, 1, num4)), top(np.linspace(0, 1, num1)), mid(np.linspace(0, 1, num2)), bot(np.linspace(0, 1, num3))))
    newcmp = ListedColormap(newcolors, name='temp')

    vmax = 40
    vmin = -110

    return newcmp, vmax, vmin

def whaticouldvedone():
    num1 = 25
    num2 = 55
    num3 = 40
    num4 = 10
    num5 = 10
    top3 = cm.get_cmap('OrRd', num5)
    top2 = cm.get_cmap('BuPu_r', num4)
    top = cm.get_cmap('PuRd', num1)
    mid = cm.get_cmap('Spectral', num2)
    bot = cm.get_cmap('bone_r', num3)

    newcolors = np.vstack((top3(np.linspace(0, 1, num5)), top2(np.linspace(0, 1, num4)), top(np.linspace(0, 1, num1)), mid(np.linspace(0, 1, num2)), bot(np.linspace(0, 1, num3))))
    newcmp = ListedColormap(newcolors, name='temp')
    return newcmp

# WV Color Tables

def msfc():
    newcmp = LinearSegmentedColormap.from_list("", [
        (0/90, "#000000"),
        (5/90, "#6e0505"),
        (15/90, "#c66523"),
        (17.5/90, "#dc9e3d"),
        (20/90, "#997541"),
        (25/90, "#5b4e3e"),
        (27.5/90, "#3f3f3e"),
        (30/90, "#565656"),
        (40/90, "#c7c9ca"),
        (40/90, "#c0cacc"),
        (50/90, "#266775"),
        (55/90, "#6d993d"),
        (60/90, "#d4d925"),
        (62.5/90, "#d9861a"),
        (65/90, "#d51312"),
        (70/90, "#9a0b09"),
        (72.5/90, "#402728"),
        (75/90, "#343132"),
        (90/90, "#dfdfdf")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def wv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#696563"),
    (10/90, "#1f1e1c"), 
    (20/90, "#a85432"),
    (30/90, "#e3e1de"),
    (45/90, "#465185"),
    (60/90, "#89d9a7"),
    (80/90, "#30453d"),
    (90/90, '#b3afaf')])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def wv2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#bf4351"),
    (5/90, "#a85432"),
    (15/90, "#1f1e1c"), 
    (25/90, "#696563"),
    (35/90, "#e3e1de"),
    (45/90, "#465185"),
    (60/90, "#89d9a7"),
    (80/90, "#30453d"),
    (90/90, '#b3afaf')])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def ssdwv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#000000"),
    (7.5/90, "#000000"),
    (8/90, "#FFA05A"),
    (25/90, "#000000"),
    (25.5/90, "#000000"),
    (37/90, "#FFFFFF"),
    (38/90, "#FFFFFF"),
    (52/90, "#005082"),
    (53/90, "#005082"),
    (60/90, "#009696"),
    (61/90, "#A09600"),
    (68/90, "#FA3200"),
    (69/90, "#9600DC"),
    (76/90, "#FA00DC"),
    (77/90, "#0000E2"),
    (84/90, "#000086"),
    (85/90, "#FFFFFF"),
    (90/90, '#FFFFFF')])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def newwv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#ff8f40"), 
    (10/90, "#d9bf00"),
    (25/90, "#171717"),
    (40/90, "#ffffff"),
    (57.5/90, "#3f426b"),
    (60/90, "#711d82"),
    (70/90, "#eb7cbe"),
    (80/90, "#a12a2a"),
    (90/90, "#240404")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def codywv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#ffdf00"), 
    (10/80, "#807000"),
    (20/80, "#000000"), 
    (30/80, "#777776"),
    (40/80, "#ffffff"),
    (50/80, "#5d73c5"),
    (60/80, "#222777"),
    (70/80, "#5f2f90"),
    (75/80, "#6d3d96"),
    (80/80, "#c32787")])

    vmax = 0
    vmin = -80

    return newcmp.reversed(), vmax, vmin

def mikewv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#1b1a17"), 
    (10/90, "#fdbf20"),
    (17.5/90, "#f36631"),
    (20/90, "#d2352c"),
    (32.5/90, "#f2f1f6"),
    (40/90, "#44b8cf"),
    (50/90, "#307584"),
    (60/90, "#223b48"),
    (70/90, "#274397"),
    (90/90, "#8927f4")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def wv3():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#804080"),
    (5/90, "#1a000d"),
    (10/90, "#661a1a"),
    (15/90, "#8f5d3c"), 
    (20/90, "#000000"),
    (40/90, "#FFFFFF"),
    (50/90, "#a9c4de"),
    (55/90, "#8e9ac8"),
    (65/90, "#88439e"),
    (70/90, "#4d014b"),
    (70/90, "#67041f"),
    (80/90, "#d1145b"),
    (90/90, "#f7f4f9")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def testwv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#992660"),
    (10/90, "#802020"),
    (15/90, "#000000"),
    (22.5/90, "#413D3E"),
    (30/90, "#FFFFFF"),
    (55/90, "#3d3d99"),
    (60/90, "#d96cd9"),
    (70/90, "#663d52"),
    (72.5/90, "#bf3030"),
    (75/90, "#bf4830"),
    (90/90, "#FFFFFF")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def camwv():
    # Define the new colormap with specified colors at specified locations
    newcmp = LinearSegmentedColormap.from_list("", [
        (0.0, "#00000a"),    # Start of the gradient
        # Assuming your color scale changes gradually, you'd place key colors at their relative positions
        (1/8, "#010055"),    # An example color partway through
        (1/4, "#0a0070"),    # Another example color partway through
        (1/2, "#4a0096"),    # Midpoint color
        (3/4, "#bf0692"),    # Further along the gradient
        (7/8, "#febd00"),    # Nearly at the end
        (1.0, "#fffff6")     # End of the gradient
    ])

    vmax = 0
    vmin = -90

    # Return the reversed colormap, vmax, and vmin
    return newcmp, vmax, vmin 

def hand():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#5d5e7f"),
    (17.5/90, "#07080c"),
    (25/90, "#061d47"),
    (40/90, "#6b81b7"),
    (50/90, "#ffe374"),
    (65/90, "#7f3c1e"),
    (70/90, "#27140d"),
    (75/90, "#8c1612"),
    (82.5/90, "#fa9e29"),
    (90/90, "#f0fdf4")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def codywv2():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0.0, "#ffdf00"), 
    (10/85, "#807000"),
    (20/85, "#000000"), 
    (30/85, "#777776"),
    (40/85, "#ffffff"),
    (45/85, "#f3f3f3"),
    (50/85, "#96b9e0"),
    (55/85, "#254f80"),
    (60/85, "#868bbc"),
    (65/85, "#ffb8b9"),
    (70/85, "#ff999b"),
    (75/85, "#e43a52"),
    (80/85, "#822049"),
    (85/85, "#250740")])

    vmax = 0
    vmin = -85

    return newcmp.reversed(), vmax, vmin

def darkwv():
    newcmp = LinearSegmentedColormap.from_list("", [
    (0/90, "#FFFFFF"),
    (10/90, "#000000"),
    (10/90, "#FFFFFF"), 
    (30/90, "#000000"),
    (45/90, "#a66441"),
    (60/90, "#61a641"),
    (70/90, "#90e8cb"),
    (90/90, "#000000")])

    vmax = 0
    vmin = -90

    return newcmp.reversed(), vmax, vmin

def oldwv():
    num1 = 20
    num2 = 40
    num3 = 30
    top = cm.get_cmap('PuRd', num1)
    mid = cm.get_cmap('BuPu_r', num2)
    bot = cm.get_cmap('Greys', num3)

    newcolors = np.vstack((top(np.linspace(0, 1, num1)), mid(np.linspace(0, 1, num2)), bot(np.linspace(0, 1, num3))))
    newcmp = ListedColormap(newcolors, name='temp')
    
    vmax = 0
    vmin = -90

    return newcmp, vmax, vmin

wvtables = {
    'msfc'  : msfc(),
    'wv'    : wv(),
    'wv2'   : wv2(),
    'wv3'   : wv3(),
    'ssd'   : ssdwv(),
    'newwv' : newwv(),
    'camwv' : camwv(),
    'codywv': codywv(),
    'codywv2': codywv2(),
    'mikewv': mikewv(),
    'testwv': testwv(),
    'hand'  : hand(),
    'dark'  : darkwv(),
    'oldwv' : oldwv()}

irtables = {
    'avn'     :avn(),
    'funktop' :funktop(),
    'jsl'     :jsl(),
    'rainbow' :rainbow(),
    'rbtop'   :rbtop(),
    'rbtop2'  :rbtop2(),
    'rbtop3'  :rbtop3(),
    'rbtop4'  :rbtop4(),
    'bd'      :bd(),
    'ibtracs' :ibtracs(),
    'rammb'   :rammb(),
    'nhc'     :nhc(),
    'wu'      :wu(),
    'shrek'   :shrek(),
    'ryglicki':ryglicki(),
    'candy'   :candy(),
    'bl'      :blhot(),
    'blcold'  :blcold(),
    'spooky'  :spooky(),
    'lava'    :lava(),
    'santa'   :santa(),
    'gay'     :gay(),
    'copper'  :copper(),
    'cody'    :cody(),
    'ir'      :ir(),
    'ira'     :ira(),
    'irb'     :irb(),
    'irc'     :irc(),
    'ird'     :ird(),
    'ire'     :ire(),
    'irf'     :irf(),
    'irg'     :irg(),
    'irh'     :irh(),
    'iri'     :ca2(),
    'irj'     :irj(),
    'irk'     :irk(),
    'irl'     :irl(),
    'irm'     :irm(),
    'irn'     :irn(),
    'irca'    :ca(),
    'test'    :test(),
    'nws'     :nws()}