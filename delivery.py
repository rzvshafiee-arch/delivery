import tkinter as tk 
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image,ImageTk

w = tk.Tk()
w.geometry("800x400")
w.config(bg="#95E4BA")
w.iconbitmap("y.ico")
w.title("delivery")

main = []

def pre ():
    a = float(en_dis.get())
    b = float(en_it.get())
    c = float(en_tra.get())
    d = float(en_ord.get())

    main.clear()
    main.append(a)
    main.append(b)
    main.append(c)
    main.append(d)

    
    data = pd.read_excel("project2_delivery_data.xlsx")

    x=data[['Distance_km', 'Item_Count', 'Traffic_Level', 'Active_Courier_Orders']]
    y=data['Delivery_Time_min']

    x_test,x_train,y_test,y_train=train_test_split(x,y,test_size=0.3)

    model = LinearRegression()

    model.fit(x_train,y_train)


    pre =model.predict(np.array([main]).reshape(1,-1))
    m = round(pre[0], 2) 



    t=y_test
    p=model.predict(x_test)

    MAE= np.mean(np.abs(p-t))
    MSE= np.mean(np.square(p-t))
    RMSE=np.sqrt(np.mean(np.square(p-t)))



    l_mae = tk.Label(text=f"MAE: {MAE:.2f}",bg="#95E4BA",font=("Century Gothic",10,"bold"))
    l_mae.place(x=250,y=80)

    l_mse = tk.Label(text=f"MSE: {MSE:.2f}",bg="#95E4BA",font=("Century Gothic",10,"bold"))
    l_mse.place(x=250,y=100)

    l_rmse = tk.Label(text=f"RMSE: {RMSE:.2f}",bg="#95E4BA",font=("Century Gothic",10,"bold"))
    l_rmse.place(x=250,y=120)


    l_pre = tk.Label(text=F"Estimated Delivery Time: {m} ± {RMSE:.2f} minutes"%(m),background="#95E4BA",font=("Century Gothic",10,"bold"))
    l_pre.place(x=68,y=280)




im = ImageTk.PhotoImage(Image.open("bg.png").resize((800,400)))

bg = tk.Label(w, image=im)
bg.image = im
bg.place(x=0, y=0)



l_tit = tk.Label(w,text="Estimated delivery time",font=("Century Gothic",18,"bold"),bg="#95E4BA")
l_tit.place(x=230,y=31)
############################################################################

l_dis = tk.Label(text="Distance(km):",bg="#95E4BA",font=("Century Gothic",10,"bold"))
l_dis.place(x=48,y=30)

en_dis = tk.Entry(justify="center", font=("Arial",12),width=120)
en_dis.place(x=50,y=50,width=120,height=20)


################################################################################


l_it = tk.Label(text="Item Count:",bg="#95E4BA",font=("Century Gothic",10,"bold"))
l_it.place(x=48,y=80)


en_it =  tk.Entry(justify="center", font=("Arial",12),width=120)
en_it.place(x=50,y=100,width=120,height=20)

########################################################################

l_tra = tk.Label(text="Traffic Level:",bg="#95E4BA",font=("Century Gothic",10,"bold"))
l_tra.place(x=48,y=130)


en_tra=  tk.Entry(justify="center", font=("Arial",12),width=120)
en_tra.place(x=50,y=150,width=120,height=20)

###################################################################################


l_ord = tk.Label(text="Active Courier Orders:",bg="#95E4BA",font=("Century Gothic",10,"bold"))
l_ord.place(x=48,y=180)


en_ord=  tk.Entry(justify="center", font=("Arial",12),width=120)
en_ord.place(x=50,y=200,width=120,height=20)

#############################################################################

butt = tk.Button(bg="#CB436B",text=" Predic",command=pre)
butt.place(x=70,y=250)

##########################################################################################

w.mainloop()
