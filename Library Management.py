
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def menu():
    print()
    print("        Library Management System")
    print()
    print("Member1 CSV File")
    print("     1.Read csv file-member")
    print("     2.Add new member in member file")
    print("     3.Search Member")
    print("     4.Delete a member")
    print("     5.Display member name in Ascending order")
    print("Book1 CSV File")
    print("     6.Read 2 records from top and 2 from bottom-member")
    print("     7.Modify data")
    print("     8.Add new book record in Book1 file")
    print("     9.Show Books file")
    print("     10.Publisher in Descending order")
    print("     11.Read CSV file - book1")
    print("     12.Find total books in Library")
    print("     13.Save changes in Book1 file")
    print("     14.Save changes in Member file") 
    print("     15.Searchbook")
    print("     16.Delete a book")
    print("     17.Issue Books")
    print("     18.Return book")
    print("     19.show issued books")
    print("Data Visualisation")
    print("     20.Line Plot")
    print("     21.Bar Plot")
    print("     22.Hist chart")
menu()

def member():
    print("Reading File Book1")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    print(df) 
    
def new_member():
    print("Adding new member in File member")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    print(df)
    ans='yes'
    while ans=='yes' or ans=='Yes':           
        MemberID=int(input("Enter the member id: "))
        Name=input("Enter the name: ")
        PhoneNo=int(input("Enter the phone number: "))
        Address=input("Enter the address: ")
        Class=input("Enter the class of student: ")
        issue_status="No"      
        n=df["MemberID"].count()
        df.at[n]=[MemberID, Name, PhoneNo, Address, Class, issue_status]
        df.to_csv(path_or_buf="C:\\Users\\itsgo\\Downloads\\Member12.csv", index=False )
        print("Member added successfully")
        ans=input("Do you want to add more books?")
    print(df)
    
    
def search_member():
    MemberID=int(input("Enter the member id: "))
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    df1=df.loc[df["MemberID"]==MemberID]
    if df1.empty:
        print("No member found with given id")
    else:
        print("Member details are: ")
        print(df1)
    
    
def delete_member():
    MemberID=int(input("Enter the member id: "))
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    bdf=df.drop(df[df["MemberID"]==MemberID].index)
    df=df.to_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv", index=False)
    print("Member deleted successfully")
    print(bdf)
    
def sort_member():
    print("Sorting members name in Ascending order")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv",index_col=0)
    df=df.sort_values('Member_Name',ascending=True)
    print(df)
    
def top_bottom():
    print("Top 2 records and Last 2 records")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    print('Top 2 rows')
    print(df.head(2))
    print()
    print('Last 2 rows')
    print(df.tail(2))
    
def modify():
    print("Enter-1: To modify book file ")
    print("Enter-2: To modify member file")
    opt=int(input("Enter the choice: "))
    if opt==1:  
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        print(df)
        ans='yes'
        BookID=0
        while ans=='yes' or ans=='Yes':
            BookID=int(input("Enter Book id :"))
            if BookID in df['BookID'].values:            
                a=input("Enter the column name to change: ")
                b=(input("Enter it's value: if string in quotes(''): "))
                df.loc[(df['BookID'] == BookID),a]=b
                print("Book id -",BookID,"has been updated successfully...")
                print(df.loc[df['BookID']==BookID])
            else:         
                print("Book is not found...")
            df.to_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv",index=False)
            ans=input("Do you want to edit more books?") 
        print(df)
    if opt==2:
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
        print(df)
        ans='yes'
        MemberID=0
        while ans=='yes' or ans=='Yes':
            MemberID=int(input("Enter Member id :"))
            if MemberID in df['MemberID'].values:            
                a=input("Enter the column name to change: ")
                b=(input("Enter it's value: if string in quotes(''): "))
                df.loc[(df['MemberID'] == MemberID),a]=b
                print("Member id -",MemberID,"has been updated successfully...")
                print(df.loc[df['MemberID']==MemberID])
            else:         
                print("Member is not found...")
            df.to_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv",index=False)
            ans=input("Do you want to edit more member details?") 
        print(df)
    
def add_book():
    print("Adding new book record in book1 file")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    print(df)
    ans='yes'
    while ans=='yes' or ans=='Yes':   
        BookID=int(input("Enter the book id: "))
        Bname=input("Enter the book name: ")
        Price=int(input("Enter the Price: "))
        Copies=1
        No_of_times_book_issued=input("Enter the No_of_times_book_issued: ")
        Edition=int(input("Enter the edition of the book: "))
        n=df["BookID"].count()
        df.at[n]=[BookID, Bname, Price, Copies,No_of_times_book_issued, Edition ]
        df=df.to_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv",index=False)
        print("Book added successfully")
        ans=input("Do you want to add more books?")
    print(df)
 
def book_name():
    print("Show Books list")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv",usecols=['Bname'])
    print(df)
    
def sort_book():
    print("Show Book name in descending order")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    df=df.sort_values('Bname',ascending=False)
    print(df)
    
def book1():
    print("Reading File Book")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    print(df)
    
def Totalbooks():
    print("Find Total Books in Library")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    Totalbooks=df['Copies'].sum()
    print(Totalbooks)
    
def changes_book1():
    m=input("Enter the column name you want to add: ")
    n=int(input("Enter the data: "))
    print("Save changes in Book1 file")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    df[m]=n
    print(df)
    df=df.to_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    
def changes_member1():
    m=input("Enter the column name you want to add: ")
    n=int(input("Enter the data: "))
    print("Save changes in Member1 file")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")   
    df[m]=n
    print(df)
    df=df.to_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    
def searchbook():
    Bname=input("Enter the book name: ")
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    df1=df.loc[df["Bname"]==Bname]
    if df1.empty:
        print("No book found with given name")
    else:
        print("Book details are: ")
        print(df1)
        
def delete_book():
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    print(df)
    BookID=int(input("Enter the book id: "))
    mdf=df.drop(df[df["BookID"]==BookID].index())
    df=df.to_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv", index=False)
    print("Book deleted successfully")
    print(mdf)
    
def issue_book():
    dfbooks=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    dfmembers=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    dfbook=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book2.0.csv")
    ans='yes'
    while ans=='yes' or ans=='Yes':     
        Mid=int(input("Enter Member id: "))
        Bid=int(input("Enter Book id to be issued: "))
        if Mid in dfmembers['MemberID'].values:
            print(dfmembers.loc[dfmembers.MemberID==Mid,['Member_Name']])
            istatus=dfmembers.loc[dfmembers['MemberID'] == Mid,
            'issue_status'].values[0]
            if (istatus=='no' or istatus=='No'):
                if Bid in dfbooks['BookID'].values:                    
                    print(dfbooks.loc[dfbooks.BookID==Bid,['Bname','Copies']])
                    cpy=dfbooks.loc[dfbooks['BookID'] == Bid, 'Copies'].values[0]
                    if cpy>0:
                        dt_iss=input("Please Enter date of Issue(dd/mm/yyyy): ")
                        data=[Bid,Mid,dt_iss,np.NaN]
                        dfbook.loc[len(dfbook)]=data
                        dfmembers.loc[dfmembers.MemberID == Mid,'issue_status']='Yes'
                        dfbooks.loc[dfbooks.BookID == Bid, 'Copies']-=1
                        print("Book Issued Successfully...")
                    else:
                        print("Sorry ! No. of copy is insufficent in the Library..")
                else:
                    print("Book is not found...")            
            else:                
                print("Sorry!...1-Book Already issued. First return it")
        else:
            print("Member is not found...")
        dfbook.to_csv("C:\\Users\\itsgo\\Downloads\\Book2.0.csv",index=False)
        dfbooks.to_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv",index=False)
        dfmembers.to_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv",index=False)
        ans=input("Do you want to issue more books?")
    print(dfbook)
    
def return_book():
    dfbooks=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
    dfmembers=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv")
    dfbook=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book2.0.csv")
    print(dfbook)
    ans='yes'
    while ans=='yes' or ans=='Yes':    
        Mid=int(input("Enter Member id: "))
        if Mid in dfbook['MemberID'].values:         
            dt_is=input("Date of Issue: ")
            dt_rtn=input("Enter Date of Return: ")
            Bid=dfbook.loc[(dfbook['MemberID'] == Mid) & (dfbook['date_of_issue']== dt_is ), 'BookID'].values[0]
            cond=(dfmembers.MemberID==Mid) & (dfmembers.issue_status=='Yes')
            if cond.any():           
               dfbook.loc[(dfbook['MemberID'] == Mid) & (dfbook['date_of_issue'] ==dt_is ), 'date_of_return']=dt_rtn
               dfmembers.loc[dfmembers.MemberID == Mid, 'issue_status']='No'
               dfbooks.loc[dfbooks.BookID == Bid, 'Copies']+=1
               n=int(input("No. of days book has been issued: "))
               if n>7:
                   fine=(n-7)*10.00
               else:
                   fine=0.00
               print("Please Pay Fine Rs.",fine)
               print("Book Returned Successfully...")
            else:           
                print("The book is already returned.. Action denied")
        else:
            print("Member is not found...")
        dfbook.to_csv("C:\\Users\\itsgo\\Downloads\\Book2.0.csv",index=False)
        dfbooks.to_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv",index=False)
        dfmembers.to_csv("C:\\Users\\itsgo\\Downloads\\Member12.csv",index=False)
        ans=input("Do you want to Return more books?")
    print(dfbook)
                
def show_issuedbooks():
    df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book2.0.csv")
    print(df)
    
                
def line_chart():
        print('Line Plot(Book name and their copies)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","Copies"]]
        df.plot("Bname","Copies",kind='line',color='red',linewidth='2',linestyle='dotted')
        plt.xlabel('Bname')
        plt.ylabel('Copies')
        plt.title('Bname and their copies')
        plt.show()  
    

def bar_chart():
    print("Press 1-Books and their price")
    print("Press 2-Bname and their copies")
    print("Press 3-Bname and numbers of times it is issued")
    opt=int(input("Enter the choice: "))
    if opt==1:
        print('Bar Plot(Book vs Price)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","Price"]]
        df.plot("Bname","Price",kind='bar',color='green',linewidth='5',linestyle='dashdot')
        plt.xlabel('Books')
        plt.ylabel('Price')
        plt.title('Books vs Price')
        plt.show() 
    if opt==2:
        print('Bar Plot(Bname vs Copies)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","Copies"]]
        df.plot("Bname","Copies",kind='bar',color='red',linewidth='5',linestyle='dotted')
        plt.xlabel('Bname')
        plt.ylabel('Copies')
        plt.title('Bname and their copies')
        plt.show()   
    if opt==3:
        print('Bar Plot(No. of times books issued vs Bname)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","No. of times book issued"]]
        df.plot("Bname","No. of times book issued",kind='bar',color='Magenta',linewidth='4',linestyle='dashed')
        plt.xlabel('Book_Name')
        plt.ylabel('No. of times books issued')
        plt.title('No. of times books issued vs Book_Name')
        plt.show()
        
def hist_chart():
    print("Press 1-Books and their price")
    print("Press 2-Bname and their copies")
    print("Press 3-Bname and numbers of times it is issued")
    opt=int(input("Enter the choice: "))
    if opt==1:
        print('Hist Plot(Book vs Price)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","Price"]]
        df.plot("Bname","Price",kind='hist',edgecolor='green',linewidth='2',linestyle=':',fill=False,hatch="o")
        plt.xlabel('Books')
        plt.ylabel('Price')
        plt.title('Books vs Price')
        plt.show() 
    if opt==2:
        print('Hist Plot(Bname vs Copies)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","Copies"]]
        df.plot("Bname","Copies",kind='hist',color='red',linewidth='5',linestyle='dotted')
        plt.xlabel('Bname')
        plt.ylabel('Copies')
        plt.title('Bname and their copies')
        plt.show()   
    if opt==3:
        print('Hist Plot(No. of times books issued vs Book_Name)')
        df=pd.read_csv("C:\\Users\\itsgo\\Downloads\\Book5.csv")
        df=df[["Bname","No. of times book issued"]]
        df.plot("Bname","No. of times book issued",kind='hist',edgecolor='Magenta',linewidth='2',linestyle='--',fill=False,hatch="o")
        plt.xlabel('Book name')
        plt.ylabel('No. of times books issued')
        plt.title('No. of times books issued vs Book_Name')
        plt.show()

 
opt=""
opt=int(input("Enter the Choice:"))
if opt==1:
    member()
elif opt==2:
    new_member()
elif opt==3:
    search_member()
elif opt==4:
    delete_member()
elif opt==5:
    sort_member()
elif opt==6:
    top_bottom()
elif opt==7:
    modify()
elif opt==8:
    add_book()
elif opt==9:
    book_name()
elif opt==10:
    sort_book()
elif opt==11:
    book1()
elif opt==12:
    Totalbooks()
elif opt==13:
    changes_book1()
elif opt==14:
    changes_member1()
elif opt==15:
    searchbook()
elif opt==16:
    delete_book()
elif opt==17:
    issue_book()
elif opt==18:
    return_book()
elif opt==19:
    show_issuedbooks()
elif opt==20:
    line_chart()
elif opt==21:
    bar_chart()
elif opt==22:
    hist_chart()
else:
    print('Invalid Option')
    
print("*************Thank You***************")
    
    
