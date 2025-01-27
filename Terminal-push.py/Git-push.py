"""""
# Git snabbintro

Skapa ett konto på [GitHub](https://github.com/).

## Installera Git

### Windows

Ladda ner och installera Git från [git-scm.com](https://git-scm.com/).

### macOS

Kommer förinstallerat på macOS.

## Skapa ett nytt repository

1. Gå till [GitHub](https://github.com/).
2. Klicka på "+" i övre högra hörnet och välj "New repository".
3. Fyll i namn och beskrivning.
4. Klicka på "Create repository".

## Skapa ett lokalt repository

Öppna terminalen och kör följande kommandon:

```bash
cd sökväg/till/ditt/projekt
git init
```

## Länka det lokala repositoryt med det på GitHub

```bash
git remote add origin "URL till ditt repository"
```

## Lägg till filer och gör en commit

```bash
git add . # Lägg till alla filer
git commit -m "Initial commit" # Gör en commit
```

## Pusha till GitHub

```bash
git push origin main
```

Du kommer säkerligen att stöta på ett problem här. Följ instruktionerna som visas i terminalen.

## Konfigurera Git

Öppna terminalen och kör följande kommandon:

```bash
git config --global user.name "Ditt namn" # Ditt namn eller användarnamn, spelar ingen roll
git config --global user.email "Din e-post" # Din e-post du använde för att skapa ditt GitHub-konto
```

## Skapa en .gitignore-fil

Skapa en fil som heter `.gitignore` i ditt projekt och lägg till filer och mappar som du inte vill ska pushas till GitHub.

T.ex:
```
.vscode/
```

## Lägg till en README.md

README fil kan vara bra att ha för att beskriva ditt projekt. Skriv en README.md fil i ditt projekt och skriv en beskrivning av ditt projekt.

## Koppla ihop ditt lokala repository med GitHub

```bash
git remote add origin "URL till ditt repository"
```

## Pusha till GitHub

```bash
git push origin main
```

## Bra att veta:


### Klona ett repository

```bash
git clone "URL till ditt repository"
```

### Hämta senaste ändringarna

```bash
git pull origin main
```

### Skapa en ny branch

```bash
git checkout -b "namn-på-branch"
```

### Byt branch

```bash
git checkout "namn-på-branch"
```

### Lägg till ändringar och gör en commit

```bash
git add .
git commit -m "Din commit"
```


### Pusha till GitHub

```bash
git push origin "namn-på-branch"
```

### Skapa en pull request

1. Gå till ditt repository på GitHub.
2. Klicka på "Pull requests".
3. Klicka på "New pull request".
4. Välj vilken branch du vill merga till main.
5. Klicka på "Create pull request".
6. Skriv en beskrivning av din pull request.
7. Klicka på "Create pull request".

### Merga en pull request

1. Gå till ditt repository på GitHub.
2. Klicka på "Pull requests".
3. Klicka på den pull request du vill merga.
4. Klicka på "Merge pull request".
5. Klicka på "Confirm merge".

### Ta bort en branch

```bash
git branch -d "namn-på-branch"
```

### Ta bort en remote branch

```bash
git push origin --delete "namn-på-branch"
```

### Se historik

```bash
git log
```

### Ångra senaste commit

```bash
git reset --soft HEAD~1
```

### Ångra senaste commit och ändringar

```bash
git reset --hard HEAD~1
```

### Ångra allt och gå tillbaka till en tidigare commit (OBS! Förlorar allt som inte är committat)
```bash
git reset --hard "commit-hash"
```

## Logga in på Github i terminalen
### Koppla din lokala git användare till GitHub

```bash
git config --global credential.helper cache
# eller
git config --global credential.helper store
```

Skillnaden mellan `cache` och `store` är att `cache` sparar dina uppgifter i 15 minuter medan `store` sparar dina uppgifter permanent.

### Spara din ssh-nyckel

Länk till anvisningar: [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```






"""""
# Instruktioner för inlämningsuppgift 1

## Inlämning
"""""
Inlämningen sker genom att du pushar dina ändringar till ditt repository på GitHub. Du ska alltså inte skicka in något via Teams eller mail förutom länken till ditt repo i Learnpoint. Se till att du har pushat alla dina ändringar innan deadline.

```bash
git add -A
git commit -m "Uppdatering"
git pull origin main
# eller master beroende på vilken branch du jobbar på
git push origin main
```

Jag har förberett med automatiska tester för varje uppgift. Dessa tester kommer att kontrollera att din lösning är korrekt. Om testerna inte passerar kommer du att få ett felmeddelande som säger att testerna har misslyckats. Du kan köra testerna genom att använda kommandot `pytest` i terminalen.

## Pytest

För att kunna testa lösningarna på dina uppgifter behöver du först installera `pytest`. Det gör du genom att köra kommandot:

```bash
pip install pytest
```

Alternativt för mac kan du använda `pip3`:

```bash
pip3 install pytest
```
### Om `pytest` inte fungerar

Testa köra:

```bash
python -m pytest test_exempel_1.py
```

## Lösa uppgifter

I varje mapp så ligger det en uppgift som du ska lösa. Uppgiften är beskriven i en README-fil i mappen. Läs igenom uppgiften och skriv din lösning i filen `uppgift_(UPPGIFTS_NUMMER).py` i samma mapp som README-filen för uppgiften.

Modifiera EJ testfilen `test_uppgift_(UPPGIFTS_NUMMER).py`. Denna fil innehåller testfall som kommer att användas för att kontrollera att din lösning är korrekt och den är samma för alla.

Döp inte om filerna, då kommer testerna inte att fungera heller. Anledningen till att filerna har understreck i sina namn är för att bindessträck och mellanslag inte är tillåtna i filnamn vid importering av moduler i Python.

## Testa uppgifterna

För att testa din lösning kör du kommandot `pytest` i samma mapp som din lösning ligger i. Om du har gjort uppgiften korrekt ska du se utskrifter i terminalen som säger att testerna har passerats.


Det ska alltså bli grönt om testerna har passerats och rött om testerna har misslyckats.
<img src="../bilder/fail-pass.png" alt="fail-pass" width="500"/>

## Navigera till mappen

För att navigera till mappen där uppgiften ligger kan du använda kommandot `cd`(change directory). Exempel:

```bash
cd inlupp/exempel
```

För att kontrollera att du är i rätt mapp kan du använda kommandot `ls`(list) för att lista alla filer och mappar i den mappen.

```bash
ls
# Output: README.md __pycache__ exempel_1.py test_exempel_1.py
```

Ni kan ignorera filen/mappen `__pycache__` då den skapas automatiskt av Python när ni kör era program.

Annars kan du använda kommandot `pwd`(print working directory) för att skriva ut vilken mapp du är i.

```bash
pwd
# Rätt mapp:
# Output: /Users/jorge/projects/tuc/DataScience/inlupp/exempel
# Fel mapp:
# Output: /Users/jorge/projects/tuc/DataScience/inlupp
```

I windows ser det snarare ut såhär:

```bash
pwd
# Output:
# C:\Users\jorge\projects\tuc\DataScience\inlupp\exempel
```

## Navigera tillbaka

För att navigera tillbaka en mapp kan du använda kommandot `cd ..`. Exempel:

```bash
cd ..
```

`..` (punkt punkt) betyder att du går tillbaka en mapp. Om du skriver `cd ../..` så går du tillbaka två mappar.

Alternativt kan du skriva hela sökvägen till mappen du vill gå till. Exempel:

```bash
cd /Users/jorge/projects/tuc/DataScience/inlupp/uppgift_1
```

Observera att sökvägen kan se annorlunda ut beroende på var du har lagt mappen `inlupp` på din dator eller om du använder Windows vs Mac/Linux.
"""""
