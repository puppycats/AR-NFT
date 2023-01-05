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

def generate_content(frame, type):
    if type == 'random':
        for i in range(384, 640):
            for j in range(384, 640):
                b = np.random.randint(0, 255)
                g = np.random.randint(0, 255)
                r = np.random.randint(0, 255)
                frame[i, j] = [b, g, r]
        return frame
    elif type == 'merge':
        for i in range(384, 640):
            for j in range(384, 640):
                frame[i, j] = (frame[i-1, j] + frame[i, j-1]) / 2
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
        return frame
    elif type == 'merge_bp':
        for i in range(384, 640, 8):
            for j in range(384, 640, 8):
                for k in range(i, i+8):
                    for l in range(j, j+8):
                        frame[k, l] = (frame[i-1, j] + frame[i, j-1]) / 2
        return frame

    
'''
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640,480))

for i in range(0, 100):
    frame = randomize()
    frame = generate_content(frame)
    out.write(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
out.release()
'''

frame = randomize()
frame = generate_content(frame, 'random')
cv2.imwrite('generated/random.png', frame)

frame = randomize()
frame = generate_content(frame, 'merge')
cv2.imwrite('generated/merge.png', frame)

frame = randomize()
frame = generate_content(frame, 'random_bp')
cv2.imwrite('generated/random_bp.png', frame)

frame = randomize()
frame = generate_content(frame, 'merge_bp')
cv2.imwrite('generated/merge_bp.png', frame)