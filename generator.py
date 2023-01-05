import cv2
import numpy as np

def create_blank(width, height, rgb_color=(0, 0, 0)):
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image

# Create new blank 300x300 red image

def randomize():
    width, height = 1024, 1024
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
    if type == 'random':
        for i in range(384, 640):
            for j in range(384, 640):
                b = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                r = np.random.randint(0, 255)
                frame[i, j] = [b, g, r]
        cv2.imwrite('generated/random.png', frame)
        return frame
    elif type == 'merge':
        for i in range(384, 640):
            for j in range(384, 640):
                frame[i, j] = (frame[i-1, j] + frame[i, j-1]) / 2
        cv2.imwrite('generated/merge.png', frame)
        return frame
    elif type == 'random_bp':
        for i in range(384, 640, 8):
            for j in range(384, 640, 8):
                b = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                r = np.random.randint(0, 255)
                for k in range(i, i+8):
                    for l in range(j, j+8):
                        frame[k, l] = [b, g, r]
        cv2.imwrite('generated/random_bp.png', frame)
        return frame
    elif type == 'merge_bp':
        for i in range(384, 640, 8):
            for j in range(384, 640, 8):
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
        for i in range(384, 640):
            for j in range(384, 640):
                add = np.random.randint(a, b)
                frame[i, j] = (frame[i-1, j] + frame[i, j-1]) / 2 + [add, add, add]
        cv2.imwrite('generated/merge_plus.png', frame)
        return frame



#frame = generate_content('random')

#frame = generate_content('merge')

#frame = generate_content('random_bp')

#frame = generate_content('merge_bp')

frame = generate_content('merge_plus')

#frame = generate_content('merge_plus_bp')