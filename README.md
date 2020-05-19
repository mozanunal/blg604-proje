# simstar_env

Download Simstar from the link:

https://eatron.sharepoint.com/:f:/s/Technology/Ei4iGw_Kf-JEr1WK3aLJLM0B_64FaBP4KepapIiZKATrtQ?e=bh9l26

### Windows 
just click on Simstar.exe and Simstar is ready

### Linux 
    cd Simstar
  
    chmod 777 -R *
  
    ./Simstar.sh

## Install Python API

      cd PythonAPI

      python setup.py install


## Installation Test

There are multiple stages that needs to be checked. 

### 1. Test Simstar Executable

Open the simstar executable, allow for networking if asked. 

### 2. Test PythonAPI installation

Run the following with success.

	cd PythonAPI

	python python_api_intro.py

### 3. Test Environment Setup

	cd GymEnv

	python example_experiment.py


### Optional Test

To test a closed loop training with Tensorflow, you can run the example DDPG agent adapted from this repository.

	
#### Requirements:
  Tensorflow 1.12

      cd example_ddpg

      python playGame_DDPG.py