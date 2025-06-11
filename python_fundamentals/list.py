data = ['apel', 'jeruk', 'mangga', 'pisang', 'anggur']

print('Data awal:', data)

print(data[-4])

# slicing
print(data[1:4])  # dari indeks 1 sampai 3

# slicing dengan step  
print(data[0:5:4])  # dari indeks 0 sampai 4 dengan step 2

# edit 
data[4] = 'alpukat'

print('Data setelah di edit', data)

# jumlah list
print(len(data))

# menambahkan data
data.append('kiwi') # menambahkan di akhir list
# data.prepend('nanas') # menambahkan di awal list
data.insert(0, 'semangka') # menambahkan di indeks 0

print('Data setelah ditambahkan', data)

# remove data
data.remove('jeruk')  # menghapus data dengan nilai 'jeruk'
data.pop(2)  # menghapus data pada indeks 2
del data[1]  # menghapus data pada indeks 1
# data.clear()  # menghapus semua data
print('Data setelah dihapus', data)

#  sort and reverse
data.sort()  # mengurutkan data
print('Data setelah diurutkan', data)
data.reverse()  # membalikkan urutan data
print('Data setelah dibalik', data)

# sum 
print(sum(data))

apam = data.copy()  # membuat salinan dari list
print('Salinan data:', apam)