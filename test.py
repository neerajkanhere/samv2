import numpy as np 
from PIL import Image
from matplotlib import pyplot as plt

image = Image.open("/home/neeraj/temp/frames/1/00000000.jpg")
image = np.array(image.convert("RGB"))
     

#plt.imshow(image)

f, axarr = plt.subplots(2,1)
axarr[0].imshow(image)

from sam2.automatic_mask_generator import SAM2AutomaticMaskGenerator
from sam2.build_sam import build_sam2
from sam2.utils.misc import variant_to_config_mapping
from sam2.utils.visualization import show_masks

model = build_sam2(
    variant_to_config_mapping["tiny"],
    "sam2_hiera_tiny.pt",
)

mask_generator = SAM2AutomaticMaskGenerator(model)
     

masks = mask_generator.generate(image)
     

output_mask = show_masks(
    image=image, masks=masks, scores=None, only_best=False, autogenerated_mask=True
)
     
axarr[1].imshow(output_mask)

plt.show()
