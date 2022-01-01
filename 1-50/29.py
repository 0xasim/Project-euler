lowlim, uplim= 2, 100
print(len({(a**b) for a in range(lowlim,uplim + 1) for b in range(lowlim, uplim + 1)}))
