import random_color as r
import spirograph as s
import hirst_spot_painting as h

mode = input("'random' or 'spirograph' or 'hirst': ")
if mode == 'random':
    r.rand_color()
elif mode == 'spirograph':
    s.spirograph()
elif mode == 'hirst':
    h.painting()