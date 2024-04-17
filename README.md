# Bootcamp-mini-hackathon-2024
![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)

# Czym będziesz się zajmować
W ramach mini hackathonu będziesz pracować nad znakami tokapu z Imperium Inków. Jest to rodzaj dekoracyjnego dzieła sztuki z motywami geometrycznymi. Znaki te umieszczane były między na ubraniach ówczesnej elity inkaskiej oraz na kubkach, na których się w tym zadaniu skupimy. Tokapu wykazuje pewne cechy będące charakterystyczne dla języka naturalnego, więc jest założenie, że każde z nich ma konkretne znaczenie. Nie wiadomo jednak, co one oznaczają dokładnie, bowiem nie ma w tym przypadku kamienia z Rosetty, który by umożliwiłby rozwikłanie zagadki. Twoim zadaniem będzie pomóc w przybliżeniu się do prawdy stojącej za tajemniczymi znakami tokapu.

W tym miejscu należą się podziękowania dla prof. Mariusza S. Ziółkowskiego oraz prof. Jarosława Arabasa, dzięki którym można było zorganizować to wydarzenie. Bardzo Panom dziękujemy!

# Organizacja mini-hackathonu
Zespoły powinny liczyć od 1 do 4 osób. Każdy z nich powinien mieć ustaloną nazwę. Prośba jest o nie tworzenie podobnych, aby uniknąć pomyłek. Oficjalnym kanałem komunikacji jest kanał *bootcamp* na discordzie Golema. Tam proszę zadawać ewentualne pytania. Rozwiązania są przesyłane na tym repozytorium za pomocą pull request. Szczegóły są opisane w sekcji *Przesyłanie rozwiązań*. Ostateczny termin przesyłania rozwiązań jest do **15 maja do godz. 23:59**. Po tym czasie repozytorium stanie się prywatne i nie będzie możliwości wprowadzania zmian.

# Opis danych
W ramach zadań dostępne będą 3 pliki csv.

Pierwszy – **znaki-sekwencje-20160604.csv** zawiera informacje o znakach znajdujących się w danej sekwencji. Poprzez sekwencję rozumiany jest ciąg kolejnych znaków (następy znak to następny wiersz), który jest cykliczny, czyli tam, gdzie się kończy sekwencja, to jest też miejsce, gdzie się zaczyna. Jest tak, ponieważ znaki są naokoło całego kubka. Założenie tutaj jest takie, że znaki czytamy od lewej do prawej strony. Każdy znak ma swój kod. Zaczyna się on od wielkiej litery określającej ogólny rodzaj znaku. Następnie oddzielone kropkami są liczby, oznaczające dodatkowe elementy/ozdoby znajdujące się na znaku. Jeśli jest ich więcej, to są oddzielone kropkami. Aby zrozumieć sposób kodowania, proszę spojrzeć w folder znaki. Grafiki tam się znajdujące powinny wyjaśnić sposób kodowania tokapu. Czasem znajdują się dwie litery z kodzie znaku, np. B.27.23.B.30. Oznacza to, że tokapu składa się z dwóch części charakterystycznych dla znaku typu B. Jest też specjalne oznaczenie „0” jako znaku uszkodzonego.
Dostępne będą również 3 zmodyfikowane wersje pliku znaki-sekwencje-20160604.csv, przygotowane specjalnie na potrzeby zadania 1. Szczegóły opisane są w następnych sekcjach.

Drugi plik – **obiekty-sekwencje-20160604.csv** zawiera informacje dotyczące obiektu i skojarzonego z nim sekwencjami. Większość obiektów ma jedną sekwencję. Zdarza się jednak, że dany kubek ma górną i dolna sekwencję. Wtedy przykładowo dla obiektu COLA28 górna sekwencja jest oznaczona jako COLA28sup, a dolna jako COLA28inf. Dodatkowo jest informacja o liczbie sekwencji na obiekcie - *l.sekwencji*, liczbie znaków w sekwencji - *l.znaków* oraz o cykliczności sekwencji - *cykliczna*, gdzie "a" oznacza acykliczną sekwencję, a w przeciwnym przypadku mamy cykliczną sekwencję, gdzie pierwszy znak sąsiaduje z drugim i ostatnim w sekwencji.

Trzecie plik – **obiekty-sceny-20160604.csv** zamiera informacje o znajdujących się na obiektach scenach. Jest napisane, ile znajduje się scen (część kubków w ogólne nie ma) oraz o rodzaju sceny. Każdy rodzaj sceny taki jak polowanie, ślub itp. ma swój własny identyfikator.

# Zadanie do wykonania
W ramach mini-hackathonu są dane dwie propozycje zadania. Różnią się one od siebie, aby każdy mógł spróbować swoich sił niezależnie od poziomu umiejętności, czy preferencji.

Jeśli jest chęć wykonania więcej niż jednego zadania, to jest taka możliwość. W takim przypadku należy dla każdego zadania przesłać osobne rozwiązanie.

## Zadanie 1.
W ramach tego zadania celem będzie stworzenie modelu generującego sekwencje. Wybór modelu jest dowolny, ale zapewniający, że nie nastąpi uczenie na pamięć. Następnie używamy modelu, aby wygenerować sekwencje.

Do dyspozycji będą dostępne trzy zmodyfikowane zbiory:
* *znaki-sekwencje-20160604-analiza1.csv* - znaki G.<...> są usunięte i zastąpione symbolem N (brak znaku),
* *znaki-sekwencje-20160604-analiza2.csv* - znaki A.36, A.37, A.38 są usunięte i zastąpione symbolem N,
* *znaki-sekwencje-20160604-analiza3.csv* - znaki G.<...> są usunięte i zastąpione symbolem G (czy znamy rodzaj znaku, ale nie mamy informacji o jego ozdobnikach).

Dla każdego ze zbiorów należy nauczyć model. Należy pamiętać o podziale każdego ze zbiorów *<...>-analiza1.csv*, *<...>-analiza2.csv*, *<...>-analiza3.csv* na zbiór treningowy oraz testowy w proporcjach 80/20. Proszę to zrobić w sposób inteligentny.  Wygenerowane sekwencje należy porównać wygenerowane znaki w pustych miejscach z oryginalnymi znakami.
Oryginalne sekwencje są dostępne w pliku *znaki-sekwencje-20160604-original.csv*. Wszystkie dane zostały umieszczone w folderze **dane/zadanie_1**.

## Zadanie 2.
W tym zadaniu twoim celem będzie dokonanej dogłębnej analizy. Głównym zadaniem będzie uchwycenie schematów, zależności, może powiązanie znaków ze współistniejącymi scenami. Istotne jest, aby wyciągnąć jak najwięcej przydatnych informacji z danych. Ciekawe może tutaj okazać się użycie klasteryzacji, jeśli to możliwe. Zadanie jest otwarte, więc można do niego podchodzić różnorodnie. Poza oryginalnością doceniane będzie dogłędnośći jakość przeprowadzonych analiz. Wszystkie dane potrzebne do tego zadania zostały umieszczone w folderze **dane/zadanie_2**.

## Propozycja własna
Jest możliwość zdefiniowania samemu problemu do rozwiązania. W takim przypadku prosimy o kontakt do Filipa Szymplińskiego za pośrednictwem discorda. Pomysł zostanie zweryfikujemy i w przypadku pozytywnego rozpatrzenia, zespół dostanie pozwolenie na jego realizację. Dane w takim przypadku należy wziąć z folderu **dane/zadanie_2**. Wszelkie zmiany, które zostaną na nich dokonane, należy opisać w raporcie.

# Przesyłanie rozwiązań
Aby przesłać rozwiązanie, należy zrobić pull request na to repozytorium. Folder z rozwiązaniem nazywać się ma tak jak nazwa zespołu. Kod rozwiązania powinien znajdować się w podfolderze **code**. Nie przesyłamy żadnych danych. Kod powinien być napisany schludnie, aby nie było problematyczne jego przeczytanie. Proszę zwrócić uwagę na reprodukowalność rozwiązań, przykładowo poprzez ustawienie ziarna.

Rozwiązanie musi zawierać krótki raport. Ma on zawierać opis rozwiązania, zastosowanych metod, uzyskanych wyników i ewentualne wnioski. Preferowany format pliku to pdf, ewentualnie notatnik jupyterowy (nie zalecamy).

Ostatni wymagany plik to REAMME.md. Jego zadaniem ma być krótki opis plików znajdujących się w folderze *code*, aby nie trzeba było się domyślać, co za co odpowiada.

Podsumowując, dla zespołu o nazwie *Danonki* struktura folderu z rozwiązaniem powinna wyglądać następująco:

**Danonki**
* code
* code_file_1.py
* code_file_2.py
* code_file_3.py
* README.md
* raport.pdf

## Dodatkowe uwagi do rozwiązań
Znaki tokapu są w pewien sposób zakodowane. Jest to wykonane w sposób pozwalający zachować informacje, jaką ma on strukturę, pozwalający porównywać między innymi podobieństwo znaków. Jeśli jednak uznasz, że w twoim rozwiązaniu lepiej będzie się sprawdzała inna reprezentacja tokapu, to należy umieścić w rozwiązaniu sposób tej zmiany oraz uzasadnienie takiego działania. Istotne jest, aby inna reprezentacja znaku zawierała taką samą ilość informacji co wcześniej, czyli nie zezwalamy na sytuację, gdyż wszystkie znaki typu B będą kodowane jedną literką, bo to zmniejsza ilość informacji w kodowaniu.

Jeśli ktoś podejmie się rozwiązania samemu zdefiniowanego problemu, należy do rozwiązania dołączyć plik **opis_wlasnego_zadania.pdf**. Znajdować się ma w nim dokładny opis własnego zadania. Ma być to napisane w sposób zrozumiały dla osoby niewtajemniczonej.