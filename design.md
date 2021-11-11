# Toy Robot Challenge - Design Document
## November 12, 2021

## Author
* Ze Fei Teo, zefeiteo@gmail.com

## Reviewer
* Donald Cong Huang, donald.huang@sick.com.au

## Functional description
The software will allow users to:
* Control a robot with simple commands
* Obtain positioning data

## User interface
* Command line input
* Graphical user interface (GUI) fits into a small terminal window
* Intuitive design elements - compass, chess board

![Inspired by a compass](https://upload.wikimedia.org/wikipedia/commons/9/99/Kompas_Sofia.JPG)

![Inspired by a chess board](https://upload.wikimedia.org/wikipedia/commons/c/c3/Chess_board_opening_staunton.jpg)

       ^                 [ ][ ][ ]              [ ][ ][ ]               [ ][ ][ ]
    <     >               [ ][ ][ ]       ->     ^ [ ][ ]       ->       > [ ][ ]       
       v                  ^ [ ][ ]              [ ][ ][ ]               [ ][ ][ ]
     Arrows              place(0,0,north)       move                    right

## Prioritisation
1. Reliability: robot must execute all commands precisely
2. Safety: robot must not fall off the table
3. Appearance: user interface can be simple

## Goals and milestones
* Requirements analysis & validation
    - [x] *place* functionality
    - [x] *move* functionality
    - [x] *left/right* functionality
    - [x] *report* functionality
    - [x] Command line functionality
    - [x] GUI functionality
* Design
    - [x] Existing *argparse* CLI module
    - [x] Python 3.8 due to familiarity
    - [x] Test scripting with *unittest*
    - [x] Kanban board for Agile project management
* Implementation
    - [x] Classes for robot, table, controller and GUI
    - [x] Methods to compute or check robot position and heading
    - [x] Methods for command line input and GUI
    - [x] Fix bugs where necessary
* Verification
    - [x] Unit testing
    - [x] Integration testing
    - [] User acceptance testing
* Documentation
    - [x] Requirements brief
    - [x] Design document
    - [x] Release notes
    - [x] Package dependency definitions

## Timeline
Nov  8, 2021: Receipt of project requirements, Requirements gathering
Nov  9, 2021: Project planning, Wireframing
Nov 10, 2021: Research, Pseudo-development
Nov 11, 2021: Research, Development
Nov 12, 2021: Development, Documentation