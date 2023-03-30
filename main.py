import io
from tkinter import *
import requests
from urllib.request import urlopen
from PIL import Image,ImageTk
import webbrowser

class News:

    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=c9b35b3a066'
                                 '14643b81c75bfa31f2bf3').json()
        print(self.data)
        self.home_screen()
        self.load_news_item(0)
        self.root.mainloop()

    def home_screen(self):
        self.root = Tk()
        self.root.geometry('900x700')
        self.root.title('News-Talk')
        self.root.configure(bg='black')
        self.root.resizable(False,False)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        self.clear()
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            final = Image.open(io.BytesIO(raw_data)).resize((500,300))
            photo = ImageTk.PhotoImage(final)
        except:
            img_url = 'https://t4.ftcdn.net/jpg/02/51/95/53/360_F_251955356_FAQH0U1y1TZw3ZcdPGybwUkH90a3VAhb.jpg'
            raw_data = urlopen(img_url).read()
            final = Image.open(io.BytesIO(raw_data)).resize((500, 300))
            photo = ImageTk.PhotoImage(final)

        image_label = Label(self.root,image=photo)
        image_label.place(x=200,y=200)

        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',font=('Arial Black',17),wraplength=800,justify='center')
        heading.pack(pady=20)

        description = Label(self.root,text=self.data['articles'][index]['description'],bg='black',fg='white',font=('Candara',17),wraplength=800,justify='center')
        description.pack(side=BOTTOM,pady=40)

        frame = Frame(self.root,width=900,height=40,bg='#131313')
        frame.pack()

        if index!=0:
            prvs_btn = Button(frame,width=30,bg='#131313',text='Previous',borderwidth=0,font=('Candara',15),fg='white',command=lambda:self.load_news_item(index-1))
            prvs_btn.pack(side=LEFT)

        read_btn = Button(frame, width=30, bg='#131313', text='Read More', borderwidth=0,font=('Candara',15),fg='white',command=lambda:webbrowser.open(self.data['articles'][index]['url']))
        read_btn.pack(side=LEFT)

        if index!=len(self.data['articles'])-1:
            nxt_btn = Button(frame,width=30,bg='#131313',text='Next',borderwidth=0,font=('Calibri',15),fg='white',command=lambda:self.load_news_item(index+1))
            nxt_btn.pack(side=LEFT)

a = News()