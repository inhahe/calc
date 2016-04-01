Usage: calc &lt;mathematical-expression>

The mathematical expression may include any constants or functions available in math.py.

Includes calc.bat for Windows users, which lets Windows users simply type "calc <mathematical expression>" at the command prompt, and if no mathematical expression is given then it runs Windows' calc.exe, the graphical calculator tool. calc.exe will run anyway unless calc.bat is placed somewhere in the system path before any windows directory containing a calc.exe. 

calc.bat must be modified by the user to correctly point to python.exe. It currently contains my own path to python.exe, but if python.exe is in your system path then I guess just changing the path to python.exe should work.

Prints the result value with commas included for easy reading. calc.bak.py prints without the commas, if you're interested in that.

Please let me know if there's a better way to print with commas than using the if/elif/else statement I'm using for it now.
