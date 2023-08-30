from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from interest import *
from bank_comparison import *

root = Tk()
root.resizable(False, False)

root.title("DreamSavers 1.0")
root.geometry("854x480")
root.iconbitmap("Assets\icon.ico")

timedep_time = IntVar()
simple_time = IntVar()
mode = StringVar()

def simple_page():
    home_nav.configure(fg="#000000")
    simple_nav.configure(fg="#FFFFFF")
    timedep_nav.configure(fg="#000000")
    bankinfo_nav.configure(fg="#000000")
    about_nav.configure(fg="#000000")
    simple_frame = Frame(root)
    simple_frame.place(relx=0.164, rely=0)
    simple_frame.configure(width=714, height=480)

    global simple_bg

    simple = Image.open("Assets\coins.jpg")
    resized_simple = simple.resize((854, 480), Image.ANTIALIAS)
    simple_bg = ImageTk.PhotoImage(resized_simple)

    sim_bg = Label(simple_frame, image=simple_bg).place(x=-2, y=-2)
    
    def bank_selection(event):
        bdo_logo = Label()
        bpi_logo = Label()
        pnb_logo = Label()
        noBank_img = Label()
        custom_img = Label()
        if clicked.get() == "Select a Bank":
            rate_value.delete(0, 'end')
            noBank_img = Label(image=noBank_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'BDO':
            rate_value.delete(0, 'end')
            rate_value.insert(0, "0.0625")
            bdo_logo = Label(image=bdo_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'Landbank':
            rate_value.delete(0, 'end')
            rate_value.insert(0,"0.05")
            bpi_logo = Label(image=bpi_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'PNB':
            rate_value.delete(0, 'end')
            rate_value.insert(0,"0.1")
            pnb_logo = Label(image=pnb_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'Custom':
            rate_value.delete(0,'end')
            custom_logo = Label(image=custom_image, width=150, height=150).place(relx=0.735, rely=0.05)

    def compute():
        result.delete(1.0, END)
        computation = str()
        if rate_value.get() != '' and deposit_value.get() != '' and time_value.get() != '' and simple_time.get() == 0:
            try:
                interest_rate = float(rate_value.get())
                interest_rate = interest_rate/100
                deposit = float(deposit_value.get())
                time = int(time_value.get())
                if clicked.get() == 'Select a Bank':
                    computation = "Computation Error: Please Select A Bank"
                elif clicked.get() == 'BDO' and deposit >= 2000:
                    computation = simple_interest(deposit, interest_rate, time, time_unit="years", bank="BDO", comparison=False)
                elif clicked.get() == 'Landbank' and deposit >= 5000:
                    computation = simple_interest(deposit, interest_rate, time, time_unit="years", bank="Landbank", comparison=False)
                elif clicked.get() == 'PNB' and deposit >= 3000:
                    computation = simple_interest(deposit, interest_rate, time, time_unit="years", bank="PNB", comparison=False)
                elif clicked.get() == 'Custom':
                    computation = simple_interest(deposit, interest_rate, time, time_unit="years", bank="Custom", comparison=False)
                else:
                    computation = "Deposit Value is low. Please see Bank Information"
            except ValueError:
                computation = "Computation Error: Invalid Input"

        elif rate_value.get() != '' and deposit_value.get() != '' and time_value.get() != '' and simple_time.get() == 1:
            try:
                interest_rate = float(rate_value.get())
                interest_rate = interest_rate/100
                deposit = float(deposit_value.get())
                time = int(time_value.get())
                if clicked.get() == 'Select a Bank':
                    computation = "Computation Error: Please Select A Bank"
                elif clicked.get() == 'BDO' and deposit >= 2000:
                    computation = simple_interest(deposit, interest_rate, time, time_unit="months", bank="BDO", comparison=False)
                elif clicked.get() == 'Landbank' and deposit >= 5000:
                    computation = simple_interest(deposit, interest_rate, time, time_unit="months", bank="Landbank", comparison=False)
                elif clicked.get() == 'PNB' and deposit >= 3000:
                    computation = simple_interest(deposit, interest_rate, time, time_unit="months", bank="PNB", comparison=False)
                elif clicked.get() == 'Custom':
                    computation = simple_interest(deposit, interest_rate, time, time_unit="months", bank="Custom", comparison=False)
                else:
                    computation = "Deposit Value is low. Please see Bank Information"

            except ValueError:
                computation = "Computation Error: Invalid Input"

        else:
            computation = "Computation Error: One or more fields are missing!"

        result.insert(INSERT, computation)

    def compare():
        result.delete(1.0, END)
        com = str()
        if rate_value.get() != '' and deposit_value.get() != '' and time_value.get() != '' and simple_time.get() == 0:
            try:
                interest_rate = float(rate_value.get())
                interest_rate = interest_rate/100
                deposit = float(deposit_value.get())
                time = int(time_value.get())
                if clicked.get() == 'Custom':
                    com = compare_simple_banks(deposit, interest_rate, time, time_unit="years", custom=True)
                else:
                    com = compare_simple_banks(deposit, interest_rate, time, time_unit="years", custom=False)
            except ValueError:
                com = "Computation Error: Invalid Input"

        elif rate_value.get() != '' and deposit_value.get() != '' and time_value.get() != '' and simple_time.get() == 1:
            try:
                interest_rate = float(rate_value.get())
                interest_rate = interest_rate/100
                deposit = float(deposit_value.get())
                time = int(time_value.get())
                if clicked.get() == 'Custom':
                    com = compare_simple_banks(deposit, interest_rate, time, time_unit="months", custom=True)
                else:
                    com = compare_simple_banks(deposit, interest_rate, time, time_unit="months", custom=False)
            
            except ValueError:
                com = "Computation Error: Invalid Input"

        else:
            com = "Computation Error: One or more fields are missing!"

        result.insert(INSERT, com)

    def save_result():
        file = filedialog.asksaveasfile(defaultextension='.txt', title="Save Result", filetypes=[
            ("Text File", ".txt")
        ])
        filetext = str(result.get(1.0, END))
        file.write(filetext)
        file.close()

    def load_result():
        file = filedialog.askopenfilename(initialdir="", title="Load Existing Log", filetypes=[
            ("Text File", ".txt")
        ])
        file = open(file, 'r')
        content = file.read()
        result.delete(1.0, END)
        result.insert(INSERT, content)
        file.close()

    choose = Label(simple_frame, text="Choose a Bank: ")
    deposit = Label(simple_frame, text="Deposit: ")
    rate = Label(simple_frame, text="Rate: ")
    time = Label(simple_frame, text="Time: ")
    percentage = Label(simple_frame, text="%").place(relx=0.26, rely=0.19)

    deposit_value = Entry(simple_frame, width=10, borderwidth=2)
    rate_value = Entry(simple_frame, width=10, borderwidth=2)
    time_value = Entry(simple_frame, width=7, borderwidth=2)

    year = Radiobutton(simple_frame, text="Years", variable=simple_time, value=0)
    months = Radiobutton(simple_frame, text="Months", variable=simple_time, value=1)

    result = Text(simple_frame, width=77, height=15, borderwidth=3)

    load = Button(simple_frame, text="Load Result", command=load_result)
    save = Button(simple_frame, text="Save Result", command=save_result)
    compare = Button(simple_frame, text="Compare", command=compare)
    compute = Button(simple_frame, text="Compute", command=compute)

    noBank_image = (Image.open("Assets\selection_none.png"))
    custom_image = (Image.open("Assets\custom.png"))
    bdo_image = (Image.open("Assets\logo1.jpeg"))
    bpi_image = (Image.open("Assets\logo2.jpg"))
    pnb_image = (Image.open("Assets\pnb.png"))

    resized_noBank_image = noBank_image.resize((150,150), Image.ANTIALIAS)
    resized_custom_image = custom_image.resize((150,150), Image.ANTIALIAS)
    resized_bdo_image = bdo_image.resize((150,150), Image.ANTIALIAS)
    resized_bpi_image = bpi_image.resize((150,150), Image.ANTIALIAS)
    resized_pnb_image = pnb_image.resize((150,150), Image.ANTIALIAS)

    noBank_image = ImageTk.PhotoImage(resized_noBank_image)
    custom_image = ImageTk.PhotoImage(resized_custom_image)
    bdo_image = ImageTk.PhotoImage(resized_bdo_image)
    bpi_image = ImageTk.PhotoImage(resized_bpi_image)
    pnb_image = ImageTk.PhotoImage(resized_pnb_image)

    bank_options = ["Select a Bank", "BDO", "Landbank", "PNB", "Custom"]
    clicked = StringVar()
    clicked.set(bank_options[0])

    noBank_img = Label(image=noBank_image, width=150, height=150).place(relx=0.735, rely=0.05)
    bank_drop = OptionMenu(simple_frame, clicked, *bank_options, command=bank_selection)

    bank_drop.place(relx=0.17,rely=0.05)
    choose.place(relx=0.03,rely=0.063)
    deposit.place(relx=0.03, rely=0.14)
    deposit_value.place(relx=0.17, rely=0.135)
    rate.place(relx=0.03, rely=0.19)
    rate_value.place(relx=0.17, rely=0.19)
    result.place(relx=0.03, rely=0.4)
    time.place(relx=0.03, rely=0.246)
    year.place(relx=0.162,rely=0.244)
    months.place(relx=0.25,rely=0.244)
    time_value.place(relx=0.17,rely=0.3)
    compute.place(relx=0.17, rely=0.34)
    save.place(relx=0.03, rely=0.92)
    compare.place(relx=0.43, rely=0.92)
    load.place(relx=0.802, rely=0.92)

def timedeposit_page():
    home_nav.configure(fg="#000000")
    simple_nav.configure(fg="#000000")
    timedep_nav.configure(fg="#FFFFFF")
    bankinfo_nav.configure(fg="#000000")
    about_nav.configure(fg="#000000")
    time_dep_frame = Frame(root)
    time_dep_frame.place(relx=0.164, rely=0)
    time_dep_frame.configure(width=714, height=480)
    
    global time_dep_bg

    time_bg = Image.open("Assets\dep.jpg")
    resized_time_bg = time_bg.resize((854, 480), Image.ANTIALIAS)
    time_dep_bg = ImageTk.PhotoImage(resized_time_bg)

    background = Label(time_dep_frame, image=time_dep_bg).place(x=-2, y=-2)

    def bank_selection(event):
        bdo_logo = Label()
        bpi_logo = Label()
        pnb_logo = Label()
        noBank_img = Label()
        custom_img = Label()
        if clicked.get() == "Select a Bank":
            rate_value.delete(0, 'end')
            noBank_img = Label(image=noBank_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'BDO':
            rate_value.delete(0, 'end')
            bdo_logo = Label(image=bdo_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'Landbank':
            rate_value.delete(0, 'end')
            bpi_logo = Label(image=bpi_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'PNB':
            rate_value.delete(0, 'end')
            pnb_logo = Label(image=pnb_image, width=150, height=150).place(relx=0.735, rely=0.05)
        elif clicked.get() == 'Custom':
            rate_value.delete(0, 'end')
            custom_img = Label(image=custom_image, width=150, height=150).place(relx=0.735, rely=0.05)
 
    def compute():
        result.delete(1.0, END)
        time_computation = str()
        if deposit_value.get() != '' and timedep_time.get() == 0:
            try:
                deposit = float(deposit_value.get())
                if deposit >= 1000:
                    if clicked.get() == 'Select a Bank':
                        time_computation = "Computation Error: Please select a bank!"
                    elif clicked.get() == 'BDO':
                        time_computation = bdo_time_deposit(deposit, term=30, comparison=False)
                    elif clicked.get() == 'Landbank':
                        time_computation = landbank_time_deposit(deposit, term=30, comparison=False)
                    elif clicked.get() == 'PNB':
                        time_computation = pnb_time_deposit(deposit, term=30, comparison=False)
                    elif clicked.get() == 'Custom':
                        interest = float(rate_value.get())
                        interest = interest/100
                        time_computation = custom_time_deposit(deposit, interest, term=30, comparison=False)
                else:
                    time_computation = "Deposit Value is low. Please see bank information"

            except ValueError:
                time_computation = "Computation Error: Invalid Input"

        elif deposit_value.get() != '' and timedep_time.get() == 1:
            try:
                deposit = float(deposit_value.get())
                if deposit >= 1000:
                    if clicked.get() == 'Select a Bank':
                        time_computation = "Computation Error: Please select a bank!"
                    elif clicked.get() == 'BDO':
                        time_computation = bdo_time_deposit(deposit, term=180, comparison=False)
                    elif clicked.get() == 'Landbank':
                        time_computation = landbank_time_deposit(deposit, term=180, comparison=False)
                    elif clicked.get() == 'PNB':
                        time_computation = pnb_time_deposit(deposit, term=180, comparison=False)
                    elif clicked.get() == 'Custom':
                        interest = float(rate_value.get())
                        interest = interest/100
                        time_computation = custom_time_deposit(deposit, interest, term=180, comparison=False)
                else:
                    time_computation = "Deposit Value is low. Please see bank information"

            except ValueError:
                time_computation = "Computation Error: Invalid Input"

        elif deposit_value.get() != '' and timedep_time.get() == 2:
            try:
                deposit = float(deposit_value.get())
                if deposit >= 1000:
                    if clicked.get() == 'Select a Bank':
                        time_computation = "Computation Error: Please select a bank!"
                    elif clicked.get() == 'BDO':
                        time_computation = bdo_time_deposit(deposit, term=360, comparison=False)
                    elif clicked.get() == 'Landbank':
                        time_computation = landbank_time_deposit(deposit, term=360, comparison=False)
                    elif clicked.get() == 'PNB':
                        time_computation = pnb_time_deposit(deposit, term=360, comparison=False)
                    elif clicked.get() == 'Custom':
                        interest = float(rate_value.get())
                        interest = interest/100
                        time_computation = custom_time_deposit(deposit, interest, term=360, comparison=False)
                else:
                    time_computation = "Deposit Value is low. Please see bank information"
            except ValueError:
                time_computation = "Computation Error: Invalid Input"
        
        else:
            time_computation = "Computation Error: One or more fields are missing!"

        result.insert(INSERT, time_computation)

    def compare():
        result.delete(1.0, END)
        com = str()
        if deposit_value.get() != '' and timedep_time.get() == 0:
            try:
                deposit = float(deposit_value.get())
                if clicked.get() == 'Custom':
                    interest = float(rate_value.get())
                    interest = interest/100
                    com = compare_timedep_banks_custom(deposit, interest, 30)
                else:
                    com = compare_timedep_banks(deposit, 30)

            except ValueError:
                com = "Computation Error: Invalid Input"

        elif deposit_value.get() != '' and timedep_time.get() == 1:
            try:
                deposit = float(deposit_value.get())
                if clicked.get() == 'Custom':
                    interest = float(rate_value.get())
                    interest = interest/100
                    com = compare_timedep_banks_custom(deposit, interest, 180)
                else:
                    com = compare_timedep_banks(deposit, 180)

            except ValueError:
                com = "Computation Error: Invalid Input"

        elif deposit_value.get() != '' and timedep_time.get() == 2:
            try:
                deposit = float(deposit_value.get())
                if clicked.get() == 'Custom':
                    interest = float(rate_value.get())
                    interest = interest/100
                    com = compare_timedep_banks_custom(deposit, interest, 360)
                else:
                    com = compare_timedep_banks(deposit, 360)
        
            except ValueError:
                com = "Computation Error: Invalid Input"
        
        else:
            com = "Computation Error: One or more fields are missing!"

        result.insert(INSERT, com)

    def save_result():
        file = filedialog.asksaveasfile(defaultextension='.txt', title="Save Result", filetypes=[
            ("Text File", ".txt")
        ])
        filetext = str(result.get(1.0, END))
        file.write(filetext)
        file.close()

    def load_result():
        file = filedialog.askopenfilename(initialdir="", title="Load Existing Log", filetypes=[
            ("Text File", ".txt")
        ])
        file = open(file, 'r')
        content = file.read()
        result.delete(1.0, END)
        result.insert(INSERT, content)
        file.close()

    choose = Label(time_dep_frame, text="Choose a Bank: ")
    deposit = Label(time_dep_frame, text="Deposit: ")
    tenure = Label(time_dep_frame, text="Tenure: ")
    rate_value = Entry(time_dep_frame, width=10, borderwidth=2)
    rate = Label(time_dep_frame, text="Rate: ")
    percentage = Label(time_dep_frame, text="% (Input rate if you chose custom)").place(relx=0.26, rely=0.19)

    deposit_value = Entry(time_dep_frame, width=10, borderwidth=2)
    rate_value = Entry(time_dep_frame, width=10, borderwidth=2)

    monthly = Radiobutton(time_dep_frame, text="30", variable=timedep_time, value=0)
    semi_annually = Radiobutton(time_dep_frame, text="180", variable=timedep_time, value=1)
    annually = Radiobutton(time_dep_frame, text="360", variable=timedep_time, value=2)

    result = Text(time_dep_frame, width=77, height=15, borderwidth=3)

    load = Button(time_dep_frame, text="Load Result", command=load_result)
    save = Button(time_dep_frame, text="Save Result", command=save_result)
    compare = Button(time_dep_frame, text="Compare", command=compare)
    compute = Button(time_dep_frame, text="Compute", command=compute)

    noBank_image = (Image.open("Assets\selection_none.png"))
    custom_image = (Image.open("Assets\custom.png"))
    bdo_image = (Image.open("Assets\logo1.jpeg"))
    bpi_image = (Image.open("Assets\logo2.jpg"))
    pnb_image = (Image.open("Assets\pnb.png"))

    resized_noBank_image = noBank_image.resize((150,150), Image.ANTIALIAS)
    resized_custom_image = custom_image.resize((150,150), Image.ANTIALIAS)
    resized_bdo_image = bdo_image.resize((150,150), Image.ANTIALIAS)
    resized_bpi_image = bpi_image.resize((150,150), Image.ANTIALIAS)
    resized_pnb_image = pnb_image.resize((150,150), Image.ANTIALIAS)

    noBank_image = ImageTk.PhotoImage(resized_noBank_image)
    custom_image = ImageTk.PhotoImage(resized_custom_image)
    bdo_image = ImageTk.PhotoImage(resized_bdo_image)
    bpi_image = ImageTk.PhotoImage(resized_bpi_image)
    pnb_image = ImageTk.PhotoImage(resized_pnb_image)

    bank_options = ["Select a Bank", "BDO", "Landbank", "PNB", "Custom"]
    clicked = StringVar()
    clicked.set(bank_options[0])

    noBank_img = Label(image=noBank_image, width=150, height=150).place(relx=0.735, rely=0.05)
    bank_drop = OptionMenu(time_dep_frame, clicked, *bank_options, command=bank_selection)

    bank_drop.place(relx=0.17,rely=0.05)
    choose.place(relx=0.03,rely=0.063)
    deposit.place(relx=0.03, rely=0.14)
    deposit_value.place(relx=0.17, rely=0.135)
    result.place(relx=0.03, rely=0.4)
    rate.place(relx=0.03, rely=0.19)
    rate_value.place(relx=0.17, rely=0.19)
    tenure.place(relx=0.03, rely=0.246)
    monthly.place(relx=0.165,rely=0.244)
    semi_annually.place(relx=0.22,rely=0.244)
    annually.place(relx=0.285,rely=0.244)
    compute.place(relx=0.17, rely=0.34)
    save.place(relx=0.03, rely=0.92)
    compare.place(relx=0.43, rely=0.92)
    load.place(relx=0.802, rely=0.92)


def bank_info_page():
    home_nav.configure(fg="#000000")
    simple_nav.configure(fg="#000000")
    timedep_nav.configure(fg="#000000")
    bankinfo_nav.configure(fg="#FFFFFF")
    about_nav.configure(fg="#000000")
    bank_info_frame = Frame(root)
    bank_info_frame.place(relx=0.164, rely=0)
    bank_info_frame.configure(width=714, height=480)
    
    global bank_info_bg

    bank = Image.open("Assets\info_bank_bg.jpg")
    resized_bank = bank.resize((854, 480), Image.ANTIALIAS)
    bank_info_bg = ImageTk.PhotoImage(resized_bank)

    banking = Label(bank_info_frame, image=bank_info_bg).place(x=-2, y=-2)

    bank_info = Label(bank_info_frame, text="", bg="#FFD700")

    def bank_selection(event):
        if clicked.get() == 'BDO':
            logo.configure(image=bdo_image, width=150, height=150)
            logo.place(x=430, y=100)
            bank_info.configure(text=display_bank_info(1), bg="#FFD700", fg="#000000")
            bank_info.place(x=230, y=260)
        elif clicked.get() == 'Landbank':
            logo.configure(image=bpi_image, width=150, height=150)
            logo.place(x=430, y=100)
            bank_info.configure(text=display_bank_info(2), bg="#00FF00", fg="#000000")
            bank_info.place(x=230, y=260)
        elif clicked.get() == 'PNB':
            logo.configure(image=pnb_image, width=150, height=150)
            logo.place(x=430, y=100)
            bank_info.configure(text=display_bank_info(3), bg="#000080", fg="#FFFFFF")
            bank_info.place(x=230, y=260)
    
    bdo_image = (Image.open("Assets\logo1.jpeg"))
    bpi_image = (Image.open("Assets\logo2.jpg"))
    pnb_image = (Image.open("Assets\pnb.png"))

    resized_bdo_image = bdo_image.resize((150,150), Image.ANTIALIAS)
    resized_bpi_image = bpi_image.resize((150,150), Image.ANTIALIAS)
    resized_pnb_image = pnb_image.resize((150,150), Image.ANTIALIAS)

    bdo_image = ImageTk.PhotoImage(resized_bdo_image)
    bpi_image = ImageTk.PhotoImage(resized_bpi_image)
    pnb_image = ImageTk.PhotoImage(resized_pnb_image)

    logo = Label(image="", width=150, height=150)

    bank_options = ["BDO", "Landbank", "PNB"]
    clicked = StringVar()
    clicked.set(bank_options[0])

    bank_drop = OptionMenu(bank_info_frame, clicked, *bank_options, command=bank_selection)

    logo.configure(image=bdo_image, width=150, height=150)
    logo.place(x=430, y=100)
    bank_info.configure(text=display_bank_info(1))
    bank_info.place(x=230, y=260)

    bank_drop.place(x=330,y=30)


def about_page():
    home_nav.configure(fg="#000000")
    simple_nav.configure(fg="#000000")
    timedep_nav.configure(fg="#000000")
    bankinfo_nav.configure(fg="#000000")
    about_nav.configure(fg="#FFFFFF")
    about_frame = Frame(root)
    about_frame.place(relx=0.164, rely=0)
    about_frame.configure(width=714, height=480)

    global d_pic, about_bg_pic

    developer_pic = Image.open("Assets\devs.jpg")
    about_bg = Image.open("Assets\code.jpg")
    resized_developer_pic = developer_pic.resize((300,240), Image.ANTIALIAS)
    resized_about_bg = about_bg.resize((854,480), Image.ANTIALIAS)
    about_bg_pic = ImageTk.PhotoImage(resized_about_bg)
    d_pic = ImageTk.PhotoImage(resized_developer_pic)

    about_background = Label(about_frame, image=about_bg_pic).place(x=-2, y=-2)
    title = Label(about_frame, text="This Program was Developed By: ", font=("Segoe UI", 16, "bold")).place(x=205, y=10)
    dev_pic = Label(about_frame, image=d_pic, width=300, height=240).place(x=214,y=60)
    names = Label(about_frame, text="""Raphael Karlo Santiago
Emmanuel Alviar
Isaiah Miranda""", font=("Segoe UI", 12)).place(x=284, y=320)


def home_page():
    home_nav.configure(fg="#FFFFFF")
    simple_nav.configure(fg="#000000")
    timedep_nav.configure(fg="#000000")
    bankinfo_nav.configure(fg="#000000")
    about_nav.configure(fg="#000000")
    home_frame = Frame(root)
    home_frame.place(relx=0.164, rely=0)
    home_frame.configure(width=714, height=480)

    global new_bg, logo

    bg = Image.open("Assets\ground.jpg")
    resized_bg = bg.resize((864,480), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized_bg)

    logo_open = Image.open("Assets\Logo.png")
    resized_logo = logo_open.resize((200, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_logo)

    background = Label(home_frame, image=new_bg).place(x=-2, y=-2)
    logo_label = Label(home_frame, image=logo).place(x=270, y=125)
    welcome = Label(home_frame, text="Welcome To", font=('Calibri Light', 24)).place(x=290, y=60)
    subtitle = Label(home_frame, text="A LBYCPA1 Final Project", font=('Calibri Light', 16)).place(x=270, y=360)
    quote = Label(home_frame, text="Invest in the bank today for a fruitful future tomorrow.", font=('Calibri Light', 16)).place(x=140, y=400)

nav_frame = Frame(root, bg='#7dca5c')
nav_frame.place(relx=0, rely=0)
nav_frame.configure(width=140,height=480)

program_name = Label(nav_frame, bg='#7dca5c', text="DreamSavers", font=('Calibri Light', 12, 'bold')).place(x=18, y=10)
home_nav = Button(nav_frame, bg='#7dca5c', bd=0, text="Home", font=('Bold', 11), command=home_page)
home_nav.place(x=44, y=80)
simple_nav = Button(nav_frame, bg='#7dca5c', bd=0, text="Simple Interest", font=('Bold', 11), command=simple_page)
simple_nav.place(x=16, y=120)
timedep_nav = Button(nav_frame, bg='#7dca5c', bd=0, text="Time Deposit", font=('Bold', 11), command=timedeposit_page)
timedep_nav.place(x=21, y=160)
bankinfo_nav = Button(nav_frame, bg='#7dca5c', bd=0, text="Bank Information", font=('Bold', 11), command=bank_info_page)
bankinfo_nav.place(x=11, y=200)
about_nav = Button(nav_frame, bg='#7dca5c', bd=0, text="About", font=('Bold', 11), command=about_page)
about_nav.place(x=45, y=240)

home_page()

root.mainloop()