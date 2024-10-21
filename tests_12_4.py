import unittest
import logging
class Runner:
    def __init__(self, name, speed = 5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f"Скорость не может быть отрицательной, сейчас {speed}")

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


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner_walk = Runner('Пешеход', -12)
            logging.info('"test_walk" выполнен успешно')
            i = 0
            while i < 10:
                runner_walk.walk()
                i += 1
            self.assertEqual(runner_walk.distance, 120)
        except ValueError as warn:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            return




    def test_run(self):
        try:
            runner_run = Runner(121, 12)
            logging.info('"test_run" выполнен успешно')
            i = 0
            while i < 10:
                runner_run.run()
                i += 1
            self.assertEqual(runner_run.distance, 240)

        except TypeError as TE_warn:
            logging.warning('Неверный тип данных для Runner', exc_info=True)
            return


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


# class TournamentTest(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.all_results = {}
#
#     def setUp(self):
#         self.runner_1 = Runner('Усэйн', 10)
#         self.runner_2 = Runner('Андрей', 9)
#         self.runner_3 = Runner('Ник', 3)
#
#     @classmethod
#     def tearDownClass(cls):
#         # print(cls.all_results.items())
#         for test_key, test_value in cls.all_results.items():
#             for key, value in test_value.items():
#                 print({key: value.name})
#         # for i in cls.all_results:
#         #     print(i)
#
#     def test_turn1(self):
#         # list_test = [[self.runer_1, self.runer_3], [self.runer_2, self.runer_3],
#         #              [self.runer_1, self.runer_2, self.runer_3]]
#         turn_1 = Tournament(90, self.runner_1, self.runner_3)
#         result = turn_1.start()
#         # print(result[list(result.keys())[-1]] == 'Ник')
#         self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
#         self.all_results['turn1'] = result
#
#     def test_turn2(self):
#         turn_2 = Tournament(90, self.runner_2, self.runner_3)
#         result = turn_2.start()
#         self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
#         self.all_results['turn2'] = result
#
#     def test_turn3(self):
#         turn_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
#         result = turn_3.start()
#         self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
#         self.all_results['turn3'] = result
#
#     # def test_turn4(self):
#     #     """
#     #     Дополнительный тест, выявляющий ошибку алгоритма start класса Tournament
#     #     Ошибка заключается в том, что удаление объекта из списка participants может
#     #     происходить до того, как будет обработан весь цикл и для каждого объекта будет
#     #     запущен метод participant.run()
#     #     :return: None
#     #     """
#     #     turn_4 = Tournament(6, self.runner_1, self.runner_2, self.runner_3)
#     #     result = turn_4.start()
#     #     self.assertTrue(result[list(result.keys())[-1]] == 'Ник', 'Ошибка! Последним должен быть Ник')
#     #     self.all_results['test_turn4'] = result