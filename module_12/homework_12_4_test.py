from homework_12_4 import Runner
import unittest
import logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Runner', -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError as exc:
            logging.warning(f'Неверная скорость для Runner: {exc}', exc_info=True)
            self.fail("Тест не запускается для отрицательной скорости")

    def test_run(self):
        try:
            runner = Runner(100500, 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except TypeError as exc:
            logging.warning(f'"Неверный тип данных для объекта Runner: {exc}"', exc_info=True)
            self.fail(f'"Тест не запущен по причине: {exc}"')




if __name__ == '__main__':
    unittest.main()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(levelname)s | %(message)s')
