#!/usr/bin/env python3
import matplotlib.pyplot as plt
from matplotlib import widgets

class WidgetRow:
    def __init__(self):
        pass

class WidgetColum:
    def __init__(self):
        pass

class Gui:
    def __init__(self):
        # interactive, single-plot, non-animated matplotlib gui
        self.fig, self.axImg = plt.subplots() # axImg is drawn at Bbox([[0.125, 0.10999999999999999], [0.9, 0.88]]). fig size default is 640x480 pixels
        self.fig.canvas.mpl_connect('button_press_event',self._onclick)
        self.fig.canvas.mpl_connect('key_press_event',self._onkeypress)
        self.adding_axis = 0
        self.axis_coords = [] # top-left, bottom-right
        self.add_widget_callback = None
        
        self.buttons = []
        
    def _onclick(self, event):
        print(f'clicked: {event.x} {event.y}') # pixels. bottom-left is 0,0
        figsize = self.fig.get_size_inches()*self.fig.dpi # pixels
        x_ = event.x / figsize[0]
        y_ = event.y / figsize[1]
        print(f'figsize = {figsize}')
        if self.adding_axis == 1:
            self.axis_coords.append([x_,y_])
            print('click where the lower right should go')
            self.adding_axis = 2
        elif self.adding_axis == 2:
            self.axis_coords.append([x_,y_])
            self.adding_axis = 0
            self.add_widget_callback()            
        else:
            pass
    
    def _onkeypress(self,event):
        print(f'pressed {event.key}')
        if event.key == 'b':
            self._add_button()
        elif event.key == 'c':
            self._add_checkbox()
        elif event.key == 't':
            self._add_textbox()
    
    def _add_button(self):
        self.axis_coords = []
        print('click where the top left should go')
        self.adding_axis=1
        self.add_widget_callback = self._add_button_callback
    def _add_button_callback(self):
        #top, left, bottom, right = self.axis_coords
        left, top = self.axis_coords[0]
        right, bottom = self.axis_coords[1]
        width = right - left
        height = top - bottom
        newAx = self.fig.add_axes((left,bottom,width,height))
        nButtons = len(self.buttons)
        newbtn = widgets.Button(newAx,'button'+str(nButtons))
        newAx.draw(newAx.figure.canvas.get_renderer())
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        self.buttons.append([newbtn,newAx])
    #    #rect : tuple (left, bottom, width, height)
    #    #The dimensions (left, bottom, width, height) of the new Axes. All
    #    #quantities are in fractions of figure width and height.




gui = Gui()
plt.show()

        