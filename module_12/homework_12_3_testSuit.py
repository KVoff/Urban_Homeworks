import unittest
import homework_12_2_test
import homework_12_1_test

suit_test = unittest.TestSuite()
suit_test.addTest(unittest.TestLoader().loadTestsFromTestCase(homework_12_1_test.RunnerTest))
suit_test.addTest(unittest.TestLoader().loadTestsFromTestCase(homework_12_2_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suit_test)

