import random
f=open("dbms.txt","w")
kf=open("key_no.txt","w")
#ff=open("C:\\Users\\ASUS\\Desktop\\mbox-short.txt","r")
#st=ff.read()
st=input("Enter the data:")
st= bytearray(st,"ascii") 
key=random.randint(10,99) #This for creating a key
# this is incription part
for i,v in enumerate(st):
    st[i]=v^key
st=st.decode()
#this file_no add in the end of the file and key
file_no=int(random.randint(10,89))
df=file_no^10 #for data filea
f.write(st+str(df))
file_no=file_no^4 #for key_no
kf.write(str(key)+str(file_no))
f.close()
kf.close()
print("Your data is encrypted.\nNow your data is safe.")
