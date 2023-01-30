import customtkinter
from datetime import datetime
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('blue')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Main Variable
        self.CUSTOMERACCOUNT = 0
        paddingSmall = ['pady=5', 'padx=5']

        #Configure window
        self.geometry('515x430')
        self.resizable()
        self.title('Tibia Dice App')

        #Configure frames
        self.frame_1 = customtkinter.CTkFrame(self)
        self.frame_1.grid(column=0, row=3, pady=10, padx=10)
        self.frame_2 = customtkinter.CTkFrame(self)
        self.frame_2.grid(column=0, row=4, pady=10, padx=10)
        self.frame_3 = customtkinter.CTkFrame(self)
        self.frame_3.grid(column=0, row=6, pady=10, padx=10)        

        #Configure widgets
        self.customerValueLabel = customtkinter.CTkLabel(self, text="Customer account: ", font=('Calibri', 20))
        self.customerValueLabel.grid(column=0, row=1)
        self.customerValue = customtkinter.CTkLabel(self, text="0", font=('Calibri', 20))
        self.customerValue.grid(column=0, row=2)

        self.provisionLabel = customtkinter.CTkLabel(master=self.frame_1, text="Customer return rate")
        self.provisionLabel.grid(column=0, row=1)
        self.slider = customtkinter.CTkSlider(master=self.frame_1, command=self.sliderAction, from_=0, to=100)
        self.slider.set(80)
        self.slider.grid(column=1, row=1)
        self.actualprovisionLabel = customtkinter.CTkLabel(master=self.frame_1, text="80.0 %")
        self.actualprovisionLabel.grid(column=2, row=1)
        self.customerPayIntoPot = customtkinter.CTkLabel(master=self.frame_1, text="Customer pays into the pot:")
        self.customerPayIntoPot.grid(column=0, row=2)
        self.customerPayIntoPotEntry = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="amount")
        self.customerPayIntoPotEntry.grid(column=1, row=2)
        self.customerPayIntoPotButton = customtkinter.CTkButton(master=self.frame_1, text="Add", command=self.addButtonAction)
        self.customerPayIntoPotButton.grid(column=2, row=2)
        self.betLabel = customtkinter.CTkLabel(master=self.frame_2, text="Bet")
        self.betLabel.grid(column=0, row=1,pady=5, padx=5)
        self.betEntry = customtkinter.CTkEntry(master=self.frame_2, placeholder_text="amount")
        self.betEntry.grid(column=1, row=1,pady=5, padx=5)
        self.winButton = customtkinter.CTkButton(master=self.frame_2, text="Win", command=self.winAction)
        self.winButton.grid(column=0, row=2,pady=5, padx=5)
        self.loseButton = customtkinter.CTkButton(master=self.frame_2, text="Lose", command=self.loseAction)
        self.loseButton.grid(column=1, row=2,pady=5, padx=5)

        self.textBox = customtkinter.CTkTextbox(self, width=480, height=150)
        self.textBox.grid(column=0, row=5)

        self.newPlayerButton = customtkinter.CTkButton(master=self.frame_3, text='Restart', command=self.restartButton)
        self.newPlayerButton.grid(column=0, row=0,pady=5, padx=5)

        self.saveButton = customtkinter.CTkButton(master=self.frame_3, text='Save Data', command=self.saveContent)
        self.saveButton.grid(column=1, row=0,pady=5, padx=5)

    def sliderAction(self, value):
        roudedValue = str(round(value,0))
        self.actualprovisionLabel.configure(text=f'{roudedValue} %')

    def addButtonAction(self):
        self.CUSTOMERACCOUNT += int(self.customerPayIntoPotEntry.get())
        self.logging(f"Customer added {self.customerPayIntoPotEntry.get()} into the pot")
        self.customerPayIntoPotEntry.delete(0, 'end')
        self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))   

    def logging(self, message):
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.textBox.insert('0.0', f"{self.dt_string} - {message}\n")
    
    def winAction(self):
        value = int(self.betEntry.get())
        value -= int(self.betEntry.get()) *(100 - int(self.slider.get()))/100
        self.CUSTOMERACCOUNT += int(value)
        self.customerValue.configure(text=str(int(self.CUSTOMERACCOUNT)))
        self.logging(f'Customer win {value} an his new balance is {self.CUSTOMERACCOUNT}')
        self.betEntry.delete(0, 'end')

    def loseAction(self):
        self.CUSTOMERACCOUNT -= int(self.betEntry.get())
        self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))
        self.logging(f'Customer lost {self.betEntry.get()} and his new balance is {self.CUSTOMERACCOUNT}')
        self.betEntry.delete(0, 'end')

    def saveContent(self):
        Files = [('All Files', '*.*'),
                ('Python Files', '*.py'),
                ('Text Document', '*.txt')]
        
        file = asksaveasfile(filetypes = Files, defaultextension = Files)
        file.write(self.textBox.get(1.0, "end-1c"))
        file.close()

    def restartButton(self):
        response = messagebox.askyesno("Restart?", "Do you realy want to restart?")
        if response:
            self.CUSTOMERACCOUNT = 0
            self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))
            self.textBox.delete(1.0, "end-1c")
        else:
            pass
        
if __name__ == "__main__":
    app = App()
    app.mainloop()