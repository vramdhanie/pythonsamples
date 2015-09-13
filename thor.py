import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

 # light_x: the X position of the light of power
 # light_y: the Y position of the light of power
 # initial_tx: Thor's starting X position
 # initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

thorX = initial_tx
thorY = initial_ty

# game loop
count = 100
while count > 0:
    count -= 1
    # remaining_turns = int(raw_input())
    
    x_dir = ""
    y_dir = ""

    if thorX < light_x:
        x_dir = "E"
        thorX += 1
    else:
        if thorX > light_x:
            x_dir = "W"
            thorX = thorX - 1

    if thorY < light_y:
        y_dir = "S"
        thorY += 1
    else:
        if thorY > light_y:
            y_dir = "N"
            thorY = thorY - 1

    print("Thor:(%d,%d); Light:(%d, %d)\n" % (thorX, thorY, light_x, light_y))
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print ("%s%s"%(y_dir, x_dir))
