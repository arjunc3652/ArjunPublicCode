import cv2

#Access Algorithim
trained_faces_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")




#Get Image
ask=input("Enter the direct path to your image \n")
#Convert image to grayscale
image = cv2.imread(ask)
grayscaled_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#Detect Faces and Put Coordinates In A Simplified List
face_coordinates = trained_faces_data.detectMultiScale(grayscaled_img)
mylist=[]



#Draw Rectangle Around Face Using Coordinates
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 4)
    
    
    
#Show image    
cv2.imshow("Face Detected",image)
cv2.waitKey()
    
































  


