from typing import List

class BowlingGame:
    def __init__(self):
        self.rolls: List[int] = []
        self.frames: int = 0
        self.cur_frame_rolls: int = 0
        self.extra_bowls: int = 0

    def get_frame_count(self) -> int:
        return self.frames

    def roll(self, pins: int) -> None:
        # error check: pin number
        if pins > 10 or pins < 0:
            print ('ERROR: unsuccessful roll, pins must be in the range of 0 and 10')
            return
        # error check: frame can't knock more than 10 pins down
        if self.cur_frame_rolls == 1 and self.rolls[-1] != 10 and 10-self.rolls[-1] - pins < 0:
            print ('ERROR: max pins down in one frame can only be 10')
            return

        # check if final frame
        if self.frames == 10:
            if self.extra_bowls <= 0:
                print ('Sorry, but the game is already over.')
            elif self.extra_bowls > 0:
                self.rolls.append(pins)
                self.extra_bowls -= 1
            return

        # max 2 rolls per frame
        if self.cur_frame_rolls == 2:
            self.cur_frame_rolls = 0

        self.rolls.append(pins)

        self.cur_frame_rolls += 1
        # finished another frame, given the following conditions
        if self.cur_frame_rolls == 2 or pins == 10:
            self.frames += 1

            # check if finished last frame
            if self.frames == 10:
                # last bowl was a strike
                if self.rolls[-1] == 10:
                    print ('Congrats, you get another 2 bowls!!')
                    self.extra_bowls = 2
                    return
                # last bowl was a spare
                if sum(self.rolls[-2:]) == 10:
                    print ('Congrats, you get another bowl!')
                    self.extra_bowls = 1
                    return

    def _roll_many(self, *pins_list: int) -> None:
        for pins in pins_list:
            self.roll(pins)

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


if __name__ == '__main__':
    bg = BowlingGame()

    while True:
        user = input('')
        method, *other = user.lower().split()

        if method == 'roll':
            numbers: List[int] = list(map(int, other))
            bg._roll_many(*numbers)
        elif method == 'score':
            print (f'> {bg.score()}')
        elif method in ['done', 'end', 'exit']:
            print ('Thanks for playing :)')
            exit(0)

    print (f'Your final score is: {bg.score()}')