import os
import random
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox
# import libs

def ID():#product and group IDs reading
    global product_ID
    global group_ID
    ID_s=open("Shop/ID_s.txt","r")
    group_ID=ID_s.readline()
    product_ID=ID_s.readline()
    
    ID_s.seek(0)
    ID_s.close()
    

class Product_Operations:
    def __init__(self):
        
        self._product_ID=product_ID#initialize
        self.dummy_gain_arr=[0,0]
        self.month_number=0
        self.month_gain_arr=[]
        
    def Add_Product(self,product_group,product_ID,product_name,purchase_price,sale_price,number_of_product):
        
        if len(product_group)*len(product_ID)*len(product_name)*len(purchase_price)*len(sale_price)*len(number_of_product)!=0:# check data
            self.products_inf=open(f"Shop/Groups/{product_group.title()}_inf.txt","a")
            self.products_inf.write(f"\n***\nProductID\n{product_ID}\nProductName\n{product_name}\nPurchasePrice\n{purchase_price}\nSale Price\n{sale_price}\nNumber Of Product\n{number_of_product}\n\n***\n\n")
            self.products_inf.close()# write file
            
            self.products=open(f"Shop/Groups/Products/{product_group.title()}.txt","a")
            
            for i in range(int(number_of_product)):
                self._product_ID=str(int(self._product_ID)+1)
                self.products.write(f"\n***\nProductID\n{self._product_ID+product_group.title()[0]}\nProductName\n{product_name}\nPurchasePrice\n{purchase_price}\nSale Price\n{sale_price}\n\n***\n")
            self.products.close()# write file
        else:
            messagebox.showerror("Error Message","Something went wrong, you are redirected to the home screen!")
            screen.Main_Desing()#Error message
    
    def Sale_Product(self,product_group_name,product_name,index,number_of_product):
        
        self.products_inf=open(f"Shop/Groups/{product_group_name.title()}_inf.txt","r")
        self.products_inf_in=self.products_inf.readlines()
        self.products_inf.close()# read file and creat arry
        
        if int(self.products_inf_in[5+(index*15)+6].split("\\n")[0])>=int(number_of_product):#check useability
            self.new_value=int(self.products_inf_in[5+(index*15)+6].split("\\n")[0])-int(number_of_product)
            
            if self.new_value==0:
                market.Add_Statistic(product_group_name,index,number_of_product,0)
     
            else:
                
                self.products_in=open(f"Shop/Groups/Products/{product_group_name.title()}.txt","r")
                self.products_in_inf=self.products_in.readlines()
                self.products_in.close()# read file and creat arry

                self.products_in=open(f"Shop/Groups/Products/{product_group_name.title()}.txt","w")
                
                for i in self.products_in_inf[int(number_of_product)*12:]:
                    self.products_in.write(i)
                self.products_in.close()# write file
                
                
                self.pre_products_inf_in=self.products_inf_in[:5+(index*15)+6]# value range
                self.pre_products_inf_in.append(str(self.new_value)+"\n")
                self.next_products_inf_in=self.products_inf_in[5+(index*15)+7:]# value range
                
                for i in self.next_products_inf_in:
                    self.pre_products_inf_in.append(i)# append to arry
                    
                try:
                    self.products_inf=open(f"Shop/Groups/{product_group_name.title()}_inf.txt","w")
                    
                    for i in self.pre_products_inf_in:
                        self.products_inf.write(i)
                    self.products_inf.close()
                    
                except:
                    messagebox.showerror("Error Message","Something went wrong, you are redirected to the home screen!")
                    screen.Main_Desing()
                    
                market.Add_Statistic(product_group_name,index,number_of_product,1)
                #write file
        else:
            self.products_inf.close()
            messagebox.showerror("Error Message","You wanted more products than the number of products in stock, number of products in the stock: {}".format(self.products_inf_in[5+(index*15)+6].split('\n')[0]))
            screen.Product_Sale_Desing()
    
        
        screen.Product_Sale_Desing()

        
    def Add_Statistic(self,product_group_name,index,number_of_product,d):
        if d==1:# sale type
            self.products=open(f"Shop/Groups/{product_group_name.title()}_inf.txt","r")
            self.products_in=self.products.readlines()
            self.products.close()#read file and creat arry
            self.statistics_inf=open(f"Shop/Statistics/statistics.txt","a")
            self.gain=(int(self.products_in[3+(index*15)+6].split("\\n")[0])-int(self.products_in[1+(index*15)+6].split("\\n")[0]))*int(number_of_product)
            self.statistics_inf.write(f"\n\n***\n\nProduct Group Name\n{product_group_name.title()}\nTotal Gain\n{self.gain}\n\n***")
            self.statistics_inf.close()#calculation and write to file
                        
        elif d==0:# sale type
            
            self.products=open(f"Shop/Groups/{product_group_name.title()}_inf.txt","r")
            self.products_in=self.products.readlines()
            self.products.close()#read file and creat arry
            
            self.statistics_inf=open(f"Shop/Statistics/statistics.txt","a")
            self.gain=(int(self.products_in[3+(index*15)+6].split("\\n")[0])-int(self.products_in[1+(index*15)+6].split("\\n")[0]))*int(number_of_product)
            print(self.products_in[3+(index*15)+6].split("\\n")[0])
            print(self.products_in[1+(index*15)+6].split("\\n")[0])
            self.statistics_inf.write(f"\n\n***\n\nProduct Group Name\n{product_group_name.title()}\nTotal Gain\n{self.gain}\n\n***")
            self.statistics_inf.close()#calculation and write to file
            
            os.remove(f"Shop/Groups/{product_group_name.title()}_inf.txt")
            os.remove(f"Shop/Groups/Products/{product_group_name.title()}.txt")# remove the useless files
            
        self.dummy_gain_arr[0]=self.gain
        self.statistics_inf=open(f"Shop/Statistics/Product_Statistics/{product_group_name}_statistics.txt","w")
        self.statistics_inf.write(f"\n\n***\n\nProduct Group Name\n{product_group_name.title()}\nTotal Gain\n{self.dummy_gain_arr[0]+self.dummy_gain_arr[1]}\n\n***")
        self.statistics_inf.close()
        self.dummy_gain_arr[1]=self.gain# for draw statistics
        

    def Draw_Graphics(self,c):
        screen.window.destroy()
        self.statistics_inf=open("Shop/Statistics/statistics.txt","r")
        self.statistic_inf_in = self.statistics_inf.readlines()#read file and creat arry
        if len(self.statistic_inf_in)>0:
            
            if c==0:
                
                plt.xlabel="Number of Months"
                plt.ylabel="Gain"
                plt.plot(self.months,self.gains)
                plt.grid(True)
                plt.show()#draw statistics
                
                screen.Window_Creat()
                screen.Main_Desing()# back to the main
                    
            elif c==1:
                
                screen.Window_Creat()
                self.Lb1 = tk.Listbox(screen.window)
                self.Lb1.config(height="6",width="10",bg="red",fg="white",font="bold")
                self.Lb1.place(x=0,y=0)
                self.Lb2 = tk.Listbox(screen.window)
                self.Lb2.config(height="6",width="10",bg="black",fg="white",font="bold")
                self.Lb2.place(x=200,y=0)
                btn_back=tk.Button(screen.window,text="Back",command= screen.View_Statistic_Desing)
                btn_back.place(x=130,y=40)# creat desing
        
                self.statistics_inf.seek(0)
                self.statistic_inf_in = self.statistics_inf.readlines()
                self.statistics_inf.close()
                
                for i in range(len(self.statistic_inf_in)-1):
                    try:
                        self.Lb1.insert(1,self.statistic_inf_in[5+(i*9)])
                        self.Lb2.insert(1,self.statistic_inf_in[7+(i*9)])# add data to listbox
                        
                    except:
                        break
        else:
            messagebox.showerror("Error Message","Something went wrong, you are redirected to the home screen.")
            screen.Main_Desing()
        
            
        
        
    def End_Month(self):
        
        self.month_number+=1
        dirList=os.listdir(r"Shop\Statistics\Product_Statistics\\")
        gain_list=[]
        data_list=[]
        total_gain=0#short-lived variable identification
        for l_n in dirList:
            if l_n!="Months_Gain":# useless name check
                
                self.statistic_IN=open(f"Shop/Statistics/Product_Statistics/{l_n}","r")
                self.statistic_INF=self.statistic_IN.readlines()#read file and creat arry
                self.statistic_IN.close()
                
                data_list.append(self.statistic_INF)
                gain_list.append(self.statistic_INF[7].split('\n')[0])#get datas
                
                os.remove(f"Shop/Statistics/Product_Statistics/{l_n}")#remove the useless files
            
            
            
        move_data=open(f"Shop/Statistics/Product_Statistics/Months_Gain/{self.month_number}M_Gain.txt","w")
        for data in data_list:
            for i in data:
                move_data.write(i)
        move_data.close()# write file
        
        
        
        for g in gain_list:
            total_gain+=int(g)
            #calculation total gain
                   
        self.month_gain_arr.append([self.month_number,total_gain])
        self.months=[]
        self.gains=[]#special varibles
        for i in self.month_gain_arr:
            self.months.append(i[0])
        for i in self.month_gain_arr:
            self.gains.append(i[1])
        # add functions

            
        v=tk.IntVar()
        R3 = tk.Radiobutton(screen.window, text="View Statistics",value=3,variable=v,command=screen.View_Statistic_Desing)
        R3.place(x=90,y=65)#add radiobutton
        
    def Quit(self,group_ID):
        ID_s=open("Shop/ID_s.txt","w")
        ID_s.write("{}\n0".format(group_ID.split('\n')[0]))#save last ID
        ID_s.close()
        messagebox.showinfo("Information Message","All data has been saved, the application is closing.")
        screen.window.destroy()
        
class Screen():
    def __init__(self):
        
        self._group_ID=group_ID
        
    def Window_Creat(self):
        
        self.window=tk.Tk()
        self.window.title("EVO SUPER MARKET CHIN")
        self.window.geometry("300x110")# creat window

    def Product_Add_Function(self):
        
        self._group_ID=str(int(self._group_ID[0])+1)+"G"
        try:
            market.Add_Product(self.ent_product_group.get(),self._group_ID,self.ent_product_name.get(),self.ent_product_purchase_price.get(),self.ent_product_sale_price.get(),self.ent_product_number_of_product.get())
            screen.Product_Add_Desing()# give the values and call Product Add screen

        except:
            messagebox.showerror("Error Message","Something went wrong, you are redirected to the home screen.")
            screen.Main_Desing()
            
    def Product_Sale_Function(self,product_group_name):
        
        self.product_group_names=open(f"Shop\Groups\{product_group_name.title()}_inf.txt","r")
        self.products_name_arr=self.product_group_names.readlines()# read file and creat arry
        
        if len(self.products_name_arr)>0:# checking the availability of data
            self.Lb1.delete(0,"end")#clear listbox
            
            for name_number in range(len(self.products_name_arr)-1):
                try:
                    self.Lb1.insert(1, self.products_name_arr[5+(name_number*15)])#add item
                except:
                    break
            
            self.product_group_names.close()
            self.ent_product_number_of_product.place(x=100,y=20)
            self.label.place(x=100,y=0)#visble on
            try:
                self.btn_save.config(text="Sale",command=lambda:market.Sale_Product(product_group_name,self.Lb1.get("active"),self.Lb1.index(self.Lb1.curselection()),self.ent_product_number_of_product.get()))
                # give the values
            except:
                messagebox.showerror("Error Message","Something went wrong, you are redirected to the home screen.")
                screen.Main_Desing()
        else:
            messagebox.showinfo("Information Message","Not found a data, you are redirected to the home screen.")
            screen.Main_Desing()     
            
    def Product_Add_Desing(self):
        
        self.window.destroy()
        screen.Window_Creat()
        
        label = tk.Label(self.window,text = "Product Group",background='#101010',foreground="#D6D6D6")
        label.grid(column=0,row=0)
        
        label = tk.Label(self.window,text = "Product Name",background='#101010',foreground="#D6D6D6")
        label.grid(column=0,row=2)
        
        label = tk.Label(self.window,text = "Purchase Price",background='#101010',foreground="#D6D6D6")
        label.grid(column=0,row=4)
        
        label = tk.Label(self.window,text = "Sale Price",background='#101010',foreground="#D6D6D6")
        label.grid(column=0,row=6)
        
        label = tk.Label(self.window,text = "Number Of Product",background='#101010',foreground="#D6D6D6")
        label.grid(column=0,row=8)

        self.ent_product_group=tk.Entry(self.window)
        self.ent_product_group.grid(column=1,row=0)

        self.ent_product_name=tk.Entry(self.window)
        self.ent_product_name.grid(column=1,row=2)
        
        self.ent_product_purchase_price=tk.Entry(self.window)
        self.ent_product_purchase_price.grid(column=1,row=4)
        
        self.ent_product_sale_price=tk.Entry(self.window)
        self.ent_product_sale_price.grid(column=1,row=6)
        
        self.ent_product_number_of_product=tk.Entry(self.window)
        self.ent_product_number_of_product.grid(column=1,row=8)

        btn_add=tk.Button(self.window,text="Add",command=screen.Product_Add_Function)
        btn_add.place(x=260,y=10)

        btn_main=tk.Button(self.window,text="Main",command=screen.Main_Desing)
        btn_main.place(x=260,y=50)# Product Add Desing

    def Product_Sale_Desing(self):

        dirList=os.listdir(r"Shop\Groups\\")#this function reads the file names in the specified path
        
        if len(dirList)>1:
            self.window.destroy()
            screen.Window_Creat()
            self.Lb1 = tk.Listbox(self.window)
            for dic in dirList:
                if dic!="Products":#check useless name
                    self.Lb1.insert(1, dic.split("_")[0])
            self.Lb1.config(height="6",width="10",bg="red",fg="white",font="bold")
            
            self.Lb1.place(x=0,y=0)

            self.label = tk.Label(self.window,text = "Number Of Product",background='#101010',foreground="#D6D6D6")
            self.label.place_forget()
            
            self.ent_product_number_of_product=tk.Entry(self.window)
            self.ent_product_number_of_product.place_forget()# Entry's visible off
            
            try:
                self.btn_save=tk.Button(self.window,text="Select",command=lambda: screen.Product_Sale_Function(self.Lb1.get("active")))
                self.btn_save.place(x=260,y=0)# give the values
            except:
                messagebox.showerror("Error Message","Something went wrong, you are redirected to the home screen.")
                screen.Main_Desing()
                
            btn_main=tk.Button(self.window,text="Main",command= screen.Main_Desing)
            btn_main.place(x=260,y=40)
            
        else:
            messagebox.showinfo("Information Message","You haven't any products.")
            screen.Main_Desing()

           
        
    def View_Statistic_Desing(self):

        screen.window.destroy()
        screen.Window_Creat()

        btn_product_view=tk.Button(self.window,text="Total Gain Tablo",command= lambda:market.Draw_Graphics(0))
        btn_product_view.place(x=200,y=40)
        
        btn_total_gain=tk.Button(self.window,text="Sold Products",command= lambda: market.Draw_Graphics(1))
        btn_total_gain.place(x=0,y=40)

        btn_main=tk.Button(self.window,text="Main",command=lambda:screen.Main_Desing())
        btn_main.place(x=125,y=70)
        #View Statistic Desing
        
        
    def Main_Desing(self):
        
        self.quoatations_arr=["The number one principle of sales ethics is this: A sale that does not benefit the buyer brings harm to the seller.",

"Sales advisors should avoid the centrist way of speaking. No matter how humble you speak, this kind of speech is repulsive.",

"As a sales consultant, you have to convince your customer. To achieve this, you must first believe in the value of the product you offer, the superiority of the company you represent, and your own talent.",

"Hurry is only for catching flies. Russian word",

"Our confession of our minor flaws is to make everyone believe that we have no major flaws. La Rochefoucauld",

"Always say it right so that you don't have to remember what you said. T.L.Osborn",

"Managing just for profit is like playing tennis by looking at the leaderboard. Ichak Adizes",

"But fools and dead never change their minds. J.R.Cowell"]#advice list
        
        self.window.destroy()
        screen.Window_Creat()
        
        label = tk.Label(self.window,text = "Please Select Operation",background='#101010',foreground="#D6D6D6")
        label.place(x=90,y=0)
        
        button=tk.Button(self.window,text="i",command= lambda:messagebox.showinfo("Info Message",self.quoatations_arr[random.randint(0,len(self.quoatations_arr)-1)]))
        button.place(x=285,y=85)

        button=tk.Button(self.window,text="End Month",command=market.End_Month)
        button.place(x=110,y=85)

        button=tk.Button(self.window,text="Quit",command=lambda:market.Quit(self._group_ID))
        button.place(x=250,y=0)
        
        v=tk.IntVar()
        R1 = tk.Radiobutton(self.window, text="Add Product",value=1,variable=v,command=screen.Product_Add_Desing)
        R1.place(x=90,y=25)
        R2 = tk.Radiobutton(self.window, text="Sale Product",value=2,variable=v,command=screen.Product_Sale_Desing)
        R2.place(x=90,y=45)#Main Desing
        
        self.window.mainloop()
        
 
if __name__ == "__main__":
    
    ID()
    screen=Screen()
    market=Product_Operations()

    screen.Window_Creat()
    screen.Main_Desing()
   
#dirList https://www.ozban.com/python-ile-dosya-ve-klasor-listeleme
#State https://stackoverflow.com/questions/20983309/how-to-enable-disable-tabs-in-a-tkinter-tix-python-gui
#Lb1 index https://stackoverflow.com/questions/47580444/python-tkinter-listbox-getting-index
# Quoatations https://www.biymed.com/forum/isyonetimi/satisuzerine-ozlu-sozler-13643.html,translate Google Translate
#Hide Object http://python.6.x6.nabble.com/Tutor-Showing-hiding-widgets-in-Tkinter-td1755056.html
# Delete file https://python-ogren.readthedocs.io/en/latest/file_remove.html
