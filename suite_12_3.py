import unittest
import tests_12_3

tournament_TS = unittest.TestSuite()
tournament_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
tournament_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

tour_runner = unittest.TextTestRunner(verbosity=2)
tour_runner.run(tournament_TS)