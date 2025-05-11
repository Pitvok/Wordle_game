# Wordle_game
Egy wordle játék, könnyü és nehéz moddal, napi játékkal, több játékos moddal, és játék megoldoval

## Követelmények

- A program **Visual Studio** környezetben lett írva

## Szükséges fájlok

- `words.txt` – angol nyelvű 5 betűs szavakat tartalmaz (kisbetűvel, soronként egy szó)

## A program futtatása

1. Nyisd meg a projektet Visual Studio-ban vagy más Python-IDE-ben
2. Győződj meg róla, hogy a `NH.py` és `words.txt` egy mappában vannak

## Futtatás

A program elinditásával a főmenübe érkezünk:

```bash
WORDLE - Menü
1. Napi szó játék
2. Szabad játék (véletlen szó)
3. Kétjátékos mód
4. AI teszt
0. Kilépés
Válassz egy opciót:
```

Az 1,2,3 billentyű lenyomásával erre a menűre érkezünk:

```bash
Válassz nehézségi szintet:
1. Könnyű
2. Nehéz
3. Vissza
Opció:
```

Ahol a könnyü nehézség egy egyszerü wordle játékhoz vezet.
A nehéz nehézség a szigorubb szabáju játékhoz vezet. Szabályok:
- ha egy betűnek tudjuk a helyét akkor az a többi tiippünkben is ott kell szerepelnie
- ha egy betűröl tudjuk hogy szerepel a szoban, akkor a tippjeinkben szerepelnie kell

Napi és Szabad Játéknál a random generált szavat kell kitalálnod. Ehhez segitséget tudsz kérni. 

Ezt a tipp helyére beirt help-pel tudod megtenni

```bash
Találd ki az 5 betűs szót. Összesen 6 próbálkozásod van.
Írd be: 'help' ha segítséget kérsz (lehetséges szavakat kapsz).
1. próbálkozás: help
Lehetséges szavak: rossa, jetty, wizzo, cuppa, cohoe...
1. próbálkozás:
```

Kétjátékos modban a társunk adja meg a kitalálandó szavat.

```bash
Egy játékos adjon meg egy 5 betűs titkos szót, amit a másik kitalál.
Titkos szó (nem jelenik meg később): clone

A szó elmentve. Add át a másik játékosnak.
Nyomj Enter-t a folytatáshoz...
```
A játék visszajelzése ezek lehetnek:
- Nagybetű (pl. A) – jó betű, jó helyen
- Kisbetű (pl. a)  – jó betű, rossz helyen
- Aláhúzás (_)     – ez a betű nincs a szóban

A főmenüből, ha a 4. opciora megyünk akkor elérjük az AI-t. Itt a program próbálja kitalálni a játékos álltal megadott szavat. 

```bash
AI teszt menü:
1. Egyszerű AI
2. Fejlett AI
0. Vissza
Választás:
```

Az „AI teszt” menüben kétféle AI választható:

- Egyszerű AI – mindig az első lehetséges szót tippeli
- Fejlett AI – a gyakran előforduló betűk alapján próbál választani

## Péda Játék

Nehéz Mod:
```bash
WORDLE - Menü
1. Napi szó játék
2. Szabad játék (véletlen szó)
3. Kétjátékos mód
4. AI teszt
0. Kilépés
Válassz egy opciót: 1

Válassz nehézségi szintet:
1. Könnyű
2. Nehéz
3. Vissza
Opció: 2

Találd ki az 5 betűs szót. Összesen 6 próbálkozásod van.
Írd be: 'help' ha segítséget kérsz (lehetséges szavakat kapsz).
1. próbálkozás: quick
Válasz: __i__
2. próbálkozás: pizza
Válasz: _I__A
3. próbálkozás: help
Lehetséges szavak: linga, vivda, winna, dinna, tiara...
3. próbálkozás: vivda
Válasz: VI__A
4. próbálkozás: help
Lehetséges szavak: vitta, virga, viola, villa, vigia...
4. próbálkozás: vigia
Válasz: VI__A
5. próbálkozás: aaaaa
Ez a szó nincs a listában.
5. próbálkozás: aaaa
A szó pontosan 5 betűs kell legyen.
5. próbálkozás: quick
A nehéz módban tartani kell a korábban kiderített betűket.
5. próbálkozás: Vista
Válasz: VISTA

Gratulálok! Kitaláltad a szót 5 próbálkozás alatt.
```
Ai:
```bash
WORDLE - Menü
1. Napi szó játék
2. Szabad játék (véletlen szó)
3. Kétjátékos mód
4. AI teszt
0. Kilépés
Válassz egy opciót: 4

AI teszt menü:
1. Egyszerű AI
2. Fejlett AI
0. Vissza
Választás: 2
Adj meg egy 5 betűs titkos szót az AI-nak: vista
Fejlett AI tipp: soare => s_a__
Fejlett AI tipp: tails => tai_s
Fejlett AI tipp: vista => VISTA
Siker: 3 próbálkozásból.

```
