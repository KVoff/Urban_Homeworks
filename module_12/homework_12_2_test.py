import unittest
from homework_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        # метод, где создаётся атрибут класса all_results.
        # Это словарь в который будут сохраняться результаты всех тестов.
        cls.all_results = {}

    def setUp(self):
        # метод, где создаются 3 объекта:
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        # метод, где выводятся all_results по очереди в столбец.
        for value in cls.all_results.values():
            # result = ', '.join(f'{place}: {runner.name}' for place, runner in value.items())
            print(value)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        # Усейн и Ник
        tournament_1 = Tournament(90, self.runner_1, self.runner_3)
        result = tournament_1.start()
        self.__class__.all_results['tournament_1'] = result  # сохраняем результаты теста 1 в all_results
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == self.runner_3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        # Андрей и Ник
        tournament_2 = Tournament(90, self.runner_2, self.runner_3)
        result = tournament_2.start()
        self.__class__.all_results['tournament_2'] = result  # сохраняем результаты теста 2 в all_results
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == self.runner_3)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        # Усейн, Андрей и Ник
        tournament_3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament_3.start()
        self.__class__.all_results['tournament_3'] = result  # сохраняем результаты теста 3 в all_results
        last_place = max(result.keys())
        self.assertTrue(result[last_place] == self.runner_3)


if __name__ == '__main__':
    unittest.main()
