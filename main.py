# Initial data
library = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
]

# 1. Create a new book and add it to the library
new_book = {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988}
library.append(new_book)

# 2. Print the titles of all the books in the library
titles = [book["title"] for book in library]
print("\n".join(titles))

# 3. Calculate the average publication year
total_years = sum(book["year"] for book in library)
average_year = total_years / len(library)
print(f"Average publication year: {average_year:.2f}")

# 4. Convert the list of books into a set to remove duplicates (based on title)
unique_titles = {book["title"] for book in library}
print("Unique book titles:", unique_titles)

# 5. List comprehension to get books published in or after a specific year
target_year = 1950
recent_books = [book for book in library if book["year"] >= target_year]
print(f"Books published in or after {target_year}:\n" + "\n".join([book["title"] for book in recent_books]))

# 6. List comprehension to get titles of all books
titles = [book["title"] for book in library]
print("Titles of all books:\n" + "\n".join(titles))

# 7. Sort books by publication year in ascending order
sorted_library = sorted(library, key=lambda book: book["year"])
print("Books sorted by publication year:")
print("\n".join([f"{book['title']} ({book['year']}))" for book in sorted_library]))
