# Aplikasi Penerimaan dan Pengelolaan Beasiswa Universitas Kelompok 8

**Nama : Raffy Seyhan Islamy Pasha (2409116043)**

**Nama : Rabiatul Hikmah (2409116049)**

**Nama : Asriah Ainun Fazah (2409116068)**

# Flowchart
## Menu Login
![PA DDP drawio (2)-Login drawio](https://github.com/user-attachments/assets/d74941be-bd1a-4efa-b082-6780cc54d9ea)


## Menu Admin
![PA DDP drawio (2)-menu admin drawio](https://github.com/user-attachments/assets/85489800-7ba0-48a1-80ef-6a324560bc13)


## Menu User
![PA DDP drawio (2)-menu user drawio](https://github.com/user-attachments/assets/41dd1abc-5f39-4a0c-bf30-9c0931ffcb09)



# Dokumentasi Program dan Penjelasan
## Tampilan Awal Program : Menu Login

![Screenshot 2024-11-09 210414](https://github.com/user-attachments/assets/70584275-77aa-4648-b5bd-2e88e8487cb9)


Pada tampilan ini terdapat 3 opsi menu seperti yang ada pada gambar diatas. 
Opsi pertama ditujukan untuk admin atau user yang sudah memiliki akun sebelumnya, opsi kedua ditujukan kepada user yang belum memiliki akun dan opsi ketiga ditujukan apabila admin atau user ingin keluar program.

## 1. Register

![Screenshot 2024-11-09 210139](https://github.com/user-attachments/assets/7af4f736-6feb-4ffc-9ff8-5374dc28c35d)

jika memasukan pilihan 1 maka tampilan akan seperti ini.

akan diminta input :
* Nama username yang baru
* Buat password
* Memasukan IPK
  

## 2. Login

Untuk opsi login, kita akan diminta untuk memasukkan nama dan juga password yang sesuai.

###  * Jika login sebagai Admin 
akan diminta memasukan username dan password admin dan jika berhasil tampilanya akan seperti ini :
  
![Screenshot 2024-11-09 211250](https://github.com/user-attachments/assets/bba6ddaa-d02c-410e-b858-f00fc0652821)

Akan langsung ditampilkan fitur-fitur admin

Fitur Admin yaitu :
1. Lihat beasiswa/user
2. Tambah Beasiswa
3. Update beasiswa/user
4. Hapus beasiswa/user
5. Logout

### * Jika login sebagai user
akan diminta memasukan username dan password admin dan jika berhasil tampilanya akan seperti ini :

![Screenshot 2024-11-09 225838](https://github.com/user-attachments/assets/696ff3d5-baf3-4523-a395-4baa3ed8d7c0)

akan langsung ditampilkan fitur-fitur user

Fitur User yaitu :
1. Daftar beasiswa
2. Biodata diri
3. Status pendaftaran
4. Pengumuman
5. Tarik Uang
6. Logout

## 3. Keluar Program
jika memilih opsi tiga, maka akan program akan langsung berhenti dan menampilkan output "keluar program"

![Screenshot 2024-11-09 230438](https://github.com/user-attachments/assets/43909eac-9cad-4ea9-98d8-602b50f6c118)



## Penjelasan Fitur Admin

## 1. Lihat beasiswa/user

jika memilih opsi satu maka tampilannya akan seperti ini :

akan ada pilihan : 
1. Melihat list akun
2. Melihat list beasiswa
   
![Screenshot 2024-11-09 213347](https://github.com/user-attachments/assets/b54be357-9e34-41b3-832e-91f31ac6432e)

### Jika memilih opsi 1 

akan ditampilkan list akun yang ada :

![Screenshot 2024-11-09 214622](https://github.com/user-attachments/assets/db18ccc4-61d6-4bbf-865d-9bbe5381c3cc)

* dan akan langsung kembali ke menu admin

### Jika memilih opsi 2

akan ditampilkan list dari beasiswa :

![image](https://github.com/user-attachments/assets/061623eb-fa17-4e44-908f-f91b3c9f54b7)

dan akan langsung kembali ke menu admin

## 2. Tambah beasiswa 
jika memilih opsi 2 pada menu admin maka akan diminta input yaitu :
* Nama Beasiswa (harus baru dan tidak ada dalam daftar)
* Minimal IPK (tidak boleh lebih 4)
* Nominal Beasiswa (tidak boleh mines)
* Kuota Penerimaan Beasiswa(tidak boleh mines)
  
![Screenshot 2024-11-09 215451](https://github.com/user-attachments/assets/ad022ef9-b836-4f7d-84e4-39c18b94cce9)

* jika tidak memnuhi syarat akan mengulang inputan dari awal :

![Screenshot 2024-11-09 220227](https://github.com/user-attachments/assets/2308579a-b2f9-4615-9245-36154040d2e9)

## 3. Update beasiswa/user

jika memilih opsi tiga maka tampilannya akan seperti ini :

akan ada pilihan :
1. Update akun
2. Update beasiswa
   
![Screenshot 2024-11-09 223240](https://github.com/user-attachments/assets/a5a8605f-6a0d-4509-a43f-ba37e32824ba)


### Jika memilih opsi 1 
akan ditampilkan list dari akun yang ada.
input pertama, akan diminta memasukkan pilihan ingin mengubah akun menjadi admin atau user.
kemudian input kedua diminta untuk memasukkan saldo baru(jika tidak ingin diubah maka bisa langsung pencet enter)

dan tapilannya akan seperti ini :

![Screenshot 2024-11-09 220705](https://github.com/user-attachments/assets/38dc50b1-d9a2-4702-ba62-d17617ae755e)

### Jika memilih opsi 2
akan diampilkan list dari beasiswa.
* kemudian diminta id yang ingin di update
* masukan IPK baru (dapat dikosongkan jika tidak ingin diubah)
* masukan nominal beasiwa baru (dapat dikosongkan jika tidak ingin diubah)
* masukan kuota beasiswa baru (dapat dikosongkan jika tidak ingin diubah)

![Screenshot 2024-11-09 220815](https://github.com/user-attachments/assets/4404441a-1f3b-440a-a960-28ab4274486a)


## 4. Hapus beasiswa/user
jika memilih opsi empat maka tampilannya akan seperti ini :

akan ada pilihan :
1. Hapus akun
2. Hapus beasiswa
   
![Screenshot 2024-11-09 223251](https://github.com/user-attachments/assets/d4ab23ec-f2b4-4c8f-9bd9-3b192789bbc5)


### Jika memilih opsi 1 

akan ditampilkan list dari akun yang ada. kemudian, diminta untuk memasukan nama yang ingin dihapus. 
  
![Screenshot 2024-11-09 222408](https://github.com/user-attachments/assets/27166e61-ce9e-4d7d-a7ca-c691c728584d)

### Jika memilih opsi 2

akan ditampilkan list dari beasiswa. kemudian, diminta untuk memasukan ID beasiswa yang ingin dihapus.

![Screenshot 2024-11-09 220815](https://github.com/user-attachments/assets/9fa7878d-8fff-4b13-ae89-40d16c10c32e)


## 5. Logout

jika memilih opsi lima maka program akan langsung kembali ke menu login:

![Screenshot 2024-11-09 223108](https://github.com/user-attachments/assets/02f368ac-dcbb-4073-96b5-6c4006d6f7ba)

## Penjelasan Fitur User

![image](https://github.com/user-attachments/assets/2b2d6602-fbd9-47fc-942e-595efde9e3fa)

Di menu user terdapat 6 pilihan:
1. Daftar beasiswa
2. Biodata diri
3. Status pendaftaran
4. Pengumuman
5. Tarik uang
6. Logout

## 1. Daftar Beasiswa

![image](https://github.com/user-attachments/assets/a0b512d7-63fb-4998-b3ec-5a266a8cd6b5)

![image](https://github.com/user-attachments/assets/429a6b40-2537-457a-9f86-09e9708afaac)

akan muncul list beasiswa dan akan diminta input id yang ingin didaftarkan atau ketik s untuk search atau ketik r untuk sorting

jika memilih id dan berhasil maka akan muncul invoice 

![image](https://github.com/user-attachments/assets/e68d6937-7702-447e-b6df-03f08177967e)

jika memilih id tapi gagal akan muncul tulisan

![image](https://github.com/user-attachments/assets/2efd09f8-83c3-4598-8d35-ba577996fc04)

jika memilih search (s) maka akan diminta input nama beasiswa, dan jika kita mencari nama maka akan ke search seperti:

![image](https://github.com/user-attachments/assets/5b45a4fb-b7cb-44c4-b36c-7d736611924c)

jika memilih sorting (r) maka akan muncul 3 pilihan yaitu ipk, nominal, dan id dan setelah itu akan diminta urutan dari tertinggi ke rendah atau sebaliknya dan akan ke sorting

![image](https://github.com/user-attachments/assets/6b690987-313d-43a4-a73e-463f56bf8c46)


## 2. Biodata Diri
jika memilih biodata diri akan muncul biodata diri yang terdiri nama, password, ipk, saldo:

![image](https://github.com/user-attachments/assets/a03ceac6-2b94-48e6-bee8-3fa4a276c1a0)

## 3. Status Pendaftaran
jika memilih status pendaftaran maka akan muncul beasiswa yang kita telah kita daftar dan tanggal pendaftaran

![image](https://github.com/user-attachments/assets/56f9ec1f-dd58-4e0d-bde3-3e6d1717f04f)

## 4. Pengumuman
jika memiih pengumuman maka kita bisa mengundi beasiswa yang kita daftar dengan kemungkinan 50% dengan cara input nomer
jika dapat saldo akan bertambah

![image](https://github.com/user-attachments/assets/7da25f53-2106-4310-9805-ad0187ff806e)

## 5. Tarik uang
jika memilih tarik saldo maka kita bisa memilih jumlah saldo yang ingin kita tarik

![image](https://github.com/user-attachments/assets/e405fe0e-fe1f-4a4d-8541-dfc04cdf4878)

## 6. Logout 
jika memilih logout maka akan kembali ke menu login

![image](https://github.com/user-attachments/assets/df32c921-284c-4438-8667-adf42c4cf4e0)







