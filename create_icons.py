from PIL import Image, ImageDraw, ImageFont

# Create simple bus icon
size = 512
img = Image.new('RGB', (size, size), '#007bff')
draw = ImageDraw.Draw(img)

# Draw bus outline
draw.rounded_rectangle([50, 100, size-50, size-50], radius=20, fill='white', outline='#007bff', width=8)
draw.rounded_rectangle([100, 130, size-100, size-130], radius=10, fill='#87CEEB', outline='#007bff', width=4)
draw.circle((150, size-100), 50, fill='#333', outline='white', width=6)
draw.circle((size-150, size-100), 50, fill='#333', outline='white', width=6)
draw.rectangle([180, size-60, size-180, size-50], fill='#333')

# Save icons
img.resize((192, 192)).save('C:/Users/Jimmy/workspace/bus-eta/icon-192.png')
img.resize((512, 512)).save('C:/Users/Jimmy/workspace/bus-eta/icon-512.png')
print("Icons created")
