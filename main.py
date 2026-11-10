

from models import Book, Magazine, DVD, Member, LibraryItem


book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 101)
dvd = DVD("Python Tutorial", 3, 120)
extra_book = Book("Java Basics", 4, "R. Kumar")


alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)


print("LIBRARY MANAGEMENT SYSTEM")
print("--------------------------")


print("\n1. Borrowing an item")

try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
except ValueError as e:
    print("Could not borrow:", e)


print("\n2. Borrowing an already borrowed item")

try:
    bob.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)


print("\n3. Borrowing the same item twice")

try:
    alice.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)


print("\n4. Borrowing limit demonstration")

try:
    bob.borrow(magazine)
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)
except ValueError as e:
    print("Could not borrow:", e)


print("\n5. Returning an item not borrowed")

try:
    bob.return_item(extra_book)
except ValueError as e:
    print("Could not return:", e)


print("\n6. Returning Bob's borrowed item")

fee = bob.return_item(magazine, 3)
print("Bob returned magazine. Late fee: Rs", fee)


print("\n7. Alice borrowing three items")

alice.borrow(magazine)
alice.borrow(dvd)

print("Alice borrowed:", alice.borrowed_titles())


print("\n8. Testing the fourth item borrowing limit")

try:
    alice.borrow(extra_book)
except ValueError as e:
    print("Could not borrow:", e)


print("\n9. Returning Alice's borrowed items")

fee = alice.return_item(book, 3)
print("Alice returned book. Late fee: Rs", fee)

fee = alice.return_item(magazine, 3)
print("Alice returned magazine. Late fee: Rs", fee)

fee = alice.return_item(dvd, 3)
print("Alice returned DVD. Late fee: Rs", fee)


print("\n10. Polymorphism demonstration")

items = [book, magazine, dvd]

for item in items:
    print(item.describe(), "-> late fee for 3 days: Rs", item.late_fee(3))


print("\n11. Encapsulation demonstration")

try:
    print(book.__available)
except AttributeError as e:
    print("Cannot directly access private availability:", e)

print("Book availability:", book.is_available())


print("\n12. Abstract class demonstration")

try:
    item = LibraryItem("Test", 5)
except TypeError as e:
    print("Cannot create LibraryItem directly:", e)


print("\n13. Class attribute demonstration")

print("Total items created:", LibraryItem.total_items)


print("\n14. Borrowed items demonstration")

print("Alice borrowed items:", alice.borrowed_titles())
print("Bob borrowed items:", bob.borrowed_titles())
