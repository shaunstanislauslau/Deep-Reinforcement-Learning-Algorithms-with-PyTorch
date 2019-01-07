import copy
import random

import gym
import numpy as np
from Base_Environment import Base_Environment

class Bit_Flipping_Environment(Base_Environment):

    def __init__(self, environment_dimension=50):
        self.environment_dimension = environment_dimension
        self.reset_environment()
        self.reward_for_achieving_goal = 1
        self.step_reward_for_not_achieving_goal = 0

    def reset_environment(self):
        self.desired_goal = self.randomly_pick_state_or_goal()
        self.state = self.randomly_pick_state_or_goal()
        self.state.extend(self.desired_goal)
        self.achieved_goal = self.state[:self.environment_dimension]
        self.step_count = 0

    def randomly_pick_state_or_goal(self):
        return [random.randint(0, 1) for _ in range(self.environment_dimension)]

    def conduct_action(self, action):

        self.step_count += 1

        if action != self.environment_dimension + 1: #otherwise no bits are flipping
            self.next_state = copy.copy(self.state)
            self.next_state[action] = self.next_state[action] % 1

        if self.goal_achieved(self.next_state):
            self.reward = 1
            self.done = True

        else:
            self.reward = 0

            if self.step_count >= self.environment_dimension:
                self.done = True
            else:
                self.done = False

        self.achieved_goal = self.next_state[:self.environment_dimension]

    def goal_achieved(self, next_state):
        return next_state[:self.environment_dimension] == next_state[-self.environment_dimension:]

    def get_action_size(self):
        return self.environment_dimension + 1

    def get_state_size(self):
        return len(self.state)

    def get_state(self):
        return np.array(self.state)

    def get_next_state(self):
        return np.array(self.next_state)

    def get_reward(self):
        return self.reward

    def get_done(self):
        return self.done

    def get_desired_goal(self):
        return self.desired_goal

    def get_achieved_goal(self):
        return self.achieved_goal

    def get_reward_for_achieving_goal(self):
        return self.reward_for_achieving_goal

    def step_reward_for_not_achieving_goal(self):
        return self.step_reward_for_not_achieving_goal

    def get_max_steps_per_episode(self):
        return self.environment_dimension

    def get_action_types(self):
        return "CONTINUOUS"

    def get_score_to_win(self):
        return 1

    def get_rolling_period_to_calculate_score_over(self):
        return 20
