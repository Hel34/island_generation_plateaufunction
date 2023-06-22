def plateau(x, y, tau, height, a):
    """
    see the readme file for a detailed explanation
    x,y: position
    tau: dropspeed
    a: falloff point
    """
    r = max(abs(x), abs(y))
    return height*(1-pow(2.71, -(r+a)/tau))*(1-pow(2.71, (r-a)/tau))
