from tkinter import *
import numpy as np
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split
import lightgbm as ltb

root =Tk()
root.title("Order Predictor")
root.geometry('1000x563')
root.resizable(False,False)

img=PhotoImage(file=r"Orders predictor\salespreimg.png")
Label(root,image=img,bg='white').place(x=0,y=0)


data=pd.read_csv("Orders predictor\TRAIN.csv")

data["Discount"]=data["Discount"].map({"No":0,"Yes":1})
data["Store_Type"]=data["Store_Type"].map({"S1":1,"S2":2,"S3":3,"S4":4})
data["Location_Type"]=data["Location_Type"].map({"L1":1,"L2":2,"L3":3,"L4":4,"L5":5})

X=np.array(data[["Store_Type","Location_Type","Holiday","Discount"]])
y=np.array(data["#Order"])

X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.25,random_state=42)
model=ltb.LGBMRegressor()
model.fit(X_train,y_train)

Label(root,text='Number of Order' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 18 bold')).place(x=20,y=30)
Label(root,text='Predictor' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 18 bold')).place(x=20,y=60)
Label(root,text='Enter Details' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 18 bold')).place(x=720,y=30)
Label(root,text='Store Type:' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 13')).place(x=650,y=100) 
Label(root,text='Location Type:' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 13')).place(x=650,y=150) 
Label(root,text='Holiday:' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 13')).place(x=650,y=200) 
Label(root,text='Discount:' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 13')).place(x=650,y=250) 



def submit():
    st=stype.get()
    lt=ltype.get()
    holi=hol.get()
    disc=dis.get()
    ans=model.predict([[int(st[1]),int(lt[1]),holi,disc]])
    Label(root,text='Number of order is:' ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 13 bold')).place(x=690,y=400) 
    Label(root,text=int(ans[0]) ,fg='#36271E', bg='#B4B1AC' ,font=('Aerial 13 bold')).place(x=850,y=400) 




# menu1= StringVar()
# menu1.set("Select Store Type")
# drop1=OptionMenu(root,menu1,"S1","S2","S3","S4")
# drop1.config(bg="white",border=0)
# drop1.place(x=300,y=100)

s=["S1","S2","S3","S4"]
stype=ttk.Combobox(root,value=s)
stype.current(0)
stype.place(x=770,y=100)

# menu2= StringVar()
# menu2.set("Select Location Type")
# drop2=OptionMenu(root,menu2,"L1","L2","L3","L4","L5")
# drop2.config(bg="white",border=0)
# drop2.place(x=300,y=150)

l=["L1","L2","L3","L4","L5"]
ltype=ttk.Combobox(root,value=l)
ltype.current(0)
ltype.place(x=770,y=150)



hol = IntVar()
R1 = Radiobutton(root, text="Yes", variable=hol, value=1)
R1.config(bg="#B4B1AC",border=0,activebackground="#8A786E")
R1.place( x=770,y=200 )

R2 = Radiobutton(root, text="No", variable=hol, value=0)
R2.config(bg="#B4B1AC",border=0,activebackground="#8A786E")
R2.place(x=840,y=200 )



dis = IntVar()
R3 = Radiobutton(root, text="Yes", variable=dis, value=1)
R3.config(bg="#B4B1AC",border=0,activebackground="#8A786E")
R3.place( x=770,y=250 )

R4 = Radiobutton(root, text="No", variable=dis, value=0)
R4.config(bg="#B4B1AC",border=0,activebackground="#8A786E")
R4.place(x=840,y=250 )



sub_but=Button(root,width=7,pady=2,text='Submit',border=0,bg="#8A786E",fg="white",font=("bold"),command=submit)
sub_but.place(x=740,y=320)






root.mainloop()