from ultralyticsplus import YOLO, render_result
import numpy as np

from PIL import Image,ImageOps,ImageEnhance,ImageFilter
def extractTable(image):
    # load model
    model = YOLO('foduucom/table-detection-and-extraction')

# set model parameters
    model.overrides['conf'] = 0.25  # NMS confidence threshold
    model.overrides['iou'] = 0.45  # NMS IoU threshold
    model.overrides['agnostic_nms'] = False  # NMS class-agnostic
    model.overrides['max_det'] = 1000  # maximum number of detections per image
    # perform inference
    results = model.predict(image)

# observe results
    print(results[0].boxes)
    print(len(results))
    render = render_result(model=model, image=image, result=results[0])
    render.show()

    x1, y1, x2, y2, _, _ = tuple(int(item) for item in results[0].boxes.data.numpy()[0])
    img = np.array(Image.open(image))
    #cropping the image
    cropped_image = img[y1:y2, x1:x2]
    cropped_image = Image.fromarray(cropped_image)
    return cropped_image

def preprocessImageForImprovingQuality(originalImage,improvedImage):
        output_path="highresimage.png"
        dpi=300
        originalImage.save(output_path, dpi=(dpi, dpi))
        grayscale_image = ImageOps.grayscale(originalImage)
        enhancer = ImageEnhance.Contrast(grayscale_image)
        newImage=enhancer.enhance(2.0)
        finalImage=newImage.filter(ImageFilter.MedianFilter(size=3))
        finalImage.save (improvedImage)


if __name__ == '__main__':
    image = 'page_1.png'
    croppedImage=extractTable(image)
    newImageName="finalQualityImage.png"
    preprocessImageForImprovingQuality(croppedImage,newImageName)