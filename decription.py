f=open("C:\\Users\\ASUS\\Desktop\\projects\\incription_decription\\dbms.txt","r")
kf=open("C:\\Users\\ASUS\\Desktop\\projects\\incription_decription\\key_no.txt","r")
st=f.read()
key=kf.read()
kfile_no=key[-2]+key[-1]
key=key[:-2]
file_no=st[-2]+st[-1]
st=st[:-2]
key,kfile_no,file_no=int(key),int(kfile_no),int(file_no)
kfile_no,file_no=kfile_no^4,file_no^10
if kfile_no==file_no:
    st= bytearray(st,"ascii") 
    for i,v in enumerate(st):
        st[i]=v^key
    print(st.decode())
else:
    print("This key is not valid.")
f.close()
kf.close()