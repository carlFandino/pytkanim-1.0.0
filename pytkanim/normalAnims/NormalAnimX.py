class NormalAnimX:
	"""This animates the X AXIS to the widget given. speed param can be ex.1000 = 1 second or 100 = 1ms or 30 for smoother animation.

	Run anim when button is clicked.
	>>> import tkinter as tk
	>>> root = tk.Tk()
	>>> Label = NormalAnimX(tk.Label(bg="Black"),"backwards")
	>>> Button = tk.Button(command=Label.run)
	>>> Button.pack()
	>>> root.geometry("1080x600")
	>>> root.mainloop()


	"""
	
	normal_speed = 30
	def __init__(self,widget,direction,startAX=0,startAY=0,speed=normal_speed):
		widget.place_configure(relx=startAX,rely=startAY)
		self.widget = widget
		self.__startAX = startAX
		self.__startAY = startAY
		self.speed = speed 
		self.direction = direction.lower()
		self.isStop = False
		self.__isrunning = False


	def __run__(self):
		
		if self.isStop == False:
			if self.direction == "forward" or self.direction == "backwards":
				if self.direction == "forward":
					self.__startAX += 0.005
				elif self.direction == "backwards":
					self.__startAX -= 0.005
			else:
				raise TypeError("direction must be forward and backwards")

		self.widget.place_configure(relx=self.__startAX,rely=self.__startAY) 
		self.widget.after(self.speed,self.__run__)

	def run(self):
		"""Start animating"""
		if self.__isrunning == False:
			self.__isrunning =True
			self.__run__()
		else:
			pass

	def stop(self):
		"""Stops the animation."""
		self.isStop = True

	def continueAnim(self):
		"""Continue animation from animating."""
		self.isStop = False

	def changeDirection(self,direction):
		"""Change direction according to the param direction given."""
		direction = direction.lower()
	
		if direction == "forward" or direction == "backwards":
			self.direction = direction
		else:
			raise TypeError("direction must be forward and backwards")
			