from tkinter import *
from tkinter.ttk import *
from tkcalendar import *


class StudentWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Студент")
        self.geometry("350x500")
        self.grab_set()
        '''self.wait_window()'''

        self.last_name_label = Label(self, text='Фамилия')
        self.last_name_label.pack(side=TOP, anchor=W, padx=50)

        self.last_name_entry = Entry(self, width=40)
        self.last_name_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.first_name_label = Label(self, text='Имя')
        self.first_name_label.pack(side=TOP, anchor=W, padx=50)

        self.first_name_entry = Entry(self, width=40)
        self.first_name_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.middle_name_label = Label(self, text='Отчество')
        self.middle_name_label.pack(side=TOP, anchor=W, padx=50)

        self.middle_name_entry = Entry(self, width=40)
        self.middle_name_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.birth_date_label = Label(self, text='Дата рождения')
        self.birth_date_label.pack(side=TOP, anchor=W, padx=50)

        self.birth_date_entry = DateEntry(self, width=37)
        self.birth_date_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.phone_label = Label(self, text='Номер телефона')
        self.phone_label.pack(side=TOP, anchor=W, padx=50)

        self.phone_entry = Entry(self, width=40)
        self.phone_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.address_label = Label(self, text='Адрес')
        self.address_label.pack(side=TOP, anchor=W, padx=50)

        self.address_entry = Entry(self, width=40)
        self.address_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.group_label = Label(self, text='Группа')
        self.group_label.pack(side=TOP, anchor=W, padx=50)

        self.group_combobox = Combobox(self, width=40)
        self.group_combobox.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.average_mark_label = Label(self, text='Средний балл')
        self.average_mark_label.pack(side=TOP, anchor=W, padx=50)

        self.average_mark_entry = Entry(self, width=40)
        self.average_mark_entry.pack(side=TOP, anchor=W, padx=50, pady=[0, 15])

        self.buttons_frame = Frame(self)

        self.add_button = Button(self.buttons_frame, text='Добавить')
        self.add_button.pack(side=LEFT)

        self.cancel_button = Button(self.buttons_frame, text='Отменить')
        self.cancel_button.pack(side=LEFT)

        self.buttons_frame.pack(side=TOP)
        """self.photo = photo"""
