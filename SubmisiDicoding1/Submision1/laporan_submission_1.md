# Laporan Proyek Machine Learning - Brylian Fandhi Safsalta
## Domain Proyek
Kanker paru merupakan salah satu penyakit yang mungkin sudah banyak diketahui oleh masyarakat. Biasanya kanker paru akan sangat mudah terjadi kepada seseorang yang sering terpapar dengan asap rokok, baik perokok aktif maupun perokok pasif. Selain itu juga mudah menyerang masyarakat yang bekerja dengan asbes, arsen, kromat, nikel, klorometil eter, gas mustard dan paparan oven arang. Tentunya memiliki sejumlah ciri atau gejala bila seseorang terjangkit penyakit tersebut.

Dari masalah tersebut, suatu perusahaan ingin membuat suatu sistem yang dimana dari gejala gejala yang ada dapat ditentukan bahwa orang tersebut terkena penyakit kanker paru-paru atau tidak.

## Business Understanding
### Problem Statements
Berdasarkan kondisi yang telah diuraikan sebelumnya, perusahaan akan mengembangkan sebuah sistem prediksi/mengkategor8ikan penyakit secara otomatis untuk menjawab permasalahan berikut:
- Dari serangkaian fitur yang ada, fitur apa yang paling berpengaruh terhadap penyakit tersebut?
- Berapa banyak fitur yang mempengaruhi besarnya kategori penyakit?
- Berapa besar tingkat eror dari hasil prediksi yang dilakukan?

### Goals
Untuk menjawab pertanyaan tersebut, perusahaan membuat predictive modelling dengan tujuan atau goals sebagai berikut:
- Mengetahui fitur yang memliki korelasi tinggi dengan gejala penyakit
- Membuat model machine learning yang dapat memprediksi/menggolongkan apakah orang tersebut terjangkit atau tidak dengan seakurat mungkin berdasarkan fitur-fitur yang ada
- Melakukan evaluasi model yang telah dibangun untuk mengetahui tingkat kesalahan model

### Solution Statements
Dari tujuan atau goals yang ditentukan, berikut ini solusi atau cara untuk meraih goals tersebut:
- Analisis data dilakukan lebih detail dengan membersihkan data dan beberapa visualisasi data sebelum mencari nilai korelasi
- Menggunakan beberapa model machine learning untuk memperoleh hasil prediksi yang paling akurat dan setiap model tersebut dilakukan hyperparameter tuning untuk memperoleh model terbaik. Dan mencoba menggunakan berbagai pengolahan data.
- Seluruh hasil pelatihan model akan dievaluasi berdasarkan metrik Mean Squared Error (mse)

## Data Understanding
Pembuatan model machine learning pada proyek menggunakan 1338 data dari Medical Cost Personal Datasets, data dapat diunduh pada tautan ini.

### Variabel-variabel pada Lung Cancer DataSet adalah sebagai berikut:
- 32 sampel (sebagai pasien) dan 56 atribut (banyak data yang harus dipertimbangkan).
- terdapat nilai yang hilang.
- class label ada pada atribut pertama.
- class label adalah nominal, dengan range: 1, 2, 3.

![Box Plot](https://github.com/BrylianFandhi/ProgresBelajarku/blob/d52116c14dd145014a601a1d13d9f3e6a36dc652/SubmisiDicoding1/Submision1/data%20123.png)


Pada bagian ini dilakukan beberapa proses analisis untuk melihat bagaimana kondisi dari dataset. Hal pertama yang dilakukan adalah melihat apakah ada nilai yang kosong pada data dengan cara cek null data dan cek data nol (0) pada seluruh fitur.  Dimana dari data yang ada, fitur 4 dan fitur 38 terdapat data yang kosong. Fitur 4 memiliki 4 data yang kosong, sedangkan fitur 38 memiliki 1 data kosong.
fitur 4     4
fitur 38    1
dtype: int64

Dimana fitur yang kosong tersebut memiliki prosentase sebesar 
fitur 4     12.5
fitur 38     3.1
dtype: float64
yang dapat mempengaruhi hasil nantinya. Dari hasil tersebut maka data dapat dilakukan ke proses selanjutnya untuk mengisi data yang kosong tersebut.


https://github.com/BrylianFandhi/ProgresBelajarku/blob/d52116c14dd145014a601a1d13d9f3e6a36dc652/SubmisiDicoding1/Submision1/korr1.png

https://github.com/BrylianFandhi/ProgresBelajarku/blob/d52116c14dd145014a601a1d13d9f3e6a36dc652/SubmisiDicoding1/Submision1/kor2.png


Dasi hasil korelasi tersebut, menunjukkan korelasi antara data sangat berkaitan. Sehingga data dapat dilanjutkan ke proses selanjutnya, dengan mengisi data yang kosong.

## Data Preparation
Setelah analisis dilakukan, pada bagian ini data akan dilakukan beberapa proses teknik data preparation diantaranya yaitu melakukan pengisian data yang kosong menggunakan nilai rata rata, mengubah data menjadi numerik, dan melaklukan encoding data serta spliting untuk dilakukan pelatihan model dengan membagi data menjadi training = 70% dan testing = 30%. Serta nantinya ada beberapa jenis standarisasi data untuk melakukan perbandingan antara proses data, antara lain( Data original, Normalisasi, PCA, dan PCA Normalisasi)

Tahapan pertama yaitu mengubah yang dilakukan yaitu mengisi data kosong dengan data asumsi menggunakan nilai tengah atau median dari baris pada fitur atau data. Dari hasil tengah dari barisan fitur tersebut, akan diisikan ke dalam data yang kosong tersebut. 

Setelah melakukan pengisian data, selanjutnya melakukan pengecekan data dengan melihat prosentase yang kosong, melakukan poenghapusan data duplikat, dan menghapus fitur yang bernilai konstan.

### Mengkonsturuksi DAta
terdiri dari :
- Representasi fitur dan merubah tipenya.
- Membagi data menjadi training dan testing.
- Membandingkan Data Original, Data Normalisasi, Data Original PCA, Data Normalisasi PCA

Representasi fitur dan merubah tipenya.
Yaitu dengan melakukan penggantian tipe data agar menjadi numerik dan dapat diproses pada permodelan nantinya.

Membagi data sebagai fitur dan sebagai objek. 
Dimana fitur 1 - 56 akan menjadi fitur yang ditantai dengan X. Dan y sebagai penanda object atau class

Melakukan pembagian data menajadi Data Original, Data Normalisasi, Data Original PCA, Data Normalisasi PCA dengan spliting data 70% untuk data training dan 30 % sebagai data testing.
- Data Original
|	|fitur 1|fitur 2|fitur 3|fitur 4|fitur 5|fitur 6|fitur 7|fitur 8|fitur 9|fitur 10|...	|fitur 56|
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|------|--------|
|10	|0	|2	|2	|0	|0	|3	|2	|3	|1	|1	 |...	|2	 |
|15	|0	|3	|2	|2	|1	|2	|2	|2	|1	|1	 |...	|2	 |	
|26	|0	|2	|2	|2	|0	|2	|1	|2	|1	|1	 |...	|1	 |	
|6	|0	|3	|2	|1	|0	|3	|3	|3	|1	|2	 |...	|2	 |	
|3	|0	|2	|3	|2	|1	|3	|3	|3	|1	|2	 |...	|1	 |	
5 rows × 56 columns

- Data Normalisasi 
Melakukan Normalisasi menggunakan StandardScaler
array([[-0.1796053 ,  1.14707867, -2.00118448, ..., -1.13389342,
         0.48038446,  0.62554324],
       [-0.1796053 ,  1.14707867,  0.95441106, ..., -1.13389342,
         0.48038446,  0.62554324],
       [-0.1796053 ,  1.14707867,  0.95441106, ...,  0.8819171 ,
        -2.081666  ,  0.62554324],
       ...,
       [-0.1796053 , -0.6882472 , -1.01598597, ...,  0.8819171 ,
         0.48038446, -1.59861051],
       [-0.1796053 , -0.6882472 ,  0.95441106, ..., -1.13389342,
         0.48038446,  0.62554324],
       [-0.1796053 , -0.6882472 ,  0.95441106, ...,  0.8819171 ,
         0.48038446,  0.62554324]])
         
- Data Original PCA
Dimana data original akan dilakukan PCA atau  Principal component analysis yang digunakan untuk meringkas informasi yang tercantum dalam tabel data besar.
Heads of Original_PCA:         
0         1         2         3         4         5         6   \
0 -1.057646  2.260422 -1.985713 -0.023184 -0.771633 -0.695836  0.125112   
1 -2.031824  1.281974  1.597589 -1.688171  0.754078  0.411962  0.874224   
2 -1.601070 -1.522187  0.904781  0.490203 -0.237550 -1.095035 -1.915412   
3 -0.841556 -1.738084  0.484309  2.097076  1.255459 -1.088126 -1.547277   
4 -1.464877  0.901017  1.088615  0.745350  1.286815  1.848524  0.612184  

- Data Normalisasi PCA
Selanjutnya data normalisasi yang dilakukan PCA
Heads of iris_pca:          
0         1         2         3         4         5         6   \
0 -1.875112 -1.074126 -3.114162 -0.202740 -1.578644  0.472907 -0.306629   
1 -2.228485 -3.085196 -0.355241  0.321562  0.962612  1.183493  1.933027   
2 -2.045345 -0.560281  2.529009  1.166134 -1.090708 -2.418340 -2.856828   
3 -1.232962  0.268831  1.314142 -1.177625  0.699316 -4.038767 -1.566536   
4 -1.185845 -1.218255  0.987464 -2.566320  0.910664  0.388925  1.540951   

## Modeling
- Teknik Pemodelan yang dipakai:
    - Menggunakan Decision Tree
    - Parameter yang dipakai:
        - [criterion: gini, entropy]
        - [max_depth] = 1,21
        - [min sample split] = 2,11
        - [min sample leaf] = 1,101,2
- Skenario Pengujian
    - Menggunakan akurasi, presisi dan recall.
    - Pengujian menggunakan Data Original.
    - Pengujian menggunakan Data yang sudah dinormalisasi.
    - Pengujian menggunakan Data Original yang diberikan PCA.
    - Pengujian menggunakan Data yang sudah dinormalisasi dan diberikan PCA.

## Training Model
Proses Training model dengan menggunakan 1 arsitektur model yang diterapkan pada beberapa jenis data. 

## Evaluation
Tahapan terakhir yang perlu dilakukan adalah evaluasi model machine learning. Dari hasil training model yangg dilakukan, menghasilkan

### Data Original
Hasil perhitungan convusion matrix berdasarkan data testing.
- Akurasi pada training set:  0.6363636363636364
- Precision pada training set:  0.6363636363636364
- Recall pada training set:  0.6363636363636364
- Akurasi pada test set:  0.5
- Precision pada test set:  0.5
- Recall pada test set:  0.5

Visualisasi convusion matrix:
https://github.com/BrylianFandhi/ProgresBelajarku/blob/de121aa724036a0fd1ecbb815adcc41a54865dad/SubmisiDicoding1/Submision1/1.png

### Data Normalisasi
Hasil perhitungan convusion matrix berdasarkan data testing
- Akurasi pada training set:  0.6363636363636364
- Precision pada training set:  0.6363636363636364
- Recall pada training set:  0.6363636363636364
- Akurasi pada test set:  0.5
- Precision pada test set:  0.5
- Recall pada test set:  0.5

Visualisasi convusion matrix:
https://github.com/BrylianFandhi/ProgresBelajarku/blob/de121aa724036a0fd1ecbb815adcc41a54865dad/SubmisiDicoding1/Submision1/2.png

### Data Original PCA
Hasil perhitungan convusion matrix berdasarkan data testing
- Akurasi pada training set:  0.6363636363636364
- Precision pada training set:  0.6363636363636364
- Recall pada training set:  0.6363636363636364
- Akurasi pada test set:  0.4
- Precision pada test set:  0.4
- Recall pada test set:  0.4

Visualisasi convusion matrix:
https://github.com/BrylianFandhi/ProgresBelajarku/blob/de121aa724036a0fd1ecbb815adcc41a54865dad/SubmisiDicoding1/Submision1/3.png

### Data Normalisasi PCA
Hasil perhitungan convusion matrix berdasarkan data testing
- Akurasi pada training set:  0.9090909090909091
- Precision pada training set:  0.9090909090909091
- Recall pada training set:  0.9090909090909091
- Akurasi pada test set:  0.6
- Precision pada test set:  0.6
- Recall pada test set:  0.6

Visualisasi convusion matrix:
https://github.com/BrylianFandhi/ProgresBelajarku/blob/de121aa724036a0fd1ecbb815adcc41a54865dad/SubmisiDicoding1/Submision1/4.png

## Melakukan Proses Review Pemodelan

	Model	Training Accuracy	Test Accuracy
0	Decision Tree Data Original	0.636364	0.5
1	Decision Tree Data Normalisasi	0.636364	0.5
2	Decision Tree PCA Data Original	0.636364	0.4
3	Decision Tree PCA Data Normalisasi	0.909091	0.6


Model	Accuracy	Recall	Precision
0	Decision Tree Data Original	0.5	0.5	0.5
1	Decision Tree Data Normalisasi	0.5	0.5	0.5
2	Decision Tree PCA Data Original	0.4	0.4	0.4
3	Decision Tree PCA Data Normalisasi	0.6	0.6	0.6


Visualisasi perbandingan
https://github.com/BrylianFandhi/ProgresBelajarku/blob/de121aa724036a0fd1ecbb815adcc41a54865dad/SubmisiDicoding1/Submision1/Visualisasi%20Review.png


### Kesimpulan
Model terbaik dari Dataset Kanker Paru-Paru adalah menggunakan Decision Tree PCA Data Normalisasi dengan nilai akurasi tertinggi pada Data Training sebesar 90,9% dan akurasi tertinggi pada Data Testing sebesar 60%.
