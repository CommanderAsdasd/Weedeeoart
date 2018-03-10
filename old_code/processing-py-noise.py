def setup():
    xnoise = 0.0
    ynoise = 0.0
    float inc = 0.04
    size(500, 500)
    for i in range(0, height):
        for j in range(0, height):
            gray = noise(xnoise, ynoise) * 255
            stroke(gray)
            point(x, y)
            xnoise = xnoise + inc
        xnoise = 0
        ynoise = ynoise + inc
      