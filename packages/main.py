import packages.image_processing.ImageCropper as cropper
import cv2

processor = cropper.ImageCropper()
filename = "corns.jpg"
image = cv2.imread(filename,0)


coordinates = processor.select_crop(image,"test",3)



correct = True

first = coordinates[0]
second = coordinates[1]
third = coordinates [2]


second[1] = first[1]

third[0] = first[0]


#incorrect x-value for second point
if(second[0] <= first[0]):
    correct = False

#incorrect y-value for third point
if(third[1] <= first[1]):
    correct = False

coordinates[0] = first
coordinates[1] = second
coordinates[2] = third
if(correct):
    width = second[0] - first[0]
    height = third[1] - first[1]
    x = first[0]
    y = first[1]
    coord = ((x,y),width,height)
    lst = []
    lst.append(coord)

    processor.partition_image(filename,lst)



else:
    print("You made an error")
