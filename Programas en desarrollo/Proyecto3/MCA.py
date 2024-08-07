def midPointCircleDraw(x0, y0, r):
    x = r
    y = 0

    # Storing the initial point the
    # axes after translation
    tp = [(x + x0, y + y0)]

    if (r > 0) :
        tp.append((x + x0, -y + y0))
        tp.append((y + x0, x + y0))
        tp.append((-y + x0, x + y0))
     
    # Initialising the value of P
    P = 1 - r
 
    while x > y:
        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:        
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if (x < y):
            break

        # Storing the generated point its reflection
        # in the other octants after translation
        tp.append((x + x0, y + y0))
        tp.append((-x + x0, y + y0))
        tp.append((x + x0, -y + y0))
        tp.append((-x + x0, -y + y0))
         
        # If the generated point on the line x = y then
        # the perimeter points have already been printed
        if x != y:
            tp.append((y + x0, x + y0))
            tp.append((-y + x0, x + y0))
            tp.append((y + x0, -x + y0))
            tp.append((-y + x0, -x + y0))
                             
# Driver Code
if __name__ == '__main__':
     
    # To draw a circle of radius 3
    # centered at (0, 0)
    midPointCircleDraw(0, 0, 3)