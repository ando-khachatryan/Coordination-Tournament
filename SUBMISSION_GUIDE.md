# How to Submit Your Strategy

## The Game

You are playing a **Battle of the Sexes** game against other students' strategies. Each match lasts a number of rounds (we'll tell you how many before the tournament). Every round, both players simultaneously choose either **U** (Up) or **D** (Down).

The payoff table has this form:

|               | Opponent plays U | Opponent plays D |
|---------------|:----------------:|:----------------:|
| **You play U** |       0, 0       |       X, Y       |
| **You play D** |       Y, X       |       0, 0       |

Where **X > Y > 0**. For example, X=3 and Y=1:

- If you both play the same thing, you both get **0**.
- If you play **U** and your opponent plays **D**, you get **3** and they get **1**.
- If you play **D** and your opponent plays **U**, you get **1** and they get **3**.

**The exact values of X and Y can change between tournaments** (but stay the same for all rounds within a tournament). That's why the payoff matrix is passed to your function — don't hardcode the numbers, read them from the `payoffs` dictionary.

Your goal is to **maximize your total payoff** across all matches in the tournament. You will play against every other submitted strategy.

---

## What You Need to Submit

A single Python file named **`firstname_lastname.py`** (use your actual name, all lowercase, separated by an underscore). For example: `jane_doe.py`.

This file must contain a function called `strategy`. That's it — one file, one function.

---

## The `strategy` Function

Your function must look like this:

```python
def strategy(my_plays, op_plays, payoffs):
    # your code here
    return 'U'  # or 'D'
```

It receives three arguments:

| Argument    | What it is |
|-------------|------------|
| `my_plays`  | A list of your previous moves. Example: `['U', 'D', 'U']` means you played U, then D, then U in rounds 1-3. |
| `op_plays`  | A list of your opponent's previous moves, in the same format. |
| `payoffs`   | A dictionary with the payoff values, e.g. `{'UU': 0, 'UD': 3, 'DU': 1, 'DD': 0}`. The key `'UD'` means "I played U, opponent played D". **Don't hardcode these numbers** — use the dictionary. |

It must **return** either the string `'U'` or the string `'D'`.

### Important details

- On the **first round**, both `my_plays` and `op_plays` are **empty lists** (`[]`).
- To know what round you're on: `len(my_plays) + 1` (it's 1 on the first call, 2 on the second, etc.).
- **You don't know in advance how many rounds there will be.** Don't write strategies that depend on a specific number of rounds.
- You can import standard Python libraries (e.g., `random`, `numpy`) at the top of your file.

---

## Examples

### Simplest possible strategy — always play U

```python
def strategy(my_plays, op_plays, payoffs):
    return 'U'
```

### Play U first, then copy whatever the opponent did last round

```python
def strategy(my_plays, op_plays, payoffs):
    if len(my_plays) == 0:
        return 'U'
    return op_plays[-1]
```

### Random: play U or D with equal probability

```python
import random

def strategy(my_plays, op_plays, payoffs):
    return random.choice(['U', 'D'])
```

### Use the payoffs to decide

```python
def strategy(my_plays, op_plays, payoffs):
    # payoffs['UD'] is what I get when I play U and opponent plays D
    # payoffs['DU'] is what I get when I play D and opponent plays U
    if payoffs['UD'] > payoffs['DU']:
        return 'U'
    else:
        return 'D'
```

---

## Checklist Before Submitting

1. Your file is named `firstname_lastname.py` (your real name, lowercase).
2. Your file contains a function called exactly `strategy`.
3. The function takes exactly three arguments: `my_plays`, `op_plays`, `payoffs`.
4. The function always returns either `'U'` or `'D'`.
5. Your code doesn't crash when `my_plays` and `op_plays` are empty (round 1!).
6. You read payoff values from the `payoffs` dictionary instead of hardcoding numbers.
7. You didn't accidentally leave a `print()` call that breaks things (printing is fine for debugging locally, but clean it up before submitting).

---

## How to Test Locally

1. Place your file in the `bots/` folder alongside the example bots.
2. Run the tournament from the project root:
   ```
   python run.py
   ```
   By default this runs 10 rounds per match. You can change the number of rounds:
   ```
   python run.py --rounds 100
   ```
3. You'll see the results of your strategy playing against every other bot in the `bots/` folder.

---

## Common Mistakes

- **Crashing on round 1** by accessing `op_plays[-1]` or `op_plays[0]` when the list is empty. Always check `if len(my_plays) == 0` first.
- **Hardcoding payoff values** instead of reading from the `payoffs` dictionary. The values can change between tournaments.
- **Forgetting the `return` statement** — if your function returns `None` instead of `'U'` or `'D'`, the tournament will break.
- **Naming the function** something other than `strategy`. It must be called exactly `strategy`.
- **Naming the file** with spaces or capital letters. Use `firstname_lastname.py`.
