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
    usage: prog.py [-h] [-p x y head] [-m] [-l] [-r] [--report] [-x]
    -h     --help      Show this help message and exit
    -p     --place     Sets robot home position & heading
    -m     --move      Moves robot 1 step forward
    -l     --left      Rotates robot -90deg
    -r     --right     Rotates robot +90deg
           --report    Reports robot position
    -x     --exit      Exits program

## Example input
    --place 1 2 east
    --move
    --move
    --left
    --move
    --report
    --exit