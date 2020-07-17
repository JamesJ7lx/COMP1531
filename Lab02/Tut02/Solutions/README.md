# Tutorial 1

## A. Group Formation

Under the guidance of your tutor, form into project teams. Note that:

* You should aim to have a team of 4 members, but keep in mind that teams of 5 may be necessary due to class sizes not being divisible by 4.
* You will be working with your team regularly throughout the term.
* While your tutor will endeavour to meet your preferences, they may have to move you to another team to ensure all teams are of the right size. They ultimately have authority over who is in each team.

Once your team is formed, **one** member needs to register it on the course website.

1. Click on **Groups** on the left.
2. Click on **Create**
3. Give the group a name of the form *TUTE*-*name*, where *TUTE* is the tutorial code as on the timetable on the course website and *name* is a name for your team (e.g. T13A-cool_kids). The name portion can be whatever you want (within reason) but must contain only alphanumeric characters and underscores (no whitespace or special characters).
4. Ensure that the group type is **Project**.
5. Click **Create** to create the group.

Other groups members should then **join** this group.

1. Click on **Groups** on the left.
2. Find your group in the list.
3. Click **Join**

**EVERYONE MUST BE A MEMBER OF A TEAM BY THURSDAY WEEK 2 (26th September) AT 9PM**

## B. Testing in python

Consider this problem:

 > Given a list of integers, compute the average of only the *positive* elements.

Your tutor will clone `COMP1531/19T3-cs1531-tut02`

There is a stub for a function that solves this problem in `rainfall.py`. Before implementing it, write some pytest compatible tests for the function.

* What needs to be tested for?
* What are the edge cases and how should they be handled?

Once the tests are written, commit them to git.

## C. Python programming

On a separate branch (`rainfall_solution`), implement the function such that it passes all the tests.

* How confident are you that your solution is correct?
* Is your solution very different from how you might do it in C?

Go back to the `master` branch and try to implement the function a different way. If your previous solution did not use the `sum()` function, rewrite it so it does. If your previous solution *did* use the `sum()` function, rewrite it so it doesn't (also avoiding an intermediate list).

After testing it to ensure correctness, commit this alternate solution to `master`.

## D. Git merges

Try to merge `rainfall_solution` back into `master`. This will create a merge conflict.

With the class, discuss which solution is better and how you might resolve the merge conflict to ensure it is the one used.
