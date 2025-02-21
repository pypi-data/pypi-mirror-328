import unittest
import time
from secureutils.threadpool import ThreadPool

def test_function(x):
    time.sleep(0.1)  # Simulate work
    return x * 2

class TestThreadPool(unittest.TestCase):
    def setUp(self):
        self.pool = ThreadPool(max_workers=4)

    def tearDown(self):
        self.pool.shutdown()

    def test_submit_task(self):
        future = self.pool.submit(test_function, 5)
        result = future.result()
        self.assertEqual(result, 10)

    def test_map(self):
        numbers = [1, 2, 3, 4, 5]
        futures = self.pool.map(test_function, numbers)
        results = [f.result() for f in futures]
        self.assertEqual(results, [2, 4, 6, 8, 10])

    def test_priority(self):
        results = []
        def priority_test(x):
            results.append(x)
            time.sleep(0.1)
            return x

        # Submit tasks with different priorities
        self.pool.submit(priority_test, 2, priority=2)
        self.pool.submit(priority_test, 1, priority=1)
        self.pool.submit(priority_test, 3, priority=3)

        # Wait for all tasks to complete
        time.sleep(0.5)
        
        # First result should be from highest priority task
        self.assertEqual(results[0], 1)

if __name__ == '__main__':
    unittest.main()
