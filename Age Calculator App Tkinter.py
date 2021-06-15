#all widget displayed on tkinter window
def all_widgets (root) :
    global _list
    _list = root.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list

#Clear all widget function
def delete_all_widgets():
    widget_list = all_widgets(root)
    for item in widget_list:
        item.destroy()

def days_next_birthday(end,start):
    return abs(end-start).days
def next_birthday():
    global next_birthday_label
    if int(today_month)-int(birth_month)>0:
        next_birth_date=date(int(today_year)+1,int(birth_month),int(birth_day))
    else:
        next_birth_date=date(int(today_year),int(birth_month),int(birth_day))
        
    days_to_next_birthday= days_next_birthday(next_birth_date,today_date)
    delta=relativedelta.relativedelta(next_birth_date,today_date)
    next_bday_month=delta.months
    next_bday_day=delta.days
    if next_bday_month==0 and next_bday_day>1:
        next_birthday_label=Label(root,text="Your next birthday is in "+"\n"+str(next_bday_day)
                                  +" days or "
                                  +"\n"+str(days_to_next_birthday)+" days",
                              bg="#9966FF",fg="white",font=("Arial", 20))
    elif next_bday_day==0 and next_bday_month>1:
        next_birthday_label=Label(root,text="Your next birthday is in "+"\n"+ str(next_bday_month)
                              + " months or "
                                  +"\n"+str(days_to_next_birthday)+" days",
                              bg="#9966FF",fg="white",font=("Arial", 20))
    elif next_bday_month==1 and next_bday_day>1:
        next_birthday_label=Label(root,text="Your next birthday is in "+"\n"+ str(next_bday_month)
                              + " month and "+str(next_bday_day)+"days or "
                                  +"\n"+str(days_to_next_birthday)+" days",
                              bg="#9966FF",fg="white",font=("Arial", 20))
    elif next_bday_month==0 and next_bday_day==1:
        next_birthday_label=Label(root,text="Tomorrow is your birthday! ",
                              bg="#9966FF",fg="white",font=("Arial", 20))
    elif next_bday_day==1 and next_bday_month>1:
        next_birthday_label=Label(root,text="Your next birthday is in "+"\n"+ str(next_bday_month)
                              + " month and "+str(next_bday_day)+"day or "
                                  +"\n"+str(days_to_next_birthday)+" days",
                              bg="#9966FF",fg="white",font=("Arial", 20))        
        
    else:
        next_birthday_label=Label(root,text="Your next birthday is in "+"\n"+ str(next_bday_month)
                              + " months and "+str(next_bday_day) +" days or "
                                  +"\n"+str(days_to_next_birthday)+" days",
                              bg="#9966FF",fg="white",font=("Arial", 20))
#function to calculate age in year,month and day
def calculate_result():
    global result_year
    global result_month
    global result_day
    global today_date,birth_date
    global today_month
    global today_year
    global today_day
    global birth_month
    today_day=time.strftime("%d")
    today_month=time.strftime("%m")
    today_year=time.strftime("%Y")
    today_date = date(int(today_year),int(today_month),int(today_day))
    
    if birth_month_entry.get()=="January" or birth_month_entry.get()=="Jan" or birth_month_entry.get()=="january" or birth_month_entry.get()=="jan":
        birth_month=1
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="February" or  birth_month_entry.get()=="Feb" or birth_month_entry.get()=="february" or birth_month_entry.get()=="feb":
        birth_month=2
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="March" or  birth_month_entry.get()=="March" or birth_month_entry.get()=="march" or birth_month_entry.get()=="march":
        birth_month=3
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="April" or  birth_month_entry.get()=="Apr" or birth_month_entry.get()=="april" or birth_month_entry.get()=="ap":
        birth_month=4
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="May" or  birth_month_entry.get()=="May" or birth_month_entry.get()=="may" or birth_month_entry.get()=="may":
        birth_month=5
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="June" or  birth_month_entry.get()=="Jun" or birth_month_entry.get()=="june" or birth_month_entry.get()=="jun":
        birth_month=6
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="July" or  birth_month_entry.get()=="Jul" or birth_month_entry.get()=="july" or birth_month_entry.get()=="jul":
        birth_month=7
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="August" or  birth_month_entry.get()=="Aug" or birth_month_entry.get()=="august" or birth_month_entry.get()=="aug":
        birth_month=8
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="September" or  birth_month_entry.get()=="Sept" or birth_month_entry.get()=="september" or birth_month_entry.get()=="sept":
        birth_month=9
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="October" or  birth_month_entry.get()=="Oct" or birth_month_entry.get()=="october" or birth_month_entry.get()=="oct":
        birth_month=10
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="November" or  birth_month_entry.get()=="Nov"or birth_month_entry.get()=="november" or birth_month_entry.get()=="nov":
        birth_month=11
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    elif birth_month_entry.get()=="December" or  birth_month_entry.get()=="Dec" or birth_month_entry.get()=="december" or birth_month_entry.get()=="dec":
        birth_month=12
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))
    else:
        birth_month=int(birth_month_entry.get())
        birth_date = date(int(birth_year_entry.get()),birth_month,int(birth_day_entry.get()))

    delta=relativedelta.relativedelta(today_date,birth_date)
    result_year=delta.years
    result_month=delta.months
    result_day=delta.days
    
    return result_year,result_month,result_day

def back():
    delete_all_widgets()
    start_page()
    
def result_page():
    global birth_day
    root.title("Result")
    root.geometry("350x350")
    root.resizable(False,False)
    root.configure(bg="#9966FF")
    calculate_result()
    name=name_entry.get()
    birth_day=birth_day_entry.get()
    delete_all_widgets()
    name_label=Label(root,text=name,bg="#9966FF",fg="white",font=("Arial", 20))
    name_label.grid(row=0,column=0,columnspan=2)
    if result_year==0:
        result_label=Label(root,text="You are " + str(result_month)+
                           " months and "+str(result_day)+" days old.",
                           bg="#9966FF",fg="white",font=("Arial", 20))
    elif result_month==0 and result_day==0:
                result_label=Label(root,text="You are " + str(result_year) + " years old ",
                                   bg="#9966FF",fg="white",font=("Arial", 20))
    elif result_month==0:
        result_label=Label(root,text="You are " + str(result_year) + " years and "+"\n"+
                           str(result_day)+" days old.",
                           bg="#9966FF",fg="white",font=("Arial", 20))
    elif result_day==0:
        result_label=Label(root,text="You are " + str(result_year) + " years and "+"\n"+str(result_month)+
                           " months old.",
                           bg="#9966FF",fg="white",font=("Arial", 20))
    else:
        result_label=Label(root,text="You are " + str(result_year) + " years, "+"\n"+str(result_month)+
                       " months and "+str(result_day)+" days old.",
                       bg="#9966FF",fg="white",font=("Arial", 20))
        
    result_label.grid(row=1,column=0,padx=20,pady=20)
    next_birthday()
    next_birthday_label.grid(row=2,column=0)
    back_button=Button(root,text="Back",bg="#9966FF",fg="white",command=back)
    back_button.grid(row=3,column=0,padx=100,pady=10)
    quit_button=Button(root,text="Exit",bg="#9966FF",fg="white",command=quit)
    quit_button.grid(row=4,column=0,padx=100,pady=10)
#Start page function
def start_page():
    global result_year
    global result_month
    global result_day
    global birth_year_entry
    global birth_month_entry
    global birth_day_entry
    global name_entry
    root.title(" Age Calculator App")
    root.geometry("350x320")
    root.resizable(False,False)
    root.configure(bg="#9966FF")
    title_label=Label(root,text="Age Calculator App",font=("Arial", 20),bg="#9966FF",fg="white")
    title_label.grid(row=0,column=0,columnspan=2)
    name_label=Label(root,text="Name",bg="#9966FF",fg="white")
    name_label.grid(row=1,column=0,padx=10,pady=10)
    name_entry=Entry(root)
    name_entry.grid(row=1,column=1,padx=10,pady=10)
    birth_day_label=Label(root,text="Birth Day: ",bg="#9966FF",fg="white")
    birth_day_label.grid(row=2,column=0,padx=10,pady=10)
    birth_day_entry=Entry(root)
    birth_day_entry.grid(row=2,column=1,padx=10,pady=10)
    birth_month_label=Label(root,text="Birth Month: ",bg="#9966FF",fg="white")
    birth_month_label.grid(row=3,column=0,padx=10,pady=10)
    birth_month_entry=Entry(root)
    birth_month_entry.grid(row=3,column=1,padx=10,pady=10)
    birth_year_label=Label(root,text="Birth Year: ",bg="#9966FF",fg="white")
    birth_year_label.grid(row=4,column=0,padx=10,pady=10)
    birth_year_entry=Entry(root)
    birth_year_entry.grid(row=4,column=1,padx=10,pady=10)
    enter_button=Button(root,text="Enter",bg="#9966FF",fg="white",command=result_page)
    enter_button.grid(row=5,column=1)
    quit_button=Button(root,text="Exit",bg="#9966FF",fg="white",command=quit)
    quit_button.grid(row=5,column=0)
    
if __name__=='__main__':
    from tkinter import *
    from datetime import date
    from datetime import datetime
    import time
    from dateutil import relativedelta
    global root    
    root=Tk()
    start_page()
    mainloop()
