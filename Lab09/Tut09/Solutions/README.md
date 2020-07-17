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

    * `Seller`, `Category`, `Buyer`, `Enquiry`, `Response`
        All of these are nouns with specific meaning in the above domain, so would be entities in that domain.
    * `Item`, `Advertisement`
        Both of these are used interchangeably in the description, suggesting that in this domain they are synonymous. Only one should be kept in the domain model.
    * `Price`, `Description`, `Phone number`
        While these are nouns in the description, they have no meaning in the domain beyond that which is commonly understood. Therefore, they are not entities in the domain model.

2. Draw a domain model as a UML class diagram, carefully considering the relationships between the classes.

    * See `uml.pdf`. Note that it is a domain model and not a strict OO model.

3. Considering the verbs in the description and the behaviours they imply, write an implementation in python that corresponds to the model.

    * See `classifieds.py`

## B. Difficulities within a group

Q. How would you deal with the following situations appearing in a group?
* Team member has written code they weren't asked to write?
  * Sit down and talk about how a miss-communication may have happened that caused them
    to produce something they weren't meant to
* Team member not replying / not doing any work
  * Reach out to them in writing, make clear your issues, ask them for an action by a certain time
* Team member replying, seeming engaged, but when push comes to shove not producing anything
  * Reach out to them in writing, make clear your issues, explain that you'll have to reduce their tasks if it continues
* Most of your team not doing any work
  * Reach out to your tutor
* You're feeling anxious about a team-work situation
  * Email your tutor

## C. Single Responsibilites & Cohesion

```python
def get_num(question):
    num = int(input(question))
    return num

def exponent(base,exp):
    answer = pow(base, exp)
    return answer

if __name__ == '__main__':
    base = get_num("Insert base: ")
    exp = get_num("Insert power to raise base to: ")
    answer = exponent(base, exp)
    print(answer)
```

## D. Decorators

Write a very simple decorator that you can use on functions that return strings. This decorator will be called "greeting" and will add "Hello, " to the beginning of the string the function it decorates returns.

```python
def greeting(function):
    def wrapper():
        return "Hello, " + function()
    return wrapper

@greeting
def hayden():
    return "Hayden"

@greeting
def rob():
    return "Rob"

if __name__ == '__main__':
    nameFns = [hayden, rob]
    for nameFn in nameFns:
        print(nameFn())
```