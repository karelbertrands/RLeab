# RLeab
This library can be used to determine which potential to apply on a single potentiostat channel based on windowed current measurements

Currently the module Preduction contains a function called NewPotential which, as the name indicates, can ge used to predict the voltage
to apply based on the windowed input current. 

GET STARTED
The user forms a vector consisting of 5 sequential current measurements and supplies this as input to the NewPotential function. Additionally, 
a choise concerning the preferred reinforcement learning agent (A2C, ACKTR, ACER or PPO) has to be made. By standard PPO is chosen, if 
the user would like to change this, a string spelling the name of the algorithm as to be supplied as input for the function. The resulting 
output is a single voltage level. 

FUTURE EXTENSIONS
- ....

This simplified library was constructed by Bertrands Karel and Darcis Michiel. For more information, contact karelbertrands@gmail.com or 
michiel.darcis@gmail.com
