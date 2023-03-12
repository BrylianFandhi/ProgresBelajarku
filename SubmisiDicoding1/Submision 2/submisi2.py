# -*- coding: utf-8 -*-
"""Submisi2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IweoH8DJBOD36kushp5RdAGFHtH0sMc5

# Import Library
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf

# %matplotlib inline

import tensorflow as tf
import pandas as pd
import numpy as np
import cv2
from PIL import Image


import os
import zipfile
import shutil
import random
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
from shutil import copyfile


from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img
from tensorflow.keras.preprocessing import image_dataset_from_directory
from keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers.experimental import preprocessing

# Library Evaluation 
import shutil
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


import pathlib

"""# Load Data

### Download data
"""

shutil.rmtree('data', ignore_errors=True)

! mkdir data

! pip install kaggle

#Tidak Tau

! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

# os.remove('anime-recommendation-database-2020.zip')
! kaggle datasets download -d arashnic/book-recommendation-dataset
! mkdir data
! unzip book-recommendation-dataset.zip -d data/buku
os.remove('book-recommendation-dataset.zip')

"""### Read CSV"""

path_buku = '/content/data/buku/Books.csv'
path_user = '/content/data/buku/Users.csv'
path_rating = '/content/data/buku/Ratings.csv'


buku = pd.read_csv(path_buku)
user = pd.read_csv(path_user)
rating = pd.read_csv(path_rating)

"""# Data Understanding

Macam-macam file yang ada:
- `Books.csv` Berisi informasi Buku, seperti ID, Judul, penulis, penerbit, DSB.
- `Ratings.csv` Rating User terhadap Buku yang dibaca.
- `Users.csv` Informasi mengenai pengguna.
"""

print('Jumlah data Buku: ', len(buku))
print('Jumlah data  user: ', len(user))
print('Jumlah data rating: ', len(rating))

"""### Analisis data pada Books.csv"""

buku.info()

buku = buku[["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication", "Publisher"]]
buku.columns = ["ISBN", "Book_Title", "Book_Author", "Year_Of_Publication", "Publisher"]

buku.head()

print("Jumlah Buku berdasarkan ID:", len(buku.ISBN.unique()))

print("Jumlah Publisher:", len(buku.Publisher.unique()))

"""cek data null"""

buku.isnull().sum()

"""cek duplicated data"""

buku.duplicated().sum()

# top rating
total_rating_complete_user = buku.Book_Author.value_counts()
pd.DataFrame({
    "Auhor": list(total_rating_complete_user.keys()),
    "Total": list(total_rating_complete_user)
}).head(10)

"""### Analisis data pada rating.csv

This dataset only considers animes that the user has watched completely (watching_status==2) and gave it a score (score!=0)
"""

rating.head()

rating = rating[["User-ID", "ISBN", "Book-Rating"]]
rating.columns = ['user_id', 'ISBN', 'rating']

rating.info()

"""cek data null"""

rating.isnull().sum()

"""cek ducplicated data"""

rating.duplicated().sum()

print("Jumlah aktivitas user terhadap anime:", len(rating.user_id.unique()))
print("Jumlah anime:", len(rating.ISBN.unique()))

# top rating
total_rating_complete_user = rating.rating.value_counts()
pd.DataFrame({
    "Rating": list(total_rating_complete_user.keys()),
    "Total": list(total_rating_complete_user)
})

plt.figure(figsize=(12,6))
sns.barplot(x = list(total_rating_complete_user.keys()),
            y = list(total_rating_complete_user))
plt.title("Diagram Top Rating Seluruh User (dalam satuan 10 juta)")
plt.show()

"""### Analisis data pada animelist.csv"""

user.info()

user = user[["User-ID", "Location", "Age"]]
user.columns = ['user_id', 'location', 'age']

"""cek data kosong"""

user.isnull().sum()

"""cek duplikasi data"""

user.duplicated().sum()

"""# Data Preparation

Memilih data yang akan digunakan
"""

df_user = user
df_buku = buku
df_rating = rating

df_buku.head()

df_user.head()

df_rating.head()

"""Dikarenakan pada data rating memiliki data yang bernilai 0 atau rating yangg bernilai 0 terlalu banyak, maka akan dilakukan penghapusan data"""

df_rating.drop(df_rating.loc[df_rating['rating']==0].index, inplace=True)

# top rating
total_rating_complete_user = df_rating.rating.value_counts()
pd.DataFrame({
    "Rating": list(total_rating_complete_user.keys()),
    "Total": list(total_rating_complete_user)
})

print("Jumlah anime yang digunakan:", len(df_rating.ISBN.unique()))
print("Jumlah user yang digunakan:", len(df_rating.user_id.unique()))
print("Jumlah rating user yang digunakan:", len(df_rating))

"""karena data terlalu besar, training model dilakukan hanya mengambil data sebanyak 1000 user saja"""

# user_ids = np.array(df_rating.user_id.unique().tolist())

# np.random.seed(42)
# np.random.shuffle(user_ids)
# user_ids = user_ids[:1000]

# df_rating = df_rating[df_rating.user_id.isin(user_ids)]

print("Jumlah anime yang digunakan:", len(df_rating.ISBN.unique()))
print("Jumlah user yang digunakan:", len(df_rating.user_id.unique()))
print("Jumlah rating user yang digunakan:", len(df_rating))

"""cek data hubungan anime dengan rating, apakah semua rating anime memiliki detail anime"""

df_merge = pd.merge(df_rating, df_buku[['user_id', 'Book_Title']], on='user_id', how='left')
df_merge.head()

df_merge = pd.merge(df_merge, df_buku[['ISBN', 'Book_Title']], on='ISBN', how='left')
df_merge.head()

df_merge.isna().sum()

"""Karena terlalu banyak data kosong pada judul Buku. Maka bisa dilakukan eliminasi."""

df2 = df_merge.dropna()

df2.isna().sum()

df2.head()

"""cek data hubungan anime dengan rating, apakah semua detail anime memiliki rating"""

df_merge2 = pd.merge(df_buku[['ISBN', 'Book_Title']], df_rating, on='ISBN', how='left')
df_merge2.head()

df_merge2.isna().sum()

"""Mengghapus data kosong"""

df3 = df_merge2.dropna()

df3.isna().sum()

df3.head()

"""terdapat 8763 data detail anime yang tidak memiliki rating"""

unused_anime_id = df_merge[df_merge.rating.isna()].ISBN.unique().tolist()

df_buku2 = df_buku[~(df_buku.ISBN.isin(unused_anime_id))]
print("Jumlah detail anime yang digunakan:", len(df_buku.ISBN.unique()))

"""save final data"""

df_rating.to_csv('final_rating.csv', index=False)
df_buku2.to_csv('final_buku.csv', index=False)

"""load final data"""

df_rating = pd.read_csv('final_rating.csv')
df_book = pd.read_csv('final_buku.csv')

df_rating

"""encoding data"""

# Mengubah user_id menjadi list tanpa nilai yang sama
user_ids = df_rating['user_id'].unique().tolist()
 
# Melakukan encoding user_id
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
 
# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

# Mengubah book_id menjadi list tanpa nilai yang sama
book_ids = df_rating['ISBN'].unique().tolist()
 
# Melakukan proses encoding book_id
book_to_book_encoded = {x: i for i, x in enumerate(book_ids)}
 
# Melakukan proses encoding angka ke book_id
book_encoded_to_book = {i: x for i, x in enumerate(book_ids)}

# Mapping user_id ke dataframe user
df_rating['user'] = df_rating['user_id'].map(user_to_user_encoded)
 
# Mapping book_id ke dataframe book
df_rating['book'] = df_rating['ISBN'].map(book_to_book_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)
 
# Mendapatkan jumlah book
num_book = len(book_encoded_to_book)
print(num_book)
 
# Mengubah rating menjadi nilai float
df_rating['rating'] = df_rating['rating'].values.astype(np.float32)
 
# Nilai minimum rating
min_rating = min(df_rating['rating'])
 
# Nilai maksimal rating
max_rating = max(df_rating['rating'])
 
print('Number of User: {}, Number of Book: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_book, min_rating, max_rating
))

# Mengacak dataset
df_rating = df_rating.sample(frac=1, random_state=42)
df_rating

"""splitting data"""

# Membuat variabel x untuk mencocokkan data user_id dan book_id menjadi satu value
x = df_rating[['user', 'book']].values
 
# Membuat variabel y untuk membuat rating dari hasil 
y = df_rating['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values
 
# Membagi menjadi 90% data train dan 10% data validasi
train_indices = int(0.8 * df_rating.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x[:10], y[:10])

print(f'Total # of sample in whole dataset: {len(x)}')
print(f'Total # of sample in train dataset: {len(x_train)}')
print(f'Total # of sample in test dataset: {len(x_val)}')

"""# Model Development"""

class RecommenderNet(tf.keras.Model):
 
  # Insialisasi fungsi
  def __init__(self, num_users, num_book, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_book = num_book
    self.embedding_size = embedding_size
    self.user_embedding = tf.keras.layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = tf.keras.regularizers.l2(1e-6)
    )
    self.user_bias = tf.keras.layers.Embedding(num_users, 1) # layer embedding user bias
    self.book_embedding = tf.keras.layers.Embedding( # layer embeddings book
        num_book,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = tf.keras.regularizers.l2(1e-6)
    )
    self.book_bias = tf.keras.layers.Embedding(num_book, 1) # layer embedding buku bias
    self.dense1 = tf.keras.layers.Dense(32, activation=tf.nn.relu) # layer dense
    self.dense2 = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid) # layer output activation sigmoid
 
  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0])
    user_bias = self.user_bias(inputs[:, 0]) 
    book_vector = self.book_embedding(inputs[:, 1]) 
    book_bias = self.book_bias(inputs[:, 1]) 
 
    dot_user_book = tf.tensordot(user_vector, book_vector, 2) 
 
    x = dot_user_book + user_bias + book_bias
    x = self.dense1(x)
    x = self.dense2(x)
    return x

def create_model(optimizer, embedding_size):
    tf_model = RecommenderNet(num_users, num_book, embedding_size)
    tf_model.compile(
        loss = tf.keras.losses.BinaryCrossentropy(),
        optimizer = optimizer,
        metrics=[tf.keras.metrics.RootMeanSquaredError()]
    )
    return tf_model

# Memulai training
import warnings
warnings.filterwarnings('ignore')

model_params = {
    'optimizer': ['Adam', 'RMSprop'],
    'embedding_size': [50, 100]
}

model = {}
history = {}
params = {}

print("Training Parameter: ", model_params)

k = 1
for i in range(2):
    for j in range(2):
        opt = model_params['optimizer'][i]
        emb_size = model_params['embedding_size'][j]

        print("Start Training with optimizer: {} embedding_size: {}".format(opt, emb_size))
        model["model_"+str(k)] = create_model(
            optimizer=opt,
            embedding_size=emb_size,
        )

        history["model_"+str(k)] = model["model_"+str(k)].fit(
            x = x_train,
            y = y_train,
            batch_size = 64,
            epochs = 10,
            validation_data = (x_val, y_val)
        )

        params["model_"+str(k)] = "opt: {}, emb_size: {}".format(opt, emb_size)
        k = k + 1

print("Finish Training")

"""# Evaluation"""

print("Modelname -- Parameter")
for k, v in params.items():
  print("{} -- {}".format(k, v))

"""## Plot History Setiap Model"""

list_modelnames = list(history.keys())

dict_acc = {}
dict_val_acc = {}
dict_loss = {}
dict_val_loss = {}

for modelname, modelhistory in history.items():
  dict_acc[modelname] = modelhistory.history['root_mean_squared_error']
  dict_val_acc[modelname] = modelhistory.history['val_root_mean_squared_error']
  dict_loss[modelname] = modelhistory.history['loss']
  dict_val_loss[modelname] = modelhistory.history['val_loss']

label_plot = list_modelnames
marker_plot = ['o','x','v','^']

plt.figure(figsize=(15, 16))
plt.subplot(2, 1, 1)
for i in range(len(list_modelnames)):
  plt.plot(dict_acc[list_modelnames[i]], label=label_plot[i], marker=marker_plot[i], markersize=6, alpha=0.6)

plt.legend(loc='lower right')
plt.ylabel('RMSE')
plt.title('Training RMSE')

plt.subplot(2, 1, 2)
for i in range(len(list_modelnames)):
  plt.plot(dict_val_acc[list_modelnames[i]], label=label_plot[i], marker=marker_plot[i], markersize=6, alpha=0.6)

plt.legend(loc='lower right')
plt.ylabel('RMSE')
plt.title('Validation RMSE')
plt.xlabel('epoch')
plt.savefig('acc_all_model.png')

plt.show()

plt.figure(figsize=(15, 16))
plt.subplot(2, 1, 1)

for i in range(len(list_modelnames)):
  plt.plot(dict_loss[list_modelnames[i]], label=label_plot[i], marker=marker_plot[i], markersize=6, alpha=0.6)

plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.title('Training Loss')

plt.subplot(2, 1, 2)

for i in range(len(list_modelnames)):
  plt.plot(dict_val_loss[list_modelnames[i]], label=label_plot[i], marker=marker_plot[i], markersize=6, alpha=0.6)
  
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.title('Validation Loss')
plt.xlabel('epoch')

plt.savefig('loss_all_model.png')

plt.show()

"""## Membandingkan Metrik Evaluasi Setiap Model"""

# evaluate all model
dict_score_train = {}
dict_score_valid = {}

for modelname, modelresult in model.items():
  dict_score_train[modelname] = modelresult.evaluate(x_train, y_train)
  dict_score_valid[modelname] = modelresult.evaluate(x_val, y_val)

# prepare data before plot
df1 = pd.DataFrame({
    'Model': list_modelnames,
    'Train': [eval[1] for eval in dict_score_train.values()],
    'Valid': [eval[1] for eval in dict_score_valid.values()],
})

df2 = pd.DataFrame({
    'Model': list_modelnames,
    'Train': [eval[0] for eval in dict_score_train.values()],
    'Valid': [eval[0] for eval in dict_score_valid.values()],
})

tidy1 = df1.melt(id_vars='Model').rename(columns=str.title)

tidy2 = df2.melt(id_vars='Model').rename(columns=str.title)

df2

# plot comparison all models evaluate
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# first plot
sns.barplot(x='Model', y='Value', hue='Variable', data=tidy1, ax=ax1)
ax1.set_ylabel('RMSE')
ax1.set_ylim([0.125, 0.145])
ax1.set_title('RMSE Performance')

for p, data in zip(ax1.patches, tidy1['Value']):
    ax1.annotate(round(data, 5), xy=(p.get_x()+p.get_width()/2, p.get_height()),
                ha='center', va='bottom')

# second plot
sns.barplot(x='Model', y='Value', hue='Variable', data=tidy2, ax=ax2)
ax2.set_ylabel('Loss')
ax2.set_ylim([0.53, 0.55])
ax2.set_title('Loss Performance')

for p, data in zip(ax2.patches, tidy2['Value']):
    ax2.annotate(round(data, 5), xy=(p.get_x()+p.get_width()/2, p.get_height()),
                ha='center', va='bottom')

plt.savefig('evaluate_all_model.png')
plt.show()

"""model_3 (opt: RMSprop, emb_size: 50) dipilih karena memiliki tingkat RMSE paling rendah dan loss relatif rendah

## Mengambil Rekomendasi Satu User
"""

# Mengambil sample user
user_id = df_rating.user_id.sample(1).iloc[0]
book_watched_by_user = df_rating[df_rating.user_id == user_id]
 
book_not_watched = df_book[~df_book['ISBN'].isin(book_watched_by_user.ISBN.values)]['ISBN'] 
book_not_watched = list(
    set(book_not_watched)
    .intersection(set(book_to_book_encoded.keys()))
)
 
book_not_watched = [[book_to_book_encoded.get(x)] for x in book_not_watched]
user_encoder = user_to_user_encoded.get(user_id)
user_book_array = np.hstack(
    ([[user_encoder]] * len(book_not_watched), book_not_watched)
)

ratings_predict = model["model_3"].predict(user_book_array).flatten()
 
top_ratings_indices = ratings_predict.argsort()[-10:][::-1]
recommended_book_ids = [
    book_encoded_to_book.get(book_not_watched[x][0]) for x in top_ratings_indices
]
 
print('Showing recommendations for users: {}'.format(user_id))
print('====' * 10)
print('Top 10 book with high ratings from user')
print('----' * 10)
 
top_book_user = (
    book_watched_by_user.sort_values(
        by = 'rating',
        ascending=False
    )
    .head(10)
    .ISBN.values
)

df_book_rows = df_book[df_book['ISBN'].isin(top_book_user)]
for row in df_book_rows.itertuples():
    print("{} ({}) : {}".format(row.Book_Title, row.Publisher, row.Book_Author))
 
print('----' * 10)
print('Top 10 book recommendation')
print('----' * 10)
 
recommended_book = df_book[df_book['ISBN'].isin(recommended_book_ids)]
for row in recommended_book.itertuples():
    print("{} ({}) : {}".format(row.Book_Title, row.Publisher, row.Book_Author))

print("Book with high ratings from user")
df_book_rows

print("Top 10 Book recommendation")
recommended_book

"""Top Author user likes and recommendation"""

user_authors = []
list_book_authors = df_book_rows.Book_Author.unique()

for i, v in enumerate(list_book_authors):
  user_authors.extend(v.split(', '))

user_authors = sorted(set(user_authors))

total_author_by_user = {g: 0 for g in user_authors}

for book_author in df_book_rows['Book_Author']:
  list_book_author = book_author.split(', ')
  for author in list_book_author:
    total_author_by_user[author] = total_author_by_user[author] + 1

total_author_by_user = dict(sorted(total_author_by_user.items(), key=lambda x:x[1], reverse=True))

plt.figure(figsize=(9,5))
sns.barplot(x = list(total_author_by_user.keys())[:10],
            y = list(total_author_by_user.values())[:10],
            )
plt.xticks(rotation=90)
plt.title("Diagram Top 10 User author book")
plt.show()

recommended_authors = []
list_book_authors = recommended_book.Book_Author.unique()

for i, v in enumerate(list_book_authors):
  recommended_authors.extend(v.split(', '))

recommended_authors = sorted(set(recommended_authors))

total_author_by_recommendation = {g: 0 for g in recommended_authors}

for book_author in recommended_book['Book_Author']:
  list_book_author = book_author.split(', ')
  for author in list_book_author:
    total_author_by_recommendation[author] = total_author_by_recommendation[author] + 1

total_author_by_recommendation = dict(sorted(total_author_by_recommendation.items(), key=lambda x:x[1], reverse=True))

plt.figure(figsize=(9,5))
sns.barplot(x = list(total_author_by_recommendation.keys())[:10],
            y = list(total_author_by_recommendation.values())[:10],
            )
plt.xticks(rotation=90)
plt.title("Diagram Top 3 Recommendation author book")
plt.show()

