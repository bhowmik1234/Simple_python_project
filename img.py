from PIL import Image
import cv2

img = Image.open("oppo.png")
transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
transpose_img.save("corr.png")

print("done")

img = cv2.imread("p1.png")
clahe = cv2.createCLAHE()

g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ench_img = clahe.apply(g_img)

cv2.imwrite("p2.png")

