from PIL import Image

word_matrix = Image.open('word_matrix.png')

print (f"Size of the Image: {word_matrix.size}")

matrix_h, matrix_w = word_matrix.size

mask = Image.open('mask.png')

print (f"Size of the mask: {mask.size}")

new_mask = mask.resize((int(matrix_h),int(matrix_w)))

print (f"Resize of the mask: {new_mask.size}")

new_mask.putalpha(120)

word_matrix.paste(new_mask,box=(0,0),mask=new_mask)

word_matrix.show()