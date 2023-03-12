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

### `anime.csv`
Pada dataset ini terdapat 34 kolom dan 17.562 baris data. Dataset ini berisi informasi umum pada setiap anime seperti name, genre, premiered, studio, dll. Beberapa data yang penting dalam proyek ini yaitu judul anime dan genre anime. Pada bagian genre dilakukan analisis lebih lanjut dengan mengambil jumlah seluruh anime terhadap genre tertentu, terdapat 44 genre berbeda pada seluruh anime yang ada, kemudian data jumlah anime terhadap diurutkan berdasarkan terbesar ke terkecil. Berikut ini diagram hasil jumlah anime setiap genre.

![Top Genre](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/DU_TG.png)


Jika dilihat dari data tersebut berikut tabel 10 top genre anime terbanyak.

| Index |         Genre | Total |
|------:|--------------:|------:|
|   0   |        Comedy |  6029 |
|   1   |        Action |  3888 |
|   2   |       Fantasy |  3285 |
|   3   |     Adventure |  2957 |
|   4   |          Kids |  2665 |
|   5   |         Drama |  2619 |
|   6   |        Sci-Fi |  2583 |
|   7   |         Music |  2244 |
|   8   |       Shounen |  2003 |
|   9   | Slice of Life |  1914 |

Dari hasil tersebut dapat dilihat bahwa terdapat 6029 anime ber-genre Comedy, genre tersebut terbanyak daripada genre lainnya, disusul dengan genre Action dan Fantasy.

### `animelist.csv`
Pada dataset ini terdapat 5 kolom dan 109.224.747 baris data. Dataset ini berisi daftar seluruh anime yang diberi rating oleh user, didukung dengan status menonton (watching_status) dan jumlah episode yang telah ditonton. Pada dataset ini terdapat 325.772 user yang memberikan rating terhadap 17.562 judul anime. Kemudian analisis lebih lanjut terhadap nilai rating dan watching_status. 

Pada nilai rating (0 - 10) dilakukan analisis terhadap berapa jumlah user yang memberikan rating tertentu terhadap seluruh anime. Berikut hasil pengurutan jumlah rating 0 - 10, rating 0 adalah nilai ketika user tidak memberikan rating terhadap anime.

![Top Rating](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/DU_TR.png)

Jika dilihat dari data tersebut berikut tabel top jumlah rating user terbanyak.

| Index | Rating |    Total |
|------:|-------:|---------:|
|   0   |      0 | 46827035 |
|   1   |      8 | 15422150 |
|   2   |      7 | 14244633 |
|   3   |      9 | 10235934 |
|   4   |      6 |  7543377 |
|   5   |     10 |  7144392 |
|   6   |      5 |  4029645 |
|   7   |      4 |  1845854 |
|   8   |      3 |   905700 |
|   9   |      2 |   545339 |
|   10  |      1 |   480688 |

Dari hasil tersebut dapat dilihat bahwa rating dengan nilai 0 menjadi rating terbanyak yang ada oleh user, yang artinya mayoritas user tidak memberikan rating terhadap anime yang mereka tonton. Kemudian disusul dengan rating 8 dan 7 dibawahnya.

Kemudian pada watching_status dilakukan analisis terhadap jumlah status user ketika menonton anime. Terdapat 5 status yang ada yaitu sebagai berikut.

| index | status |        description |
|------:|-------:|-------------------:|
|   0   |      1 | Currently Watching |
|   1   |      2 |          Completed |
|   2   |      3 |            On Hold |
|   3   |      4 |            Dropped |
|   4   |      6 |      Plan to Watch |

Namun dari 5 status tersebut ketika dilakukan cek unique data ternyata terdapat data yang salah input, yaitu terdapat nilai 5, 33, dan 55. Sehingga baris data yang terdapat pada nilai yang salah tersebut harus dihapus. Kemudian data yang telah dibersihkan dihitung jumlah user pada setiap watching_status. Berikut ini diagram hasil jumlah user setiap watching_status.

![Top Status](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/DU_TS.png)

Jika dilihat dari data tersebut berikut tabel top jumlah watching_status user terbanyak.

| Index | Watching Status |    Total |
|------:|----------------:|---------:|
|   0   |               2 | 68089751 |
|   1   |               6 | 27938693 |
|   2   |               1 |  5228658 |
|   3   |               4 |  4266591 |
|   4   |               3 |  3700514 |
|   5   |               0 |      531 |

Dari hasil tersebut dapat dilihat bahwa watching_status terbanyak bernilai 2, yang artinya mayoritas user telah selesai menonton anime tersebut, kemudian diikuti dengan status bernilai 6 yaitu user berencana untuk menonton anime tersebut.

### `rating_complete.csv`
Pada dataset ini terdapat 3 kolom dan 57.633.278 baris data yang berisi daftar seluruh anime yang diberi rating oleh user dengan status user telah selesai menonton anime tersebut dan memberikan rating 1 - 10. Pada dataset ini terdapat 310.059 user memberikan rating terhadap 16.872 judul anime. Analisis dilakukan pada dataset ini dengan mencari nilai rating terbanyak yang diberikan oleh user. Berikut hasil pengurutan jumlah rating 1 - 10.

![Top Rating Complete](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/DU_TRC.png)

Jika dilihat dari data tersebut berikut tabel top jumlah rating user terbanyak.

| Index | Rating |    Total |
|------:|-------:|---------:|
|   0   |      8 | 14642156 |
|   1   |      7 | 13325549 |
|   2   |      9 |  9773857 |
|   3   |      6 |  6849293 |
|   4   |     10 |  6716048 |
|   5   |      5 |  3436250 |
|   6   |      4 |  1455102 |
|   7   |      3 |   696048 |
|   8   |      2 |   405556 |
|   9   |      1 |   333419 |

Dari hasil data tersebut dapat dilihat bahwa rating yang paling banyak diberikan oleh user bernilai 8 dan diikuti oleh rating 7, kemudian rating yang paling sedikit yaitu bernilai 1. Hasil data tersebut tersebar secara merata disekitar rating 6-10. 

## Data Preparation
Setelah analisis dilakukan, pada bagian ini hal pertama yang dilakukan adalah memilih dataset yang akan digunakan. Data yang dipilih untuk digunakan yaitu pada `anime.csv` (kolom: "MAL_ID", "Name", "Score", "Genres", "Premiered") dimasukan kedalam variabel `df_anime` sebagai tempat seluruh detail anime dan `rating_complete.csv` (kolom: "user_id", "anime_id", "rating") dimasukan kedalam variabel `df_rating` sebagai nilai rating yang diberikan oleh user. Kemudian kolom pada data `df_anime` dilakukan rename agar format nama menjadi sama rata. Berikut contoh data tersebut.

Dataset `df_anime`
| index | anime_id |                            name | score |                                            genres |   premiered |
|------:|---------:|--------------------------------:|------:|--------------------------------------------------:|------------:|
|   0   |        1 |                    Cowboy Bebop |  8.78 |   Action, Adventure, Comedy, Drama, Sci-Fi, Space | Spring 1998 |
|   1   |        5 | Cowboy Bebop: Tengoku no Tobira |  8.39 |             Action, Drama, Mystery, Sci-Fi, Space |     Unknown |
|   2   |        6 |                          Trigun |  8.24 | Action, Sci-Fi, Adventure, Comedy, Drama, Shounen | Spring 1998 |
|   3   |        7 |              Witch Hunter Robin |  7.27 | Action, Mystery, Police, Supernatural, Drama, ... | Summer 2002 |
|   4   |        8 |                  Bouken Ou Beet |  6.98 |         Adventure, Fantasy, Shounen, Supernatural |   Fall 2004 |

Dataset `df_rating`
| index | user_id | anime_id | rating |
|------:|--------:|---------:|-------:|
|   0   |       0 |      430 |      9 |
|   1   |       0 |     1004 |      5 |
|   2   |       0 |     3010 |      7 |
|   3   |       0 |      570 |      7 |
|   4   |       0 |     2762 |      9 |

Kemudian dari data tersebut melihat jumlah data yang digunakan yaitu:
- Jumlah anime yang digunakan: 16872
- Jumlah user yang digunakan: 310059
- Jumlah rating user yang digunakan: 57633278

### Reduksi Data
Dengan jumlah dataset yang sangat besar, model machine learning akan sangat sulit dijalankan karena keterbatasan resource hardware dan tingkat waktu yang lama, sehingga perlu dilakukan reduksi data. Data yang digunakan akan diambil berdasarkan user dengan jumlah 1000 user, sehingga jumlah data akan berubah menjadi seperti ini.
- Jumlah anime yang digunakan: 8799
- Jumlah user yang digunakan: 1000
- Jumlah rating user yang digunakan: 185054

Kemudian dari data `df_rating` terlihat bahwa hanya 8799 anime yang digunakan, sehingga pada data anime dapat dihapus beberapa baris yang tidak digunakan pada data `df_rating` dengan cara merge data kemudian menghapus baris yang memiliki nilai Null di kolom rating.

### Save & Load Data
Data yang telah dipilih dan direduksi, selanjutnya perlu disimpan agar dapat langsung digunakan kembali tanpa harus load data yang besar di awal. Proses save & load data dapat dilakukan dengan mudah menggunakan library dari Pandas.

### Encoding Data
Encoding data dilakukan untuk mengubah fitur user_id dan anime_id menjadi indeks integer yang terurut, perlakuan tersebut diperlukan sesuai kebutuhan model. Berikut tabel hasil encoding yang dilakukan.

|  index | user_id | anime_id | rating | user | anime |
|-------:|--------:|---------:|-------:|-----:|------:|
| 138194 |  273551 |    33023 |   10.0 |  780 |  1512 |
| 181703 |  347346 |     9907 |   10.0 |  973 |  2723 |
| 142278 |  277840 |      482 |    5.0 |  796 |  2042 |
| 158594 |  316982 |    14117 |    7.0 |  896 |  4409 |
| 135400 |  264929 |    20159 |    8.0 |  756 |   767 |

kolom user merupakan hasil encoding dari kolom user_id, dan kolom anime merupakan hasil encoding dari kolom anime_id. Kolom user, anime, dan rating tersebut yang akan dimasukkan ke dalam pelatihan model.

### Splitting Data & Normalization
Setelah itu, splitting dataset dilakukan untuk membagi dataset menjadi data training dan data testing dengan rasio perbandingan 90% data training dan 10% data testing. Tahapan ini dilakukan untuk mempertahankan beberapa data sehingga sebagian data akan dilakukan training pada model kemudian sebagian data lainnya dapat dilakukan testing untuk evaluasi terhadap model yang telah di-training. Sehingga total jumlah data hasil splitting yaitu:
- Total sample in whole dataset: 185054
- Total sample in train dataset: 166548
- Total sample in test dataset: 18506

Selain itu normalisasi data juga diterapkan pada fitur target yaitu fitur y sebagai nilai rating yang diberikan user. Normalisasi dilakukan dengan mengambil nilai minimum dan maksimum data y dan mengubah data tersebut menjadi rentang 0 - 1.

## Modelling
Selanjutnya ketika data sudah siap untuk digunakan maka pengembangan model machine learning akan dilakukan. Pada bagian ini, model dibuat dengan menerapkan metode Collaborative Filtering, modelling dilakukan dengan menghitung skor kecocokan antara user dan anime dengan teknik embedding. Pertama, dilakukan proses embedding terhadap data user dan anime. Selanjutnya, melakukan operasi perkalian dot product antara embedding user dan anime. Selain itu, bias juga ditambahkan untuk setiap user dan anime. Kemudian layer dense juga diterapkan dengan aktivasi Relu sebelum layer output. Terakhir pada layer output skor kecocokan ditetapkan dalam skala [0,1] dengan fungsi aktivasi sigmoid.

Untuk menghasilkan model yang terbaik, parameter tuning diterapkan pada model dengan dua variasi parameter yaitu pada optimizer dan jumlah ukuran embedding yang digunakan, berikut parameter yang akan di-tuning.
- 'optimizer': ['Adam', 'RMSprop'],
- 'embedding_size': [50, 100]

Kemudian perhitungan loss yang digunakan pada model binary crossentropy dan metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE). Selanjutnya pelatihan dimulai dengan jumlah epochs=30 dan batch_size=64.

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

![Evaluation Epoch RMSE](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/EV_ERM.png)

![Evaluation Epoch Loss](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/EV_ELS.png)

Selanjutnya adalah visualisasi dari perbadingan rmse dan loss dari hasil training pada setiap model menggunakan bar chart.

![Evaluation Model](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/EV_COM.png)

Dari hasil perbandingan performa model tersebut, model_3 dengan optimizer RMSprop dan emb_size 50 memperoleh tingkat RMSE yang paling rendah pada data training maupun data testing dan pada tingkat loss model memiliki nilai yang relatif cukup rendah daripada model yang lain. Sehingga pada proyek ini model yang akan digunakan adalah model_3.

### Mengambil rekomendasi dari satu user

Pada bagian ini model akan diuji secara langsung dengan menginput satu user data untuk melihat bagaimana hasil rekomendasi anime yang diperoleh. Pada contoh disini diambil satu user dengan top 10 anime yang telah ditonton dan diberi rating adalah sebagi berikut.

| rank | anime_id |                                            name | score |                                            genres |   premiered |
|-----:|---------:|------------------------------------------------:|------:|--------------------------------------------------:|------------:|
|   1  |     5630 |                                 Higashi no Eden |  7.83 | Action, Sci-Fi, Mystery, Drama, Romance, Thriller | Spring 2009 |
|   2  |     6213 |                         Toaru Kagaku no Railgun |  7.72 |                       Action, Sci-Fi, Super Power |   Fall 2009 |
|   3  |     6880 |                              Deadman Wonderland |  7.22 |     Action, Horror, Sci-Fi, Shounen, Supernatural | Spring 2011 |
|   4  |     7054 |                           Kaichou wa Maid-sama! |  8.06 |                   Comedy, Romance, School, Shoujo | Spring 2010 |
|   5  |     7724 |                                           Shiki |  7.79 |  Horror, Mystery, Supernatural, Thriller, Vampire | Summer 2010 |
|   6  |    15315 | Mondaiji-tachi ga Isekai kara Kuru Sou Desu yo? |  7.56 |             Action, Comedy, Fantasy, Supernatural | Winter 2013 |
|   7  |    21431 |                           Gokukoku no Brynhildr |  6.92 |                    Drama, Mystery, Sci-Fi, Seinen | Spring 2014 |
|   8  |    22319 |                                     Tokyo Ghoul |  7.81 | Action, Mystery, Horror, Psychological, Supern... | Summer 2014 |
|   9  |    27655 |                         Aldnoah.Zero 2nd Season |  6.98 |                      Action, Mecha, Sci-Fi, Space | Winter 2015 |
|  10  |    33253 |                                 Ajin 2nd Season |  7.68 |     Action, Horror, Mystery, Seinen, Supernatural |   Fall 2016 |

Dari 10 anime yang telah ditonton, dapat dilihat bagaimana genre yang paling disukai dengan mencari jumlah genre setiap anime tersebut. Berikut ini hasil visualisasi top 10 genre anime yang disukai user.

![Top User Genre](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/EV_TUG.png)

Dari visualisasi diatas terlihat bahwa user tersebut sangat menyukai anime dengan genre action, mystery, sci-fi, supernatural, dan horror.

Kemudian sistem rekomendasi akan melakukan prediksi terhadap user tersebut dengan menginput data daftar anime yang belum pernah ditonton. Berikut ini adalah top 10 anime yang direkomendasikan.

| rank | anime_id |                                              name | score |                                            genres |   premiered |
|-----:|---------:|--------------------------------------------------:|------:|--------------------------------------------------:|------------:|
|   1  |      457 |                                          Mushishi |  8.69 | Adventure, Slice of Life, Mystery, Historical,... |   Fall 2005 |
|   2  |      820 |                              Ginga Eiyuu Densetsu |  9.07 |                    Military, Sci-Fi, Space, Drama |     Unknown |
|   3  |     4181 |                              Clannad: After Story |  8.96 | Slice of Life, Comedy, Supernatural, Drama, Ro... |   Fall 2008 |
|   4  |     5114 |                  Fullmetal Alchemist: Brotherhood |  9.19 | Action, Military, Adventure, Comedy, Drama, Ma... | Spring 2009 |
|   5  |     9969 |                                          Gintama' |  9.08 | Action, Sci-Fi, Comedy, Historical, Parody, Sa... | Spring 2011 |
|   6  |    11061 |                            Hunter x Hunter (2011) |   9.1 |  Action, Adventure, Fantasy, Shounen, Super Power |   Fall 2011 |
|   7  |    15335 | Gintama Movie 2: Kanketsu-hen - Yorozuya yo Ei... |  8.96 | Action, Sci-Fi, Comedy, Historical, Parody, Sa... |     Unknown |
|   8  |    15417 |                               Gintama': Enchousen |  9.04 | Action, Comedy, Historical, Parody, Samurai, S... |   Fall 2012 |
|   9  |    28977 |                                          Gintama° |   9.1 | Action, Comedy, Historical, Parody, Samurai, S... | Spring 2015 |
|  10  |    38524 |                Shingeki no Kyojin Season 3 Part 2 |   9.1 | Action, Drama, Fantasy, Military, Mystery, Sho... | Spring 2019 |

Selanjutnya dari 10 anime yang direkomendasikan, dapat dilihat genre anime yang direkomendasi. Berikut ini hasil visualisasi top 10 genre anime rekomendasi.

![Top Recommendation Genre](https://raw.githubusercontent.com/RTAgung/Machine-Learning-Terapan/master/assets/submission_2/EV_TRG.png)

Dari visualisasi diatas terlihat bahwa anime yang direkomendasikan kebanyakan memiliki genre action, shounen, comedy, historical, dan sci-fi. Jika dibandingkan dengan genre anime yang disukai user, terdapat kesamaan dari hasil rekomendasi yaitu genre comedy dan sci-fi. Hasil tersebut dapat membuktikan bahwa prediksi yang dihasilkan dari sistem rekomendasi sudah cukup baik untuk digunakan oleh user.

## Referensi
- [Anime Industry Report 2019](https://namafar.ir/wp-content/uploads/2022/02/2019_Anime_ind_rpt_summary_enr.pdf)
- [Rekomendasi Anime dengan Latent Semantic Indexing Berbasis Sinopsis Genre](https://www.researchgate.net/publication/274712918_Rekomendasi_Anime_dengan_Latent_Semantic_Indexing_Berbasis_Sinopsis_Genre)