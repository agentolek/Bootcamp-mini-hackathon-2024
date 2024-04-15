# Bootcamp-mini-hackathon-2024
![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)

# Czym będziesz się zajmować
W ramach mini hackathonu będziesz pracować nad znakami tokapu Imperium Inków. Jest to rodzaj dekoracyjnego dzieła sztuki z motywami geometrycznymi. Znaki te umieszczane były między na ubraniach ówczesnej elity inkaskiej oraz na kubkach, na których się w tym zadaniu skupimy. Tokapu wykazuje pewne cechy będące charakterystyczne dla języka naturalnego, więc jest założenie, że każde z nich ma konkretne znaczenie. Nie wiadomo jednak, co one oznaczają dokładnie, bowiem nie ma w tym przypadku kamienia z Rosetty, który by umożliwiłby rozwikłanie zagadki. Twoim zadaniem będzie pomóc w przybliżeniu się do prawdy stojącej za tajemniczymi znakami tokapu.

# Opis danych
W ramach zadania dostępne będą 3 pliki csv.

Pierwszy – **znaki-sekwencje-20160604.csv** zawiera informacje o znakach znajdujących się w danej sekwencji. Poprzez sekwencję rozumiany jest ciąg kojelnych znaków (następy znak to następny wiersz), który jest cykliczny, czyli tam, gdzie się kończy sekwencja, to jest też miejsce, gdzie się zaczyna. Jest tak, ponieważ znaki są naokoło całego kubka. Założenie tutaj jest takie, że znaki czytamy od lewej do prawej strony. Każdy znak ma swój kod. Zaczyna się on od wielkiej litery określającej ogólny rodzaj znaku. Następnie oddzielone kropkami są liczy, oznaczające elementy odzobne znajdujące się na zanku. Jeśli jest ich więcej, to są oddzielone kropkami. Aby zrozumieć sposób kodowania, proszę spojrzeć w folder znaki. Grafiki tam się znajdujące powinny wyjaśnić sposób kodowania tokapu. Czasem znajdują się dwie litery z kodzie znaku, np. B.27.23.B.30. Oznacza to, że tokapu składa się z dwóch części charakterystycznych dla znaku typu B. Jest też specjalne oznaczenie „0” jako znaku uszkodzonego.

Drugi plik – **obiekty-sekwencje-20160604.csv** zawiera informacje dotyczące obiektu i skojarzonego z nim sekwencjami. Większość obiektów ma jedną sekwencję. Zdarza się jednak, że dany kubek ma górną i dolna sekwencję. Wtedy przykładowo dla obiektu COLA28 górna sekwencja jest oznaczona jako COLA28sup, a dolna jako COLA28inf. Dodatkowo jest infoamcja o liczbie sekwencji na obiekcie (l.sekwencji), liczbie znaków w sekwencji (l.znaków) oraz o (nie pamiętam co tutaj oznaczała kolumna cykliczna).

Trzecie plik – **obiekty-sceny-20160604.csv** zamiera infoamcje o znajdujących się na obiektach scenach. Jest napisane ile znajduje się scen (część kubków w ogólne nie ma) oraz o rodzaju sceny. Każdy rodzaj sceny taki jak polowanie, ślub itp. ma swój własny identyfikator. Potrzeba jakiegoś pliku opisującego, co dany kod sceny oznacza.

# Organizacja hackathonu
W ramach mini-hackathonu są dane dwie propozycje zadania. Różnią się one od siebie, aby każdy mógł spróbować swoich sił niezależnie od poziomu umiejętności, czy preferencji. Jeśli ktoś będzie miał ochotę, to może wykonać dwa zadania.

# Zadanie do wykonania
## Zadanie 1.
W tym zadaniu twoim celem będzie stworzenie narzędzia, które pozwoli na przewidywanie brakujących znaków bądź grupy znaków w sekwencji. Braki te mogą być w dowolnym miejscu (na początku, w środku, na końcu). Kluczowe może okazać się tutaj uwzględnienie współistniejących scen na kubku. Liczmy w tym zadaniu na twoją kreatywność.

## Zadanie 2.
W tym zadaniu twoim celem będzie dokonanej dogłębnej analizy i klasteryzacji znaków. Ważna jest przede wszystkim powiązanie znaków w sekwencjach ze współistniejącymi scenami, bądź ich brakiem. Istotne jest, aby pomogło to w głębszym zrozumieniu znaczenia znaków tokapu.

## Propozycja własna
Jest możliwość zdefiniowania samemu problemu do rozwiązania. W takim przypadku prosimy o kontakt do organizatorów bootcampów za pośrednictwem discorda. Pomysł zostanie zweryfikujemy i w przypadku pozytywnego rozpatrzenia, pozwolimy na jego realizację.

## Uwagi do rozwiązań
Roz

Znaki tokapu są w pewien sposób zakodowane. Jest to wykonane w sposób pozwalający zachować informacje, jaką ma on strukturę, pozwalający porównywać między innymi podobieństwo znaków. Jeśli jednak uznasz, że w twoim rozwiązaniu lepiej będzie się sprawdzała inna reprezentacja tokapu, to należy umieścić w rozwiązaniu sposób tej zmiany oraz uzasadnienie takiego działania. Instotne jest, aby inna reprezentacja znaku zawierała taką samą ilość informacji co wcześniej, czyli nie zezwalamy na sytuację, gdzy wszystkie znaki typu B będą kodowane jedną literką, bo to zmniejsza ilość informacji w kodowaniu.


# Przesyłanie rozwiązań
Aby przesłać rozwiązanie, należy zrobic pull request na to repozytorium. Folder z rozwiązaniem nazwany 