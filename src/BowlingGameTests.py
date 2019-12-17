from BowlingGame import BowlingGame
import unittest

class Test(unittest.TestCase):

    def test_normal_game(self):
        bg = BowlingGame()
        bg._roll_many(3, 6, 1, 7, 4, 4)
        self.assertEqual(bg.score(), 25)
        self.assertEqual(bg.get_frame_count(), 3)

    def test_spare_game(self):
        # start with a spare
        bg = BowlingGame()
        bg._roll_many(4, 6, 5, 0)
        self.assertEqual(bg.score(), 20)
        self.assertEqual(bg.get_frame_count(), 2)

        # mid-game with a spare
        bg = BowlingGame()
        bg._roll_many(2, 3, 5, 5, 2, 7)
        self.assertEqual(bg.score(), 26)
        self.assertEqual(bg.get_frame_count(), 3)

        # end with a spare
        bg = BowlingGame()
        bg._roll_many(3, 5, 9, 1)
        self.assertEqual(bg.score(), 18)
        self.assertEqual(bg.get_frame_count(), 2)

    def test_strike_game(self):
        # start with a strike
        bg = BowlingGame()
        bg._roll_many(10, 5, 4)
        self.assertEqual(bg.score(), 28)
        self.assertEqual(bg.get_frame_count(), 2)

        # mid-game with a strike
        bg = BowlingGame()
        bg._roll_many(7, 1, 10, 3, 3)
        self.assertEqual(bg.score(), 30)
        self.assertEqual(bg.get_frame_count(), 3)

        # end-game with a strike
        bg = BowlingGame()
        bg._roll_many(4, 1, 10)
        self.assertEqual(bg.score(), 15)
        self.assertEqual(bg.get_frame_count(), 2)

    def test_frames(self):
        # normal: 10 frames
        bg = BowlingGame()
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        self.assertEqual(bg.get_frame_count(), 10)
        self.assertEqual(bg.score(), 40)

        # normal: 11 frames
        bg = BowlingGame()
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        self.assertEqual(bg.get_frame_count(), 10)
        self.assertEqual(bg.score(), 40)

        # spare: 11 frames
        bg = BowlingGame()
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 8, 2)
        self.assertEqual(bg.get_frame_count(), 10)
        self.assertEqual(bg.score(), 50)

        # strike: 11 frames
        bg = BowlingGame()
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
        bg._roll_many(2, 2, 2, 2, 2, 2, 2, 2, 10, 4, 5)
        self.assertEqual(bg.get_frame_count(), 10)
        self.assertEqual(bg.score(), 64)

if __name__ == '__main__':
    unittest.main()