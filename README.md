# pytkanim-1.0.0
PyTkAnim is extension for tkinter that provides animator and simple usage.


Note:This package is under construction and many style of animations soon!
     for now you can only animate X and Y

# animate Y when button is clicked
```python
import tkinter as tk
from pytkanim import normalAnims

root = tk.Tk() 
                                   #Widget Name    can be also 'up'
Label = normalAnims.NormalAnimY(tk.Label(bg="Black"),"down") 
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()

root.geometry("800x600")
root.mainloop()
```


# animate X when button is clicked
```python
import tkinter as tk
from pytkanim import normalAnims

root = tk.Tk()
                                  #Widget Name    can be also 'backwards'
Label = normalAnims.NormalAnimX(tk.Label(bg="Black"),"forward") 
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()

root.geometry("800x600")
root.mainloop()
```

# You can add starter X and Y positions too! by simple doing this
```python
import tkinter as tk
from pytkanim import normalAnims

root = tk.Tk()

Label = normalAnims.NormalAnimX(tk.Label(bg="Black"),"backwards",startAX=0.5,startAY=0.5)
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()

root.geometry("800x600")
root.mainloop()
```

# and also how speed to animate is.
```python
import tkinter as tk
from pytkanim import normalAnims

root = tk.Tk()

Label = normalAnims.NormalAnimX(tk.Label(bg="Black"),"forward",startAX=0.5,startAY=0.5,speed=10) #Higher amount of speed the more it goes slower.r
Button = tk.Button(text="Click Me",command=Label.run)
Button.pack()

root.geometry("800x600")
root.mainloop()
```

# Stop and Continue Animation 
```python
import tkinter as tk
from pytkanim import normalAnims
stopped = False
root = tk.Tk()

Label = normalAnims.NormalAnimX(tk.Label(bg="Black"),"forward",startAX=0,startAY=0.5,speed=10)
Label.run()

def continueAndStop():
    global stopped,Label
    if stopped == False:
        stopped = True
        Label.stop()
    else:
        stopped = False
        Label.continueAnim()


Button = tk.Button(text="Stop/Continue",command=continueAndStop)
Button.pack()

root.geometry("800x600")
root.mainloop()
```

# Changing Direction
```python
import tkinter as tk
from pytkanim import normalAnims
direction = "backwards"
root = tk.Tk()

Label = normalAnims.NormalAnimX(tk.Label(bg="Black"),"forward",startAX=0,startAY=0.5,speed=10)
Label.run()

def changingDirection():
    global direction,Label
    if direction == False:
        direction = True
        Label.changeDirection("forward")
    else:
        direction = False
        Label.changeDirection("backwards")


Button = tk.Button(text="Stop/Continue",command=changingDirection)
Button.pack()

root.geometry("800x600")
root.mainloop()
```
