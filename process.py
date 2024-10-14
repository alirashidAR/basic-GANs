from PIL import Image,ImageDraw
import tensorflow

# Open an image file
image_path = "image.jpg"  # Replace with your image file path
image = Image.open(image_path)

image.show()


f'''
# Resize the image to fit the requirements of the keras_ocr pipeline
target_size = (640, 480)  # Replace with the target size required by keras_ocr
resized_image = image.resize(target_size)

# Convert the image to a numpy array
image_array = np.array(resized_image)

# Create a keras_ocr.pipeline.Pipeline object
pipeline = keras_ocr.pipeline.Pipeline()

# Use the pipeline to perform OCR on the image
predictions = pipeline.recognize([image_array])

mask = Image.new("L", resized_image.size, 255)

# Draw on the mask to hide the detected "name" text regions
draw = ImageDraw.Draw(mask)
for prediction in predictions:
    for text, bbox in prediction:
        if text.lower() == "name":
            # Convert bounding box to integer values
            bbox = [(int(coord[0]), int(coord[1])) for coord in bbox]
            # Draw filled polygon with white color (255) to hide the "name" text
            draw.polygon(bbox, fill=255)

# Apply the mask to the resized image to remove the "name" text
image_without_name = Image.composite(resized_image, Image.new("RGB", resized_image.size, (255, 255, 255)), mask)

'''