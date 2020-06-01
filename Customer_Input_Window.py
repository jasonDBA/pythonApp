# WindowGUI_tkinter
# Customer Info Input Window

from tkinter import *
from tkinter.ttk import *

# Frame Class
class MyFrame(Frame):
    # Constructor
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("Customer Information")
        self.pack(fill=BOTH, expand=True)   # For both reading & writing input.

        # Customer Name
        cusNameFrame = Frame(self)  # Create a frame for Name
        cusNameFrame.pack(fill=X)

        lblName = Label(cusNameFrame, text="Customer Name", width=15)   # left side: label
        lblName.pack(side=LEFT, padx=10, pady=10)

        entryName = Entry(cusNameFrame)     # right side: input(entry)
        entryName.pack(fill=X, padx=10, expand=True)

        # Company
        companyFrame = Frame(self)  # Create a frame for Company
        companyFrame.pack(fill=X)

        lblCompany = Label(companyFrame, text="Company", width=15)      # left side: label
        lblCompany.pack(side=LEFT, padx=10, pady=10)

        entryCompany = Entry(companyFrame)      # right side: input(entry)
        entryCompany.pack(fill=X, padx=10, expand=True)

        # Comment
        commentFrame = Frame(self)  # Create a frame for Comment
        commentFrame.pack(fill=BOTH, expand=True)   # X: fill horizontally, Y: fill vertically, BOTH: fill both

        lblComment = Label(commentFrame, text="Comment", width=15)      # left side: label
        lblComment.pack(side=LEFT, padx=10, pady=10)

        entryComment = Entry(commentFrame)      # right side: input(entry)
        entryComment.pack(fill=BOTH, padx=10, pady=10, expand=True)

        # Save Button
        btnFrame = Frame(self)
        btnFrame.pack(fill=X)

        btnSave = Button(btnFrame, text="SAVE")
        btnSave.pack(side=LEFT, padx=10, pady=10)

# Main Function
def main():
    window = Tk()
    window.geometry("600x550+100+100")
    app = MyFrame(window)
    window.mainloop()

# Main Output
if __name__ == '__main__':
    main()