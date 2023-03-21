from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.ai_game = ai_game
        self.settings = ai_game.settings
        self.reset_status()
        # High score should never be reset.
        self.high_score = self._read_high_score_from_file()


    def reset_status(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _read_high_score_from_file(self):
        """Read the high_score from file and load it."""
        path = Path(self.ai_game.resource_path("assets/high_score"))
        try:
            content = path.read_text()
        except FileNotFoundError:
            path.write_text("0")
            content = path.read_text()
        content = int(content)
        return content


         