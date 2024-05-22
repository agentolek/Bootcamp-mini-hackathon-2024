Analyze each category of signs:
Przeanalizowaliśmy każdą kategorię znakó, pod względem występowania, specjalnych znaków z R lub z podwójnymi B. Ciekawostki.

Clustering gaussian i kmeans:
Klasteryzujemy sekwencje różnymi metodami, a do wktoryzacji używami td-df.
Ciekawy wynik to 1 klaster zawierający w każdej sekwencji jeden znak.

Correlation:
W tym pliku za pomocą Word2Vec zamieniamy nazwy obiektów i sekwencje na wektory, póżniej za pomocą TSNE zmnijeszamy wymiar do jednego. Dla scen stosujemy one hot encoding. I wtedy korelujemy każdą kolumnę z każdą. Pokazuję to że nie ma mocnych korelacji w tym zbiorze danych.

Cosine similarity:
Próba dynamicznej klasteryzacji.

Counting seq len scenes:
w tym pliku liczymy, co ile razy się powtarza. Sekwencje, sceny, cykle i powiązanie liczby scen a sekwencji.

Frequency sign after sign:
Ile razy który znak jest ile razy po jakim.

Unique symbol and scene:
Badanie związku między unikatowymi symbolami a scenami.