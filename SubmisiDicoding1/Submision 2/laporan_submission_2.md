# Laporan Proyek Machine Learning - Brylian Fandhi Safsalta
## Project Overview
Buku memiliki peranan penting dalam pengembangan ilmu pengetahuan. Buku merupakan salah satu sumber bahan ajar. Ilmu pengetahuan, informasi, danhiburan dapat diperoleh dari buku, oleh karena itu, buku merupakan komponen wajib yang harus ada di lembaga pendidikan baik lembaga pendidikan formalmaupun nonformal. Lembaga pendidikan merupakan tempat dilaksanakannya proses pembelajaran sebagai proses interaksi antara peserta didik dengan pendidik dan sumber belajar pada suatu lingkungan belajar.Seseoranng penggiat buku memiliki pengetahuan lebih mengenai buku-buku yang telah dibaca. Tentunya dalam situasi tersebut alangkah lebih mudahnya seseorang mendapatkan sebuah rekomendasi buku yang mungkin mereka sukai.

Berdasarkan pada masalah tersebut, maka proyek ini dilakukan untuk memberi rekomendasi buku kepada user berdasarkan rating user terhadap buku sebelumnya. Diharapkan dengan memberikan rekomendasi buku yang sesuai dapat memudahkan dan mempercepat proses pencarian buku bagi para peminatnya.

## Business Understanding
### Problem Statements
Berdasarkan kondisi yang telah diuraikan sebelumnya, berikut permasalahan yang diangkat:
- Data apa saja yang digunakan dalam membuat sistem rekomendasi buku?
- Bagaimana membuat sistem rekomendasi vuku dari data tersebut?
- Berapa besar tingkat eror dari hasil sistem rekomendasi yang dilakukan?

### Goals
Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Mengetahui dan membersihkan data yang akan digunakan dalam model
- Membuat model machine learning yang dapat melakukan rekomendasi buku seakurat mungkin berdasarkan data yang ada
- Melakukan evaluasi model yang telah dibangun untuk mengetahui tingkat kesalahan model

### Solution Statements
- Analisis data dilakukan lebih detail dengan membersihkan data dan beberapa visualisasi data sebelum memilih data
- Menggunakan model machine learning yang dilakukan parameter tuning untuk memperoleh model terbaik
- Seluruh hasil pelatihan model akan dievaluasi berdasarkan metrik Root Mean Squared Error (rmse)

## Data Understanding
Pada proyek ini mengambil dataset dari website Kaggle (dapat diunduh pada [tautan ini](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)). Dataset memiliki empat file csv terpisah diantaranya yaitu:
- `Books.csv` Berisi informasi Buku, seperti ID, Judul, penulis, penerbit, DSB.
- `Ratings.csv` Rating User terhadap Buku yang dibaca.
- `Users.csv` Informasi mengenai pengguna.

Pada bagian ini dilakukan beberapa proses analisis (seperti cek data null, cek duplicated data, dll) untuk melihat bagaimana kondisi dari seluruh dataset. Analisis dibagi berdasarkan file dataset, berikut ini 3 file yang dianalisis.

### `Books.csv`
Pada dataset ini terdapat 5 kolom dan 271360 baris data. Dataset ini berisi informasi umum pada setiap buku seperti 
- ISBN yang merupakan nomor buku
- Book_Title yang merupakan judul buku
- Book_Author merupakan penulis buku
- Year_Of_Publication merupakan kapan buku tersebut terbit
- Publisher merupakan nama penerbit 

|index|ISBN|Book\_Title|Book\_Author|Year\_Of\_Publication|Publisher|
|---|---|---|---|---|---|
|0|0195153448|Classical Mythology|Mark P\. O\. Morford|2002|Oxford University Press|
|1|0002005018|Clara Callan|Richard Bruce Wright|2001|HarperFlamingo Canada|
|2|0060973129|Decision in Normandy|Carlo D'Este|1991|HarperPerennial|
|3|0374157065|Flu: The Story of the Great Influenza Pandemic of 1918 and the Search for the Virus That Caused It|Gina Bari Kolata|1999|Farrar Straus Giroux|
|4|0393045218|The Mummies of Urumchi|E\. J\. W\. Barber|1999|W\. W\. Norton &amp; Company|

Data yang didapatkan nilai yang kosong berjumlah 3, yaitu pada 1 pengarang, 2 penerbit.

Pada bagian penulis dilakukan analisis lebih lanjut dengan mengambil jumlah seluruh vuku terhadap buku tertentu, terdapat 102024 genre berbeda pada seluruh buku yang ada, kemudian data jumlah buku terhadap diurutkan berdasarkan terbesar ke terkecil. Berikut ini hasil jumlah buku setiap penulis. Mengapa diambil yang penulis, karena biasanya seseorang penggemar buku menyukai buku sesuai penulisnya siapa.

Jika dilihat dari data tersebut berikut tabel 10 top penulis buku dengan karya terbanyak.
|index|Auhor|Total|
|---|---|---|
|0|Agatha Christie|632|
|1|William Shakespeare|567|
|2|Stephen King|524|
|3|Ann M\. Martin|423|
|4|Carolyn Keene|373|
|5|Francine Pascal|372|
|6|Isaac Asimov|330|
|7|Nora Roberts|315|
|8|Barbara Cartland|307|
|9|Charles Dickens|302|

Dari hasil tersebut dapat dilihat bahwa terdapat 632 buku karya Agatha Christie, penulis tersebut memiliki karya terbanyak daripada penulis lainnya.

### `Ratings.csv`
Pada dataset ini terdapat 3 kolom dan 1149780 baris data. Dataset ini berisi daftar seluruh anime yang diberi rating oleh user. Pada dataset ini terdapat 105.283 user yang memberikan rating terhadap 340.556 judul buku. Kemudian analisis lebih lanjut terhadap nilai rating pada buku. 

|index|User-ID|ISBN|Book-Rating|
|---|---|---|---|
|0|276725|034545104X|0|
|1|276726|0155061224|5|
|2|276727|0446520802|0|
|3|276729|052165615X|3|
|4|276729|0521795028|6|

Dimana attribut dari dataset tersebut yaitu
- User-ID sebagai id pengguna
- ISBN sebagai nomor buku
- book-rating sebagai penilaian dari Buku

Pada nilai rating (0 - 10) dilakukan analisis terhadap berapa jumlah user yang memberikan rating tertentu terhadap seluruh anime. Berikut hasil pengurutan jumlah rating 0 - 10, rating 0 adalah nilai ketika user tidak memberikan rating terhadap buku.

![1](https://user-images.githubusercontent.com/76621303/224552970-ca4311f3-c03a-41d1-841e-fff621b0171d.png)

Jika dilihat dari data tersebut berikut tabel top jumlah rating user terbanyak.

|index|Rating|Total|
|---|---|---|
|0|0|716109|
|1|8|103736|
|2|10|78610|
|3|7|76457|
|4|9|67541|
|5|5|50974|
|6|6|36924|
|7|4|8904|
|8|3|5996|
|9|2|2759|
|10|1|1770|

Dari hasil tersebut dapat dilihat bahwa rating dengan nilai 0 menjadi rating terbanyak yang ada oleh user, yang artinya mayoritas user tidak memberikan rating terhadap anime yang mereka tonton. Kemudian disusul dengan rating 8 dan 10 dibawahnya.

### `Users.csv`
Pada dataset ini terdapat 3 kolom dan 278858 baris data yang berisi daftar seluruh informasi pengguna. dimana terdapat 3 attribut data, yaitu 

- user_id sebagai ID pengguna 
- Location sebagai lokasi pengguna
- age sebagai umur

|index|user\_id|location|age|
|---|---|---|---|
|0|1|nyc, new york, usa|NaN|
|1|2|stockton, california, usa|18\.0|
|2|3|moscow, yukon territory, russia|NaN|
|3|4|porto, v\.n\.gaia, portugal|17\.0|
|4|5|farnborough, hants, united kingdom|NaN|

Data set tersebut memiliki nilai kosong yang begitu banyak terutama pada attribut umur/age yaitu sebesar 110762

## Data Preparation
Setelah analisis dilakukan, pada bagian ini hal pertama yang dilakukan adalah memilih dataset yang akan digunakan. Data yang dipilih untuk digunakan yaitu pada `Books.csv` dengan attribut ['ISBN', 'Book_Title'] dimasukan kedalam variabel `df_buku` sebagai tempat seluruh detail bukudan `Rating.csv` dimasukan kedalam variabel `df_rating` sebagai nilai rating yang diberikan oleh user. Kemudian kolom pada data `df_buku` dilakukan rename agar format nama menjadi sama rata. Berikut contoh data tersebut.

Dataset `df_buku`
|index|user\_id|ISBN|rating|Book\_Title|
|---|---|---|---|---|
|0|276817|0671749609|0|PERFUME : PERFUME|
|1|277052|9513098648|8|NaN|
|2|277073|0060595183|0|The Doors of Perception and Heaven and Hell \(Perennial Classics\)|
|3|277124|0425189864|9|Mortal Prey|
|4|277124|0440236053|9|Writ of Execution|

Dataset `df_rating`
|index|user\_id|ISBN|rating|Book\_Title|
|---|---|---|---|---|
|0|276817|0671749609|0|PERFUME : PERFUME|
|1|277052|9513098648|8|NaN|
|2|277073|0060595183|0|The Doors of Perception and Heaven and Hell \(Perennial Classics\)|
|3|277124|0425189864|9|Mortal Prey|
|4|277124|0440236053|9|Writ of Execution|

Kemudian dari data tersebut melihat jumlah data yang digunakan yaitu:
- Jumlah buku yang digunakan: 340556
- Jumlah user yang digunakan: 105283
- Jumlah rating user yang digunakan: 1149780

### Reduksi Data
Dengan jumlah dataset yang sangat besar, model machine learning akan sangat sulit dijalankan karena keterbatasan resource hardware dan tingkat waktu yang lama, sehingga perlu dilakukan reduksi data. Data yang digunakan akan diambil berdasarkan user dengan jumlah 1000 user, sehingga jumlah data akan berubah menjadi seperti ini.
- Jumlah vuku yang digunakan: 27636
- Jumlah user yang digunakan: 3000
- Jumlah rating user yang digunakan: 34897

Dan melakukan penghapusan data kosong dari penggabungan data tersebut, karena dapat mengganggu jalannya proses training model

Kemudian dari data `df_rating` terlihat bahwa hanya 271360 anime yang digunakan.

### Save & Load Data
Data yang telah dipilih dan direduksi, selanjutnya perlu disimpan agar dapat langsung digunakan kembali tanpa harus load data yang besar di awal. Proses save & load data dapat dilakukan dengan mudah menggunakan library dari Pandas.

### Encoding Data
Encoding data dilakukan untuk mengubah fitur user_id dan anime_id menjadi indeks integer yang terurut, perlakuan tersebut diperlukan sesuai kebutuhan model. Berikut tabel hasil encoding yang dilakukan.

|index|user\_id|ISBN|rating|user|book|
|---|---|---|---|---|---|
|31390|254465|044661064X|0\.0|2756|7112|
|15895|155149|3828450431|0\.0|1728|13404|
|28973|242639|0743467523|2\.0|2624|11898|
|32803|266824|3426011476|5\.0|2885|26292|
|4884|55821|0671776134|0\.0|629|4498|
|13987|142524|0811813088|0\.0|1575|11974|
|24224|212898|0552136832|0\.0|2335|20006|
|29321|243077|0451454537|0\.0|2629|9878|

kolom user merupakan hasil encoding dari kolom user_id, dan kolom anime merupakan hasil encoding dari kolom ISBN. Kolom user, buku, dan rating tersebut yang akan dimasukkan ke dalam pelatihan model.

### Splitting Data & Normalization
Setelah itu, splitting dataset dilakukan untuk membagi dataset menjadi data training dan data testing dengan rasio perbandingan 80% data training dan 20% data testing. Tahapan ini dilakukan untuk mempertahankan beberapa data sehingga sebagian data akan dilakukan training pada model kemudian sebagian data lainnya dapat dilakukan testing untuk evaluasi terhadap model yang telah di-training. Sehingga total jumlah data hasil splitting yaitu:
- Total # of sample in whole dataset: 34897
- Total # of sample in train dataset: 27917
- Total # of sample in test dataset: 6980

Selain itu normalisasi data juga diterapkan pada fitur target yaitu fitur y sebagai nilai rating yang diberikan user. Normalisasi dilakukan dengan mengambil nilai minimum dan maksimum data y dan mengubah data tersebut menjadi rentang 0 - 1.

## Modelling
Selanjutnya ketika data sudah siap untuk digunakan maka pengembangan model machine learning akan dilakukan. Pada bagian ini, model dibuat dengan menerapkan metode Collaborative Filtering, modelling dilakukan dengan menghitung skor kecocokan antara user dan anime dengan teknik embedding. Pertama, dilakukan proses embedding terhadap data user dan anime. Selanjutnya, melakukan operasi perkalian dot product antara embedding user dan anime. Selain itu, bias juga ditambahkan untuk setiap user dan anime. Kemudian layer dense juga diterapkan dengan aktivasi Relu sebelum layer output. Terakhir pada layer output skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid.

Untuk menghasilkan model yang terbaik, parameter tuning diterapkan pada model dengan dua variasi parameter yaitu pada optimizer dan jumlah ukuran embedding yang digunakan, berikut parameter yang akan di-tuning.
- 'optimizer': ['Adam', 'RMSprop'],
- 'embedding_size': [50, 100]

Kemudian perhitungan loss yang digunakan pada model binary crossentropy dan metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE). Selanjutnya pelatihan dimulai dengan jumlah epochs=30 dan batch_size=64.

### Mengambil rekomendasi dari satu user

Pada bagian ini model akan diuji secara langsung dengan menginput satu user data untuk melihat bagaimana hasil rekomendasi anime yang diperoleh. Pada contoh disini diambil satu user dengan top 10 buku yang telah ditonton dan diberi rating adalah sebagi berikut.
|index|ISBN|Book\_Title|Book\_Author|Year\_Of\_Publication|Publisher|
|---|---|---|---|---|---|
|7717|0451173139|Night over Water|Ken Follett|1992|Signet Book|
|13753|0060951273|El plan infinito|Isabel Allende|1995|Rayo|
|28228|8429445617|El burlador de Sevilla / Don Juan Tenorio|Tirso De Molina|1995|Santillana USA Publishing Company|
|165447|2737626811|Du cÃ?Â´tÃ?Â© de chez Swann|Marcel Proust|1990|Futuropolis|
|165622|8401380332|Cantar De Agapito Robles/Revelation of Agapito Robles|Manuel Scorza|1983|Aims Intl Books|
|166316|379131260X|Max Ernst: Dada and the Dawn of Surrealism|William A\. Camfield|1993|Prestel|
|166424|8401381126|El Presidente \(Plaza &amp; JanÃ©s literaria\)|CristÃ³bal Zaragoza|1987|Plaza &amp; JanÃ©s|
|166499|8420672114|El 19 de Marzo y El 2 de Mayo|Benito Perez Galdos|2001|Alianza|
|166732|0195010434|Marcelino Pan Y Vino|J\.M\. Sanchez-Silva|1940|Oxford University Press|
|166879|8420612693|Cuentos Romanos|Alberto Moravia|1992|Alianza|
|index|ISBN|Book\_Title|Book\_Author|Year\_Of\_Publication|Publisher|

Dari 10 buku yang telah dibaca, dapat dilihat bahwa data dari 10 . 

Kemudian sistem rekomendasi akan melakukan prediksi terhadap user tersebut dengan menginput data daftar anime yang belum pernah dibaca. Berikut ini adalah top 10 buku yang direkomendasikan.

|---|---|---|---|---|---|
|243|140003180X|The Kalahari Typing School for Men \(No\. 1 Ladies' Detective Agency\)|ALEXANDER MCCALL SMITH|2004|Anchor|
|249|0804111359|Secret History|DONNA TARTT|1993|Ballantine Books|
|1207|0380789019|Neverwhere|Neil Gaiman|1998|Avon|
|1324|0385335881|Shopaholic Takes Manhattan \(Summer Display Opportunity\)|Sophie Kinsella|2002|Delta|
|1375|044990928X|Operating Instructions: A Journal of My Son's First Year|Anne Lamott|1994|Ballantine Books|
|4941|0066214122|Prey: A Novel|Michael Crichton|2002|HarperCollins|
|10176|0425107469|Watchers|Dean R\. Koontz|1996|Berkley Publishing Group|
|11121|0743211227|The Prize Winner of Defiance, Ohio : How My Mother Raised 10 Kids on 25 Words or Less|Terry Ryan|2001|Simon &amp; Schuster|
|41078|0380709120|Henry Huggins \(50th Anniversary Edition\)|Beverly Cleary|1990|HarperTrophy|
|41246|0425144062|Witches' Bane|Susan Wittig Albert|1994|Berkley Publishing Group|


Dari hasil yang didapatkan, dapat dilihat program dapat memunculkan hasil dari rekomendasi buku yang dapat dibaca oleh pengguna. 

## Evaluation
Tahapan terakhir yang perlu dilakukan adalah evaluasi model machine learning. Seperti yang sudah dijelaskan pada bagian-bagian sebelumnya bahwa proyek ini akan menghitung evaluasi model menggunakan root mean squared error (rmse). Root Mean Square Error (RMSE) adalah metode pengukuran dengan mengukur perbedaan nilai dari prediksi sebuah model sebagai estimasi atas nilai yang diobservasi. Root Mean Square Error adalah hasil dari akar kuadrat Mean Square Error. RMSE dihitung dengan mengurangi nilai aktual dengan nilai peramalan kemudian dikuadratkan dan dijumlahkan keseluruhan hasilnya kemudian dibagi dengan banyaknya data. Hasil perhitungan tersebut selanjutnya dihitung kembali untuk mencari nilai dari akar kuadrat.

$$ RMSE = \sqrt{\frac{\sum_{t=1}^{n} \left ( actual_t-predict_t \right )}{n}} $$

Dari hasil modelling yang telah dilakukan, terdapat empat model yang dihasilkan setelah training selesai, yaitu sebagai berikut.

| Index |   Model | Parameters                  |
|------:|--------:|-----------------------------|
|   0   | model_1 | opt: Adam, emb_size: 50     |
|   1   | model_2 | opt: Adam, emb_size: 100    |
|   2   | model_3 | opt: RMSprop, emb_size: 50  |
|   3   | model_4 | opt: RMSprop, emb_size: 100 |

Berikut ini adalah perbandingan evaluasi RMSE dan Loss dari hasil training per epoch yang telah dilakukan pada setiap model.

![2](https://user-images.githubusercontent.com/76621303/224554655-aed41c66-5c76-439b-94bc-22c9f325da0a.png)

![3](https://user-images.githubusercontent.com/76621303/224554661-06a7eb39-a88f-4bc9-a664-da3df0c013fd.png)

Selanjutnya adalah visualisasi dari perbadingan rmse dan loss dari hasil training pada setiap model menggunakan bar chart.

![4 bener](https://user-images.githubusercontent.com/76621303/224555024-3075306a-b888-4db3-94c2-68dd23e00cd3.png)


Dari hasil perbandingan performa model tersebut, model_2 dengan optimizer RMSprop dan emb_size 50 memperoleh tingkat RMSE yang paling rendah pada data testing dan pada tingkat loss model memiliki nilai yang relatif cukup rendah daripada model yang lain yaitu 0,31 pada training dan 0,46. Sehingga pada proyek ini model yang akan digunakan adalah model_2.


