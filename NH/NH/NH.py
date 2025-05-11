
import random
import datetime
from collections import Counter

# Betölti az 5 betűs szavakat a megadott fájlból
def load_words(filename='words.txt'):
    with open(filename, 'r') as f:
        return [line.strip().lower() for line in f if len(line.strip()) == 5]

# Visszaadja a napi szót a dátum alapján
def get_daily_word(words):
    today = datetime.date.today()
    index = today.toordinal() % len(words)
    return words[index]

# Kiértékeli a tippet, és visszaad egy feedback stringet:
# - Nagybetű = jó helyen van
# - Kisbetű = rossz helyen, de benne van
# - _ = nincs benne
def give_feedback(guess, secret):
    result = []
    secret_temp = list(secret)
    used = [False] * 5

    # Első kör: helyes pozíciók
    for i in range(5):
        if guess[i] == secret[i]:
            result.append(guess[i].upper())
            used[i] = True
        else:
            result.append(None)


    # Második kör: rossz pozíciók és hiányzók
    for i in range(5):
        if result[i] is not None:
            continue
        if guess[i] in secret_temp:
            for j in range(5):
                if guess[i] == secret[j] and not used[j]:
                    result[i] = guess[i]
                    used[j] = True
                    break
            if result[i] is None:
                result[i] = '_'
        else:
            result[i] = '_'
    return ''.join(result)


# Megmondja, hogy egy szó lehet-e még jó megoldás a korábbi tippek és visszajelzések alapján
def is_possible_word(word, guesses, feedbacks):
    for guess, feedback in zip(guesses, feedbacks):
        required = [None] * 5  # Betűk, amiknek pontos helyen kell lenniük
        present = []           # Betűk, amik benne vannak, de máshol
        excluded = set()       # Betűk, amik kizártak
        min_counts = Counter()
        max_counts = {}

        guess_letter_counts = Counter(guess)
        feedback_counts = Counter()

        # Első kör: pozíció és jelenlét
        for i in range(5):
            g_char = guess[i]
            f_char = feedback[i]
            if f_char.isupper():
                required[i] = g_char
                min_counts[g_char] += 1
                feedback_counts[g_char] += 1
            elif f_char.islower():
                present.append(g_char)
                min_counts[g_char] += 1
                feedback_counts[g_char] += 1
            elif f_char == "_":
                feedback_counts[g_char] += 0

        # Második kör: kizárás és max mennyiségek kezelése
        for i in range(5):
            g_char = guess[i]
            f_char = feedback[i]
            if f_char == "_":
                if guess_letter_counts[g_char] > feedback_counts[g_char]:
                    max_counts[g_char] = feedback_counts[g_char]
                else:
                    excluded.add(g_char)

        # Ellenőrzés: pozíciók
        for i in range(5):
            if required[i] and word[i] != required[i]:
                return False

        # Ellenőrzés: kizárt betűk
        if any(c in word for c in excluded):
            return False

        # Ellenőrzés: jelenlevő betűk
        word_counter = Counter(word)
        for char in present:
            if char not in word:
                return False

        # Ellenőrzés: minimum előfordulások
        for char, count in min_counts.items():
            if word_counter[char] < count:
                return False

        # Ellenőrzés: maximum előfordulások
        for char, max_count in max_counts.items():
            if word_counter[char] > max_count:
                return False

    return True

# Nehéz módban ellenőrzi, hogy a játékos tartja-e a felfedett információkat
def validate_guess(guess, guesses, feedbacks):
    for i, feedback in enumerate(feedbacks[-1]):
        prev_guess = guesses[-1]
        if feedback.isupper() and guess[i] != prev_guess[i]:
            return False
        elif feedback.islower() and prev_guess[i] not in guess:
            return False
    return True

# Játék lefolyása emberi játékossal
def play_game(secret, words, hard_mode=False):
    attempts = 6
    guesses = []
    feedbacks = []

    print("\nTaláld ki az 5 betűs szót. Összesen 6 próbálkozásod van.")
    print("Írd be: 'help' ha segítséget kérsz (lehetséges szavakat kapsz).")

    for attempt in range(1, attempts + 1):
        while True:
            guess = input(f"{attempt}. próbálkozás: ").strip().lower()

            if guess == "help":
                possible = [w for w in words if is_possible_word(w, guesses, feedbacks)]
                if possible:
                    print("Lehetséges szavak:", ', '.join(possible[:5]) + ("..." if len(possible) > 5 else ""))
                else:
                    print("Nincs találat a jelenlegi információ alapján.")
                continue

            if len(guess) != 5:
                print("A szó pontosan 5 betűs kell legyen.")
            elif guess not in words:
                print("Ez a szó nincs a listában.")
            elif hard_mode and guesses and not validate_guess(guess, guesses, feedbacks):
                print("A nehéz módban tartani kell a korábban kiderített betűket.")
            else:
                break

        feedback = give_feedback(guess, secret)
        guesses.append(guess)
        feedbacks.append(feedback)
        print("Válasz:", feedback)

        if guess == secret:
            print(f"\nGratulálok! Kitaláltad a szót {attempt} próbálkozás alatt.")
            return

    print(f"\nVesztettél! A szó ez volt: {secret}")


# Kétjátékos mód - egyik játékos titkos szót ad meg
def custom_word_mode(words, hard_mode=False):
    print("\nEgy játékos adjon meg egy 5 betűs titkos szót, amit a másik kitalál.")
    while True:
        secret = input("Titkos szó (nem jelenik meg később): ").strip().lower()
        if len(secret) != 5:
            print("A szó pontosan 5 betűs kell legyen.")
        elif secret not in words:
            print("Ez a szó nincs az engedélyezett listában.")
        else:
            break
    print("\nA szó elmentve. Add át a másik játékosnak.")
    input("Nyomj Enter-t a folytatáshoz...")
    play_game(secret, words, hard_mode)


# Nehézségi szint kiválasztása
def difficulty_selection():
    while True:
        print("\nVálassz nehézségi szintet:")
        print("1. Könnyű")
        print("2. Nehéz")
        print("3. Vissza")
        choice = input("Opció: ").strip()
        if choice in ['1', '2']:
            return choice == '2'
        elif choice == '3':
            return None
        else:
            print("Érvénytelen választás.")


# Egyszerű AI - mindig az első lehetséges szót választja a listából
def simple_ai_guess(secret, words):
    guesses = []
    feedbacks = []
    candidates = words[:]

    while True:
        candidates = [w for w in candidates if is_possible_word(w, guesses, feedbacks)]
        if not candidates:
            print("Az Egyszerű AI feladta.")
            return

        guess = candidates[0]
        feedback = give_feedback(guess, secret)
        guesses.append(guess)
        feedbacks.append(feedback)

        print(f"Egyszerű AI tipp: {guess} => {feedback}")
        if guess == secret:
            print(f"Siker: {len(guesses)} próbálkozásból.")
            return


# Fejlett AI - gyakoriság alapján súlyoz, hogy jobb tippet adjon
def advanced_ai_guess(secret, words):
    guesses = []
    feedbacks = []
    candidates = words[:]

    while True:
        if not candidates:
            print("A Fejlett AI feladta.")
            return

        freq = Counter()
        for word in candidates:
            freq.update(word)

        scored = [(sum(freq[c] for c in set(word)), word) for word in candidates]
        scored.sort(reverse=True)
        guess = scored[0][1]

        feedback = give_feedback(guess, secret)
        guesses.append(guess)
        feedbacks.append(feedback)

        print(f"Fejlett AI tipp: {guess} => {feedback}")
        if guess == secret:
            print(f"Siker: {len(guesses)} próbálkozásból.")
            return

        candidates = [w for w in candidates if is_possible_word(w, guesses, feedbacks)]


# AI menü - kétféle AI közül lehet választani
def ai_mode(words):
    while True:
        print("\nAI teszt menü:")
        print("1. Egyszerű AI")
        print("2. Fejlett AI")
        print("0. Vissza")
        choice = input("Választás: ").strip()
        if choice in ["1", "2"]:
            while True:
                secret = input("Adj meg egy 5 betűs titkos szót az AI-nak: ").strip().lower()
                if len(secret) != 5:
                    print("A szó pontosan 5 betűs kell legyen.")
                elif secret not in words:
                    print("Ez a szó nincs a listában.")
                else:
                    break
            if choice == "1":
                simple_ai_guess(secret, words)
            else:
                advanced_ai_guess(secret, words)
        elif choice == "0":
            return
        else:
            print("Érvénytelen választás.")


# Főmenü és program kezdés pontja
def main():
    words = load_words()
    while True:
        print("\nWORDLE - Menü")
        print("1. Napi szó játék")
        print("2. Szabad játék (véletlen szó)")
        print("3. Kétjátékos mód")
        print("4. AI teszt")
        print("0. Kilépés")
        choice = input("Válassz egy opciót: ").strip()

        if choice in ['1', '2', '3']:
            hard_mode = difficulty_selection()
            if hard_mode is None:
                continue

            if choice == "1":
                daily_word = get_daily_word(words)
                play_game(daily_word, words, hard_mode)
            elif choice == "2":
                word = random.choice(words)
                play_game(word, words, hard_mode)
            elif choice == "3":
                custom_word_mode(words, hard_mode)
        elif choice == "4":
            ai_mode(words)
        elif choice == "0":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
