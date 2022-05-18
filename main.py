import csv
import random
from textwrap import wrap
from tkinter import messagebox

from Deliverytime import DeliveryTime
from exponentialsearch import Search
from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import ImageTk, Image

################### RUN THIS MAIN FILE ########################


class mainapp:
    def __init__(self, root):
        file = open("MYDATA.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        # print(header)
        rows = []
        for row in csvreader:
            rows.append(row)
        file.close()

        self.lst = []
        self.dict = {}
        for i in rows:
            name = str(i[1])
            self.lst.append(name)
            key = int(i[0])
            price = float(i[2])
            quantity = int(i[3])
            self.dict[key] = (price, quantity)
        self.root = root
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.title("DS2 project - HU Restaurant")
        self.root.geometry("%dx%d" % (self.width, self.height))
        self.root.resizable(False, False)
        self.q = StringVar()
        self.clicked = StringVar()
        self.deliverymins = StringVar()
        self.myLabel = Label()
        self.availability = Label()
        self.my_tree = ttk.Treeview()
        self.places = ["Cafeteria", "Dhaaba", "East Street", "Central Street 2", "Central Lower Ground",
                       "Gym", "Swimming Pool", "Amphitheater", "Circuits and Electronic Lab 1", "Music Room", "Library", "Central Street 1",
                       "Linux And Networking Lab", "Visualization And Graphics Lab", "Zen Garden", "Multipurpose Sports Courts 1", "Wellness Courtyard", "Office Of Student Life",
                       "Reception", "Earth Courtyard", "Student Lounge", "Soorty Hall", "East Zone", "Learn Courtyard",
                       "Arif Habib Classroom", "Air Courtyard", "Water Courtyard", "Fire Courtyard", "Chemistry Lab",
                       "Digital Systems and Instrumentation Lab", "Engineering Workshop", "Student Center", "Prayer Area",
                       "Faculty Cafeteria", "Day Care", "Amin Issa Tai Classroom", "Design Studio", "Baithak", "Playground"]
        self.delivery = DeliveryTime()

        self.randomlist = []  # random list created to store the numbers generated
        for i in range(0, 2000):
            n = random.randint(1, 2000)
            if n not in self.randomlist:
                self.randomlist.append(n)

        self.randomlist.sort()
        self.len = len(self.randomlist)

        # Background Image:
        imgTemp = Image.open("images/picture.jpg")
        img2 = imgTemp.resize((self.width, self.height))
        self.bg = ImageTk.PhotoImage(img2)
        self.bg_image = Label(self.root, image=self.bg).pack(
            side='top', fill=Y, expand=True)

        # Title Frame
        Frame_title = Frame(self.root, bg="white")
        Frame_title.place(x=150, y=150, height=100, width=600)

        title = Label(
            Frame_title, text="Welcome to HU Restaurant's Application", font=("Impact", 20, "bold"), fg="#d77337", bg="white").place(x=80, y=30)

        login_btn = Button(self.root, command=self.starters, text="Enter", fg="white", bg="#d77337", font=(
            "times new roman", 20)).place(x=400, y=300)

    def update(self, rows, index, name):
        # For a particular item being searched, it displays its information
        self.my_tree.delete(*self.my_tree.get_children())
        self.my_tree.insert(parent='', index='end', iid=index,
                            text=name, values=(rows[0], rows[1]))

    def updateall(self):
        # When clear search button is clicked, it updates the tree-view
        self.my_tree.delete(*self.my_tree.get_children())
        for key in self.dict:
            price_quantity = []
            keyy = key-1
            name = self.lst[keyy]
            price_quantity.insert(0, self.dict[key][0])
            price_quantity.insert(1, self.dict[key][1])
            self.my_tree.insert(parent='', index='end', iid=key, text=name, values=(
                price_quantity[0], price_quantity[1]))
        self.ent.delete(0, 'end')
        self.availability.config(
            text="Availability")

    def displayInfo(self):
        q2 = self.q.get()
        print(q2)

        price_quantityy = []

        index = -1
        for idx in range(len(self.lst)):
            compare = self.lst[idx]
            if compare.lower() == q2.lower():
                index = idx
        if index == -1:
            self.availability.config(
                text="This food item DOESNT EVEN EXIST!")
        if index in self.dict:
            keyy = index
            name = self.lst[keyy]
            price_quantityy.insert(0, self.dict[index][0])
            price_quantityy.insert(1, self.dict[index][1])
        self.update(price_quantityy, index, name)

        self.classsearch = Search(self.lst, q2, index)
        result = self.classsearch.exponentialSearch(
            self.randomlist, self.len, index)
        if result == -1:
            print(
                "The food item is not avaliable in the restaurant! Order something else please! ")
            self.availability.config(
                text="The food item is not avaliable in the restaurant! Order something else please! ")
        else:
            print("The food item is avaliable in the restaurant")
            self.availability.config(
                text="The food item is avaliable in the restaurant")

    def deliverytime(self):
        # Uses DIJKSTRA ALGORITHM to find time in minutes
        location = self.clicked.get()
        self.deliverymins = self.delivery.minDeliveryTime(location)
        self.deliverymins = str(self.deliverymins)
        self.deliverymins = self.deliverymins + " minutes"
        self.myLabel.config(text=self.deliverymins)

    def starters(self):
        starter_window = Toplevel(root)
        starter_window.title("DS2 project - HU Restaurant")
        starter_window.geometry("%dx%d" % (self.width, self.height))
        starter_window.resizable(False, False)

        wrapper2 = LabelFrame(starter_window, text="Search & Sort")
        wrapper3 = LabelFrame(starter_window, text="Place Order")

        wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
        wrapper3.pack(fill="both", expand="yes", padx=10, pady=10)

        tree_frame = Frame(starter_window)
        tree_frame.pack(pady=50)

        # SCROLL BAR CONFIRGURATION
        treescroll = Scrollbar(tree_frame)
        treescroll.pack(side=RIGHT, fill=Y)

        # SETTING UP THE TREEVIEW
        self.my_tree = ttk.Treeview(
            tree_frame, yscrollcommand=treescroll.set)

        self.my_tree.config(height=15)
        self.my_tree['columns'] = ("Price", "Quantity")

        self.my_tree.column("#0", width=500, minwidth=25)
        self.my_tree.column("Price", anchor=W, width=300)
        self.my_tree.column("Quantity", anchor=CENTER, width=200)

        self.my_tree.heading("#0", text="Name", anchor=W)
        self.my_tree.heading("Price", text="Price", anchor=W)
        self.my_tree.heading("Quantity", text="Quantity", anchor=CENTER)

        # DISPLAYING THE MENU IN A TREEVIEW
        for key in self.dict:
            price_quantity = []
            keyy = key-1
            name = self.lst[keyy]
            price_quantity.insert(0, self.dict[key][0])
            price_quantity.insert(1, self.dict[key][1])
            self.my_tree.insert(parent='', index='end', iid=key, text=name, values=(
                price_quantity[0], price_quantity[1]))

        self.my_tree.pack(pady=50)
        treescroll.config(command=self.my_tree.yview)

        lbl = Label(wrapper2, text="Search")
        lbl.pack(side='left', padx=10)
        self.ent = Entry(wrapper2, textvariable=self.q, width=30)
        self.ent.pack(side='left', padx=10)
        Search = Button(wrapper2, text="SEARCH",
                        command=self.displayInfo)
        Search.pack(side='left', padx=6)
        Clearsearch = Button(wrapper2, text="Clear Search",
                             command=self.updateall)
        Clearsearch.pack(side='left', padx=10)

        self.availability = Label(wrapper2, text="Availability")

        lbl2 = Label(wrapper3, text="Your Location")
        lbl2.pack(side='left', padx=20)
        drop = OptionMenu(wrapper3, self.clicked, *self.places)
        drop.pack(side=LEFT)

        myButton = Button(wrapper3, text="Show Delivery Time",
                          command=self.deliverytime)

        self.myLabel = Label(wrapper3, text="Time in minutes")

        myButton.pack(side=LEFT, padx=50)
        self.myLabel.pack(side=LEFT, padx=50)
        self.availability.pack(side=RIGHT, padx=10)


root = Tk()
obj = mainapp(root)
root.mainloop()
