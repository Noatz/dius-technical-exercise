from BowlingGame import BowlingGame
import unittest

class Test(unittest.TestCase):

    def test_normal_game(self):
        bg = BowlingGame()
        bg.roll(3, 6, 1, 7, 4, 4)
        self.assertEqual(bg.score(), 25)
    
    def test_spare_game(self):
        # start with a spare
        bg = BowlingGame()
        bg.roll(4, 6, 5, 0)
        self.assertEqual(bg.score(), 20)

        # mid-game with a spare
        bg = BowlingGame()
        bg.roll(2, 3, 5, 5, 2, 7)
        self.assertEqual(bg.score(), 26)

        # end with a spare
        bg = BowlingGame()
        bg.roll(3, 5)
        bg.roll(9, 1)
        self.assertEqual(bg.score(), 18)
    
    def test_strike_game(self):
        # start with a strike
        bg = BowlingGame()
        bg.roll(10, 5, 4)
        self.assertEqual(bg.score(), 28)

        # mid-game with a strike
        bg = BowlingGame()
        bg.roll(7, 1, 10, 3, 3)
        self.assertEqual(bg.score(), 30)

        # end-game with a strike
        bg = BowlingGame()
        bg.roll(4, 1, 10)
        self.assertEqual(bg.score(), 15)

if __name__ == '__main__':
    unittest.main()