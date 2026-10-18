# Reinforcement quiz answers

Expected answers from the English question bank, with qualifications where the lesson simplifies a concept.

## Quiz 45: Reinforcement 1: Pre-Lecture Quiz

1. What is reinforcement learning?  
   **Answer:** a learning technique that deciphers the optimal behavior of an agent in some environment by running many experiments  
   The agent learns from rewards over interactions. A finite experiment does not guarantee finding an optimal policy.
2. What is a policy?  
   **Answer:** a function that returns the action at any given state  
   A deterministic policy chooses an action; a stochastic policy can instead specify action probabilities.
3. A reward function returns a score for each state of an environment.  
   **Answer:** true  
   The lesson uses a state-based reward function. More generally a reward can depend on the state, action, and resulting state.

## Quiz 46: Reinforcement 1: Post-Lecture Quiz

1. What is Q-Learning?  
   **Answer:** both of the above  
   The source combines the two descriptions of learning action values from rewarded transitions.
2. For what values does a Q-Table correspond to the random walk policy?  
   **Answer:** all equal values  
   Equal values support a uniform policy only if ties or probability sampling are handled accordingly. Deterministic argmax alone chooses one tied action.
3. It was better to use exploration than exploitation during the learning process in our lesson.  
   **Answer:** false  
   Learning needs both exploration and exploitation; their useful balance changes during training.

## Quiz 47: Reinforcement 2: Pre-Lecture Quiz

1. Chess and Go are games with continuous states.  
   **Answer:** false  
   Board positions are discrete even though the games have extremely large state spaces.
2. What is the CartPole problem?  
   **Answer:** a simplified version of balancing  
   CartPole asks an agent to keep a pole upright by moving a cart.
3. What tool can we use to play out different scenarios of potential states in a game?  
   **Answer:** simulation environments  
   Simulation supplies transitions, rewards, and termination signals for experiments.

## Quiz 48: Reinforcement 2: Post-Lecture Quiz

1. Where do we define all possible actions in an environment?  
   **Answer:** action space  
   The action space specifies the actions the environment accepts.
2. What pair did we use as the dictionary key-value?  
   **Answer:** (state, action) as the key, Q-Table entry as the value  
   A Q table stores an action value for each discrete state/action pair.
3. What are the hyperparameters we used during Q-Learning?  
   **Answer:** learning rate, discount factor, exploration/exploitation factor  
   These are alpha, gamma, and epsilon. The notebook states explicitly whether epsilon means exploration or exploitation.
