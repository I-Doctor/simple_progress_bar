# simple_progress_bar_Python
It's a simple Python progress bar module. It supports the use of tee or other redirection methods to record output to files, which is not easy for other similar modules.

## Use the module in code
Just clone it into your project and import it in your code as follow:
from simple_progress_bar import Bar
Then you can use it as follow in a loop:

And the info before or after the bar can be setted.

## Record output into files
You may use the following command to run your programme in order ot record the standard output into your log file.
python xxx.py | tee log.txt

## Principle
Its principle is to use standard error output to achieve the effect of progress bar, and cover it with standard output once after the progress bar is full, so that the final result of the progress bar output into standard output can be recorded by TEE command.
