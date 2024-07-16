# # #list
# # list_contoh=['hello',1,1,3,True]
# # print(list_contoh)
# # print(type(list_contoh))

# # #indexing (positif)
# # print(list_contoh[0])

# # print(list_contoh[4])

# # #negatif
# # print(list_contoh[-3])

# # print(list_contoh[4]!=list_contoh[-4])


# # #slicing
# # print(list_contoh[4:1])

# # #soal 1
# # # Buat list (isi bebas) berisi 6 value, lalu panggil value urutan ke 2 sampai urutan terakhir
# # list_soal1=[' ','P','u','r','w','a']
# # print(list_soal1[-5:])

# # list_contoh=['Hello',1,1,3,True]
# #change value in list
# # print(f'list sebelum dilakukan perubahan value adalah {list_contoh}')
# # list_contoh[3]='Tiga'
# # print(f'list setelah dilakukan perubahan value adalah {list_contoh}')

# # #add
# # #append
# # print(f'list sebelum dilakukan penambahan value adalah {list_contoh}')
# # list_contoh.append('Indonesia')
# # # print(f'list setelah dilakukan penambahan value adalah {list_contoh}')

# # #insert
# # list_contoh.insert(1,'Malaysia')
# # print(f'list setelah dilakukan penambahan value adalah {list_contoh}')

# #Delete
# #remove, pop, del
# # print(f'list sebelum dilakukan penghapusan value adalah {list_contoh}')
# # list_contoh.remove('Hello')
# # print(f'list setelah dilakukan penghapusan value menggunakan remove adalah {list_contoh}')
# # list_contoh.pop()
# # print(f'list setelah dilakukan penghapusan value menggunakan pop adalah {list_contoh}')
# # del list_contoh[2]
# # print(f'list setelah dilakukan penghapusan value menggunakan del adalah {list_contoh}')
# # #clear
# # list_contoh.clear()
# # print(f'list setelah dilakukan penghapusan value menggunakan clear adalah {list_contoh}')


# # Soal 2 - 7
# # 1. Buat list yang berisi angka genap dari 1 sampai 30, lalu print
# # 2. ubah angka pada urutan pertama menjadi 2.0, dan urutan terakhir menjadi 30.0, lalu print
# # 3. tambah bilangan 3 pada urutan kedua, dan bilangan 5 pada urutan keempat(setelah ditambahkan bil 3), lalu print
# # 4. tambahkan bilangan 32 pada urutan terakhir, lalu print
# # 5. hapus bilangan ganjil menggunakan remove dan hapus juga bilangan terakhir menggunakan del, lalu print
# # 6. hapus semua value yang ada di list terakhir pada no 5, lalu print

# # list1=[i for i in range(2,31,2)] #1
# # print(f'no 1: {list1}')
# # list1[0]=float(2) #2
# # list1[14]=float(30) #2
# # print(f'no 2: {list1}')
# # list1.insert(1,3) #3
# # list1.insert(3,5) #3
# # print(f'no 3: {list1}')
# # list1.append(32) #4
# # print(f'no 4: {list1}')
# # list1.remove(3) #5
# # del list1[15] #5
# # print(f'no 5: {list1}')
# # list1.clear() #6
# # print(f'no 6: {list1}')


# # loop in list
# # list_contoh=['Hello',1,1,3,True]
# # print(list_contoh)
# # for item in list_contoh:
# #     print(item)

# # # conditional statement
# # if 'Hello' in list_contoh:
# #     print('ada string "Hello" di list_contoh')
# # else:
# #     print('tidak ada string "Hello" di list_contoh')

# # # len 
# # print(f'panjang list "list_contoh" adalah {len(list_contoh)}')


# # list_contoh=['Hello',1,1,3,True]
# # #tanpa .copy() --> merubah list yang lama
# # new_list_contoh1=list_contoh
# # new_list_contoh1[0]='Hi'
# # #dengan .copy() --> tidak merubah list yang lama
# # new_list_contoh2=list_contoh.copy()
# # new_list_contoh2[-1]=False
# # print(f'list_contoh : {list_contoh}')
# # print(f'new_list_contoh1 : {new_list_contoh1}')
# # print(f'new_list_contoh2 : {new_list_contoh2}')


# # import math
# # list_contoh=['Hello',1,1,3,True]
# # list_baru=['Purwadhika',False, 5.3, math.pi]
# # print(f'list_contoh : {list_contoh}')
# # print(f'list_baru : {list_baru}')

# # # "+""
# # list_tambah1=list_contoh+list_baru
# # print(f'list_tambah1 : {list_tambah1}')

# # #extend
# # list_contoh.extend(list_baru)
# # print(f'list_contoh : {list_contoh}')

# # #find index
# # list_contoh=[0,1,1,3,1]
# # print(list_contoh.index(False))

# # #sort ascending
# # print(f' list sebelum dilakukan sort adalah {list_contoh}')
# # list_contoh.sort()
# # print(f' list setelah dilakukan sort adalah {list_contoh}')

# # #sort descending
# # list_contoh=[0,1,1,3,1]
# # print(f' list sebelum dilakukan sort descending adalah {list_contoh}')
# # list_contoh.sort(reverse=True)
# # print(f' list setelah dilakukan sort descending adalah {list_contoh}')

# # #reverse
# # list_contoh=[0,1,1,3,1]
# # print(f' list sebelum dilakukan reverse adalah {list_contoh}')
# # list_contoh.reverse()
# # print(f' list setelah dilakukan reverse adalah {list_contoh}')

# # list_2d=[['Red Pen','Blue Pen'],['Analog Clock', 'Digital Clock'],['Futsal Shoes', 'Badminton Shoes']]
# # # 'Futsal Shoes', 'Badminton Shoes'
# # print(list_2d[2])
# # # 'Analog Clock'
# # print(list_2d[1][0])
# # # ['Red Pen','Blue Pen'],['Analog Clock', 'Digital Clock']
# # print(list_2d[0:2])

# # # 'Red Pen', 'Futsal Shoes'
# # print([list_2d[0][0],list_2d[2][0]])




# # #Tuple
# # tuple_contoh=('Hello',1,1,3,True)
# # print(tuple_contoh)
# # print(type(tuple_contoh))

# # #indexing (positif)
# # print(tuple_contoh[0])

# # print(tuple_contoh[4])

# # #negatif
# # print(tuple_contoh[-3])

# # print(tuple_contoh[4]!=tuple_contoh[-4])


# # #slicing
# # print(tuple_contoh[4:1])

# ## change value in tuple
# # list_tuple_contoh=list(tuple_contoh)
# # list_tuple_contoh[0]='Hi'
# # tuple_contoh=tuple(list_tuple_contoh)
# # print(tuple_contoh)


# # # loop in tuple
# # tuple_contoh=('Hello',1,1,3,True)
# # print(tuple_contoh)
# # for item in tuple_contoh:
# #     print(item)

# # # conditional statement
# # if 'Hello' in tuple_contoh:
# #     print('ada string "Hello" di tuple_contoh')
# # else:
# #     print('tidak ada string "Hello" di tuple_contoh')

# # # len 
# # print(f'panjang tuple "tuple_contoh" adalah {len(tuple_contoh)}')

# # import math
# # tuple_contoh=('Hello',1,1,3,True)
# # tuple_baru=('Purwadhika',False, 5.3, math.pi)
# # print(f'tuple_contoh : {tuple_contoh}')
# # print(f'tuple_baru : {tuple_baru}')

# # # "+""
# # tuple_tambah1=tuple_contoh+tuple_baru
# # print(f'tuple_tambah1 : {tuple_tambah1}')


# # #find index
# # tuple_contoh=[0,1,'Andy',3,1]
# # print(tuple_contoh.index('Andy'))



# # tuple_2d=(('Red Pen','Blue Pen'),('Analog Clock', 'Digital Clock'),('Futsal Shoes', 'Badminton Shoes'))
# # # 'Futsal Shoes', 'Badminton Shoes'
# # print(tuple_2d[2])
# # # 'Analog Clock'
# # print(tuple_2d[1][0])
# # # ['Red Pen','Blue Pen'],['Analog Clock', 'Digital Clock']
# # print(tuple_2d[0:2])

# # # 'Red Pen', 'Futsal Shoes'
# # print((tuple_2d[0][0],tuple_2d[2][0]))

# # print(list([list(tuple_2d[0]),list(tuple_2d[1]),list(tuple_2d[2])]))


# # Soal 3
# # Buat tuple 2D yang berisi merk dan tipe mobil 2x3, lalu print, 
# # kemudian ubah value pada tuple kedua dan urutan terakhir menjadi value yang baru, lalu print


# # #LATIHAN LIST
# # #1
# # numbers=[41,5,1,3,89,32]
# # print(f'list angka : {numbers}')

# # min=numbers[0]
# # for angka in numbers:
# #     if angka < min:
# #         min=angka
# # print(f'angka terkecil yang ada di dalam list tersebut adalah {min}')

# # max=numbers[0]
# # for angka in numbers:
# #     if angka > max:
# #         max=angka
# # print(f'angka terkecil yang ada di dalam list tersebut adalah {max}')

# #2
# # list_before=[41,5,1,3,89,32]
# # print(f'list angka sebelum di sort: {list_before}')
# # for i in range(len(list_before)):
# #     for j in range(i+1,len(list_before)):
# #         if(list_before[i]>list_before[j]):
# #             list_before[i],list_before[j]=list_before[j],list_before[i]
# # print(f'list angka setelah di sort: {list_before}')


# # # Dictionary
# # dict_1={'Nama':'Budi',
# #         'Usia':25,
# #         'Pekerjaan':'Developer'}

# # print(dict_1)
# # print(type(dict_1))



# # dict_2=dict(Nama='Andi',Usia=27,Pekerjaan='Data Scientist')
# # print(dict_2)
# # print(type(dict_2))

# #memanggil value pada dictionary
# # print(dict_1['Nama'])
# # print(dict_1.get('Usia'))

# #hapus dictionary dengan pop, del, pop_item
# # dict_1.pop('Usia')
# # print(f'dictionary setelah dihapus menggunakan pop menjadi {dict_1}')

# # del dict_1['Pekerjaan']
# # print(f'dictionary setelah dihapus menggunakan del menjadi {dict_1}')

# # dict_1.popitem()
# # print(f'dictionary setelah dihapus menggunakan pop_item menjadi {dict_1}')

# # dict_1.clear()
# # print(f'dictionary setelah dihapus menggunakan clear menjadi {dict_1}')

# # #add key, value to dictionary
# # dict_1['Income']=1e6
# # print(f'dictionary setelah ditambahkan key dan value baru menjadi {dict_1}')

# # #change value in dictionary
# # dict_1['Usia']=27
# # print(f'dictionary setelah valuenya diubah menjadi {dict_1}')


# # #for loop in dictionary
# #panggil keys
# # for key in dict_1:
# #     print(f'{key}={dict_1[key]}')

# # for key in dict_1.keys():
# #     print(f'{key}={dict_1[key]}')

# # panggil values
# # for val in dict_1.values():
# #     print(val)

# #panggil keys dan values
# # for key,val in dict_1.items():
# #     print(f'{key}={val}')


# # things = {
# #     'food1': {
# #         'name': 'Ramen',
# #         'price': 25000
# #     },
# #     'food2': {
# #         'name': 'Pizza',
# #         'price': 30000
# #     },
# #     'food3': {
# #         'name': 'Spaghetti',
# #         'price': 20000
# #     }
# # }



# # print(things['food2']['price'])

# while True:
#     tipe_tambah = input('\nMasukkkan tipe ban (A/T, M/T, RADIAL, ECO): ').upper()
#     valid = True
#     for char in tipe_tambah:
#         if (char.isdigit() or char != '/'):
#             valid = False
#             break
#     if valid and '/' in tipe_tambah:
#         break
#     else:
#         print('Masukkan tipe ban dengan benar.')

# print(f'{tipe_tambah}')

# # #Set
# # set1={'Andy','Budi','Charli','Charli','Andy'}
# # print(set1)

# # list2=['Andy','Budi',1,1,True,0, False]
# # set_list2=set(list2)
# # print(set_list2)

# # tuple2=('Andy','Budi',1,1,True,0, False)
# # set_tuple2=set(tuple2)
# # print(set_tuple2)

# # dict2={'Nama':'Andy',
# #        'Usia':31,
# #        'Pekerjaan':'Data Scientist'}
# # set_dict2=set(dict2)
# # print(set_dict2)

# # set_dict_values2=set(dict2.values())
# # print(set_dict_values2)

# # set_dict_items2=set(dict2.items())
# # print(set_dict_items2)


# # Soal
# # Buat dictionary dengan key 'Merk/Brand', lalu valuenya menggunakan 'type', kemudian print dictionary tersebut, 
# # lalu ubah ke dalam set(key, values, items)

# # dict2={'Daihatsu':('Terios','Xenia','Ayla'),
# #        'Mitsubishi':('Pajero','Xpander','Lancer')}
# # print(f'Dictionary sebelum diubah menjadi set adalah {dict2}')


# # set_dict2=set(dict2)
# # print(f'Keys dari dictionary setelah diubah menjadi set adalah {set_dict2}')

# # set_dict_values2=set(dict2.values())
# # print(f'Values dari dictionary setelah diubah menjadi set adalah {set_dict_values2}')

# # set_dict_items2=set(dict2.items())
# # print(f'Keys dan values dari dictionary setelah diubah menjadi set adalah {set_dict_items2}')


# # # Loop in set
# # setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

# # for item in setContoh:
# #     print(item)



# # # add item in set
# # setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}

# # setContoh.add('Iron Man 3')
# # print(setContoh)

# # ## update item(add many items)
# # setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron'}
# # print(setContoh)
# # setContoh.update({'Iron Man 4','Hulk','Iron Man 100'})
# # print(setContoh)

# #delete values in set with remove, discard, pop
# # setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk', 'Wonder Woman'}
# # setContoh.remove('The Avengers')
# # print(setContoh)

# # setContoh.discard('Hulk')
# # print(setContoh)

# # setContoh.pop()
# # print(setContoh)

# # setContoh.clear()
# # print(setContoh)


# # ## len dari set
# # setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}

# # print(len(setContoh))  # 4

# # # conditional statement in set
# # setContoh = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
# # if 'Hulk' in setContoh:
# #     print('Ada "Hulk" pada setContoh')
# # else:
# #     print('Tidak ada "Hulk" pada setContoh')


# # setMovie1 = {'The Avengers', 'Iron Man 3', 'Avengers: Age of Ultron', 'Hulk'}
# # setMovie2 = {'Titanic', 'The Avengers'}

# # #union
# # setGabungan = setMovie1.union(setMovie2)
# # print(setGabungan)


# # #difference
# # setDifference=setMovie1.difference(setMovie2)
# # print(setDifference)

# # setMovie1.difference(setMovie2)
# # print(setMovie1)

# # #symmetric difference
# # set_sym_Difference=setMovie1.symmetric_difference(setMovie2)
# # print(set_sym_Difference)

# # setMovie1.symmetric_difference_update(setMovie2)
# # print(setMovie1)

# # # intersection
# # setIntersect=setMovie1.intersection(setMovie2)
# # print(setIntersect)

# # setMovie1.intersection_update(setMovie2)
# # print(setMovie1)


# # himp_kecil={1,2,3}
# # himp_besar={i for i in range(1,10)}
# # #cek disjoint
# # # print(himp_kecil.isdisjoint(himp_besar))

# # #cek subset
# # print(himp_kecil.issubset(himp_besar))

# # #cek superset
# # print(himp_kecil.issuperset(himp_besar))


# #================================================================================================================================================================================================#

# #soal market
# #soal 4:
# # list_buah=[['Apel ',20,10000],['Jeruk',15,15000],['Anggur',25,20000]]
# # cart=[]
# # while True:
# #     pilihanMenu=input('''
# #                 Selamat Datang di Pasar Buah
                      
# #                 List Menu:
# #                 1. Menampilkan Daftar Buah
# #                 2. Menambah Buah
# #                 3. Menghapus Buah
# #                 4. Membeli Buah
# #                 5. Exit Program
# #                 Masukkan Angka Menu yang ingin dijalankan : ''')

# #     if(pilihanMenu=='1'): #case saat user memilih menu 1
# #         print('Daftar Buah\n') #print judul
# #         print('Index\t| Nama  \t| Stok \t| Harga') #header dari tabel
# #         for i in range(len(list_buah)): #print value dari tabel
# #             print(f'{i}\t| {list_buah[i][0]} \t| {list_buah[i][1]} \t| {list_buah[i][2]}')
# #     elif(pilihanMenu=='2'):
# #         namaBuah=input('Masukkan Nama Buah : ') #inputan untuk nama buah yang ingin ditambahkan
# #         stockBuah=int(input('Masukkan Stock Buah : ')) #inputan untuk stock buah yang ingin ditambahkan
# #         hargaBuah=int(input('Masukkan Harga Buah : ')) #inputan untuk harga buah yang ingin ditambahkan
# #         list_buah.append([namaBuah,stockBuah,hargaBuah]) #tambah data yang baru dengan fungsi append
# #         print('Daftar Buah\n') #print judul
# #         print('Index\t| Nama  \t| Stok \t| Harga') #header dari tabel
# #         for i in range(len(list_buah)): #print value dari tabel
# #             print(f'{i}\t| {list_buah[i][0]} \t| {list_buah[i][1]} \t| {list_buah[i][2]}')       
# #     elif(pilihanMenu=='3'):
# #         print('Daftar Buah\n') #print judul
# #         print('Index\t| Nama  \t| Stok \t| Harga') #header dari tabel
# #         for i in range(len(list_buah)): #print value dari tabel
# #             print(f'{i}\t| {list_buah[i][0]} \t| {list_buah[i][1]} \t| {list_buah[i][2]}')  
# #         indexBuah=int(input('Masukkan index buah yang ingin dihapus : '))
# #         del list_buah[indexBuah]       
# #         print('Daftar Buah\n') #print judul
# #         print('Index\t| Nama  \t| Stok \t| Harga') #header dari tabel
# #         for i in range(len(list_buah)): #print value dari tabel
# #             print(f'{i}\t| {list_buah[i][0]} \t| {list_buah[i][1]} \t| {list_buah[i][2]}')  
# #     elif(pilihanMenu=='4'):
# #         print('Daftar Buah\n') #print judul
# #         print('Index\t| Nama  \t| Stok \t| Harga') #header dari tabel
# #         for i in range(len(list_buah)): #print value dari tabel
# #             print(f'{i}\t| {list_buah[i][0]} \t| {list_buah[i][1]} \t| {list_buah[i][2]}') 
# #         while True: 
# #             indexBuah=int(input('Masukkan index buah yang ingin dibeli : ')) #masukkan index buah yg ingin dibeli 
# #             qtyBuah=int(input('Masukkan jumlah buah yang ingin dibeli : ')) #masukkan qty buah yg ingin dibeli
# #             if qtyBuah > list_buah[indexBuah][1]:
# #                 print(f'stok tidak cukup, stok buah tersisa {list_buah[indexBuah][1]}')
# #             else:
# #                 cart.append([list_buah[indexBuah][0],qtyBuah,list_buah[indexBuah][2]])
# #             print('Isi Cart :')
# #             print('Nama\t|Qty \t|Harga')
# #             for i in range(len(cart)): #print value dari tabel
# #                 print(f'{cart[i][0]} \t| {cart[i][1]}  \t| {cart[i][2]}') 
# #             checker=input('Mau beli yang lain? (ya/tidak)') #checker
# #             if checker == 'ya':
# #                 continue
# #             else:
# #                 print('Daftar Belanja : ')
# #                 print('Nama\t|Qty\t\t|Harga \t\t|Total Harga')
# #                 total_harga=0
# #                 for i in range(len(cart)): #print value dari tabel
# #                     print(f'{cart[i][0]} \t| {cart[i][1]} \t\t| {cart[i][2]} \t| {cart[i][1]*cart[i][2]}') 
# #                     total_harga+=cart[i][1]*cart[i][2] #jumlahan dari semua total harga
# #                 break
# #         print(f'Total harga yang harus dibayar = {total_harga}')
# #         while True:
# #             userInput_uang= int(input('Masukkan jumlah uang: '))
# #             if userInput_uang < total_harga:
# #                 print(f'Uang anda kurang sebesar: {total_harga - userInput_uang}')
# #             elif userInput_uang > total_harga:
# #                 print('Terimakasih\n')
# #                 print(f'Uang kembali anda: {userInput_uang - total_harga}')
# #                 break
# #             else:
# #                 print('Terimakasih\n')
# #                 break
# #     elif(pilihanMenu=='5'):
# #         break









# # # harga_apel=10000
# # # harga_jeruk=15000
# # # harga_anggur=20000
# # # stok_apel=5
# # # stok_jeruk=7
# # # stok_anggur=6
# # # #apel
# # # while(True):
# # #     jumlah_apel=int(input('Masukkan Jumlah Apel: '))
# # #     if jumlah_apel > stok_apel:
# # #         print(f'Jumlah yang dimasukkan terlalu banyak. \nStock sisa apel tinggal {stok_apel} buah')
# # #     else:
# # #         break
# # # #jeruk
# # # while(True):
# # #     jumlah_jeruk=int(input('Masukkan Jumlah Jeruk: '))
# # #     if jumlah_jeruk > stok_jeruk:
# # #         print(f'Jumlah yang dimasukkan terlalu banyak. \nStock sisa jeruk tinggal {stok_jeruk} buah')
# # #     else:
# # #         break
# # # #anggur
# # # while(True):
# # #     jumlah_anggur=int(input('Masukkan Jumlah Anggur: '))
# # #     if jumlah_anggur > stok_anggur:
# # #         print(f'Jumlah yang dimasukkan terlalu banyak. \nStock sisa anggur tinggal {stok_anggur} buah')
# # #     else:
# # #         break


# # # total=jumlah_apel*harga_apel+jumlah_jeruk*harga_jeruk+jumlah_anggur*harga_anggur
# # # print(f'''
# # # Detail Belanja
# # # Apel : {jumlah_apel} x {harga_apel} = {jumlah_apel*harga_apel}
# # # Jeruk : {jumlah_jeruk} x {harga_jeruk} = {jumlah_jeruk*harga_jeruk}
# # # Anggur : {jumlah_anggur} x {harga_anggur} = {jumlah_anggur*harga_anggur}
# # # total={jumlah_apel*harga_apel+jumlah_jeruk*harga_jeruk+jumlah_anggur*harga_anggur}
# # # ''')

# # # while(True):
# # #     uang_customer=int(input('Masukkan jumlah uang : '))
# # #     if (uang_customer> total) :
# # #         print(f'Terimakasih\n\nUang kembali anda : {uang_customer-total}')
# # #         break
# # #     elif (uang_customer==total):
# # #         print('Terima kasih')
# # #         break
# # #     else:
# # #         print(f'Transaksi anda dibatalkan uangnya kurang sebesar {total-uang_customer}')

        
