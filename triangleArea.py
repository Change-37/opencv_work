"""
    주석처리하기~~~
"""
width = 3
height = 5
RectArea = width * height
TriArea = RectArea / 2

print(RectArea)
print(width, "*", height, "=", RectArea)

# {} 로 format
print("{0} : {1} * {2} / 2 = {3}".format('Triangle Area', width, height, TriArea))

