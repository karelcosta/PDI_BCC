import cv2

img = cv2.imread("color_red.jpg")
# if not img.isOpened():
#     print("Erro ao acessar a imagen")
#     exit()
gray = img.copy()
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

row, coll = img.shape[0:2]

for i in range(row):
    for j in range(coll):
        if (hsv[i][j][0]<170 or hsv[i][j][0]>200 ):
            gray[i][j] = sum(img[i][j]) * 0.33

cv2.imshow("gray", gray)
cv2.waitKey()
cv2.destroyAllWindows()