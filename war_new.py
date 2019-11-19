from tkinter import *
import random
import time

font = ('Roboto', 18)
#the battlefield
class Pixel():

    def __init__(self, p_number):
        self.p_number = p_number#=pixel number: is the number of squares on a side
        rel_p_width = 1/p_number
        self.create_color_list()
        self.p_list = [[] for x in range(p_number)]#=list containing all the Labels
        #creating the Labels
        for x in range(p_number):
            for y in range(p_number):
                p = Label(pixel_f, bg=self.c(self.colors[x][y]))
                p.place(relx=y*rel_p_width, rely=x*rel_p_width, relwidt=rel_p_width, relheight=rel_p_width)
                self.p_list[x].append(p)

    def create_color_list(self):
        self.colors = [[] for x in range(self.p_number)]#=list cointaining all the current colors in the form of 0 and 1
        self.new_colors = [[] for x in range(self.p_number)]#=temporaney list for the new Labels colors
        for x in range(self.p_number):
            for y in range(self.p_number//2):
                self.colors[x].append(0)#=red
            for y in range(self.p_number//2):
                self.colors[x].append(1)#=blue

    def c(self, i):
        if i==0:#this function converts 0 and 1 in colors strings (readble by tkinter)
            return 'red'
        else:
            return 'blue'

    def change_colors(self):
        for x in range(self.p_number):
            for y in range(self.p_number):
                near = []
                try:#up, try and except used because the Labels on the sides have no neighbour
                    near.append(self.colors[x-self.p_number-1][y])
                except:
                    near.append(self.colors[x][y])
                try:#right
                    near.append(self.colors[x][y+1])
                except:
                    near.append(self.colors[x][y])
                try:#down
                    near.append(self.colors[x+1][y])
                except:
                    near.append(self.colors[x][y])
                try:#left
                    near.append(self.colors[x][y-self.p_number-1])
                except:
                    near.append(self.colors[x][y])

                self.new_colors[x].append(random.choice(near))#random choiche in the near color of neighbours
        self.colors = self.new_colors
        self.new_colors = [[] for x in range(self.p_number)]#=temporaney list for the new Labels colors

    def run(self):
        undone = True
        while undone:
            self.change_colors()
            blacks = 0#blacks label counter
            for x in range(self.p_number):#showing up the changed colors
                for y in range(self.p_number):
                    self.p_list[x][y].config(bg=self.c(self.colors[x][y]))
                    w.update_idletasks()
                    w.update()
                    blacks += self.colors[x][y]
            if (blacks == self.p_number**2) or (blacks==0):#if it's all black or all withe
                undone = False


w = Tk()
w.geometry('600x700')
w.title('pixel')

def go():
    go_button.config(state='disabled')
    this = Pixel(e_pixel.get())
    this.run()
    del this
    go_button.config(state='active')

pixel_f = Frame(w)
pixel_f.place(x=0, y=0, relwidt=1, height=600)

data_f = Frame(w, bg='white')
data_f.place(x=0, y=600, relwidt=1, height=100)

e_pixel = Scale(master=data_f, font=font, orient='horizontal', from_=2, to=50, resolution=2, bg='white')
e_pixel.pack(side='left', expand=True, fill='x')

go_button = Button(master=data_f, font=font, text='Go!', relief='groove', bg='white', command=go)
go_button.pack(side='right', expand=True, fill='both')

w.mainloop()
