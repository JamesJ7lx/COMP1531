# Tutorial 8

* SE Design Principles
* Domain modelling

## A. Domain modelling

Given the following description of a system for classified ads, answer the questions below:

* Sellers advertise items for sale in one or more categories.
* Buyers place enquiries about advertisements that sellers can respond to.
* Each item for sale has an associated price, description, and phone number.
* Buyers subscribe to categories they are interested in.
* After receiving a response to their enquiry, buyers can accept that response to indicate they are satisfied with it.
* Sellers can change the categories an item belongs to after the advertisement has been made.

1. Extract the nouns from the description above and decide which of those form entities in the ubiquitous language of the domain.

2. Draw a domain model as a UML class diagram, carefully considering the relationships between the classes.

3. Considering the verbs in the description and the behaviours they imply, write an implementation in python that corresponds to the model.

## B. Difficulities within a group

Q. How would you deal with the following situations appearing in a group?
* Team member has written code they weren't asked to write?
* Team member not replying / not doing any work
* Team member replying, seeming engaged, but when push comes to shove not producing anything
* Most of your team not doing any work
* You're feeling anxious about a team-work situation

## C. Single Responsibilites & Cohesion

```python
def exponent():
    num = int(input("Enter in a number: "))
    exponent = int(input("Raise the number to the power of: "))
    answer = pow(num, exponent)
    print(answer)

if __name__ == '__main__':
    exponent()
```

## D. Decorators

Write a very simple decorator that you can use on functions that return strings. This decorator will be called "greeting" and will add "Hello, " to the beginning of the string the function it decorates returns.

```python
def hayden():
    return "Hayden"

def rob():
    return "Rob"

if __name__ == '__main__':
    nameFns = [hayden, rob]
    for nameFn in nameFns:
        print(nameFn())
```

## E. Catch up

Your tutor will spend some time reviewing topics that you feel that you are struggling with the most