"""Peter's apple-seeking exercise and resource-aware assignment world."""

ACTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
WATER = {(1, 1), (1, 2), (3, 3)}
APPLES = ((1, 0), (3, 2))
REST = {(2, 0), (4, 2)}
WOLF = (4, 4)
STARTS = [(x, y) for x in range(5) for y in range(5)
          if (x, y) not in WATER | set(APPLES) | {WOLF}]


def simple_step(position, action):
    dx, dy = ACTIONS[action]
    new = (position[0] + dx, position[1] + dy)
    if not (0 <= new[0] < 5 and 0 <= new[1] < 5):
        return position, -1, False, "ongoing"
    if new in WATER or new == WOLF:
        return new, -10, True, "lost"
    if new in APPLES:
        return new, 10, True, "won"
    return new, -0.1, False, "ongoing"


def walk(start, rng, max_steps=100, avoid_revisits=False):
    """Return the apple-seeking path, including its start, and its outcome."""
    if max_steps < 0:
        raise ValueError("The move limit must be nonnegative")
    path = [start]
    visited = {start}
    for _ in range(max_steps):
        choices = range(4)
        if avoid_revisits:
            choices = [action for action in choices
                       if simple_step(path[-1], action)[0] not in visited]
        if not choices:
            return path, "trapped"
        position, _, done, outcome = simple_step(path[-1], int(rng.choice(choices)))
        path.append(position)
        visited.add(position)
        if done:
            return path, outcome
    return path, "timeout"


def step(state, action):
    x, y, energy, fatigue, apples = state
    if action not in range(4):
        raise ValueError("An action must be one of 0, 1, 2, 3")
    dx, dy = ACTIONS[action]
    position = (x + dx, y + dy)
    reward = -0.1
    if not (0 <= position[0] < 5 and 0 <= position[1] < 5):
        position = (x, y)
        reward -= 2
    energy = max(0, energy - 1)
    fatigue = min(8, fatigue + 1)
    if position in APPLES:
        bit = 1 << APPLES.index(position)
        if apples & bit:
            energy = min(12, energy + 6)
            apples &= ~bit
    if position in REST:
        fatigue = max(0, fatigue - 4)
    next_state = (*position, energy, fatigue, apples)
    if position in WATER or energy == 0 or fatigue == 8:
        return next_state, -20, True, "lost"
    if position == WOLF:
        won = energy >= 5 and fatigue <= 4
        return next_state, 30 if won else -20, True, "won" if won else "lost"
    return next_state, reward, False, "ongoing"
