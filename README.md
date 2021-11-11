# Toy Robot Challenge - Release Notes
## November 12, 2021

## New features
* **Initialisation** - Users can set the home position and heading of the robot.
* **Positioning & Sensing** - Users can perform incremental movement or rotation of up to 90 degrees without risk of exceeding surface dimensions.
* **Reporting** - Users can request the positioning data of the robot.
* **Command Line Input** - Users can input their commands directly into the terminal.

## Bug fixes
* Fixed issue of parsing unknown arguments
* Addressed invalid robot initialisation
* Enabled parsing of capitalised user input
* Implemented flow control for user commands

## Dependencies
* You will need to install the following:
    * argparse
    * setuptools
* You will need to set up your Python path.

## CLI commands
    _usage: prog.py [-h] [-p x y head] [-m] [-l] [-r] [--report] [-x]_
    _-h     --help      Show this help message and exit_
    _-p     --place     Sets robot home position & heading_
    _-m     --move      Moves robot 1 step forward_
    _-l     --left      Rotates robot -90deg_
    _-r     --right     Rotates robot +90deg_
    _       --report    Reports robot position_
    _-x     --exit      Exits program_

## Example input
    _--place 1 2 east_
    _--move_
    _--move_
    _--left_
    _--move_
    _--report_
    > 3,3,NORTH
    _--exit_