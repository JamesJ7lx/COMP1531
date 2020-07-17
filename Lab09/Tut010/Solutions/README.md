# Tutorial 9

## A. State diagrams

Consider a large modern automated library:

* Frequently borrowed books are kept on shelves in the public area.
* Library members check out books by scanning a barcode with a phone app.
* Once a book on the shelf has not been borrowed for 6 months, it is moved to the basement archive.
* Members can borrow books in the archives by requesting they be brought up by robot and delivered directly to them. Scanning is not required.
* Books are returned by members putting them on the shelves and using the phone app to acknowledge their return.

Model the possible states an individual book can be in as a state diagram. Assuming the robots fail regularly (most do), what state would the books they were carrying be in?

## B. Generators

Run-length encoding is a technique for compressing data with many adjacent repeated values. It works by converting a string into a series of tuples, `(c,n)`, where `c` is the character and `n` is the number of times it is repeated. For example, the string `Helllloooooo!` is encoded as `[('H',1), ('e',1), ('l', 4), ('o', 6), ('!',1)]`.

Write a *generator*, `encode(string)`, that generates the run-length encoding of the given string.

Why this is better than a conventional iterator or a function that returns a list?

Write a function, `decode(encoded)`, that converts the encoded data back to a string.

## C. Property-based testing

What property do the `encode()` and `decode()` functions have that can be expressed as a property-based test?

Write this test using hypothesis in python.

Assuming that the functions satisfy this property, is that sufficient to guarantee they work correctly?

## D. More domain modelling

Develop a domain model (as a UML class diagram) for the following system:

* Members of a website can rent out their couches to other members for a number of nights.
* After the stay, guests leave reviews for their hosts and hosts for their guests.
* In addition to a short description, reviews also contain a 5 star rating.
* Reviews are flagged as exceptional, if the the star rating given is at or above the reviewers average, and/or dubious, if the star rating is significantly above the reviewees average rating.

Implement the domain model as a series of classes in python.
