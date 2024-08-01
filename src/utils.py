from PIL import ImageDraw

def filter_persons(results):
    return [x for x in results.xyxy[0] if x[-1] == 0]

def draw_bounding_boxes(img, persons):
    draw_img = img.copy()
    draw = ImageDraw.Draw(draw_img)
    for *box, conf, cls in persons:
        x1, y1, x2, y2 = box
        draw.rectangle([x1, y1, x2, y2], outline='red', width=2)
        draw.text((x1, y1), f'person: {conf:.2f}', fill='yellow')
    return draw_img
