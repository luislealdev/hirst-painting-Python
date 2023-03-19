import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('noche-estrellada.jpg', 6)
hexadecimalColors = []
for colour in colors:
    colorsTuple = (colour.rgb[0], colour.rgb[1], colour.rgb[2])
    hexadecimalColors.append(colorsTuple)

print(hexadecimalColors)