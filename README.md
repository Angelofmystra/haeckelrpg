DESCRIPTION

Haeckel RPG is web application built to allow me to run pen and paper roleplaying games over the internet. It draws significant influence from MUD clients and serves a similar purpose to what software like OpenRPG and Rolld20 provide. Often such software provide functionality that I do not want (and actively gets in my way) and does not provide functionality that I do want. For example: I have no intention of providing a grid based map. It simply does not fit my style of running games. 

UNIQUE SELLING POINTS

* It is specifically designed to enhance immersion and improve the roleplaying experience.

* It will allow for a roleplaying environment that is "roleplay enforced". This notion is very difficult to do with existing systems.

* It will allow me to build a world and store it with a database. This is vastly superior to the way most Game Masters prep for their roleplaying games because they normally rely on flat storage notes or improvisation. Simply put, they cannot compare to the data storage and withdrawal capabilities that this would possess.

INSTALLATION INSTRUCTIONS

System Requirements:

* Python 2.7.5

* Django 1.6

The end users will only need to access the website in order to log on and play.

The world builders will do something similar, except that they must logon to the admin and interact with that.

To host the server three things must be done.

* You will need to activate the virtual environment. On my MAC OSX this involves typing "source venv/bin/activate" for the mysite folder

* Run the "server.py" command by typing in "python server.py" so that the RPG Game Client is hosted.

* Run the "python manage.py runserver" command so that the web server is hosted.

WHERE TO GET HELP

You can contact the author by email at raakarth[at]gmail[dot]co[dot]uk

CONTRIBUTION GUIDELINES

There are a number of things I need which I cannot do myself. Art for the website. I am not specialised in HTML5 and CSS though my skills in it are okay. Advise on how to improve my webpage is highly appreciated. If there are any usability issues you have, I am very interested in that also. If you wish to be a worldbuilder then you can contact me and I will set you up with a worldbuilder account. 

For the coding style I use the Flake8 tool, which is a wrapper around PyFlakes, pep8 and Ned Batchelder's McCabe script. I also use a script to automatically improve my code quality named "autopep" which is described as a "tool that automatically formats Python code to conform to the PEP 8 style guide". For more information on both, check:

https://pypi.python.org/pypi/flake8

https://pypi.python.org/pypi/autopep8/ 

Contributors List (in alphabetical order)

Bertrand Brompton

Matthew Collins

Paul Massey

CREDITS, INSPIRATION, ALTERNATIVES

My favourite MUD and greatest influence is carrionfields. It was this MUD which gave me greater appreciation for immersion and verisimilitude, and how the game client itself contributes to this.

There are no meaningful alternatives in the sense that my software provides something in a specific way that most alternatives simply lack. If one wishes to play pen and paper roleplaying games, they would simply use either:

* OpenRPG / Traipse
* Skype
* GameTable
* Rolld20

As well as mythweavers, or dndsheets.net in order to hold character sheet data.
 
