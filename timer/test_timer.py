import unittest
import time
from pomodoro.timer import Timer


class TimerLogicTests(unittest.TestCase):
    """Jednoduché testy logiky Timeru.

    Testy ověřují, že odpočítávání proběhne a že reset vrací stav do `idle`.
    """

    def test_work_countdown_and_completion(self):
        # Použijeme velmi krátké trvání (v minutách), aby test běžel rychle
        t = Timer(work_minutes=0.02, break_minutes=0.01)  # krátké trvání pro test
        t.start_work()
        # voláme tick po jedné sekundě, dokud timer neskončí
        total = 0
        while True:
            finished = t.tick(1)
            total += 1
            if finished:
                break
            if total > 10:
                self.fail('Timer did not finish in expected time')
        # Ověříme, že dokončení proběhlo v rozumném čase
        self.assertLessEqual(total, 10)

    def test_reset_sets_idle(self):
        # Reset by měl nastavit stav na 'idle' a zbývající čas na work_duration
        t = Timer(work_minutes=1, break_minutes=1)
        t.start_work()
        t.reset()
        self.assertEqual(t.state, 'idle')
        self.assertEqual(t.remaining, t.work_duration)


if __name__ == '__main__':
    unittest.main()
