my_image.tell()
# 0
image_data = my_image.read(5)
image_data
# b'\x89PNG\r'
type(image_data)
my_image.tell()
# 5
my_image.seek(0)
# 0
image_data = my_image.read()
len(image_data)

# 14922
