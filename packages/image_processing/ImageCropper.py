import cv2
import os

class ImageCropper:

    # modify only in get_point function
    tempX,tempY = 0,0

    def get_point(self,event,x,y,flags,param):

        global tempX,tempY

        if event == cv2.EVENT_LBUTTONDOWN:
            tempX = x
            tempY = y


    def select_crop(self,image_to_crop,image_name,crop_points):
        global tempX, tempY
        cv2.namedWindow(image_name,cv2.WINDOW_NORMAL)
        cv2.setMouseCallback(image_name, self.get_point)
        click_counter = 0
        coordinates = []
        tempX = 0
        tempY = 0

        while click_counter < crop_points:
            cv2.imshow(image_name, image_to_crop)
            k = cv2.waitKey(20) & 0xFF
            if k == ord('q'):
                break
            elif k == ord('a'):
                coordinates.append([tempX, tempY])
                click_counter += 1

        cv2.destroyAllWindows()
        return coordinates

    # crop a region of a bitmap based on a start (x,y) pair and offset in both dimensions
    def bitmap_crop(self,image,startX,startY,offsetX,offsetY):

        cropped_image = image[startY:startY + offsetY, startX:startX + offsetX]
        return cropped_image

    # partition an image in the form of a bitmap
    # the partition(s) are rectangular and specified by (x,y)-coordinate of top-left corner
    # and width and height. partitions is a list of 3-tuples that stores this data.
    # 3-tuple example = ((x,y),width,height)
    def partition_image(self,image_filename,partitions):
        partition_count = 0

        # read image as grayscale
        image = cv2.imread(image_filename,0)

        for partition in partitions:
            top_left_corner = partition[0]
            x_coordinate = top_left_corner[0]
            y_coordinate = top_left_corner[1]
            width = partition[1]
            height = partition[2]
            temp_image = self.bitmap_crop(image,x_coordinate,y_coordinate,width,height)
            process_id = os.getpid()
            cv2.imwrite(str(process_id) + "-" + str(partition_count) + ".jpg",temp_image)
            partition_count += 1