import cv2
import numpy as np

def create_blank(width, height, rgb_color=(0, 0, 0)):
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(rgb_color)
    image[:] = color
    return image

def randomize():
    width, height = 768, 768
    image = create_blank(width, height, rgb_color=(0, 0, 0))
    for i in range(0, width):
        for j in range(0, height):
            b = np.random.randint(-10, 10)
            g = np.random.randint(-10, 10)
            r = np.random.randint(-10, 10)
            image[i, j] = image[i-1, j-1] + [b, g, r]
    return image

def generate_content(type):
    frame = randomize()
    
    c_s = 256
    c_e = 512

    if type == 'random':
        for i in range(c_s, c_e):
            for j in range(c_s, c_e):
                b = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                r = np.random.randint(0, 255)
                frame[i, j] = [b, g, r]
        cv2.imwrite('generated/random.png', frame)
        return frame
    elif type == 'merge':
        for i in range(c_s, c_e):
            for j in range(256, 512):
                frame[i, j] = (frame[i-1, j] + frame[i, j-1]) / 2
        cv2.imwrite('generated/merge.png', frame)
        return frame
    elif type == 'random_bp':
        for i in range(c_s, c_e, 8):
            for j in range(c_s, c_e, 8):
                b = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                r = np.random.randint(0, 255)
                for k in range(i, i+8):
                    for l in range(j, j+8):
                        frame[k, l] = [b, g, r]
        cv2.imwrite('generated/random_bp.png', frame)
        return frame
    elif type == 'merge_bp':
        for i in range(c_s, c_e, 8):
            for j in range(c_s, c_e, 8):
                for k in range(i, i+8):
                    for l in range(j, j+8):
                        frame[k, l] = (frame[i-1, j] + frame[i, j-1]) / 2
        cv2.imwrite('generated/merge_bp.png', frame)
        return frame
    elif type == 'merge_plus':
        a = np.random.randint(0, 10)
        b = np.random.randint(0, 10)
        if a > b:
            a, b = b, a
        if a == b:
            if a > 0:
                a -= 1
            else:
                b += 1
        for i in range(c_s, c_e):
            for j in range(c_s, c_e):
                add = np.random.randint(a, b)
                frame[i, j] = (frame[i-1, j] + frame[i, j-1]) / 2 + [add, add, add]
        cv2.imwrite('generated/merge_plus.png', frame)
        return frame



frame = generate_content('random')

frame = generate_content('merge')

frame = generate_content('random_bp')

frame = generate_content('merge_bp')

frame = generate_content('merge_plus')

#frame = generate_content('merge_plus_bp')