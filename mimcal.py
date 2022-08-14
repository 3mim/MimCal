## code written by 3mim( seyed mohmmad morteza maleki)
# https://www.treem.ir
# gmail: morrtteeza@gmail.com
# use python3 and tkinter for gui
# CopyRight: GPL v3

from tkinter import *
from tkinter import messagebox
import customtkinter
from pyglet import resource,font
from webbrowser import open




# add custom fonts
resource.add_font('fonts/IRANMarker.ttf') # for  pyinstaller use this code = resource.add_font('IRANMarker.ttf')
font_ = font.load('IRANMarker')

# color of forex frame
forex_border="#16c297"
forex_bottom="#159172"
forex_hover_bottom="#1a7860"
forex_frame= ''

# color of crypto frame
crypto_border = "#1e79c0"
crypto_frame= '2da3ff'

# color of dark and light mode
dark_mode_fg_center= "#2e2e2e"
light_mode_fg_center= "#e9f5ff"
dark_mode_fr_center='#292929'
dark_mode_fr_top='#292929'
light_mode_fr_center='#bbe8ff'

dark_mode_fg_bottom= "#2e2e2e"
light_mode_fg_bottom= "#e9fff9"
dark_mode_fr_bottom='#292929'
light_mode_fr_bottom='#6edcbe'

# font persian and english
font_persian = 'IRANMarker'
font_english = 'aria'


# start  -> title,size ,icon
window = customtkinter.CTk()
window.title('MimCal')

window.geometry('320x500')
window.maxsize(420,800)
window.minsize(420,340)

window.resizable(width=False,height=True)
window.attributes('-topmost', True)
window.iconbitmap('C:/Users/MORTEZA/Documents/pythonCode/MimCal/test/logo.ico')
# end  -> title,size ,icon

# start all functions
# menu funtion
def git():
        open('https://github.com/3mim/MimCal', new=2)


def mim():
    open('https://treem.ir/mimcal', new=2)

def about():
    l = switch_language.get()
    l = int(l)
    if l == 1:
        messagebox.showinfo("Show info", 'Mimcal was written by 3mim ( seyed mohamad morteza maleki) for trading. Mimcal can calculate stop loss of crypto curency and entry lot size of forex. CopyRight: GPL v3 2022')

    else:
        messagebox.showinfo("Show info", ' سلام من سه میم هستم سید محمد مرتضی ملکی این نرم افزار برای کار ترید خودم و دوست عزیزم عرفان صیادی طراحی کردم که می تواند حدضرر در بازار کریپتو و حجم ورودی به معامله در فارکس حساب کنه. کپی و تغیر با ذکر منبع آزاد است . به امید فردای  بهتر مرداد سال 1401 (GPL v3) ')


def pin():
    window.attributes('-topmost', True)

def unpin():
    window.attributes('-topmost', False)
# menu funtion

# crypto funtions
def crypto_calculate ():
    switch =  int(switch_language.get())


    r = entry_crypto_risk.get()
    l = int(leverage.get())

    if  r.isnumeric():
        # v = int(v)
        r = int(r)
    else:
        if switch == 1:
                messagebox.showerror("wrong", "Enter Risk or Entry Volume ")
                return
        if switch == 0:
                messagebox.showerror("خطا", "!لطفا عدد های حجم یا درصد ریسک را وارد کنید")
                return

    if r > 100 or r < 1 :
        if switch == 1:
                messagebox.showinfo("info", "Risk Must be 1 t0 100")
                return
        if switch == 0:
                messagebox.showinfo("اطلاعات", "  100 ریسک شما باید بین  1 تا")
                return
        
    else:
        pass
    per = r / l

    if round(per,2) == 0.0 :
        if switch == 1:
                messagebox.showinfo("info", "NOT Allow to Enter a Trade")
                return
        if switch == 0:
                messagebox.showinfo('info',"شما اجازه ورود به معالمه را ندارید")
                return
    else:
        label_crypto_answer.configure(text='{}'.format(round(per,2))  )
# crypto functions

# slider function (leverage)
def slider_callback(value):
    var =int(value)
    label_crypto_slider.configure(text='{}'.format(var))
# slider function(leverage)

# start forex funtions
def forex_calculate():
    switch =  int(switch_language.get())
    v = entry_forex_value.get()
    r = entry_forex_risk.get()
    s = entry_forex_sl.get()
    lo = entry_forex_lot.get()
    
    if v.isnumeric() and r.isnumeric() and s.isnumeric() and lo.isnumeric() :
        v = int(v)
        r = int(r)
        s = int(s)
        lo = int(lo)
    else:
        if switch == 1:
                messagebox.showerror("Error", "Enter the numbers ")
                return
        if switch == 0:
                messagebox.showerror(" فارکس خطا", "!لطفا اعداد را وارد کنید")
                return


    if v > 9000000 or v < 0.01 :
        if switch == 1:
                messagebox.info("info", "Margin must be 0.01 to 9000000 ")
                return
        if switch == 0:
                messagebox.showinfo("اطلاعات", " 9000000 حجم ورودی شما باید بین  0.01 تا")
                return
        
    else:
        pass


    if  s < 1 :
        if switch == 1:
                messagebox.showinfo("info", "stop loss must be more than 1")
                return
        if switch == 0:
                messagebox.showinfo("اطلاعات", " فاصله حد محافط شما باید بیشتر از 1 باشد")
                return    
    else:
        pass
    

    if lo < 1 :
        if switch == 1:
                messagebox.showinfo("info", "pip value must be more than 0.01")
                return
        if switch == 0:
                messagebox.showinfo("اطلاعات", "  یک لات باید بشتر از  0.01 دلار باشد ")
                return    
        
    else:
        pass

    if r > 100 or r < 1 :
        if switch == 1:
                messagebox.showinfo("info", "Risk Must be 1 t0 100")
                return
        if switch == 0:
                messagebox.showinfo("اطلاعات", "  100 ریسک شما باید بین  1 تا")
                return
    else:
        pass
    

    rd = (v*r) / 100
    
    a= rd / s
    volume_entry= a / lo
    if round(volume_entry,2) == 0.0 :
        if switch == 1:
                messagebox.showinfo("info", "NOT Allow to Enter a Trade")
                return
        if switch == 0:
                messagebox.showinfo('info',"شما اجازه ورود به معالمه را ندارید")
                return
    else:
        label_forex_answer.configure(text='{}'.format(round(volume_entry,2))  )
# end forex funtions

# language function
def language():
    create_menu()
    l = switch_language.get()
    l = int(l)
    if l == 1:

        switch_language.configure(text='فارسی',)
        #### top frame
        label_welcome.configure(font=(font_english,12),text='Welcom to Mim cal',)
        #### center frame
        label_crypto_name.configure(text=' Crypto Stop Loss  ',font=(font_english,13))
        label_crypto_risk.configure(text=': Risk',font=(font_english,10))
        entry_crypto_risk.configure(font=(font_english,10),placeholder_text='example : 2',justify='left')
        label_crypto_leverage.configure(text='  :Leverage',font=(font_english,10))
        label_crypto_slider.configure(font=(font_english,10))
        button_crypto_answer.configure(text='Calculate SL')
        label_crypto_answer.configure(font=(font_english,10))

        # #### bottom frame
        label_forex_name.configure(text=' Lot Size of Forex ',font=(font_english,13),)
        label_forex_value.configure(text=' : Margin',font=(font_english,10))
        entry_forex_value.configure(font=(font_english,10),placeholder_text='example : 1000',justify='left')
        label_forex_risk.configure(text=' : Risk',font=(font_english,10))
        entry_forex_risk.configure(font=(font_english,10),placeholder_text='example : 2',justify='left')
        label_forex_sl.configure(text=': (pip)stop loss',font=(font_english,10))
        entry_forex_sl.configure(font=(font_english,10),placeholder_text='example : 15',justify='left')
        label_forex_lot.configure(text=': pip value per 1 lot',font=(font_english,10))
        entry_forex_lot.configure(font=(font_english,10),placeholder_text='example : 10',justify='left',)
        button_forex_answer.configure(text='Calculate lot size')
        label_forex_answer.configure(font=(font_english,10))

    else:
        # check_font()
        switch_language.configure(text='english')
        #### top frame
        label_welcome.configure(font=(font_persian,12),text='به ماشین حساب میم خوش آمدید')
        # #### center frame
        label_crypto_name.configure(text='حد ضرر کریپتو  ',font=(font_persian,13))
        label_crypto_risk.configure(text=': درصد ریسک ',font=(font_persian,9))
        entry_crypto_risk.configure(font=(font_persian,9),placeholder_text='مثال : 2',justify='right')
        label_crypto_leverage.configure(text='  :اهرم یا لوریج ',font=(font_persian,9))
        label_crypto_slider.configure(font=(font_persian,9))
        button_crypto_answer.configure(text='محاسبه حد ضرر')
        label_crypto_answer.configure(font=(font_persian,9))
        # #### bottom frame
        label_forex_name.configure(text='حجم ورودی فارکس',font=(font_persian,13),)
        label_forex_value.configure(text=' : سرمایه کل',font=(font_persian,9))
        entry_forex_value.configure(font=(font_persian,9),placeholder_text='مثال : 1000',justify='right')
        label_forex_risk.configure(text=' : درصد ریسک',font=(font_persian,9))
        entry_forex_risk.configure(font=(font_persian,9),placeholder_text='مثال : 2',justify='right')
        label_forex_sl.configure(text=': (pip) حدضرر',font=(font_persian,9))
        entry_forex_sl.configure(font=(font_persian,9),placeholder_text='مثال : 15',justify='right')
        label_forex_lot.configure(text=':1 lot  به ازای pip ارزش یک',font=(font_persian,9))
        entry_forex_lot.configure(font=(font_persian,10),placeholder_text='مثال : 10',justify='right',)
        button_forex_answer.configure(text='محاسبه حجم ورودی',)
        label_forex_answer.configure(font=(font_persian,9),)
# language function

# mode function
def dark_Light_mode():
    l = switch_mode.get()
    l = int(l)
    if l == 1 : # Dark  Mode
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        customtkinter.set_appearance_mode("dark")
        my_canvas.configure(bg='#4a4b4d')
        switch_mode.configure(text='Light Mode')
        mainframe.configure(bg='#4a4b4d')
        mainframe.configure(fg_color='#4a4b4d')
        frame_center.configure(fg_color='{}'.format(dark_mode_fr_center))
        frame_bottom.configure(fg_color='{}'.format(dark_mode_fr_bottom))
        frame_top.configure(fg_color='{}'.format(dark_mode_fr_top))

        ##### entery and label
        entry_forex_value.configure(fg_color='{}'.format(dark_mode_fg_bottom))
        entry_forex_risk.configure(fg_color='{}'.format(dark_mode_fg_bottom))
        entry_forex_sl.configure(fg_color='{}'.format(dark_mode_fg_bottom))
        entry_forex_lot.configure(fg_color='{}'.format(dark_mode_fg_bottom))
        entry_crypto_risk.configure(fg_color='{}'.format(dark_mode_fg_center))
        label_forex_answer.configure(fg_color='{}'.format(dark_mode_fg_bottom))
        label_crypto_answer.configure(fg_color='{}'.format(dark_mode_fg_center))
        label_forex_name.configure(text_color='white')
        label_crypto_name.configure(text_color='white')

        ##### frame
        frame_forex_risk.configure(fg_color='#333333')
        frame_forex_value.configure(fg_color='#333333')
        frame_forex_lot.configure(fg_color='#333333')
        frame_forex_sl.configure(fg_color='#333333')
        frame_forex_answer.configure(fg_color='#333333')
        frame_crypto_risk.configure(fg_color='#333333')
        frame_crypto_leverage.configure(fg_color='#333333')
        frame_crypto_answer.configure(fg_color='#333333')
        frame_forex_switch.configure(fg_color=dark_mode_fr_center)
        frame_crypto_name.configure(fg_color='#395e9c')
        # silder
        leverage.configure(progress_color='#aab0b5')
        window.pack_propagate(1)
        window.pack_propagate(0)



        

    else:
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
        customtkinter.set_appearance_mode("light")  
        my_canvas.configure(bg='white')
        switch_mode.configure(text='Dark Mode')
        mainframe.configure(bg='white')
        mainframe.configure(fg_color='white')
        frame_center.configure(fg_color='{}'.format(light_mode_fr_center))
        frame_bottom.configure(fg_color='{}'.format(light_mode_fr_bottom))
        frame_top.configure(fg_color='#dae9ff')

        ##### entry and label
        entry_forex_value.configure(fg_color='{}'.format(light_mode_fg_bottom))
        entry_forex_risk.configure(fg_color='{}'.format(light_mode_fg_bottom))
        entry_forex_sl.configure(fg_color='{}'.format(light_mode_fg_bottom))
        entry_forex_lot.configure(fg_color='{}'.format(light_mode_fg_bottom))
        entry_crypto_risk.configure(fg_color='{}'.format(light_mode_fg_center))
        label_forex_answer.configure(fg_color='{}'.format(light_mode_fg_bottom))
        label_crypto_answer.configure(fg_color='{}'.format(light_mode_fg_center))
        ###### frame
        frame_forex_risk.configure(fg_color='white')
        frame_forex_value.configure(fg_color='white')
        frame_forex_lot.configure(fg_color='white')
        frame_forex_sl.configure(fg_color='white')
        frame_forex_answer.configure(fg_color='white')
        frame_crypto_risk.configure(fg_color='white')
        frame_crypto_leverage.configure(fg_color='white')
        frame_crypto_answer.configure(fg_color='white')
        frame_forex_switch.configure(fg_color=light_mode_fr_bottom)
        frame_crypto_name.configure(fg_color='#608bd5')
        # button
        button_crypto_answer.configure(text_color='white')
        button_forex_answer.configure(text_color='white')
        # silder
        leverage.configure(progress_color='#6b98af')

# mode function
# end all functions

# start Create menu bar
def create_menu():
    l =int(switch_language.get())
    if l == 1:
            menubar = Menu(window)
            menubar.add_command(label='About',command=about)
            menubar.add_command(label='My website',command=mim) 
            menubar.add_command(label='Github',command=git)


            cascade = Menu(menubar,tearoff=0)
            menubar.add_cascade(label='Pin',menu=cascade)
            cascade.add_command(label='Pin',command=pin)
            cascade.add_command(label='Unpin',command=unpin)
            window.config(menu=menubar)
    else:
            menubar = Menu(window)
            menubar.add_command(label='درباره نرم افزار',command=about)
            menubar.add_command(label='سایت نویسنده',command=mim)
            menubar.add_command(label='گیت هاب',command=git)


            cascade = Menu(menubar,tearoff=0)
            menubar.add_cascade(label='پین',menu=cascade)
            cascade.add_command(label='Pin',command=pin)
            cascade.add_command(label='Unpin',command=unpin)
            window.config(menu=menubar)

# end Create menu bar

# start all frame
# start Create A Canvas
my_canvas = customtkinter.CTkCanvas(window,width=100,)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1,)
# end Create A Canvas

# start Add A Scrollbars to Canvas
y_scrollbar = customtkinter.CTkScrollbar(window,orientation=VERTICAL,command=my_canvas.yview,)
y_scrollbar.pack(side=RIGHT,fill=Y,)
# end Add A Scrollbars to Canvas

# start Configure the canvas
my_canvas.configure(yscrollcommand=y_scrollbar.set,bg='#4a4b4d')
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL))) 
# end Configure the canvas

# start create Another Frame INSIDE the Canvas
mainframe = customtkinter.CTkFrame(master=my_canvas,padx=10,pady=5)
# end create Another Frame INSIDE the Canvas

# start top frame
frame_top = customtkinter.CTkFrame(master=mainframe)
frame_top.pack(expand=True,fill='both',pady=5,ipadx=5,ipady=1)                         
label_welcome =customtkinter.CTkLabel(master=frame_top,width=5,height=30,)
label_welcome.pack()
# end top frame

# start center frame
frame_center = customtkinter.CTkFrame(master=mainframe,)
frame_center.pack(fill='both',side='top',pady=5,ipadx=10)
# enter center frame

# start show crypto name
frame_crypto_name = customtkinter.CTkFrame(master=frame_center,fg_color='{}'.format(crypto_border))
frame_crypto_name.pack(pady=10,ipadx=10,)

label_crypto_name = customtkinter.CTkLabel(master=frame_crypto_name)
label_crypto_name.pack(side='right',anchor='n',padx=100,pady=5)
# end show crypto name

# start risk-crypto frame
frame_crypto_risk = customtkinter.CTkFrame(master=frame_center,)
frame_crypto_risk.pack(pady=10,ipadx=0,)

label_crypto_risk = customtkinter.CTkLabel(master=frame_crypto_risk)
label_crypto_risk.pack(side='right',anchor='n',pady=10)

entry_crypto_risk =customtkinter.CTkEntry(master=frame_crypto_risk,border_color='{}'.format(crypto_border),placeholder_text_color='#666666',placeholder_text='')
entry_crypto_risk.pack(side='right',anchor='n',pady=10,padx=40)
entry_crypto_risk.focus()
# end risk-crypto frame

# start leverage-crypto frame
frame_crypto_leverage = customtkinter.CTkFrame(master=frame_center)
frame_crypto_leverage.pack(pady=10)

label_crypto_leverage =customtkinter.CTkLabel(master=frame_crypto_leverage)
label_crypto_leverage.pack(side='right',anchor='n',pady=11)

label_crypto_slider = customtkinter.CTkLabel(master=frame_crypto_leverage,text='50' )
label_crypto_slider.pack()

leverage = customtkinter.CTkSlider(master=frame_crypto_leverage,  from_=1, to=100 ,command=slider_callback)
leverage.pack( padx=10)
# end risk-crypto frame

# start answer-crypto frame
frame_crypto_answer = customtkinter.CTkFrame(master=frame_center)
frame_crypto_answer.pack(ipadx=20,pady=10)

button_crypto_answer=customtkinter.CTkButton(master=frame_crypto_answer,command=crypto_calculate,text_font=(font_persian,10))
button_crypto_answer.pack(side='right',anchor='n',padx=20,pady=10)

label_crypto_answer= customtkinter.CTkLabel(master=frame_crypto_answer,text='0', corner_radius=5,)
label_crypto_answer.pack(side='right',anchor='n',pady=10)
# end answer-crypto frame

# start bottom frame
frame_bottom= customtkinter.CTkFrame(master=mainframe)
frame_bottom.pack(expand=True,fill='both',pady=5,ipadx=5,side='top')
# end bottom frame

# start show forex name
frame_forex_name = customtkinter.CTkFrame(master=frame_bottom,fg_color='{}'.format(forex_bottom))
frame_forex_name.pack(pady=10,ipadx=5,)

label_forex_name = customtkinter.CTkLabel(master=frame_forex_name,)
label_forex_name.pack(side='right',anchor='n',padx=100,pady=5)
# end show forex name

# start value-forex frame
frame_forex_value = customtkinter.CTkFrame(master=frame_bottom)
frame_forex_value.pack(pady=10)

label_forex_value = customtkinter.CTkLabel(master=frame_forex_value,)
label_forex_value.pack(side='right',anchor='n',pady=10)

entry_forex_value =customtkinter.CTkEntry(master=frame_forex_value,border_color='{}'.format(forex_border),placeholder_text_color='#666666',placeholder_text='')
entry_forex_value.pack(side='right',anchor='n',pady=10,padx=40)
# end value-forex frame

# start risk-forex frame
frame_forex_risk = customtkinter.CTkFrame(master=frame_bottom)
frame_forex_risk.pack(pady=10)

label_forex_risk =customtkinter.CTkLabel(master=frame_forex_risk) 
label_forex_risk.pack(side='right',anchor='n',pady=10)

entry_forex_risk =customtkinter.CTkEntry(master=frame_forex_risk,border_color='{}'.format(forex_border),placeholder_text_color='#666666',placeholder_text='')
entry_forex_risk.pack(side='right',anchor='n',pady=10,padx=40)
# end risk-forex frame

# start stoploss-forex frame
frame_forex_sl = customtkinter.CTkFrame(master=frame_bottom)
frame_forex_sl.pack(pady=10)

label_forex_sl = customtkinter.CTkLabel(master=frame_forex_sl) 
label_forex_sl.pack(side='right',anchor='n',pady=10)

entry_forex_sl =customtkinter.CTkEntry(master=frame_forex_sl,border_color='{}'.format(forex_border),placeholder_text_color='#666666',placeholder_text='')
entry_forex_sl.pack(side='right',anchor='n',pady=10,padx=40)
# end stoploss-forex frame

# start lot-forex frame
frame_forex_lot = customtkinter.CTkFrame(master=frame_bottom)
frame_forex_lot.pack(pady=10)

label_forex_lot = customtkinter.CTkLabel(master=frame_forex_lot)
label_forex_lot.pack(side='right',anchor='n',pady=10)

entry_forex_lot =customtkinter.CTkEntry(master=frame_forex_lot,border_color='{}'.format(forex_border),placeholder_text_color='#666666',placeholder_text='')
entry_forex_lot.pack(side='right',anchor='n',pady=10,padx=40)
# entry_forex_lot.insert(0,'10')

# end lot-forex frame

# start answer-forex frame
frame_forex_answer = customtkinter.CTkFrame(master=frame_bottom)
frame_forex_answer.pack(pady=10,ipadx=20)

button_forex_answer=customtkinter.CTkButton(master=frame_forex_answer,command=forex_calculate,fg_color='{}'.format(forex_bottom),hover_color='{}'.format(forex_hover_bottom),text_font=(font_persian,10))
button_forex_answer.pack(side='right',anchor='n',padx=20,pady=10)

label_forex_answer=customtkinter.CTkLabel(master=frame_forex_answer,text='0', corner_radius=5)
label_forex_answer.pack(side='right',anchor='n',pady=10)
# end answer-forex frame

# start dark and light mode
frame_forex_switch= customtkinter.CTkFrame(master=frame_bottom)
frame_forex_switch.pack(pady=10)

switch_mode = customtkinter.CTkSwitch(master=frame_forex_switch,command=dark_Light_mode)
switch_mode.pack(pady=12, padx=10,side='right')
switch_mode.select()

switch_language = customtkinter.CTkSwitch(master=frame_forex_switch,command=language)
switch_language.pack(pady=12, padx=10,side='bottom')
switch_language.select()
# end dark and light mode
# end  all frame

my_canvas.create_window(0,0,window=mainframe)
window.mainloop()
