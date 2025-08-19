import cv2 as cv

def main():
    img = cv.imread('lena-1.png')
    print_image_information(img)
    save_camera_output()

def print_image_information(img):
    if img is None:
        return
    height, width, channels = img.shape[:3]
    size = img.size
    dtype = img.dtype
    print(f"Height: {height} \nWidth: {width} \nChannels: {channels} \nSize: {size} \nType: {dtype}")

def save_camera_output():
    cap = cv.VideoCapture(0)

    if not(cap.isOpened()):
        print("Cannot open camera")
        exit()
    else:
        fps = cap.get(cv.CAP_PROP_FPS)
        frame_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

        with open("camera_outputs.txt", "w") as f:
            f.write(f"FPS: {fps}\n")
            f.write(f"Height: {frame_height}\n")
            f.write(f"Width: {frame_width}\n")

    cap.release()

if __name__ == "__main__":
    main()