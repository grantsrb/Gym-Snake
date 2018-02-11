import numpy as np

class Discrete():
    def __init__(self, n_actions):
        self.dtype = np.int32
        self.n = n_actions
        self.actions = np.arange(self.n, dtype=self.dtype)
        self.shape = self.actions.shape

    def contains(self, argument):
        for action in self.actions:
            if action == argument:
                return True
        return False

    def sample(self):
        return np.random.choice(self.n)
