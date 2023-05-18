import cv2, numpy as np, math
from skimage.metrics import structural_similarity

def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err

def rmse(imageA, imageB):
      return math.sqrt(mse(imageA, imageB))

def ssim(imageA, imageB):
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    return score

def test_inv():
    img1 = cv2.imread('in.jpg')
    img2 = cv2.imread('out.png')
    return (cv2.PSNR(img1, img2), mse(img1, img2), rmse(img1, img2), ssim(img1, img2))

def diff(text1, text2):
    ans = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            ans += 1
    return ans

def test_br(text1, text2):
    return (diff(text1, text2) / len(text2))
