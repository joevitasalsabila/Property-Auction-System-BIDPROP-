from tkinter import*
from PIL import ImageTk,Image
import csv
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from tkinter import ttk

class Property:
    def __init__(self, prop_id, description, price, bidder=None):
        self.prop_id = prop_id
        self.description = description
        self.price = price
        self.bidder = bidder

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def pop(self):
        if self.is_empty():
            print("Linked list is empty.")
            return None

        popped_data = self.head.data
        self.head = self.head.next
        return popped_data

class BidProp:
    def __init__(self, master):
        self.bid_prop = master
        self.bid_prop.geometry('900x600')
        self.bid_prop.resizable(0, 0)
        self.bid_prop.state('zoomed')
        self.bid_prop.title('BidProp')
        self.time_label= None
        self.time_update_id = None
                
        self.background_label = Label(self.bid_prop)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        image = Image.open("BIDPROP.png")  
        image = image.resize((1366, 768), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(image)
        self.background_label.configure(image=self.background_image)
            
        self.register_btn = Button(self.bid_prop, text='REGISTER', bg='grey', fg='white', font=("helvetica",18,"bold"), command=self.register)
        self.register_btn.place(x=1020, y= 330) 

        def on_username_entry_click(event):
            if self.reg_username_entry.get() == "Username":
                self.reg_username_entry.delete(0, "end")

        def on_password_entry_click(event):
            if self.reg_password_entry.get() == "Password":
                self.reg_password_entry.delete(0, "end")
                self.reg_password_entry.configure(show='*')

        def on_confirm_password_entry_click(event):
            if self.confirm_password_entry.get() == "Confirm Password":
                self.confirm_password_entry.delete(0, "end")
                self.confirm_password_entry.configure(show='*')

        self.reg_username_entry = Entry(self.bid_prop, foreground='grey',width= 30,font=20 )
        self.reg_username_entry.place(x=900, y=450)
        self.reg_username_entry.insert(0, "Username")
        self.reg_username_entry.bind("<FocusIn>", on_username_entry_click)

        self.reg_password_entry = Entry(self.bid_prop, show='', foreground='grey',width= 30, font=20)
        self.reg_password_entry.place(x=900, y=500)
        self.reg_password_entry.insert(0, "Password")
        self.reg_password_entry.bind("<FocusIn>", on_password_entry_click)
        self.reg_password_entry.bind("<Key>", lambda event: self.reg_password_entry.configure(show='*'))

        self.confirm_password_entry = Entry(self.bid_prop, show='', foreground='grey',width= 30, font=20)
        self.confirm_password_entry.place(x=900, y=550)
        self.confirm_password_entry.insert(0, "Confirm Password")
        self.confirm_password_entry.bind("<FocusIn>", on_confirm_password_entry_click)
        self.confirm_password_entry.bind("<Key>", lambda event: self.confirm_password_entry.configure(show='*'))

        self.login_btn = Button(self.bid_prop, text='LOGIN', bg='grey', fg='white', font=("helvetica",15,"bold"), command=self.login)
        self.login_btn.place(x=630, y=230)

        def y_username_entry_click(event):
            if self.login_username_entry.get() == "Username":
                self.login_username_entry.delete(0, "end")

        def y_password_entry_click(event):
            if self.login_password_entry.get() == "Password":
                self.login_password_entry.delete(0, "end")
                self.login_password_entry.configure(show='*')

        self.login_username_entry = Entry(self.bid_prop, foreground='grey',width= 25,font=20 )
        self.login_username_entry.place(x=500, y=340)
        self.login_username_entry.insert(0, "Username")
        self.login_username_entry.bind("<FocusIn>", y_username_entry_click)

        self.login_password_entry = Entry(self.bid_prop, show='', foreground='grey',width= 25, font=20)
        self.login_password_entry.place(x=500, y=390)
        self.login_password_entry.insert(0, "Password")
        self.login_password_entry.bind("<FocusIn>", y_password_entry_click)
        self.login_password_entry.bind("<Key>", lambda event: self.login_password_entry.configure(show='*'))

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password == confirm_password:
            with open('users.csv', mode='a', newline='') as users_file:
                writer = csv.writer(users_file)
                writer.writerow([username, password])
            messagebox.showinfo('Registration', 'Registration successful')
        else:
            messagebox.showerror('Registration', 'Passwords do not match')

    login_username= ""

    def login(self):
        global username
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        with open('users.csv', mode='r') as users_file:
            reader = csv.reader(users_file)
            rows = list(reader)
            found_user = False
            for row in rows:
                if row[0] == username and row[1] == password:
                    found_user = True
                    self.show_logged_in_page() 
                    break

            if found_user:

                with open('users.csv', mode='w', newline='') as users_file:
                    writer = csv.writer(users_file)
                    for r in rows:
                        if r == row:
                            writer.writerow([r[0], r[1], '1'])
                        else:
                            writer.writerow(r)
            else:
                messagebox.showerror('Login', 'Invalid username or password')

    def show_logged_in_page(self):
        for widget in self.bid_prop.winfo_children():
            widget.destroy()

        bg_image = Image.open("bgpg2fix.png")
        
        bg_image = bg_image.resize((1366, 768), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(bg_image)
        self.bg_label = Label(self.bid_prop, image=self.bg_image_tk)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        seller_button = Button(self.bid_prop, text='Seller', font=('Rockwell Extra Bold', 20), relief="ridge",  width=18, height=7, command=self.seller_page, bg='white', fg='#A0522D', bd=5, cursor='hand2')
        seller_button.place(x=0, y=314)

        buyer_button = Button(self.bid_prop, text='Buyer', font=('Rockwell Extra Bold', 20),relief="ridge", width=18, height=7, command=self.buyer_page, bg='white', fg='#A0522D', bd=5, cursor='hand2')
        buyer_button.place(x=1010, y=315)

    def seller_page(self):
        # Menghapus seluruh elemen dalam halaman
        for widget in self.bid_prop.winfo_children():
            widget.destroy()

        self.bg_label1 = Label(self.bid_prop, bg='#ddcbb5')
        self.bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
        self.ll = LinkedList()

        def browse_gambar(parent):
            path = filedialog.askopenfilename(parent=parent, filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])  # Memilih gambar dari sistem file
            if path:
                img = Image.open(path)
                img.thumbnail((50, 50)) 
                img_tk = ImageTk.PhotoImage(img)
                label_gambar.configure(image=img_tk)
                label_gambar.image = img_tk
                label_path.configure(text="Path Gambar: " + path)

        def simpan_hasil():
            global tanggal 
            nama = nama_entry.get()
            prop_id = propid_entry.get()
            desc = describ_entry.get("1.0", "end-1c")
            price = harga_entry.get()
            tanggal= date_entry.get()
            if nama != "" and prop_id != "" and price != "":
                if price.isdigit() == False:
                    messagebox.showerror('Validation', 'Input must be number!')
                    return
                
                hasil_input = [nama, price, prop_id, desc, tanggal, username]
               
                path_gambar = label_path.cget(
                    "text").replace("Path Gambar: ", "")

                with open("history11.txt", "r") as file:
                    lines = file.readlines()
                    for line in lines:
                        line = line.replace("\n", "")
                        splitLines = line.split(";;")
                        if len(splitLines) >= 3 and splitLines[2] == prop_id:
                            messagebox.showerror(
                                "Validation", "Property ID must be unique!")
                            return

                with open("history11.txt", "a") as file:
                    separation = ";;"
                    writeHistory = ""
                    for i, hasil in enumerate(hasil_input):
                        writeHistory += hasil + separation
                        
                    if path_gambar:
                        writeHistory += path_gambar
                    
                    file.write(writeHistory+"\n")
                    #file.write(tanggal + "\n")

                messagebox.showinfo(
                    'Data telah disimpan', f'Property dengan ID {propid_entry.get()} telah ditambahkan ke dalam daftar.', parent=f2)
               
                nama_entry.delete(0, 'end')
                harga_entry.delete(0, 'end')
                propid_entry.delete(0, 'end')
                describ_entry.delete("1.0", 'end')
                date_entry.delete(0, 'end')

                label_gambar.configure(image='')
                label_path.configure(text="Path Gambar: ")
            else:
                messagebox.showerror('Validation', 'Input can\'t be empty!')
                f1.focus()
       
        def tampilkan_history():
            halaman_history = Toplevel(root)

            scrollbar = Scrollbar(halaman_history)
            scrollbar.pack(side=LEFT, fill=Y)

            canvas = Canvas(halaman_history, yscrollcommand=scrollbar.set)
            canvas.pack(side=LEFT, fill=BOTH, expand=True)

            scrollbar.config(command=canvas.yview)

            frame = Frame(canvas)
            canvas.create_window((canvas.winfo_width() / 2, canvas.winfo_height() / 2), window=frame, anchor="center")

            with open("history11.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("Path Gambar"):
                        path_gambar = line.replace("Path Gambar: ", "").strip()
                        img = Image.open(path_gambar) 
                        img.thumbnail((100, 100))
                        img_tk = ImageTk.PhotoImage(img)
                        label_gambar_history = Label(frame, image=img_tk)
                        label_gambar_history.image = img_tk
                        label_gambar_history.pack()
                    else:
                        label_history = Label(frame, text=line)
                        label_history.pack()

            frame.update_idletasks()

            canvas.config(scrollregion=canvas.bbox("all"))

        def get_selected_date():
            selected_date = cal.selection_get()
            today = datetime.today().date()

            if selected_date < today:
                messagebox.showinfo('Warning',f"Tanggal yang anda dipilih sudah lewat")
            else:
                date_entry.delete(0, tk.END)  
                date_entry.insert(0, selected_date) 

        def show_calendar():
            global cal
            top = tk.Toplevel(root)
            cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')
            cal.pack(padx=10, pady=10)
            button = tk.Button(top, text="Pilih", command=get_selected_date)
            button.pack(pady=10)

        def default_home():
            f2=Frame(self.bid_prop)
            f2.place(x=0,y=45)
            l2=Label(f2,text='Home',fg='white',bg='#262626')
            l2.config(font=('Comic Sans MS',90))
            l2.place(x=0,y=45)
            toggle_win()
            home()
            
        def home():
            f1.destroy()
            f22 = Frame(self.bid_prop, width=1000, height=600, bg='#e1ded8')
            f22.place(x=330, y=75)

            l2 = Label(f22, text=f'Welcome back,\n{username}!', fg='white', bg='#393324')
            l2.config(font=('Bookman Old Style', 30))
            l2.place(x=600, y=100)

            image1 = Image.open("b5.png")
            image1 = image1.resize((500, 500), Image.LANCZOS)
            photo1 = ImageTk.PhotoImage(image1)
            label1 = Label(f22, image=photo1)
            label1.image = photo1
            label1.config(background='#e1ded8')
            label1.place(x=90, y=50)

            toggle_win()

        def data():
            f1.destroy()
            global nama_entry, harga_entry, propid_entry, describ_entry, label_gambar, label_path, f2, date_entry
            f2 = Frame(self.bid_prop, width=1000, height=600, bg='white')
            f2.place(x=330, y=75)

            label = Label(f2, text="Daftar Lelang Barang Property",
                          fg='black', bg='white')
            label.config(font=('Bookman Old Style', 20))
            label.place(x=320, y=65-45)

            nama_label = Label(f2, text="Nama Properti :",
                               fg='black', bg='white', font=('Bookman Old Style', 18))
            nama_label.place(x=100, y=90)
            nama_entry = Entry(f2, bg='white', width=100)
            nama_entry.place(x=300, y=100)

            upload = Label(
                f2, text="Gambar :", fg='black', bg='white', font=('Bookman Old Style', 18))
            upload.place(x=100, y=130)

            button = Button(f2, text="Unggah Gambar",
                            command=lambda: browse_gambar(f2))
            button.place(x=100, y=160)
            label_path = Label(f2, text="Path Gambar: ")
            label_path.place(x=300, y=140)
            label_gambar = Label(f2)
            label_gambar.place(x=300, y=160)

            harga_label = Label(f2, text="Harga Mulai :",
                                fg='black', bg='white', font=('Bookman Old Style', 18))
            harga_label.place(x=100, y=200)
            harga_entry = Entry(f2, bg='white', width=100)
            harga_entry.place(x=300, y=210)

            propid_label = Label(f2, text="ID Property :",
                                 fg='black', bg='white', font=('Bookman Old Style', 18))
            propid_label.place(x=100, y=250)
            propid_entry = Entry(f2, bg='white', width=100)
            propid_entry.place(x=300, y=260)

            describ_label = Label(f2, text="Deskripsi :",
                                  fg='black', bg='white', font=('Bookman Old Style', 18))
            describ_label.place(x=100, y=300)
            describ_entry = Text(f2, bg='white', width=75,
                                 height=5, wrap='word')
            describ_entry.place(x=300, y=310)

            label_batas_lelang = Label(f2, text="Batas Lelang:", fg='black', bg='white', font=('Bookman Old Style', 18))
            label_batas_lelang.place(x=100, y=450)

            date_entry = Entry(f2, width=50)
            date_entry.place(x=300, y=450)
            button = Button(f2, text="Pilih Tanggal", command=show_calendar)
            button.place(x=600, y=450)

            tambah_button = Button(f2, text="Input", fg='black', bg='#ddcbb5', font=(
                'Bookman Old Style', 15), command=simpan_hasil)
            tambah_button.place(x=400, y=500)

            back = Button(f2, text="Back", fg='black', bg='#ddcbb5',
                          font=('Bookman Old Style', 15), command=home)
            back.place(x=550, y=500)

            button_history = Button(f2,bg='#ddcbb5', text="Tampilkan History", font=('Bookman Old Style',15), command= tampilkan_history)
            button_history.place(x=650,y=500)

            toggle_win()

        def quit():
            f1.destroy()
            f2=Frame(self.bid_prop,width=1000,height=600,bg='white')
            f2.place(x=330, y=75)
            toggle_win()
            self.show_logged_in_page()

        def toggle_win():
            global f1
            f1=Frame(self.bid_prop,width=300,height=800,bg='#a6a6a6')
            f1.place(x=0,y=0)

            image2 = Image.open("home.png")
            image2 = image2.resize((305, 400), Image.LANCZOS)
            photo2 = ImageTk.PhotoImage(image2)
            label2 = Label(f1, image=photo2)
            label2.image = photo2
            label2.config(background='#a6a6a6')
            label2.place(x=-5,y=350)

            #buttons
            def bttn(x,y,text,bcolor,fcolor,cmd):
            
                def on_entera(e):
                    myButton1['background'] = bcolor 
                    myButton1['foreground']= '#262626'  

                def on_leavea(e):
                    myButton1['background'] = fcolor
                    myButton1['foreground']= '#262626'

                myButton1 = Button(f1,text=text,
                            width=42,
                            height=2,
                            fg='#262626',
                            border=0,
                            bg=fcolor,
                            activeforeground='#262626',
                            activebackground=bcolor,            
                                command=cmd)
                            
                myButton1.bind("<Enter>", on_entera)
                myButton1.bind("<Leave>", on_leavea)

                myButton1.place(x=x,y=y)

            bttn(0,80,'H O M E', '#e1ded8','#a6a6a6',home)
            bttn(0,117,'I N P U T','#e1ded8','#a6a6a6',data)
            bttn(0,154,'Q U I T','#e1ded8','#a6a6a6',quit)

            def dele():
                f1.destroy()
                b2=Button(self.bg_label1,image=img1,
                    command=toggle_win,
                    border=0,
                    bg='#262626',
                    activebackground='#262626')
                b2.place(x=5,y=8)

            global img2
            original_image = Image.open("close1.png")
            resized_image = original_image.resize((40, 40), Image.ANTIALIAS)
            img2= ImageTk.PhotoImage(resized_image)

            Button(f1,
                image=img2,
                border=0,
                command=dele,
                bg='#a6a6a6',
                activebackground='#a6a6a6').place(x=5,y=10)

        default_home()

        openimage = Image.open("open1.png")
        openresize = openimage.resize((40, 40), Image.ANTIALIAS)
        img1= ImageTk.PhotoImage(openresize)

        global b2
        b2=Button(self.bg_label1,image=img1,
            command=toggle_win,
            border=0,
            bg='#a6a6a6',
            activebackground='#a6a6a6')
        b2.place(x=5,y=8)
        self.ll=LinkedList()

    def add_property_to_list(self, nama_entry, propid_entry, describ_entry, harga_entry, date_entry):
        nama = nama_entry.get()
        prop_id = propid_entry.get()
        desc = describ_entry.get("1.0")
        price = harga_entry.get()
        tanggal= date_entry.get()
        new_property = Property(nama, prop_id, desc, price,tanggal)
        self.ll.add_property(new_property)

        nama_entry_var = StringVar()
        propid_entry_var = StringVar()
        describ_entry_var = StringVar()
        harga_entry_var = IntVar()
        date_entry_var = StringVar()

        nama_entry_var.set('')
        propid_entry_var.set('')
        describ_entry_var.set('')
        harga_entry_var.set(0)
        date_entry_var.set('')

        messagebox.showinfo(
            'Data telah disimpan', f'Property dengan ID {prop_id} telah ditambahkan ke dalam daftar.')

        self.seller_page()

    listAuction = []
    selectedPropertyId = ""
    selectedFrameAuction: Frame = Frame

    def format_rupiah(self, amount):
        rupiah = "Rp "
        reversed_amount = str(amount)[::-1]
        formatted_amount = ""

        for i in range(len(reversed_amount)):
            formatted_amount += reversed_amount[i]
            if (i + 1) % 3 == 0 and (i + 1) != len(reversed_amount):
                formatted_amount += "."

        formatted_rupiah = rupiah + formatted_amount[::-1] + ",00"
        return formatted_rupiah

    minBid = 0

    def add_bid(self, bid_entry, date_label):
        bid = bid_entry.get()
        bid_entry.delete(0, END)

        batas_lelang = date_label.cget('text')
        current_time = datetime.now()
        batas_lelang_time = datetime.strptime(batas_lelang, "%Y-%m-%d")
        if current_time > batas_lelang_time:
            messagebox.showinfo("Batas Lelang Terlewati", "Maaf, batas lelang sudah terlewati.")
            return
        else:
            if bid.isdigit() == False:
                messagebox.showerror('Validation', 'Input must be number!')
                return 

            if bid < self.minBid:
                messagebox.showerror(
                    'Validation', 'Input must be higher than minimum bid!')
                return

            with open("bid1.txt", "a") as file:
                file.write(username +
                        ";;" + self.selectedPropertyId + ";;" + bid+"\n")
            messagebox.showinfo(
                'Bid Info', 'Bid berhasil ditambahkan, silakan refresh!')
        
    frameTable: Frame = Frame

    def buyer_page(self):
        global updateBid
        # Menghapus seluruh elemen dalam halaman
        for widget in self.bid_prop.winfo_children():
            widget.destroy()

        buyer_page = self.bid_prop
        buyer_page.configure(bg='#DEB887')

        top_frame = Frame(buyer_page, bg='#A0522D')
        top_frame.pack(side=TOP, fill=X)

      # Load gambar "bid"
        imagebid = Image.open("logo.png")
        imagebid = imagebid.resize((80, 80), Image.ANTIALIAS)
        photobid = ImageTk.PhotoImage(imagebid)

        # Tampilkan gambar "bid"
        labelbid = Label(top_frame, image=photobid, bg='#A0522D')
        labelbid.image = photobid
        labelbid.pack(side=LEFT, padx=20, pady=20)

        def update_time():
            current_time = datetime.now().strftime("%Y-%m-%d \n %H:%M:%S")
            self.time_label.config(text= current_time)
            self.time_update_id =buyer_page.after(1000, update_time)

        self.time_label = Label(top_frame, font=('Bookman Old Style Bold', 12),fg='#ddcbb5', bg='#A0522d')
        self.time_label.pack(side=RIGHT, padx=3, pady=5)
        update_time()

        def linear_search(auctions, keyword, sort_by_price=False):
            result = []
            for auction in auctions:
                auction_name = auction[0]
                if keyword.lower() in auction_name.lower():
                    result.append(auction)

            if sort_by_price:
                result.sort(key=lambda x: x[1])  # Mengurutkan berdasarkan harga properti

            return result
        
        def binary_search(auctions, keyword, sort_by_price=False):
            result = []
            left = 0
            right = len(auctions) - 1

            while left <= right:
                mid = (left + right) // 2
                auction_name = auctions[mid][0]

                if keyword.lower() in auction_name.lower():
                    # Cari ke kiri
                    i = mid
                    while i >= left and keyword.lower() in auctions[i][0].lower():
                        # if auctions[i] not in result:
                        result.append(auctions[i])
                        i -= 1
                    # start = i + 1

                    # Cari ke kanan
                    i = mid + 1
                    while i <= right and keyword.lower() in auctions[i][0].lower():
                        # if auctions[i] not in result:
                        result.append(auctions[i])
                        i += 1
                    # end = i - 1

                if keyword.lower() < auction_name.lower():
                    right = mid - 1
                else:
                    left = mid + 1

            for auction in auctions:
                auction_name = auction[0]
                if keyword.lower() in auction_name.lower() and auction not in result:
                    result.append(auction)

            if sort_by_price:
                result.sort(key=lambda x: x[1])

            return result

        def update_auction_buttons(auctions):
            for btn in buttons_frame.winfo_children():
                btn.destroy()

            btn = []

            for i in range(len(auctions)):
                image_path = auctions[i][6]
                image = Image.open(image_path)
                image = image.resize((150, 150), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                auction_data = auctions[i]
                btn.append(Button(buttons_frame, image=photo, width=195, height=150, relief='flat',
                                command=make_button_click_command(auction_data), bd=0,
                                bg='#DEB887', activebackground='#DEB887'))
                btn[i].image = photo
                btn[i].pack(side=TOP, fill=X, padx=10, pady=10)

                label = Label(buttons_frame, text=auction_data[0], font=('Rockwell bold', 14), bg='#DEB887', fg='white')
                label.pack()

        def search_auction():
            keyword = search_entry.get()
            search_method = search_method_var.get()

            if search_method == 'Linear Search':
                filtered_auctions = linear_search(self.listAuction, keyword, sort_by_price=True)
            else:
                # sorted_auctions = sorted(self.listAuction, key=lambda x: x[1])
                filtered_auctions = binary_search(self.listAuction, keyword, sort_by_price=True)

            update_auction_buttons(filtered_auctions)

            for widget in buttons_frame.winfo_children():
                widget.destroy()

            for i in range(len(filtered_auctions)):
                image_path = filtered_auctions[i][6] 
                image = Image.open(image_path)
                image = image.resize((150, 150), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)
                auction_data = filtered_auctions[i]
                btn[i] = Button(buttons_frame, image=photo, width=195, height=150, relief='flat',
                                command=make_button_click_command(auction_data), bd=0,
                                bg='#DEB887', activebackground='#DEB887')
                btn[i].image = photo
                btn[i].pack(side=TOP, fill=X, padx=10, pady=10)

                label = Label(buttons_frame, text=auction_data[0], font=('Rockwell bold', 14), bg='#DEB887', fg='white')
                label.pack()

        labeltext = Label(top_frame, text="Bidding Property Now!", fg="#ddcbb5", bg="#A0522D", font=("Bookman Old style bold", 20))
        labeltext.pack(side=LEFT)

        search_label = Label(top_frame, bg='#A0522D', font=('Rockwell', 14))
        search_label.pack(side=RIGHT, padx=10)

        search_entry = Entry(top_frame, bg='white', width=20, font=('Helvetica', 14))
        search_entry.pack(side=RIGHT,pady=10)

        search_button = Button(top_frame, text='search',bg='#ddcbb5', command= search_auction)
        search_button.pack(side=RIGHT, padx=10)# Tambahkan ComboBox

        search_method_var = StringVar()
        search_method_combobox = ttk.Combobox(top_frame, textvariable=search_method_var)
        search_method_combobox['values'] = ('Linear Search', 'Binary Search')
        search_method_combobox.current(0)  # Atur pilihan default
        search_method_combobox.pack(side=RIGHT, padx=10)


        with open("history11.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.replace("\n", "")
                splitLines = line.split(";;")
                self.listAuction.append(splitLines)


        canvas = Canvas(buyer_page, bg='#ddcbb5', highlightthickness=0)
        canvas.pack(side='right', fill='both', expand=True, padx=0, pady=0)  


        auctionFrame = Frame(buyer_page, bg='#ddcbb5')
        auctionFrame.place(x=250, y=125)
        image = Image.open("1.jpg")
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)

        newPhoto_label = Label(auctionFrame, image=photo)

        newPhoto_label.pack(side=TOP)
        title_label = Label(auctionFrame, text="PropertyName",fg='black', bg='#ddcbb5',
                            font=("Bookman old style", 25, "bold"), wraplength=400)

        title_label.pack(side=TOP, pady=10)
        price_label = Label(auctionFrame, text="Start from " + self.format_rupiah(0),fg='black',bg='#ddcbb5',
                            font=("Bookman old style", 15, "bold"), wraplength=400)
        price_label.pack(side=TOP)
        user_label = Label(auctionFrame, text="Seller",fg='black',bg='#ddcbb5',
                            font=("Bookman old style", 15, "bold"), wraplength=400)
        user_label.pack(side=TOP)
        desc_label = Label(auctionFrame,text='Deskripsi',fg='black', bg='#ddcbb5',
                        font=("Bookman old style", 12), wraplength=400, justify="left")
        desc_label.pack(side=TOP)
        date_label = Label(auctionFrame, text="Batas Lelang",fg='black', bg='#ddcbb5',
                        font=("Bookman old style", 12), wraplength=400, justify="left")
        date_label.pack(side=TOP)
        harga_label = Label(auctionFrame,
                            fg='black',text= 'Masukkan Bid:', bg='#ddcbb5', font=('Bookman old style', 18))
        harga_label.pack(side=TOP)
        
        harga_entry = Entry(auctionFrame,bd=1, bg='#ddcbb5', width=30, font=('Rockwell', 16))
        harga_entry.pack(side=TOP, pady=10, padx=10)
        bid_btn = Button(auctionFrame, text='Bid Now!', bg='#a0522d', fg='white', font=(
            "Rockwell", 16, "bold"), command=lambda: self.add_bid(harga_entry, date_label))
        bid_btn.pack(side=TOP)
        back_btn = Button(auctionFrame, text='Back', bg='#a0522d', fg='white', font=(
            "Rockwell", 16, "bold"), command=self.show_logged_in_page)
        back_btn.pack(side=TOP) 
        
        def display_winner(auction):

            highest_bid = 0
            winner = ""
            with open("bid1.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    splitLines = line.split(";;")
                    if splitLines[1] == self.selectedPropertyId:
                        bid = int(splitLines[2])
                        if bid > highest_bid:
                            highest_bid = bid
                            winner = splitLines[0]
         
            if username == winner:
                messagebox.showinfo("Pembayaran", "Anda adalah pemenang lelang. Lakukan pembayaran.")
                self.pay_winner()

            else:
                messagebox.showinfo("Pembayaran", "Anda bukan pemenang lelang. Tidak dapat melakukan pembayaran.")

        def updateAuction(auction):
            newFrame.destroy()
            [propertyName, propertyPrice, propertyId,
                propertyDesc,propertytgl,propertyuser,propertyImg] = auction
            self.selectedPropertyId = propertyId
            title_label.config(text=propertyName)
            price_label.config(text=self.format_rupiah(propertyPrice))
            desc_label.config(text=propertyDesc)
            date_label.config(text=propertytgl)
            user_label.config(text=propertyuser)
            image = Image.open(propertyImg)
            print(propertyImg)
            image.thumbnail((150, 150))
            photo = ImageTk.PhotoImage(image)
            newPhoto_label.configure(image=photo)
            newPhoto_label.image = photo
            self.minBid = propertyPrice
            updateBid(propertyId)

        btn = {}
        def make_button_click_command(auction):
            return lambda: updateAuction(auction)

        scrollbar = Scrollbar(buyer_page, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='left', fill='y')

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        buttons_frame = Frame(canvas, bg='#DEB887')
        canvas.create_window((0, 0), window=buttons_frame, anchor='nw')
        canvas.configure(scrollregion=canvas.bbox('all'))

        def updateBid(propertyId):
            listBid = []
            with open("bid1.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.replace("\n", "")
                    splitLines = line.split(";;")
                    if splitLines[1] == propertyId:
                        listBid.append(splitLines)
            refetchTable(listBid)

        def refetchTable(listBid):
            lst = []
            i = 1
            for bidDetails in listBid:
                [username, _, bid] = bidDetails
                lst.append([i, username, int(bid)])
                i += 1

            self.frameTable = Frame(buyer_page, bg='#ddcbb5', bd=5)
            self.frameTable.place(x=750, y=150, relwidth=0.5, relheight=0.8)

            total_rows = len(lst)
            if total_rows != 0:
                lst = comb_sort_descending(lst)
                linkedData = LinkedList()

                for i in range(len(lst)):
                    linkedData.add(i+1)
                    linkedData.add(lst[i][1]) 
                    linkedData.add(lst[i][2])

                total_columns = len(lst[0])
                for i in range(total_rows):
                    for j in range(total_columns):
                        self.e = Entry(self.frameTable, width=15, fg='blue',
                                    font=('Arial', 16, 'bold'))
                        self.e.grid(row=i, column=j)
                        value = linkedData.pop() 
                        self.e.insert(END, value)
                        self.e.config(state="disabled")
            else:
                self.e = Entry(self.frameTable, width=50, fg='blue',
                            font=('Arial', 16, 'bold'))
                self.e.grid(row=0, column=0)
                self.e.insert(END, "Data Kosong")
                self.e.config(state="disabled")


        def comb_sort_descending(arr):
            n = len(arr)
            gap = n
            shrink = 1.3
            sorted = False

            while not sorted:
                gap = int(gap / shrink)
                if gap <= 1:
                    gap = 1
                    sorted = True
                    
                i = 0
                while i + gap < n:
                    if arr[i][2] < arr[i + gap][2]:
                        arr[i], arr[i + gap] = arr[i + gap], arr[i]
                        sorted = False
                    i += 1

            return arr

        def make_button_click_command(auction):
            return lambda: updateAuction(auction)

        for i in range(len(self.listAuction)):
            image_path = self.listAuction[i][6] 
            image = Image.open(image_path)
            image = image.resize((150, 150), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            auction_data = self.listAuction[i]
            btn[i] = Button(buttons_frame, image=photo, width=195, height=150, relief='flat',
                            command=make_button_click_command(auction_data), bd=0,
                            bg='#DEB887', activebackground='#DEB887')
            btn[i].image = photo
            btn[i].pack(side=TOP, fill=X, padx=10, pady=10)

            label = Label(buttons_frame, text=auction_data[0], font= ('Bookman Old Style Bold',14), bg='#DEB887', fg='white')  # Menggunakan indeks 6 sebagai contoh, sesuaikan dengan indeks data nama pada listAuction Anda
            label.pack()

        winner_button = Button(auctionFrame, text="Tampilkan Pemenang", bg='#a0522d', fg='white', font=(
            "Rockwell", 16, "bold"), command=lambda a=auction_data: display_winner(a))
        winner_button.pack(side=TOP)

        newFrame = Frame(auctionFrame, bg='#ddcbb5')
        newFrame.place(x=0, y=0)
        newFrame.config(width=500, height=700)

        image3 = Image.open("buyer.jpg")
        image3 = image3.resize((420, 630), Image.LANCZOS)
        photo3 = ImageTk.PhotoImage(image3)
        label3 = Label(newFrame, image=photo3)
        label3.image = photo3
        label3.config(background='#ddcbb5')
        label3.place(x=0,y=0)

    def pay_winner(self):
        for widget in self.bid_prop.winfo_children():
            widget.destroy()

        bg_image = Image.open("pay.png")
        
        bg_image = bg_image.resize((1366, 768), Image.LANCZOS)
        self.bg_image_tk = ImageTk.PhotoImage(bg_image)
        pay_page = Label(self.bid_prop, image=self.bg_image_tk)
        pay_page.place(x=0, y=0, relwidth=1, relheight=1)
        pay_page.pack(fill='both', expand=True)

        def on_entry_focus_in(event):
            if entry_account_number.get() == "Enter account number":
                entry_account_number.delete(0, tk.END)
                entry_account_number.config(fg='black')

        def on_entry_focus_out(event):
            if entry_account_number.get() == "":
                entry_account_number.insert(0, "Enter account number")
                entry_account_number.config(fg='grey')

        entry_account_number = Entry(pay_page, width=20, bg='#c99a5b', bd=0, font=50,fg='white')
        entry_account_number.insert(0, "Enter account number")
        entry_account_number.bind("<FocusIn>", on_entry_focus_in)
        entry_account_number.bind("<FocusOut>", on_entry_focus_out)
        entry_account_number.pack()
        entry_account_number.place(x=100,y=560)

        def on_pay_button_click():
            if self.time_update_id is not None:
                # Hentikan pembaruan waktu jika ada
                pay_page.after_cancel(self.time_update_id)
                self.time_update_id = None
        
            barcode_image = ImageTk.PhotoImage(Image.open("barcode.png"))
            barcode_label = Label(pay_page, image=barcode_image)
            barcode_label.image = barcode_image 
            barcode_label.place(x=860,y=220)

        self.button_pay = Button(pay_page, text="send",bg='#c99a5b',fg='white', command=on_pay_button_click)
        self.button_pay.place(x=400,y=555)


root=Tk()
bid_prop = BidProp(root)
root.mainloop()