import cv2


def threshold_demo(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    ret, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    print("BINARY阈值：%s" % ret)
    cv2.imshow("BINARY", binary)

    ret, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)
    print("BINARY_INV阈值：%s" % ret)
    cv2.imshow("BINARY_INV_230", binary)
    
    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_TRIANGLE)
    # ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE) 与上一行代码是同一个意思，| cv2.THRESH_TRIANGLE 就是调用这种方法来算阈值
    print("TRIANGLE自适应阈值：%s" % ret)
    cv2.imshow("TRIANGLE", binary)

    ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    print("OTSU自适应阈值：%s" % ret)
    cv2.imshow("OTSU", binary)

    ret, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_TRUNC)
    print("TRUNC截断阈值：%s" % ret)
    cv2.imshow("TRUNC_200", binary)

    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_TOZERO)
    print("TOZERO归零阈值：%s" % ret)
    cv2.imshow("TOZERO_100", binary)

if __name__ == "__main__":
    #图像获取
    from ImageInput import ScreenCapture
    myImage = ScreenCapture(origin_point="left_and_top")   
    while True:
        has_img = myImage.get_img()
        if has_img == None:
            img = myImage.grab_screen_mss(myImage.mointor)
        #src1 = cv2.imread("book.jpg")
        image = img
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
        print("BINARY阈值：%s" % ret)
        cv2.imshow("BINARY", binary)
        #cv2.imshow("book", src1)
        #threshold_demo(src1)

        if cv2.waitKey(1) & 0XFF == myImage.Exit_key:  # 默认：ESC
            cv2.destroyAllWindows()
            exit("结束")