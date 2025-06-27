# Tag 4 – Schere, Stein, Papier

Ein einfaches Python-Spiel basierend auf dem bekannten Spiel „Schere, Stein, Papier“. Der Spieler tritt gegen den Computer an, der zufällig seine Wahl trifft. ASCII-Grafiken stellen die gewählten Handzeichen visuell dar.

## 🎮 Funktionsweise

- Der Benutzer wird aufgefordert, eine Zahl einzugeben: 0 für Stein, 1 für Papier oder 2 für Schere.
- Der Computer trifft eine zufällige Entscheidung.
- Das Ergebnis sowie ASCII-Grafiken der Auswahl werden angezeigt.

## 🔢 Spielregeln

- Stein (0) schlägt Schere (2)
- Schere (2) schlägt Papier (1)
- Papier (1) schlägt Stein (0)
- Gleiche Wahl = Unentschieden

## 💡 Gelernt

- Verwendung des `random`-Moduls
- Arbeiten mit Listen (Indexierung)
- Einbindung von ASCII-Art
- Umgang mit Benutzereingaben und Fehlern

## 🖥 Beispielausgabe

<pre>
Welcome to Rock Paper Scissors!
What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.
1
You chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

PC chose: 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
You loose. PC won. Better luck next time.</pre>
