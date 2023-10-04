from tkinter import *
import csv
from tkinter import messagebox

phonelist = []
def ReadCSVFile():
	global header
	with open('StudentData.csv') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		header = next(csv_reader)
		for row in csv_reader:
			phonelist.append(row)
	set_select()		
	print(phonelist)

def WriteInCSVFile(phonelist):
	with open('StudentData.csv','w',newline='') as csv_file:
		writeobj = csv.writer(csv_file,delimiter=',')
		writeobj.writerow(header)
		for row in phonelist:
			writeobj.writerow(row)


def WhichSelected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
		


def AddDetail():
	if E_name.get()!="" and E_last_name.get()!="" and E_contact.get()!="":
		phonelist.append([E_name.get()+' '+E_last_name.get(),E_contact.get()])
		print(phonelist)
		WriteInCSVFile(phonelist)
		set_select()
		EntryReset()
		messagebox.showinfo("Confermation", "Succesfully Add New Contact")
		
	else:
		messagebox.showerror("Error", "Please fill the information")

def UpdateDetail():
	if E_name.get() and E_last_name.get() and E_contact.get():
		phonelist[WhichSelected()] = [ E_name.get()+' '+E_last_name.get(), E_contact.get()]
		WriteInCSVFile(phonelist)
		messagebox.showinfo("Confirmation", "Succesfully Update Contact")
		EntryReset()
		set_select()

	elif not(E_name.get()) and not(E_last_name.get()) and not(E_contact.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """
			messagebox.showerror("Error", message1)

def EntryReset():
	E_name_var.set('')
	E_last_name_var.set('')
	E_contact_var.set('')


def DeleteEntry():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
		if result==True:
			del phonelist[WhichSelected()]
			WriteInCSVFile(phonelist)
			set_select()
	else:
		messagebox.showerror("Error", 'Please select the Contact')

def LoadEntry():
    name, phone = phonelist[WhichSelected()]
    print(name.split(' '))
    E_name_var.set(name.split()[0])
    E_last_name_var.set(name.split()[1])
    E_contact_var.set(phone)


def set_select():
    phonelist.sort(key=lambda record: record[1])
    select.delete(0, END)
    i=0
    for name, phone in phonelist:
    	i+=1
    	select.insert(END, f"{i}  |    {name}   |   {phone}")


def SearchContact():
    search_query = E_search.get().strip()
    if not search_query:
        messagebox.showerror("Error", "Please enter a search query")
        return

    found = False
    for name, phone in phonelist:
        if search_query.lower() in name.lower() or search_query.lower() in phone.lower():
            found = True
            break

    if found:
        messagebox.showinfo("Search Result", f"Contact '{search_query}' is present")
    else:
        messagebox.showinfo("Search Result", f"Contact '{search_query}' is not found")

def AddDetail():
    first_name = E_name.get()
    last_name = E_last_name.get()
    contact = E_contact.get()

    if not first_name or not last_name or not contact:
        messagebox.showerror("Error", "Please fill in all the information")
        return

    # Check for duplicates based on phone number
    for _, existing_contact in phonelist:
        if existing_contact == contact:
            messagebox.showerror("Error", "Two contacts cannot have the same number")
            return

    # Check for duplicates based on first name and last name
    for existing_name, _ in phonelist:
        existing_first_name, existing_last_name = existing_name.split()
        if existing_first_name == first_name and existing_last_name == last_name:
            messagebox.showerror("Error", "Two contacts cannot have the same first name and last name")
            return

    phonelist.append([first_name + ' ' + last_name, contact])
    WriteInCSVFile(phonelist)
    set_select()
    EntryReset()
    messagebox.showinfo("Confirmation", "Successfully Add New Contact")



window = Tk()
window.title('Phone Book Created By S.Thofiq')
Frame1 = LabelFrame(window,text="Enter the Contact Detail")
Frame1.grid(padx=15,pady=15)


Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)
#---------------------------------------------
l_name = Label(Inside_Frame1,text="FirstName")
l_name.grid(row=0,column=0,padx=5,pady=5)
E_name_var = StringVar()

E_name = Entry(Inside_Frame1,width=30, textvariable=E_name_var)
E_name.grid(row=0,column=1,padx=5,pady=5)
#-----------------------------------------------
l_last_name= Label(Inside_Frame1,text="LastName")
l_last_name.grid(row=1,column=0,padx=5,pady=5)
E_last_name_var= StringVar()
E_last_name = Entry(Inside_Frame1,width=30,textvariable=E_last_name_var)
E_last_name.grid(row=1,column=1,padx=5,pady=5)
#---------------------------------------------------
l_contact= Label(Inside_Frame1,text="Contact")
l_contact.grid(row=2,column=0,padx=5,pady=5)
E_contact_var = StringVar()
E_contact = Entry(Inside_Frame1,width=30,textvariable=E_contact_var)
E_contact.grid(row=2,column=1,padx=5,pady=5)
#---------------------------------------------------
Frame2 = Frame(window)
Frame2.grid(row=0,column=1,padx=15,pady=15,sticky=E)
#<><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
Add_button = Button(Frame2,text="Add Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=AddDetail)
Add_button.grid(row=0,column=0,padx=8,pady=8)

Update_button = Button(Frame2,text="Update Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=UpdateDetail)
Update_button.grid(row=1,column=0,padx=8,pady=8)


Reset_button = Button(Frame2,text="Reset",width=15,bg="#6B69D6",fg="#FFFFFF",command=EntryReset)
Reset_button.grid(row=2,column=0,padx=8,pady=8)
#----------------------------------------------------------------------------

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1,column=0,padx=15,pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set,font=("Arial Bold",10),bg="#282923",fg="#E7C855",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=N+S)



#-----------------------------------------------------------------------------------
ActionFrame = Frame(window)
ActionFrame.grid(row=1,column=1,padx=15,pady=15,sticky=E)

Delete_button = Button(ActionFrame,text="Delete",width=15,bg="#D20000",fg="#FFFFFF",command=DeleteEntry)
Delete_button.grid(row=0,column=0,padx=5,pady=5,sticky=S)

Loadbutton = Button(ActionFrame,text="Load",width=15,bg="#6B69D6",fg="#FFFFFF",command=LoadEntry)
Loadbutton.grid(row=1,column=0,padx=5,pady=5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx



# Add a new frame for the search input
SearchFrame = LabelFrame(window, text="Search Contact")
SearchFrame.grid(row=2, column=0, padx=15, pady=15, sticky=W)

# Add an entry widget for search
E_search = Entry(SearchFrame, width=30)
E_search.grid(row=0, column=0, padx=5, pady=5)

# Add the 'Search' button below the 'Load' button
Search_button = Button(ActionFrame, text="Search", width=15, bg="#FFD700", fg="#FFFFFF", command=SearchContact)
Search_button.grid(row=2, column=0, padx=5, pady=5)

Loadbutton = Button(ActionFrame, text="Load", width=15, bg="#6B69D6", fg="#FFFFFF", command=LoadEntry)
Loadbutton.grid(row=1, column=0, padx=5, pady=5)










ReadCSVFile()


	

window.mainloop()