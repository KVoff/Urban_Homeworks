from homework_12_1 import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        pasha = Runner('Pasha')
        for i in range(10):
            pasha.walk()
        self.assertEqual(pasha.distance, 50)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        lena = Runner('Lena')
        for i in range(10):
            lena.run()
        self.assertEqual(lena.distance, 100)

    @unittest.skipUnless(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        lena = Runner('Lena')
        pasha = Runner('Pasha')
        for i in range(10):
            lena.run()
            pasha.walk()
        self.assertNotEqual(lena.distance, pasha.distance)


if __name__ == '__main__':
    unittest.main()
