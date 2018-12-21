class GameStats():
    """Track game statistics"""

    def __init__(self, settings):
        """Initialize method"""

        self.settings = settings
        self.score = 0

    def reset_stats(self):
        """Resets all stats"""
        self.score = 0

    def print_score(self):
        print("Score: " + str(self.score))

