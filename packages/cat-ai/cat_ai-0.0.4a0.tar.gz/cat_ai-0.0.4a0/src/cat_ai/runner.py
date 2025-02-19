import os

from .reporter import Reporter


class Runner:
    def __init__(self, test_function, reporter: Reporter):
        self.reporter = reporter
        self.test_function = test_function

    @staticmethod
    def sample_size(default_size: int = 1) -> int:
        return int(os.getenv("CAT_AI_SAMPLE_SIZE", str(default_size)))

    def run_once(self, run_number: int = 0):
        self.reporter.run_number = run_number
        result = self.test_function(reporter=self.reporter)
        return result

    def run_loop(self, tries: int = sample_size()):
        results = []
        for x in range(0, tries):
            results.append(self.run_once(x))
        return results
