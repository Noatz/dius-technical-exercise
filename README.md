# Technical Exercise - Bowling

> This exercise is from the following: https://github.com/DiUS/coding-tests/blob/master/dius_bowling.md

## How to play

* `roll x y ...`: the bowler will roll
* `score`: check what the current score is
* `exit`: leave the game

```bash
python3 src/BowlingGame.py
>>> roll 5 3
>>> score
> 8
>>> roll 10
>>> score
> 18
>>> roll 2 5
>>> score
> 32
>>> exit
```

## Testing

Test the Bowling Game: `python3 src/BowlingGameTests.py`

Test typing (via `mypy`): `mypy src/BowlingGame.py`

## Notes

The interactive mode does not include error checks, please follow the syntax.
