# Helicopter 

  # # # # # # # # # # 
  #                 # 
  #                 # 
  #       H         # 
  #                 # 
  #                 # 
  #                 # 
  #                 # 
  #                 # 
  # # # # # # # # # # 

# HW1
# # # # # # # # # # 
#                 # 
#     x x x       # 
#   x x H x x     # 
#     x x x       # 
#                 # 
#                 # 
#                 # 
#                 # 
# # # # # # # # # # 

# HW2

# # # # # # # # # # 
#     ~ ~ ~       # 
#   ~ ~ ~ ~ ~     # 
#   ~ ~ H ~ ~     # 
#   ~ ~ ~ ~ ~     # 
#     ~ ~ ~       # 
#                 # 
#                 # 
#                 # 
# # # # # # # # # # 


SCALE  = 10
hX = 5
hY = 4

map = "" 
for y in range(SCALE):
    map += str(y) + ". "
    for x in range(SCALE):

        if x == 0 or x == SCALE - 1 or y == 0 or y == SCALE - 1:
            map += "# "
        elif x == hX and y == hY:
            map += "H "
        elif x in [hX, hX+1, hX-1]  and y in [hY, hY+1, hY-1]:
            map += "x "   
        else:
            map += "  "

    map += "\n"                

print(map)
