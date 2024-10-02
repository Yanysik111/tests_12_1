
import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rnr = Runner('Felix')
        for _ in range(10):
            rnr.walk()
        self.assertEqual(rnr.distance, 50)
    def test_run(self):
        run_ = Runner('Fedor')
        for _ in range(10):
            run_.run()
        self.assertEqual(run_.distance, 100)

    def test_challenge(self):
        runi = Runner('Kate')
        runi2 = Runner('Dasha')
        for _ in range(10):
            runi.run()
            runi2.walk()
        self.assertNotEqual(runi.distance, runi2.distance)

 
if __name__ == '__main__':
    unittest.main()