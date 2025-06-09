Context
Important: Considering the short timeframe and open-endedness of the problem, it is recommended to
focus on creating a minimum viable solution meeting the basic requirements of the problem. Do not
worry about covering all edge cases or finding an optimal solution. We will mainly assess basic
functionality/correctness and code quality. Please provide proof that your code runs with a few test
cases.
Task Overview
Aurora is adding thousands of projects/week and growing steadily. Many of these projects end up being
sold and need to be installed. Smaller installers often struggle scheduling their installation crew
efficiently. Aurora is expanding its product offering into the scheduling space.
Please build a small program that helps solar installers prioritize and manage their installation crew
given a list of buildings that they need to install a PV system on. The output of the program should
be the work schedule (who works on what building for each day). No UI or persistence (DB, files
etc.) required.
Task
Given a list of buildings and a list of employees, generate the schedule for the coming work week by
implementing the method schedule(buildings, employees) and providing some proof that it
works, i.e. generates the correct results. List any edge cases, improvements, and tests you did not
have time to add and how long you think it would take to finish them.
Details
● The output schedule is for the next 5 days: assume Monday through Friday.
● All employees work full days, but can be unavailable on certain days (sick/vacation etc.)
● Assume buildings are given in the order of their importance -- no need for anything but a
simple in-order scheduling
● There are 3 types of employees:
○ Certified installers
○ Installers pending certification
○ Laborers
● There are 3 types of buildings, each requiring a different set of employees. All installs are done
in 1 day.
○ Single story homes require:
- 1 certified installer
○ Two story homes require:
- 1 certified installer AND
- 1 installer pending certification OR a laborer
○ Commercial buildings require:
- 2 certified installer AND
- 2 installers pending certification AND
- 4 workers of any type (cert, pending or laborer)