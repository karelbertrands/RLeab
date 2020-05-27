# RLeab
This library can be used to determine which potential to apply on a single potentiostat channel based on windowed current measurements

Currently the module contains 4 different algorithms, namely A2C, ACKTR, ACER and PPO. All are using 128 parallelized agents on an environment
consisting of 1e-6 amount of bacteria at the start which have an activation of 1e-3. Using these pretrained agents, a prediction can be made
on the voltage to apply in order to maximize the current density of the growing bacteria.

GET STARTED

The user forms a vector consisting of 5 sequential current measurements and supplies this as input to the NewPotential function. Additionally, 
a choise concerning the preferred reinforcement learning agent (A2C, ACKTR, ACER or PPO) has to be made. By standard PPO is chosen, if 
the user would like to change this, a string spelling the name of the algorithm as to be supplied as input for the function. The resulting 
output is a single voltage level. 

FUTURE EXTENSIONS
- ....

This simplified library was constructed by Bertrands Karel and Darcis Michiel. For more information, contact karelbertrands@gmail.com or 
michiel.darcis@gmail.com
