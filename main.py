from tkinter import *
from Controller.ControlMenu1 import ControlMenu1
from View.Menu1 import Menu1
from Controller.ControlMenu1 import ControlMenu1

class SidrraMain(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.switch_frame(Menu1, ControlMenu1(None,self.frame,self)) 

    def switch_frame(self, frame_class, control):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        if control.view == None:
            control.view = new_frame
        new_frame.set_controller(control)
        self.frame = new_frame
        self.frame.pack()

if __name__ =="__main__":
    app = SidrraMain()
    app.mainloop()