from typing import List

class BowlingGame:
    def __init__(self):
        self.rolls: List[int] = []

    def roll(self, *pins: int) -> None:
        self.rolls += pins

    def score(self) -> int:
        cur_score: int = 0

        roll_num: int = 0
        while roll_num < len(self.rolls):
            # check for a strike
            if self.rolls[roll_num] == 10:
                cur_score += sum(self.rolls[roll_num:roll_num+3])
                roll_num += 1
                continue

            # sum of the next two rolls (i.e. the frame)
            _sum: int = sum(self.rolls[roll_num:roll_num+2])

            # check for a spare
            if _sum == 10:
                # if last roll, then a spare can't add the next roll as it doesn't exist
                last_roll = 0 if roll_num+2 == len(self.rolls) else self.rolls[roll_num+2]
                cur_score += 10 + last_roll
                roll_num += 2
                continue

            # a normal frame (i.e. no strike or spare)
            cur_score += _sum

            roll_num += 2

        return cur_score