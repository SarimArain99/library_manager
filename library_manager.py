import json
from colorama import init, Fore, Style

init(autoreset=True)


def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file)


def add_book(library):
    print(Fore.CYAN + Style.BRIGHT + "\n📚 ADD A NEW BOOK")
    title = input(Fore.GREEN + "➡️  Enter book title: ")
    author = input(Fore.GREEN + "➡️  Enter author: ")
    year = int(input(Fore.GREEN + "➡️  Enter publication year: "))
    genre = input(Fore.GREEN + "➡️  Enter genre: ")
    read_status = (
        input(Fore.GREEN + "➡️  Have you read this book? (yes/no): ").strip().lower()
        == "yes"
    )

    library.append(
        {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status,
        }
    )

    print(Fore.MAGENTA + "✅ Book successfully added to the library!\n")


def remove_book(library):
    print(Fore.YELLOW + Style.BRIGHT + "\n🗑️ REMOVE A BOOK")
    title = input(Fore.RED + "➡️  Enter book title to remove: ")

    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(Fore.RED + "❌ Book removed successfully!\n")
            return

    print(Fore.RED + "❗ Book not found!\n")


def search_book(library):
    print(Fore.BLUE + Style.BRIGHT + "\n🔍 SEARCH FOR A BOOK")
    search_by = input(Fore.CYAN + "➡️  Search by (title/author): ").strip().lower()
    keyword = input(Fore.CYAN + "➡️  Enter search keyword: ").strip().lower()

    results = [book for book in library if keyword in book.get(search_by, "").lower()]

    if results:
        print(Fore.MAGENTA + "\n🎯 Search Results:")
        for i, book in enumerate(results, 1):
            print(
                Fore.BLUE
                + f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read_status'] else '❌ Unread'}"
            )
    else:
        print(Fore.RED + "❗ No matching book found.\n")


1


def display_books(library):
    print(Fore.MAGENTA + Style.BRIGHT + "\n📚 LIBRARY COLLECTION")
    if not library:
        print(Fore.RED + "❗ No books in the library!\n")
    else:
        for i, book in enumerate(library, 1):
            print(
                Fore.YELLOW
                + f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read_status'] else '❌ Unread'}"
            )


def display_stats(library):
    print(Fore.CYAN + Style.BRIGHT + "\n📊 LIBRARY STATS")
    total_books = len(library)
    read_books = len([book for book in library if book["read_status"]])
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    unread_percentage = 100 - read_percentage

    print(Fore.YELLOW + f"📚 Total Books: {total_books}")
    print(Fore.GREEN + f"✅ Read Books: {read_books} ({read_percentage:.2f}%)")
    print(
        Fore.RED
        + f"📕 Unread Books: {total_books - read_books} ({unread_percentage:.2f}%)\n"
    )


def main():
    library = load_library()

    while True:
        print(Style.BRIGHT + Fore.CYAN + "\n📖 LIBRARY MENU")
        print("1. 📗 Add a Book")
        print("2. 🗑️ Remove a Book")
        print("3. 🔎 Search for a Book")
        print("4. 📚 Display All Books")
        print("5. 📊 Display Statistics")
        print("6. 🚪 Exit")

        choice = input(Fore.YELLOW + "\n➡️  Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_library(library)
            print(Fore.GREEN + "\n💾 Library saved successfully. Goodbye!\n")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
