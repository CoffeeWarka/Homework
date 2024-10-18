import unittest
import pprint
class Runner:
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
        elif isinstance(other, Runner):
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

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # print(cls.all_results.items())
        for test_key, test_value in cls.all_results.items():
            for key, value in test_value.items():
                print(f'\t{key}: {value.name}')

    def test_turn1(self):
        # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
        #              [self.runer_1, self.runer_2, self.runer_3]]
        turn_1 = Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        # print(result[list(result.keys())[-1]] == 'Ник')
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn1'] = result

    def test_turn2(self):
        turn_2 = Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn2'] = result

    def test_turn3(self):
        turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn3'] = result

    def test_turn4(self):
        """
        Дополнительный тест, выявляющий ошибку алгоритма start класса Tournament
        Ошибка заключается в том, что удаление объекта из списка participants может
        происходить до того, как будет обработан весь цикл и для каждого объекта будет
        запущен метод participant.run()
        :return: None
        """
        turn_4 = Tournament(6, self.runner_1, self.runner_2, self.runner_3)
        result = turn_4.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
        self.all_results['test_turn4'] = result
