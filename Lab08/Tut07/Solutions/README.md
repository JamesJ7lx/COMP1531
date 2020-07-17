# Tutorial 6

## A. Estimation

> No one true solution, but points should be reasonably proportional.

The following user stories are from the lecture estimation exercise. In groups of 4 or 5 (different to your project teams), use planning poker to come up with your own point estimates for each story. Like in the lecture, the first story has been given an initial point value to act as a baseline. Unlike in the lecture, you should do this one story at a time. Don't progress to the next story till you've all agreed on an estimate for the current story.

* > As a company, I want to post job openings so that suitable candidates can find out about them

    Story points = 5

* > As a jobseeker, I want to search for jobs by attributes like location, salary range, job title, company name, and the date the job was posted, so that I can find jobs which meet my basic criteria

    Story points = ?

* > As a jobseeker, I want to view information about each job that is matched by a search, so that I can make an informed decision whether I want to apply

    Story points = ?

* > As a jobseeker I want to view detailed information about a company that has posted a job, so that I can determine if it is somewhere I want to work

    Story points = ?

* > As a jobseeker, I want to put in an applications for jobs I'm interested in, so that I can make companies aware of my suitability for a job

    Story points = ?

Once done, as a class, discuss the following questions:

* How close were your initial estimates?
* How many rounds did it take for them to converge?
* Did the number of rounds decrease as you estimated more stories?

## B. Measures

Discuss the following project-related measures and answer the questions below:

* The bus factor: the *minimum* number of people that would need to be hit by a bus for a project to fail.

   > 1. Interval scale. No true zero point as a project with a bus factor of zero is guaranteed to fail no matter what, but results can be compared and the difference between them has meaning.
   > 2. A low bus factor would be bad for a project. If a project only requires one person to leave before it fails then there is too great dependency on one or more individuals.
   > 3. This can depend on a number of factors, most obviously the size of the team. It's a worthwhile thing to consider though.
   > 4. Ideally this should be strictly greater than 1.

* Group intercommunication: How many possible channels of communication there are between `n` team members. Defined as `n(n − 1) / 2`, or the number of edges in the complete graph with `n` nodes.

    > 1. Interval scale. There is no zero point and the ratio of the measure has no meaning.
    > 2. A high number of intercommunication channels increases the chance of miscommunication. This is why large teams can be less effective than smaller teams and why adding more people to an existing team can actually slow them down as the new people need to be brought up to speed.
    > 3. As it based entirely on team size, it would be more appropriate to set a maximum team size.
    > 4. Should be 6 or 10 for teams of 4 or 5.

* Lines of Code: The number of lines of code (usually not including comments) in a codebase.

    > 1. Arguably an absolute measure, as you can only count the lines. If you choose to ignore certain lines (blank, comments, etc.) then it's a ratio measure.
    > 2. Roughly correlates to project complexity. However, the results tend not to be comparable. For example, C tends to have more lines of code than python for the same program.
    > 3. No, at least not when used for a whole project. A maximum number of lines changed per commit can be a useful target though.
    > 4. Can find out with `wc -l *.py`, but this includes comments and blank lines.

1. Are their scales nominal, ordinal, interval, ratio, or absolute?
2. What meaning can we infer from them?
3. Do they have a value or range that makes an appropriate target?
4. What are the results of applying them to your project?

## C. Cyclomatic complexity

For the following python functions, calculate their cyclomatic complexity.

```python
def foo():
    if A:
        if B:
            C
        else:
            D
    E
```

> 3

```python
def bar():
    while A:
        B
    if C:
        D
    E
```

> 3

```python
def baz():
    if A:
        if B:
            if C:
                D
    E
```

> 4

```python
def is_prime(n):
    if n <= 1:
        prime = False
    elif n <= 3:
        prime = True
    elif n % 2 == 0 or n % 3 == 0:
        prime = False
    else:
        prime = True
        i = 5
        while i*i <= n and prime:
            if n % i == 0 or n % (i + 2) == 0:
                prime = False
            i += 6
    return prime
```

> 6
