"""The lesson's tabular Bellman update, shared by both Gymnasium tasks."""

import gymnasium as gym
import numpy as np


def discretize(observation, bounds, bins):
    values = np.asarray(observation, dtype=float)
    if not np.isfinite(values).all():
        raise ValueError("Observations must be finite")
    limits = np.asarray(bounds)
    fractions = (values - limits[:, 0]) / (limits[:, 1] - limits[:, 0])
    return tuple(np.clip((fractions * bins).astype(int), 0, np.asarray(bins) - 1))


def update_q(q, state, action, reward, next_state, terminated, alpha, gamma):
    target = reward if terminated else reward + gamma * np.max(q[next_state])
    q[state + (action,)] += alpha * (target - q[state + (action,)])


def evaluate_gym(environment, q, bounds, bins, seeds, policy="greedy"):
    env = gym.make(environment, max_episode_steps=200)
    records = []
    for seed in seeds:
        rng = np.random.default_rng(seed)
        observation, _ = env.reset(seed=int(seed))
        total = 0
        for count in range(1, 201):
            if policy == "random":
                action = int(rng.integers(env.action_space.n))
            else:
                values = q[discretize(observation, bounds, bins)]
                if policy == "sampled":
                    weights = values - values.min() + 1e-4
                    action = int(rng.choice(len(values), p=weights / weights.sum()))
                else:
                    action = int(np.argmax(values))
            observation, reward, terminated, truncated, _ = env.step(action)
            total += reward
            if terminated or truncated:
                break
        records.append({"seed": int(seed), "steps": count, "return": total,
                        "terminated": terminated, "truncated": truncated,
                        "final_position": float(observation[0])})
    env.close()
    return records


def train_gym(environment, bounds, bins, episodes, seed, alpha, gamma, check_every):
    env = gym.make(environment, max_episode_steps=200)
    rng = np.random.default_rng(seed)
    q = rng.uniform(-0.01, 0, tuple(bins) + (env.action_space.n,))
    best_q = q.copy()
    best_score = -np.inf
    returns, checkpoints = [], []
    for episode in range(episodes):
        observation, _ = env.reset(seed=seed + episode)
        state = discretize(observation, bounds, bins)
        epsilon = max(0.02, 1 - episode / (0.8 * episodes))
        total = 0
        for _ in range(200):
            action = int(rng.integers(env.action_space.n)) if rng.random() < epsilon else int(np.argmax(q[state]))
            observation, reward, terminated, truncated, _ = env.step(action)
            next_state = discretize(observation, bounds, bins)
            update_q(q, state, action, reward, next_state, terminated, alpha, gamma)
            state = next_state
            total += reward
            if terminated or truncated:
                break
        returns.append(total)
        if (episode + 1) % check_every == 0:
            validation = evaluate_gym(environment, q, bounds, bins, range(100000, 100025))
            score = float(np.mean([row["return"] for row in validation]))
            checkpoints.append({"episode": episode + 1, "validation_return": score,
                                "training_mean_100": float(np.mean(returns[-100:]))})
            if score > best_score:
                best_score, best_q = score, q.copy()
            print(environment, checkpoints[-1], flush=True)
    env.close()
    return q, best_q, returns, checkpoints
