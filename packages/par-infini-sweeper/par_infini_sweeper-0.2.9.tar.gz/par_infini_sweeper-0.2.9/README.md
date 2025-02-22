# Par Infinite Minesweeper

## Description

Infinite Minesweeper TUI. Play a game of minesweeper with infinite board size!

![Par Infinite Minesweeper](https://raw.githubusercontent.com/paulrobello/par_infini_sweeper/main/Screenshot.png)

## Technology
- Python
- Textual
- Sqlite3

## Objective
The goal of the game is to uncover all the cells that do not contain mines. 
If you uncover a mine, you lose the game. 
If you uncover a cell that is not a mine, it will show a number indicating how many mines are in the neighboring cells. 
Use this information to determine which cells are safe to uncover.

## Controls

* Left click to uncover a cell. If a cell is flagged as a mine, it will not be uncovered.
* Sub grids can only be unlocked when cells neighboring the sub grid are uncovered.
* Shift or Ctrl + Left-click to toggle flagging a covered cell as a mine.
* Shift or Ctrl + Left-click on an uncovered cell it will uncover all neighboring cells.
  * As a safety you must have same number of flags as mines in the neighboring cells.
* Drag to pan the board.
* Keys:
  * `F1` Help.
  * `N` New game.
  * `O` Move view to origin.
  * `C` Move view to board center (computed as center of exposed sub grids).
  * `P` Pause.
  * `H` Highscores.
  * `T` Change theme.
  * `Q` Quit.

## Scoring

The main grid consists of 8x8 sub grids.  
Depending the difficulty level, the number of mines in each sub grid will vary.  
* Easy: 8 mines
* Medium: 12 mines
* Hard: 16 mines

When all cells that are not mines in a sub grid are uncovered the sub grid is marked solved and flags are placed on any mines that are not already flagged.  
Your score is the sum of all mines in the solved sub grids.  

## Storage

All data for the application is stored in a sqlite3 database located in `~/.pim/game_data.sqlite`  
The database is backed up daily to `~/.pim/game_data.sqlite.bak`  

## Prerequisites

The instructions assume you have `uv` installed.

## Installation

### PyPi
```shell
uv tool install par_infini_sweeper
```

### GitHub
```shell
uv tool install git+https://github.com/paulrobello/par_infini_sweeper
```

## Update

### PyPi
```shell
uv tool install par_infini_sweeper -U --force
```

### GitHub
```shell
uv tool install git+https://github.com/paulrobello/par_infini_sweeper -U --force
```


## Installed Usage
```shell
pim [OPTIONS]
```

## From source Usage
```shell
uv run pim [OPTIONS]
```


### CLI Options
```
--server              -s            Start webserver that allows app to be played in a browser
--user                -u      TEXT  User name to use [default: logged in username]
--nick                -n      TEXT  Set user nickname [default: None]
--version             -v            Show version and exit.
--help                              Show this message and exit.
```

## Roadmap

- Global Leaderboard
- More game modes
- Optimize for more performance

## Whats New
- Version 0.2.9:
  - Fixed some first run db issues
- Version 0.2.8:
  - Addata game data backup
  - Updated readme and help
- Version 0.2.7:
  - Added pause key `p`
  - Fixed bug where sometimes newly generated sub grids would not get saved if no cells were uncovered 
  - More optimizations
  - Support for future game modes
- Version 0.2.6:
  - Now only highlights unrevealed surrounding cells when shift/ctrl + left-click on uncovered cells 
- Version 0.2.6:
  - Now stops timer on game over
  - Now highlights surrounding cells when shift/ctrl + left-click on uncovered cells
- Version 0.2.5:
  - Disabled some toasts to reduce clutter
  - Moved middle click function to shift/ctrl + left-click on uncovered cells
- Version 0.2.3:
  - Enabled multi user support
- Version 0.2.0:
  - Added webserver to play in a browser
- Version 0.1.0:
  - Initial release

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Shoutout

I would like to thank [Edward Jazzhands](http://edward-jazzhands.github.io/) for all his help testing and feedback / feature requests!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Paul Robello - probello@gmail.com
