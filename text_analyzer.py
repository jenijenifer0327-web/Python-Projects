from collections import Counter
import string

def analyze_text(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()

        words = [

word.strip(string.punctuation).lower()
            for word in text.split()
        ]
        words = [word for word in words if word]

        if not words:
            print("The file is empty.")
            return

        frequency = Counter(words)

        print("\n--- TEXT ANALYZER ---")
        print("Total words:", len(words))
        print("Unique words:", len(set(words)))
        print("longest word:", max(words, key=len))

        print("\nTop 10 words:")
        for word, count in frequency.most_common(10):
            print(f"{word}: {count}")

        print("\nAll word frequencies:")
        for word, count in sorted(
            frequency.items(), key=lambda
item: item[0]
        ):
            print(f"{word}: {count}")

    except FilenotFoundeError:
        print("Error: Text file not found.")
    except OSError as error:
        print("File error:", error)

if __name__ == "__main__":
    analyze_text("sample.txt")