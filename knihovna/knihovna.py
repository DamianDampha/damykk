"""
Jednoduchá aplikace pro správu knihovny knih.
"""

class Book:
    """Třída pro jednu knihu."""

    def __init__(self, title, author, year):
        self.title = title  # název knihy
        self.author = author  # autor knihy
        self.year = year  # rok vydání

    def __str__(self):
        return f"'{self.title}' od {self.author} ({self.year})"  # text pro tisk


class Library:
    """Třída pro správu seznamu knih."""

    def __init__(self):
        self.books = []  # seznam knih v knihovně

    def add_book(self, book):
        self.books.append(book)  # přidej knihu do seznamu
        print(f"Kniha '{book.title}' byla přidána do knihovny.")

    def remove_book(self, title):
        # odstraň první knihu se stejným názvem (velká/malá písmena ignorována)
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Kniha '{title}' byla odstraněna z knihovny.")
                return True
        print(f"Kniha '{title}' nebyla nalezena.")
        return False

    def search_by_title(self, title):
        # najdi knihy, které obsahují text v názvu
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        # najdi knihy podle autora
        return [book for book in self.books if author.lower() in book.author.lower()]

    def display_all_books(self):
        if not self.books:
            print("Knihovna je prázdná.")
        else:
            print("Knihy v knihovně:")
            for book in self.books:
                print(f"  - {book}")


def main():
    library = Library()  # vytvoř knihovnu

    # přidej ukázkové knihy
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))

    while True:
        print("\n--- Správa knihovny ---")
        print("1. Přidat knihu")
        print("2. Odstranit knihu")
        print("3. Vyhledat podle názvu")
        print("4. Vyhledat podle autora")
        print("5. Zobrazit všechny knihy")
        print("6. Konec")

        choice = input("Vyberte možnost (1-6): ").strip()  # načti volbu

        if choice == "1":
            title = input("Zadejte název knihy: ").strip()
            author = input("Zadejte autora: ").strip()
            try:
                year = int(input("Zadejte rok vydání: ").strip())
                library.add_book(Book(title, author, year))
            except ValueError:
                print("Neplatný rok. Zadejte číslo.")

        elif choice == "2":
            title = input("Zadejte název knihy k odstranění: ").strip()
            library.remove_book(title)

        elif choice == "3":
            title = input("Zadejte název k vyhledání: ").strip()
            results = library.search_by_title(title)
            if results:
                print("Nalezené knihy:")
                for book in results:
                    print(f"  - {book}")
            else:
                print("Žádné knihy nenalezeny.")

        elif choice == "4":
            author = input("Zadejte autora k vyhledání: ").strip()
            results = library.search_by_author(author)
            if results:
                print("Nalezené knihy:")
                for book in results:
                    print(f"  - {book}")
            else:
                print("Žádné knihy nenalezeny.")

        elif choice == "5":
            library.display_all_books()

        elif choice == "6":
            print("Děkujeme za použití aplikace!")
            break

        else:
            print("Neplatná volba. Zkuste znovu.")


if __name__ == "__main__":
    main()