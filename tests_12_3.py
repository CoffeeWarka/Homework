import unittest

class RunnerVersion1:
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
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе походят')
    def test_walk(self):
        runner_walk = RunnerVersion1('Пешеход')
        i = 0
        while i < 10:
            runner_walk.walk()
            i += 1
        self.assertEqual(runner_walk.distance, 50)

    def test_run(self):
        runner_run = RunnerVersion1('Бегун')
        i = 0
        while i < 10:
            runner_run.run()
            i += 1
        self.assertEqual(runner_run.distance, 100)

    def test_challenge(self):
        run_challenge = RunnerVersion1('Профессиональный бегун')
        walk_challenge = RunnerVersion1('Профессиональный ходок')
        i = 0
        while i < 10:
            run_challenge.run()
            walk_challenge.walk()
            i += 1
        self.assertNotEqual(run_challenge.distance, walk_challenge.distance)


class RunnerVersion2:
    def __init__(self, name, speed = 5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, RunnerVersion2):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = RunnerVersion2('Усэйн', 10)
        self.runner_2 = RunnerVersion2('Андрей', 9)
        self.runner_3 = RunnerVersion2('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # print(cls.all_results.items())
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #              [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_turn1'] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_turn2'] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['test_turn3'] = result

