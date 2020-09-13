import pyodbc
import getpass
import datetime
import matplotlib.pyplot as plt
driverlist=pyodbc.drivers()
j=1
print("Hi there! Based on the SQL client, the driver might vary... So please select appropriate driver to continue")
for i in driverlist:
    print (str(j)+"."+i)
    j=j+1
driverselect=int(input())
driver=driverlist[driverselect-1]
print("Driver is ready! Please enter the server name")
server=str(input())
print("Please enter the database")
database=str(input())
print("Please enter the username")
username=str(input())
password=getpass.getpass()
connection=pyodbc.connect("DRIVER={"+driver+"}; SERVER="+server+";DATABASE="+database+"; UID="+username+"; PASSWORD="+password+";")
queryexecutor=connection.cursor()
print("Please enter the query to begin")
query=str(input())
query=query.title()
queryexecutor.execute(query)
header=[i[0] for i in queryexecutor.description]
array=[]
for i in queryexecutor:
    array.append(list(i))
print("Please enter the x-axis field")
xaxis=(str(input())).title()
columnindex=header.index(xaxis)
x=[]
for i in array:
    x.append(i[columnindex])
print("Please enter the y-axis field")
yaxis=(str(input())).title()
columnindex=header.index(yaxis)
y=[]
for i in array:
    y.append(i[columnindex])   
fig=plt.figure(figsize=(5,5))
print("Press 1 for bar chart and press 2 for pie chart")
choice=int(input())
if choice==1:
    plt.bar(x,y,color='lightskyblue',width=0.1)
elif choice==2:
    color=['lightskyblue','lightcoral']
    patches,texts=plt.pie(y,colors=color,shadow=True,startangle=90)
    plt.legend(patches,x,loc="best")
    plt.axis('equal')
    plt.tight_layout()
plt.show()