import numpy as np
import cv2
import math
import random
import copy

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.parent=None

class RRT():
    def __init__(self):
        self.start=Point(576,964)            
        self.radius=20
        self.path=[self.start]              
        self.img=np.zeros((1500,1500,3),np.uint8)

    def ObstacleCheck(self,pixel,frame):
    	
    	if (frame[pixel.y,pixel.x][0]<=30 and frame[pixel.y,pixel.x][1]<=30 and frame[pixel.y,pixel.x][2]<=30):
        	return 1
        if (frame[pixel.y,pixel.x][0]>=225 and frame[pixel.y,pixel.x][1]<=30 and frame[pixel.y,pixel.x][2]<=30) :
            return 1
        else:
        	return 0



    def DrawLine(self,frame):
    	while(1):
	    	random_point=Point(random.randint(0,1600),random.randint(0,2200))			
	    	min_distance=90000000000000
	    	for element in self.path:
	        	if min_distance>math.sqrt((random_point.y-element.y)**2+(random_point.x-element.x)**2):
	        		min_distance=math.sqrt((random_point.y-element.y)**2+(random_point.x-element.x)**2)
	        		j=self.path.index(element) 


	        check=1	                  #j is the index of element with smallest distance
	             
	        for h in range(self.radius) :
                                if ((random_point.x-self.path[j].x)**2+(random_point.y-self.path[j].y)**2)==0:
                                     continue
				pixel=Point(int(float(self.path[j].x)+float((random_point.x-self.path[j].x)*h)/math.sqrt((random_point.x-self.path[j].x)**2+(random_point.y-self.path[j].y)**2)),int(float(self.path[j].y)+float((random_point.y-self.path[j].y)*h)/math.sqrt((random_point.x-self.path[j].x)**2+(random_point.y-self.path[j].y)**2)))
				if pixel.y>1080 or pixel.y<50 or pixel.x>1460 or pixel.x<460:
					check=0
					break
				if self.ObstacleCheck(pixel,frame)==0:
					continue
				else:
					check = 0
					break

	        if check:
	        	cv2.line(frame,(self.path[j].x,self.path[j].y),(pixel.x,pixel.y),(0,0,255),thickness=1,lineType=8)
	        	cv2.imshow('win',frame)
	        	cv2.waitKey(5)
	        	pixel.parent=j
	        	self.path.append(pixel)
	        	print (pixel.x,pixel.y)
			if self.Dest(pixel,frame):
					print "destination has been reached"
                                        return    


    def Dest(self,pixel,frame):
                
		if pixel.y<1080 and pixel.y>50 and pixel.x<1460 and pixel.x>460:
			if frame[pixel.y,pixel.x][0]<30 and frame[pixel.y,pixel.x][1]>200 and frame[pixel.y, pixel.x][2]<30 :
                                print 1
				return 1
                        if pixel.x>1322 and pixel.x<1437 and pixel.y<339 and pixel.y>269:
                            return 1
			else:
				return 0



def main():
    cap = cv2.VideoCapture('path.mkv')

    while cap.isOpened():
        ret, frame = cap.read()
        rrt=RRT()       
        rrt.DrawLine(frame)
        

       
if __name__ == '__main__':
    main()



   # def videoCall(self):
   #      cap = cv2.VideoCapture('path.mkv')

   #      while cap.isOpened():
   #         ret, frame = cap.read()
   #         self.RandomPointGenerator()
   #         self.DrawLine(frame)
              
   #         if self.Dest():
   #          print "destination has been reached" 


