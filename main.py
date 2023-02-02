import customtkinter
from datetime import datetime
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('dark-blue')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Main Variable
        self.CUSTOMERACCOUNT = 0
        self.plLanguage = ['Tibia aplikacja kostkarza wersja 1.1','Konto klienta:', 'Procentowa wygrana', 'Klient wpłacił do puli', 'Klient wypłaca', 'Kwota',
                           'Dodaj', 'Wypłata', 'Kwota zakładu', 'Wygrana', 'Przegrana', 'Restart', 'Zapisz sesje', 'Klient dodał', 'do puli. Jego aktualny stan konta to', 
                           'Klient wypłacił', 'aktualny stan konta to', 'Klient wygrał', 'Klient przegrał']
        self.engLanguage = ['Tibia Dice Application ver 1.1', 'Customer account:', 'Customer return rate', 'Customer pays into the pot', 'Customer Withdraw', 'amount',
                            'Add', 'Withdraw', 'bet', 'Win', 'Lose', 'Restart', 'Save Data', 'Customer added', 'into the pot. Current balance is', 'Customer withdraw',
                            'current balance is', 'Customer win', 'Customer lost' ]

        self.language = ['Tibia Dice Application ver 1.1', 'Customer account:', 'Customer return rate', 'Customer pays into the pot', 'Customer Withdraw', 'amount', 
                        'Add', 'Withdraw', 'bet', 'Win', 'Lose', 'Restart', 'Save Data', 'Customer added', 'into the pot. Current balance is', 'Customer withdraw', 
                        'current balance is', 'Customer win', 'Customer lost' ]

        #Configure window
        self.geometry('533x530')
        #self.resizable(False, False)
        self.title('Tibia Dice Application ver 1.0')

        #Configure frames
        self.frame_1 = customtkinter.CTkFrame(self)
        self.frame_1.grid(column=0, row=3, pady=10, padx=10, sticky="nsew")
        self.frame_2 = customtkinter.CTkFrame(self)
        self.frame_2.grid(column=0, row=4, pady=10, padx=10)
        self.frame_3 = customtkinter.CTkFrame(self)
        self.frame_3.grid(column=0, row=6, pady=10, padx=10)        

        #Configure widgets
        self.customerValueLabel = customtkinter.CTkLabel(self, text='Customer account:', font=('Helvetica', 25, 'bold'))
        self.customerValueLabel.grid(column=0, row=1)
        self.customerValue = customtkinter.CTkLabel(self, text="0", font=('Calibri', 25, 'bold'))
        self.customerValue.grid(column=0, row=2)

        self.provisionLabel = customtkinter.CTkLabel(master=self.frame_1, text="Customer return rate")
        self.provisionLabel.grid(column=0, row=1)
        self.slider = customtkinter.CTkSlider(master=self.frame_1, command=self.sliderAction, from_=0, to=100)
        self.slider.set(80)
        self.slider.grid(column=1, row=1)
        self.actualprovisionLabel = customtkinter.CTkLabel(master=self.frame_1, text="80.0 %")
        self.actualprovisionLabel.grid(column=2, row=1,pady=5, padx=5)
        self.customerPayIntoPot = customtkinter.CTkLabel(master=self.frame_1, text="Customer pays into the pot")
        self.customerPayIntoPot.grid(column=0, row=2,pady=5, padx=5)
        self.customerPayIntoPotEntry = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="amount")
        self.customerPayIntoPotEntry.grid(column=1, row=2,pady=5, padx=5)
        self.customerPayIntoPotButton = customtkinter.CTkButton(master=self.frame_1, text="Add", command=self.addButtonAction)
        self.customerPayIntoPotButton.grid(column=2, row=2,pady=5, padx=5)
        self.customerWithdraw = customtkinter.CTkLabel(master=self.frame_1, text="Customer Withdraw")
        self.customerWithdraw.grid(column=0,row=3,pady=5, padx=5)
        self.customerWithdrawEntry = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="amount")
        self.customerWithdrawEntry.grid(column=1,row=3,pady=5, padx=5)
        self.customerWithdrawButton = customtkinter.CTkButton(master=self.frame_1, text='Withdraw', command=self.withdrawAmmount)
        self.customerWithdrawButton.grid(column=2,row=3,pady=5, padx=5)
        self.betLabel = customtkinter.CTkLabel(master=self.frame_2, text="Bet")
        self.betLabel.grid(column=0, row=1,pady=5, padx=5)
        self.betEntry = customtkinter.CTkEntry(master=self.frame_2, placeholder_text="amount")
        self.betEntry.grid(column=1, row=1,pady=5, padx=5)
        self.winButton = customtkinter.CTkButton(master=self.frame_2, text="Win", command=self.winAction)
        self.winButton.grid(column=0, row=2,pady=5, padx=5)
        self.loseButton = customtkinter.CTkButton(master=self.frame_2, text="Lose", command=self.loseAction)
        self.loseButton.grid(column=1, row=2,pady=5, padx=5)

        self.textBox = customtkinter.CTkTextbox(self, state='disabled', width=500, height=150)
        self.textBox.grid(column=0, row=5, padx=10)

        self.newPlayerButton = customtkinter.CTkButton(master=self.frame_3, text='Restart', command=self.restartButton)
        self.newPlayerButton.grid(column=0, row=0,pady=5, padx=5)

        self.saveButton = customtkinter.CTkButton(master=self.frame_3, text='Save Data', command=self.saveContent)
        self.saveButton.grid(column=1, row=0,pady=5, padx=5)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=self.frame_3, values=["Dark", "Light"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(column=0, row=1, pady=5, padx=5)

        self.languageButton = customtkinter.CTkOptionMenu(master=self.frame_3, values=['English', 'Polski'], command=self.change_language)
        self.languageButton.grid(column=1, row=1, pady=5, padx=5)

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


    def change_language(self, language):
        if(language == 'Polski'):
            self.language = self.plLanguage
            self.geometry('520x530')
            
        elif(language == 'English'):
            self.language = self.engLanguage
            self.geometry('533x530')  

        self.title(f'{self.language[0]}')
        self.customerValueLabel.configure(text=f'{self.language[1]}')
        self.provisionLabel.configure(text=f'{self.language[2]}')
        self.customerPayIntoPot.configure(text=f'{self.language[3]}')
        self.customerPayIntoPotEntry.configure(placeholder_text=f'{self.language[5]}')
        self.customerWithdrawEntry.configure(placeholder_text=f'{self.language[5]}')
        self.betEntry.configure(placeholder_text=f'{self.language[5]}')
        self.customerPayIntoPotButton.configure(text=f'{self.language[6]}')
        self.customerWithdraw.configure(text=f'{self.language[4]}')
        self.customerWithdrawButton.configure(text=f'{self.language[7]}')
        self.betLabel.configure(text=f'{self.language[8]}')
        self.winButton.configure(text=f'{self.language[9]}')
        self.loseButton.configure(text=f'{self.language[10]}')
        self.newPlayerButton.configure(text=f'{self.language[11]}')
        self.saveButton.configure(text=f'{self.language[12]}')       

    def sliderAction(self, value):
        roudedValue = str(round(value,0))
        self.actualprovisionLabel.configure(text=f'{roudedValue} %')

    def addButtonAction(self):
        self.CUSTOMERACCOUNT += int(self.customerPayIntoPotEntry.get())
        self.logging(f"{self.language[13]} {self.customerPayIntoPotEntry.get()} {self.language[14]} {self.CUSTOMERACCOUNT}")
        self.customerPayIntoPotEntry.delete(0, 'end')
        self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))  

    def withdrawAmmount(self):
        self.CUSTOMERACCOUNT -= int(self.customerWithdrawEntry.get()) 
        self.logging(f'{self.language[15]} {self.customerWithdrawEntry.get()} {self.language[16]} {self.CUSTOMERACCOUNT}')
        self.customerWithdrawEntry.delete(0,'end')
        self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))

    def logging(self, message):
        self.now = datetime.now()
        self.dt_string = self.now.strftime("%d/%m/%Y %H:%M:%S")
        self.textBox.configure(state='normal')
        self.textBox.insert('0.0', f"{self.dt_string} - {message}\n")
        self.textBox.configure(state='disabled')
    
    def winAction(self):
        value = int(self.betEntry.get())
        value -= int(self.betEntry.get()) *(100 - int(self.slider.get()))/100
        self.CUSTOMERACCOUNT += int(value)
        self.customerValue.configure(text=str(int(self.CUSTOMERACCOUNT)))
        self.logging(f'{self.language[17]} {value} {self.language[16]} {self.CUSTOMERACCOUNT}')
        self.betEntry.delete(0, 'end')

    def loseAction(self):
        self.CUSTOMERACCOUNT -= int(self.betEntry.get())
        self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))
        self.logging(f'{self.language[18]} {self.betEntry.get()} {self.language[16]} {self.CUSTOMERACCOUNT}')
        self.betEntry.delete(0, 'end')

    def saveContent(self):
        Files = [('Text Document', '*.txt')]
        
        file = asksaveasfile(filetypes = Files, defaultextension = Files)
        file.write(self.textBox.get(1.0, "end-1c"))
        file.close()

    def restartButton(self):
        response = messagebox.askyesno("Restart", "Do you really want to restart?")
        if response:
            self.CUSTOMERACCOUNT = 0
            self.customerValue.configure(text=str(self.CUSTOMERACCOUNT))
            self.textBox.configure(state='normal')
            self.textBox.delete(1.0, "end-1c")
            self.textBox.configure(state='disabled')
        else:
            pass
        
if __name__ == "__main__":
    app = App()
    app.mainloop()