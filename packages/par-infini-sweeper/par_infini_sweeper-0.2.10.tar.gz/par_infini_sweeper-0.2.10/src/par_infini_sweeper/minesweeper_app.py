#!/usr/bin/env python3
"""
Infinite Minesweeper implemented with Python 3.12 and the textual library.

The game grid is composed of subgrids (8×8 each). The first (initial) subgrid
is generated at (0, 0) and new subgrids are generated on demand as you uncover cells.
Left-clicking a cell will reveal it (unless it is marked) and if it’s a mine the game ends.
Right-clicking or Shift + Left-clicking toggles a mine mark on that cell.
Only in the initial subgrid may any cell be clicked; in other subgrids only cells bordering an already uncovered cell are clickable.
"""

from __future__ import annotations

from typing import Any

from rich.console import ConsoleRenderable, RichCast
from rich.panel import Panel
from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.visual import SupportsVisual, Visual
from textual.widgets import Footer, Header, Static

from par_infini_sweeper import __application_title__, db
from par_infini_sweeper.data_structures import GameState
from par_infini_sweeper.dialogs.difficulty_dialog import DifficultyDialog
from par_infini_sweeper.dialogs.help_dialog import HelpDialog
from par_infini_sweeper.dialogs.information import InformationDialog
from par_infini_sweeper.dialogs.theme_dialog import ThemeDialog
from par_infini_sweeper.enums import GameDifficulty
from par_infini_sweeper.main_grid import MainGrid


class MinesweeperApp(App):
    """
    Textual App for Infinite Minesweeper.
    Bindings:
      - q: Quit
      - n: New Game (prompts for difficulty)
    """

    TITLE = __application_title__
    ENABLE_COMMAND_PALETTE = False
    ALLOW_SELECT = False
    CSS_PATH = "pim.tcss"
    BINDINGS = [
        Binding(key="n", action="new_game", description="New Game"),
        Binding(key="h", action="highscores", description="Highscores"),
        Binding(key="t", action="change_theme", description="Change Theme"),
        Binding(key="q", action="quit", description="Quit"),
        Binding(key="f1", action="help", description="Help", show=True),
    ]

    def __init__(self, user_name: str, nickname: str | None = None, **kwargs: Any) -> None:
        from par_infini_sweeper import db

        with db.get_db_connection() as conn:
            db.init_db(conn, user_name)

        super().__init__(**kwargs)
        self.info = Static("Info", id="info")
        self.debug_panel = Static("Debug", id="debug")
        self.game_state = GameState.load(None, user_name, nickname)
        self.sweeper_widget = MainGrid(self.game_state, self.info, self.debug_panel)

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        with Vertical():
            yield self.info
            with Horizontal():
                yield self.sweeper_widget
                yield self.debug_panel

    def on_mount(self) -> None:
        self.theme = self.game_state.theme
        self.sweeper_widget.focus()

    @work
    async def action_change_theme(self) -> None:
        """An action to change the theme."""
        self.game_state.theme = await self.push_screen_wait(ThemeDialog())
        self.game_state.save()

    def action_help(self) -> None:
        """Show help screen"""
        self.app.push_screen(HelpDialog())

    def action_highscores(self) -> None:
        """Display the highscores for each game mode."""
        data = db.get_highscores()
        for mode, data in data.items():
            scores = "\n".join([f"{row['nickname']} - {row['score']}" for row in data])
            self.app.push_screen(InformationDialog("Highscores", Panel(scores, title=str(mode).capitalize())))

    def set_debug(self, text: ConsoleRenderable | RichCast | str | SupportsVisual | Visual) -> None:
        self.debug_panel.update(text)

    @work
    async def action_new_game(self) -> None:
        """
        Start a new game. Prompts the user for a difficulty (easy, medium, or hard),
        resets the game state, and saves it.
        """
        difficulty: GameDifficulty | None = await self.push_screen_wait(DifficultyDialog())
        if difficulty is None:
            return
        self.game_state.difficulty = difficulty
        self.game_state.new_game()
        self.sweeper_widget.action_center()
