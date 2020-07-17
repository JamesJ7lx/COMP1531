## Part A

I would recommend breaking students up into their project groups to do this activity.

A burger shall be provided to the user

  * The burger shall contain lots of pickles

  * The burger shall contain lots of mayo

  * The mayo shall not make the bun wet

  * The burger shall be warm

  * The burger shall be wrapped in a brown paper bag


## Part C
```python
import sys

if __name__ == '__main__':
    vowels = {}
    for character in 'aeiou':
        vowels[character] = 0
    words = sys.stdin.readline().split(' ')
    for word in words:
        for character in word:
            if character in 'aeiou':
                vowels[character] += 1
    for character in 'aeiou':
        print(f"{character}: {vowels[character]}")
```