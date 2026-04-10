\# Network Tool



Detta projekt innehåller ett enkelt nätverksverktyg implementerat i både Python och C.



\## Funktioner



Programmet har en meny med följande alternativ:



1\. Validera IP-adress  

2\. Validera port  

3\. Visa logg  

4\. Avsluta  



\### IP-validering

Kontrollerar att IP-adressen följer formatet X.X.X.X och att varje del är mellan 0–255.



\### Port-validering

Kontrollerar att porten är ett heltal mellan 1–65535.



\### Logg

Alla valideringar sparas och visas i en lista.



\---



\## Hur man kör programmet



\### Python

```bash

python networktool.py





\# Network Tool



\## Beskrivning

Detta projekt är ett enkelt nätverksverktyg som är skrivet i både Python och C.



Programmet kan:

\- Validera IP-adresser

\- Validera portar

\- Visa logg

\- Visa antal valideringar



\---



\## Hur man kör programmet



\### Python

```bash

python networktool.py



Reflektion

Att arbeta med både C och Python visade tydliga skillnader.

Python var enklare att använda eftersom det har inbyggda funktioner för stränghantering och listor. Det gjorde att IP-validering och loggning gick snabbare att implementera.

C var mer komplext eftersom man måste hantera minne, datatyper och input manuellt. Det kräver mer kod för samma funktionalitet.

Samtidigt ger C mer kontroll över hur programmet körs, medan Python är mer flexibelt och snabbare att utveckla i.

Genom att implementera samma program i båda språken fick jag en bättre förståelse för deras styrkor och begränsningar.



Reflektion

Python



Python är lättare att använda.

Det är enklare att skriva kod och förstå programmet.

Funktioner som split() och input() gör arbetet snabbare.



C

C är svårare.

Man måste hantera minne och datatyper själv.

Koden blir längre och mer komplex.



Jämförelse (Comparison)



Python är snabbare att utveckla.

C ger mer kontroll men är svårare.



Slutsats



Python passar bättre för enkla program.

C är bättre för avancerade system.


## Köra programmet (Hur man kör)

### Python
python networktool.py

### C
gcc networktool.c -o networktool
./networktool

---

## Reflektion

Det var enklare att skriva programmet i Python eftersom språket har enklare syntax och färdiga funktioner.

I C var det svårare eftersom man måste hantera variabler, minne och input mer manuellt.

Till exempel var IP-validering mer komplicerad i C medan det var enklare i Python.

Logg-funktionen var också enklare att implementera i Python eftersom listor är inbyggda.

I C behövde man skapa egna arrayer och hantera index manuellt.

Genom denna uppgift förstår jag bättre skillnaden mellan kompilerade språk (C) och tolkade språk (Python).




