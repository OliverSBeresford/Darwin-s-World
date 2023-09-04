# Darwin-s-World

Darwin's World simulates a two-dimensional world divided up into small squares that is populated
by a number of creatures. Each of the creatures lives in one of the squares, faces in one of the major
compass directions (North, East, South, or West) and belongs to a particular species that determines how
that creature behaves. 

A world is populated with twenty creatures, ten of one species and ten of another. The species of the creature is identied by the first letter in its name. The creature faces in the direction indicated by its pointy nose. The behavior of each creature (you can think of it as
a small robot) is controlled by a program that is species specic. Thus, all of the Rovers behave in thesame way. The behaviors of different species, however, are probably different.

As the simulation proceeds, every creature gets a turn. On its turn, a creature executes a short piece of
its program that allows it to look forward and then take some action. The possible actions are (1) moving
forward, (2) turning left or right, and (3) infecting the creature in front of it. (Infection transforms the
victim into a member of the infecting species.) After it acts, the turn for that creature ends, and some
other creature gets its turn, and then another, and so on. The goal of the game is to survive, as a species.


Species Programming
---
In order to know what to do on any particular turn, a creature executes some number of instructions
in an internal program specic to its species. For example, the program for the Flytrap species is shown below:

Step; Instruction; Comment

1 ifenemy 4 /// If there is an enemy ahead, go to step 4.  

2 left /// Turn left  

3 go 1 /// Go back to step 1

4 infect 1 /// Infect the adjacent creature, that creature starts its program at step 1

5 go 1 /// Go back to step 1

The step numbers are not part of the actual program, but are included here to make it easier to understand
the program. The step lines represent the line that a certain step is on in a text file. On its turn, a Flytrap first checks to see if it is facing an enemy creature in the adjacent
square. If so, the program jumps ahead to step 4 and infects the hapless creature that happened to be
there. If not, the program instead goes on to step 2, in which it simply turns left. In either case, the next
instruction causes the program to loop from the beginning.
All creatures start their programs at step 1 and ordinarily continue with each new instruction in
sequence, although this order can be changed by certain instructions in the program. Each creature is
responsible for remembering the number of the next step to be executed. The valid Darwin instructions
are:

* hop: The creature moves forward as long as the square it is facing is empty. If moving forward would put
the creature outside the boundaries of the world or would cause it to land on top of another creature,
the hop instruction does nothing.
* left: The creature turns left 90 degrees to face in a new direction.
* right: The creature turns right 90 degrees.
* infect n: If the square immediately in front of this creature is occupied by a creature of a different species
(an 'enemy') that creature is infected to become the same as the infecting species. When a creature
is infected, it keeps its position and orientation, but changes its internal species indicator and begins
executing the same program as the infecting creature, starting at step n of the program.
* ifempty n: If the square in front of the creature is unoccupied, the program continues from step n. If that
square is occupied or outside the world boundary, continue with the instruction that follows.
* ifwall n: If the creature is facing and is at a world boundary (which we imagine as consisting of a huge
wall) jump to step n; otherwise, continue with the next instruction.
* ifsame n: If the square the creature is facing is occupied by a creature of the same species, jump to step
n; otherwise, continue with the next instruction.
* ifenemy n: If the square the creature is facing is occupied by a creature of another species, jump to step
n; otherwise, go on with the next instruction.
* ifrandom n: In order to make it possible to write some creatures capable of exercising what might be
called the rudiments of ' free will,' this instruction jumps to step n half the time and continues with
the next instruction the other half of the time.
* go n: This instruction always jumps to step n, independent of any condition.


A creature may execute any number of if or go instructions without relinquishing its turn. The turn
ends only when the program executes one of the "action" instructions: hop, left, right, or infect. On
subsequent turns, the program starts up where it left off.

Species
---
The program for each species is stored in a text file in the subfolder named texts in the repository. Each file
consists of all of the instruction in the procedure of the creature named "x" in "x.txt".


For example for the Flytrap creature could look like this:

ifenemy 4

left

go 1

infect 1

go 1

The flytrap sits in one place and spins.
It infects anything which comes in front.
Flytraps do well when they clump.


Here are several creature files that I created:

- Flytrap: This creature spins in one square, infecting any enemy creature it sees.
- Rover: This creature walks in straight lines until it is blocked, infecting any enemy creature it sees. If it
can't move forward, it turns.
- Apex: This creature isn't necassarily the most powerful creature; it is simply a version of Rover that "exercises free will"
- Evo: perhaps the most intersting creature of them all, this creature can be trained against another: it mutates its procedure over 
and over again in different ways, by (1) creating a random procedure that is still functional, using "chunks" of
steps, (2) mutating the procedure multiple times by changing the way 1 line works within that procedure, (3) testing each of these mutations
many times and keeping the mutation that works best against the enemy species, (4) reapeating this process.
- Trained: Since the evo creature is the creature to be trained against another, we must have one that is just the fully trained version of the
evo (trained species). To use this class you must first train the evo class, then the fully trained species program will be put here, and 
not edited until you retrain the evo class. (the evo class is given a new procedure with each time you run the program)
- Spiral: The final class, the spiral class is one that finds one of the corners of the map, and circles gradually in towards the middle from there,
then goes back to the outside and repeats.

# How to Use
1. Install Python 3.x from [here](https://www.python.org/download/releases/) (Or use your preffered package manager)
2. Install poetry using this command:
```bash
$ curl -sSL https://install.python-poetry.org | python3 -
```
Another option is by using pip. Check if it is installed using:
```bash
$ pip3 --version
```
If an error is shown, you do not have pip. Install it using this command:
```bash
$ python3 -m ensurepip --upgrade
```
This will install pip in your python environment. Now you can install poetry using:
```bash
$ pip3 install poetry
```
3. Clone the repository:
```bash
$ git clone https://github.com/OliverSBeresford/Darwin-s-World
```
or download as zip and extract.

4. This python project uses poetry to install dependencies and create a virtual environment to run the code in.

Before running the program, in the root directory, run:
```bash
$ poetry install
$ poetry shell
```
This will install dependencies and create a venv for the program to run in.

5. After doing this, you can run the program on your text editor.
You can also run it from the command line in the root directory of the project with this command:
```bash
$ python3 main.py
```

Once you're done, you can exit the venv:

On macOS and Linux:

```shell
deactivate
```

On Windows:
```shell
deactivate.bat
```

You can also delete the files associated with it if you want and if they are still there after deactivating, but you don't have to.
This action cannot be undone.

On macOS and Linux:

```shell
rm -r venv
```

On Windows:
```shell
rmdir /s /q venv
```

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to modify the instructions based on your project's specific setup and requirements.