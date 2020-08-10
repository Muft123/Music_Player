import tkinter
import tkinter.messagebox
import os
import threading
import Loop

class MainUI():
    def __init__(self,dir,title):
        self.playfun = Loop.playmould(dir)
        self.listloop = threading.Thread(target=self.playfun.listloop)
        self.listloop.setDaemon(True)
        self.dirctory = dir
        #self.lyrics = self.playfun.lyrics()
        self.UI = tkinter.Tk()
        self.UI.title(title)
        self.UI.geometry("640x480")
        self.UI.resizable(width=False,height=False)
        self.muxiclist()
        self.showmusicname()
        self.showlyrics()
        self.showupbutton()
        self.showpausebutton()
        self.showrandombutton()
        self.showplaymusicbutton()
        self.showlistloopbutton()
        self.showsingleloopbutton()
        self.showstopbutton()

        self.UI.mainloop()

    def muxiclist(self):
        sb = tkinter.Scrollbar(self.UI)
        sb.pack(side="right",fill='y')
        musiclist = tkinter.Listbox(self.UI,height=23,width=20)
        musiclist.config(yscrollcommand=sb.set)
        sb.config(command=musiclist.yview)
        musiclist.place(x=10,y=10,anchor='nw')
        for item in os.listdir(self.dirctory):
            musiclist.insert(1,item)

    def showmusicname(self):
        musicname = tkinter.Text(self.UI,width=65,height=1)
        musicname.pack()
        musicname.place(x=160,y=10,anchor='nw')
        musicname.insert('insert','这里是歌名')
        musicname.config(state='disabled')

    def showlyrics(self):
        lyrics = tkinter.Text(self.UI,width = 65,height = 30)
        lyrics.pack()
        lyrics.place(x=160,y=30,anchor='nw')
        lyrics.insert('insert','这里是歌词')
        lyrics.config(state='disabled')

    def showupbutton(self):
        nextmusic = tkinter.Button(self.UI,text='上一首\n暂未实现',bg='white',width=7,fg='black')
        nextmusic.pack()
        nextmusic.place(x=10,y=439,anchor='nw')

    def showpausebutton(self):
        nextmusic = tkinter.Button(self.UI,text='暂停',bg='white',width = 7,fg='black',command = self.playfun.pause)
        nextmusic.pack()
        nextmusic.place(x=70,y=439,anchor='nw')

    def showplaymusicbutton(self):
        nextmusic = tkinter.Button(self.UI,text='播放',bg='white',width = 7,fg='black',command = self.playfun.play)
        nextmusic.pack()
        nextmusic.place(x=130,y=439,anchor='nw')

    def showstopbutton(self):
        nextmusic = tkinter.Button(self.UI,text='下一首\n暂未实现',bg='white',width = 7,fg='black')
        nextmusic.pack()
        nextmusic.place(x=190,y=439,anchor='nw')

    def showlistloopbutton(self):
        nextmusic = tkinter.Button(self.UI,text='列表',bg='white',width = 7,fg='black',command = self.listloop.start)
        #nextmusic.bind('<ButtonRelease-1>',self.playthread.start)
        nextmusic.pack()
        nextmusic.place(x=250,y=439,anchor='nw')

    def showsingleloopbutton(self):
        nextmusic = tkinter.Button(self.UI,text='单曲(未开放)',bg='white',width  = 15,fg='black',command = self.clicksingle)
        nextmusic.pack()
        nextmusic.place(x=310,y=439,anchor='nw')

    def showrandombutton(self):
        nextmusic = tkinter.Button(self.UI,text='随机(未开放)',bg='white',width = 15,fg='black',command = self.clickrandom)
        nextmusic.pack()
        nextmusic.place(x=420,y=439,anchor='nw')

    def clickrandom(self):
        tkinter.messagebox.showwarning('Warning','此功能尚未开放')

    def clicksingle(self):
        tkinter.messagebox.showwarning('Warning','此功能尚未开放')
