import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize BlipProcessor and BlipForConditionalGeneration models
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Define the URL of the image to be processed
img_url = 'https://w.forfun.com/fetch/ac/ac4ab3ca5717e7787567def744601ce6.jpeg?w=1200&r=0.5625'

# Open and convert the image to RGB format
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

# Perform conditional image captioning
text = "a photography of"
inputs = processor(raw_image, text, return_tensors="pt")

# Generate the caption for the image
out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))

# Perform unconditional image captioning
inputs = processor(raw_image, return_tensors="pt")

# Generate the caption for the image without any text prompt
out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))