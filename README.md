# a-lisp-but-its-kinda-cute

Jessica Cioffi and Nicholas Jones

A small Scheme interpreter for Professor Peter Bui's course at the University of Notre Dame

The project that we did was a Scheme interpreter.  It has the ability to perform computations, comparisons (both quantitative and logical),
and declare variables.  It accepts input from a text file that contains the different computations to be performed on each line.  Originally, we took a base code written in C++, ported it to Python in order to make expanding on the code’s functionality considerably 
easier.  From there, we added different operations that we considered vital to an interpreter.

In regards to computing history, Scheme is one dialect of the programming language LISP.  LISP is the second oldest high-level programming
language still used today.  It is one of the languages that the hackers that we read about used when writing programs in the 70s, when 
Steele and Sussman came out with their interpreter.  It helped facilitate the spread of the hacker ethic and computer knowledge with its 
easy to understand implementation, and allowed for everyday people to begin to comprehend and get their hands on software.  

This historical artifact is important not only because of its contribution to programming and computer science as a whole, it also is an 
example of an artifact that was not tainted by the greed of the game hackers in the 80s.  When Bill Gates came out with his BASIC 
interpreter, he got angry that people were freely using the software he made, and confronted The Homebrew Computer Club about wanting 
compensation from those who used it.  Meanwhile Steele and Sussman were not focused on their own personal gain from their interpreter.  
They solely wanted to spread the knowledge of computer science to expand their own horizions, as well of those of anyone interested.  

That is why the Scheme interpreter is an important historical artifact, and one we decided to replicate. 

INSTRUCTIONS:

DOWNLOAD:
- Clone the GitHub repo ( https://github.com/nicholascjones/a-lisp-but-its-kinda-cute ) onto your machine
- Enable execution privileges on 'parser.py' ($ chmod +x parser.py)

RUN SCRIPT:
- Interpret a textfile 'tf' with the following command: ($ ./parser.py tf)

TEXTFILE FORMATTING:

- All clauses in our interpreter must take the format of (<token> <input> <input>)
	* Token is a symbol that performs an action, such as a mathematical or logical operation
	* Input can either be a postive integer, a boolean literal, another clause, or a variable
- Tokens are as such:
	+ adds two numbers
	- subtracts two numbers
	/ divides two numbers
	* multiplies two numbers
	max takes maximum of two numbers
	min takes minimum of two numbers
	|| takes logical or of two booleans
	&& takes logical and of two booleans
	eq? tests for equality of two numbers
	> tests first number greater than second
	< tests first number lesser than second
	define allows definition of a variable as another value to be used later

Sources:
http://norvig.com/lispy.html
http://www.buildyourownlisp.com/contents
https://inst.eecs.berkeley.edu/~cs61a/fa12/projects/scheme/scheme.html



