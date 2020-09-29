from tkinter import Frame,Label,CENTER
import colors as c
import moves

class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('--- 2048 ---')
        self.master.bind('<Key>',self.keypress)
        self.action = {c.key_down:moves.move_down,c.key_up:moves.move_up,
        c.key_right:moves.move_right,c.key_left:moves.move_left}
        self.grid_cell=[]
        self.init_grid()
        self.init_matrix()
        print(self)
        self.update_grid()
        self.mainloop()


    def init_grid(self):
        background = Frame(self,bg = c.basic_background,width = c.size,height = c.size)
        background.grid()
        for i in range(c.grid_length):
            grid_row=[]
            for j in range(c.grid_length):
                cell = Frame(background,bg = c.text_background,height = c.size/c.grid_length,
                             width = c.size/c.grid_length)
                cell.grid(row = i,column=j,padx=c.grid_padd,pady = c.grid_padd)
                t = Label(cell,text='',background = c.basic_background,justify=CENTER,height=10,width=15)
                t.grid()
                grid_row.append(t)
            self.grid_cell.append(grid_row)

    def init_matrix(self):
        self.matrix = moves.start()
        moves.add_number(self.matrix)
        moves.add_number(self.matrix)


    def update_grid(self):
        for i in range(c.grid_length):
            for j in range(c.grid_length):
                newnumber = self.matrix[i][j]
                if newnumber:
                    self.grid_cell[i][j].configure(text = str(newnumber),bg = c.background_color_all[newnumber],fg = c.text_color_all[newnumber])
                else:
                    self.grid_cell[i][j].configure(text='',bg = c.basic_background)
        self.update_idletasks()


    def keypress(self,event):
        p = repr(event.char)
        # print(self.action[p])
        if p in self.action:
            self.matrix,flagged = self.action[repr(event.char)](self.matrix)

            if flagged:
                flagged=False
                moves.add_number(self.matrix)
                self.update_grid()
                print('he',self.matrix)
                stats = moves.status(self.matrix)
                print(stats)
                if stats=='YOU WIN':
                    self.grid_cell[1][1].configure(text='Y',bg = c.text_background)
                    self.grid_cell[1][2].configure(text='O',bg = c.text_background)
                    self.grid_cell[1][3].configure(text='U',bg = c.text_background)
                    self.grid_cell[2][1].configure(text='W',bg = c.text_background)
                    self.grid_cell[2][2].configure(text='I',bg = c.text_background)
                    self.grid_cell[2][3].configure(text='N',bg = c.text_background)
                elif stats=='GAME OVER':
                    self.grid_cell[1][0].configure(text='G',bg = c.text_background)
                    self.grid_cell[1][1].configure(text='A',bg = c.text_background)
                    self.grid_cell[1][2].configure(text='M',bg = c.text_background)
                    self.grid_cell[1][3].configure(text='E',bg = c.text_background)
                    self.grid_cell[2][0].configure(text='O',bg = c.text_background)
                    self.grid_cell[2][1].configure(text='V',bg = c.text_background)
                    self.grid_cell[2][2].configure(text='E',bg = c.text_background)
                    self.grid_cell[2][3].configure(text='R',bg = c.text_background)


lets_start = Game2048()          

                    





