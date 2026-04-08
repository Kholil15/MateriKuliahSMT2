import streamlit as st
import sys
# Membuat struktur Tuple
logApps = ("User1 login," "User2 login," "User3 login")
print (logApps)
print (sys.getsizeof(logApps))

# Membuktikan Memory tuple lebih efisien dari list
logAppsList = ["User1 Login"]
print (logAppsList)
print ("Memiliki ukuran list", sys.getsizeof(logAppsList))

# pembuktian tuple tidak bisa diubah
# 1.tambah
#logApps.append ("User4 Login")
# 2. Ubah 
# logApps [0] = "User1 logout"

# 3.Hapus 
# del logApps.append ()

print ()