import cv2

def show_avatar(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load:", image_path)
        return img

    img = cv2.resize(img, (400, 400))   # adjust size you want
    return img
