from simstarEnv import SimstarEnv
from sample_agent import Agent
import numpy as np 
import logging
import time
import os

max_episodes = 2
max_steps = 100
reward = 0
done = False

#change directory to file path
os.chdir(os.path.dirname(os.path.abspath(__file__)))
        

if __name__ == "__main__":
    log_level = logging.INFO
    
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=log_level,
        datefmt='%Y-%m-%d %H:%M:%S')
    
    logging.info("simstar env init")
    env  = SimstarEnv(synronized_mode=True,speed_up=5,hz=1)
    agent = Agent(dim_action=3)

    logging.info("entering main loop")
    for ee in range(max_episodes):
        
        episode_total_reward = 0
        logging.info("reset environment. eposde number: %d", ee+1)
        time.sleep(2)
        observation = env.reset()
        for ii in range(max_steps):
            action = agent.act(observation, reward, done)
            action[2] = 0.0
            print(ii,action)
            debug_action = [0.0,1.0,0.0]
            action = debug_action
            observation, reward, done, _ = env.step(action)
            episode_total_reward += reward
            #time.sleep(0.5)
            if(done):
                break

env.clear()