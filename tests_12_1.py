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
        runner_walk = Runner('Пешеход')
        i = 0
        while i < 10:
            runner_walk.walk()
            i += 1
        self.assertEqual(runner_walk.distance, 50)

    def test_run(self):
        runner_run = Runner('Бегун')
        i = 0
        while i < 10:
            runner_run.run()
            i += 1
        self.assertEqual(runner_run.distance, 100)

    def test_challenge(self):
        run_challenge = Runner('Профессиональный бегун')
        walk_challenge = Runner('Профессиональный ходок')
        i = 0
        while i < 10:
            run_challenge.run()
            walk_challenge.walk()
            i += 1
        self.assertNotEqual(run_challenge.distance, walk_challenge.distance)