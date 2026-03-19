
#-------------------------------------------------------------------------------------------------------------
# Imported Libraries and CSV Files
#-------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
df=pd.read_csv("Updated CSV1-copy.csv")
locationcsv=pd.read_csv("UPLocations.csv")
print(df)

#-------------------------------------------------------------------------------------------------------------
#Functions For Displaying The Main Menu
#-------------------------------------------------------------------------------------------------------------
def Menuset():
    ans='y'
    while ans=='y' or ans=='Y':
        print("\t\t=============================")
        print("\t\t   Air Polloution in Delhi   ")
        print("\t\t=============================")
        print("\t\t1: Data Manipulation Menu\n")
        print("\t\t2: Data Analysis Menu\n") 
        print("\t\t3: Data Visualization Menu\n")
        print("\t\t4: Exit Menu\n")
        print("\t\t=============================")
        opt=input("\t\tEnter your choice: ")
        if opt=='1':
            manipulation()
        elif opt=='2':
            analysis()
        elif opt=='3':
            display()
        elif opt=='4':
            chance=input("Are You Sure to exit(Y/N)")
            print('THANK You. Closing now....')
            sys.exit()
        else :
            print('Invalid option. Try Again')
            continue



#--------------------------------------------------------------------------------------------------------------
# For data manipulation
#-------------------------------------------------------------------------------------------------------------
def manipulation():
    while True:
        global df1
        df1=pd.DataFrame()
        print("\t\tManipulation Menu")
        print("\t\t*****************")
        print('''\t\t1. Insert Details of Area-wise Air Quality parameters\n
    \t\t2. Delete Details\n
    \t\t3. Delete a specific air quality parameter\n
    \t\t4. Go back to main menu\n''')
        x2=int(input("\t\tEnter your choice: "))
        if x2==1:
            col=df.columns
            print(col)
            print(df.head(1))
            p=0
            lst1=[]
            lst1=eval(input('Enter a list of values according to the columns: '))
            print(lst1)         
            '''s1=pd.Series(lst1)
            print(s1)
            s1=s1.T
            print(s1)'''
            #df1=df.append(s1,ignore_index=True)
            '''df1=df.append(lst1,ignore_index=True)'''
            count=len(df.index.values)
            df.loc[count,:]=lst1
            print('Insertion Completed !!!!')
            print(df)
        elif x2==2:
            print(df)
            x3=int(input('Enter the row index you want to delete: '))
            df1=df.drop(x3)
            print('Row No.',x3+1,' is deleted')
            print(df1)
        elif x2==3:
            print(df.columns)
            p2=input('Enter the Column Name you want to delete: ')
            w1=input('Are you Sure to delete(Y,N)')
            if w1=='y' or w1=='Y':
                del df[p2]
                print('Column:',p2,'has been deleted successfully')
                df2=pd.DataFrame()
                df2=df
                print(df2)
        elif x2==4:
            break
           

#-------------------------------------------------------------------------------------------------------------
# For Analysis of Data
#-------------------------------------------------------------------------------------------------------------
def analysis():
    while True:
        print("\t\tData Frame Analysis")
        print("\t\t~~~~~~~~~~~~~~~~~~~~~~~")
        menu=''' \t\t1. Top record
                \n\t\t 2. Bottom Records
                \n\t\t 3. To Print Specific column
                \n\t\t 4. To Print multiple columns
                \n\t\t 5. To display station details according to highest NO2 content
                \n\t\t 6. To display station details according to lowest rspm parameter
                \n\t\t 7. To Display complete statitics of the dataframe
                \n\t\t 8. To Display complete information about dataframe
                \n\t\t 9.To go back'''
        print(menu)
        opt1=int(input('\t\tEnter Your Choice : '))
        if opt1==1:
            p3=int(input('Enter the No. of records you want to see: '))
            print('Top',opt1,'records')
            print(df.head(p3))
        elif opt1==2:
            p4=int(input('Enter the No. of records you want to see: '))
            print('Bottom',opt1,'records')
            print(df.tail(p4))
        elif opt1==3:
            print('Name of column\n',df.columns)
            p5=input('Enter the Column name to be displayed: ')
            print(df[p5])
        elif opt1==4:
            print('Name of the columns\n',df.columns)
            p6=eval(input('Enter the column names as list in square brackets[]: '))
            print(df[p6])
        elif opt1==5:
            print('Original Dataframe is')
            print(df)
            df1=df.sort_values(by='no2', ascending=False)
            print('station details according to highest NO2 content is')
            print(df1)          
        elif opt1==6:
            print('Original Dataframe is')
            print(df)
            df1=df.sort_values(by='rspm', ascending=True)
            print('station details according to highest NO2 content is')
            print(df1)           
        elif opt1==7:
            print('Statistics of the database: ')
            print(df.describe())
        elif opt1==8:
            print('Information About The Database: ')
            print(df.info())
        elif opt1==9:
             break

#-------------------------------------------------------------------------------------------------------------
# For displaying Data Visualisation Menu
#-------------------------------------------------------------------------------------------------------------
def display():
    
    while True:
        print()
        print("\t\t=========================")
        print("\t\t Data Visualisation Menu ")
        print("\t\t=========================")
        print("\t\t1: Line Chart Representation of SO2 and NO2 content of specific station")
        print("\t\t2: Line chart Representation of RSPM of specific location")
        print("\t\t3: Bar chart Representation of SO2 and NO2 of specific station ")
        print("\t\t4: Bar Chart Representation of RSPM of specific location")
        print("\t\t5: Back")
        opt1=input("\t\tEnter your choice: ")
        if opt1=='1':
            line_chart()
        elif opt1=='2':
            Line_chart2()
        elif opt1=='3':
            Bar_chart()
        elif opt1=='4':
            Bar_chart2()
        elif opt1=='5':
            print("Going Back to Main Menu....")
            break
        else:
            print("Invalid input Try again")
            

#--------------------------------------------------------------------------------------------------------------
# Displaying Bar chart of RSPM
#-------------------------------------------------------------------------------------------------------------
def Bar_chart2():
    print("Available Locations In New Delhi")
    h=locationcsv['location']
    print(h)
    V=df.groupby('location')
    cname=input("Enter Location Name: ")
    df1=df.loc[(df['location']==cname)]
    x=np.arange(len(df1))
    if df1.empty!=True:
        dt=df1['Date']
        gas3=df1['rspm']
        plt.bar(x,gas3,label='RSPM',width=0.75,color='m')
        plt.xticks(x,dt,fontsize=6,rotation=90)
        plt.title('AIR POLLOUTION IN DELHI\nLevel Of Components\n',color='m',fontsize=13)
        plt.xlabel('Date of Reading->',color='m')
        plt.ylabel('RSPM ->>',color='m',fontsize=12)
        plt.grid()
        plt.legend()
        plt.show()
       
#-------------------------------------------------------------------------------------------------------------
# For displaying Bar Chart of So2 and No2
#-------------------------------------------------------------------------------------------------------------
def Bar_chart():
    print("Available Locations In New Delhi")
    h=locationcsv['location']
    print(h)
    V=df.groupby('location')
    cname=input("Enter Location Name: ")
    df1=df.loc[(df['location']==cname)]
    x=np.arange(len(df1))
    if df1.empty!=True:
        dt=df1['Date']
        gas1=df1['so2']
        gas2=df1['no2']
        plt.bar(x-0.25,gas1,label='SO2',width=0.5,color='r')
        plt.bar(x+0.25,gas2,label='NO2',width=0.5,color='g')
        plt.xticks(x,dt,fontsize=6,rotation=90)
        plt.title('AIR POLLOUTION IN DELHI\nLevel Of Components\n',color='blue',fontsize=12)
        plt.xlabel('Date of Reading->',color='g')
        plt.ylabel('SO2 and NO2->',color='g',fontsize=12)
        plt.legend()
        plt.grid()
        plt.show()
        

#------------------------------------------------------------------------------------------------------------
# For displaying Line chart of So2 and No2
#-------------------------------------------------------------------------------------------------------------
def line_chart():
    while True:
        X=[]
        V=df.groupby('location')
        print("Available Locations In New Delhi")
        h=locationcsv['location']
        print(h)
        cname=input("Enter Location Name: ")
        df1=df.loc[(df['location']==cname)]
        if df1.empty!=True:
            dt=df1['Date']
            l=np.arange(len(dt))
            y1=df1['so2']
            y2=df1['no2']
            plt.plot(l,y1,label="Level OF SO2",linestyle='solid',marker='^')
            plt.plot(l,y2,label="Level OF NO2",linestyle='solid',marker='o')
            plt.xticks(l,dt,fontsize=6,rotation=90)
            plt.xlabel("Date of Reading->",color='r')
            plt.ylabel("SO2 and NO2->",color='r',fontsize=12)
            plt.title('AIR POLLOUTION IN DELHI\nLevel Of Components\n'+cname,color='blue',fontsize=12)
            plt.grid()
            plt.legend()
            plt.show()
            break
        else:
            print("City Name is incorrect.")
            print("Please Check again and retry")
#-------------------------------------------------------------------------------------------------------------
# For displaying Line Chart of RSPM
#-------------------------------------------------------------------------------------------------------------
def Line_chart2():
    while True:
        X=[]
        V=df.groupby('location')
        print("Available Locations In New Delhi")
        h=locationcsv['location']
        print(h)
        cname=input("Enter Location Name: ")
        df1=df.loc[(df['location']==cname)]
        if df1.empty!=True:
            dt=df1['Date']
            l=np.arange(len(dt))
            y3=df1['rspm']
            plt.plot(l,y3,label="Level OF RSPM",linestyle='solid',marker='^')
            plt.xticks(l,dt,fontsize=7,rotation=90)
            plt.title('AIR POLLOUTION IN DELHI\nLevel Of Components\n'+cname,color='blue',fontsize=12)
            plt.xlabel("Date of Reading->",color='r')
            plt.ylabel("RSPM->",color='r',fontsize=12)
            plt.legend()
            plt.grid()
            plt.show()
            break
        else:
            print("City Name is incorrect.")
            print("Please Check again and retry")



 
Menuset()

#--------------------------------------------------------------------------------------------------------------
