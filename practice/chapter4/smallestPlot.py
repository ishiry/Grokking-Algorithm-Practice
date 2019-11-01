#find smallest box you can do in parcel of land
#accurate up to 4 d.p

def smallest_plot(length, width):
    if length == width:
        print ('smallest square is {} x {}'.format(length , width))
    elif length != width:
        small_line = round(min(length, width),8)
        large_line = round(max(length, width) - small_line,8)
        smallest_plot(small_line, large_line)

#test same length
length = 1
width = 1
smallest_plot(length, width)

#test width > length
length = 1
width = 12
smallest_plot(length, width)

#test length > width
length = 12
width = 12
smallest_plot(length, width)

#test decimals
length = 12.798
width = 10.569
smallest_plot(length, width)