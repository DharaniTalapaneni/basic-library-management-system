# Library Management System

## Project Description

This project is a Library Management System developed using Python. It manages books, magazines and DVDs, allows members to borrow and return items, calculates late fees and handles invalid operations using exceptions.

## 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is an abstract class because it provides common features for Book, Magazine and DVD classes. If DVD does not implement the abstract late_fee() method, Python raises a TypeError when we try to create a DVD object.

## 2. What happens when you read item.__available from outside the class, and why do we use is_available() instead?

When we try to access item.__available from outside the class, Python raises an AttributeError because the attribute uses name mangling. We use is_available() to check the availability safely without accessing the private attribute directly.

## 3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared by all objects, and it counts the total number of library items created. self.title is an instance attribute that stores the title separately for each individual item.