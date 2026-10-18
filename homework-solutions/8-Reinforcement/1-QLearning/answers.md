# Introduction to reinforcement learning

## Exercise — apple-seeking world

The [executed notebook](notebook.ipynb) adapts the lesson's four moves, random walk, epsilon-greedy action selection, and tabular Bellman update on a fixed 5×5 map. It retains the random policy and compares both policies on the same 500 pre-generated starting positions.

| Policy | Apples reached | Losses | Timeouts | Mean steps, all games |
| --- | ---: | ---: | ---: | ---: |
| Random walk | 182 | 318 | 0 | 7.198 |
| Q-learning | 500 | 0 | 0 | 2.414 |

See [recorded results](apple-world-results.csv). Q-learning uses 5,000 training episodes. Water and the wolf terminate the apple-seeking game in a loss; an apple is its goal. The resource assignment below changes that goal and reports its own comparison.

## Assignment — a more realistic world

The [world implementation](../world.py) defines these explicit rules:

- Each attempted move costs one energy and adds one fatigue. An out-of-bounds attempt keeps the position and has an extra penalty.
- An unconsumed apple restores six energy, up to twelve. Each of two apples can be eaten only once.
- Entering either rest square, representing a tree or grass, removes four fatigue. Cell effects occur before checking exhaustion.
- Zero energy, fatigue eight, or water causes a loss. Reaching the wolf wins only if energy is at least five and fatigue at most four after the move; otherwise the battle is lost.
- Continuing moves reward -0.1, a win +30, and a loss -20. The episode has a bounded length.

State is **(x, y, energy, fatigue, remaining-apple mask)**. Including the apple mask matters: position and resources alone cannot tell whether food is still available. The dense Q table contains four action values for each such state. The [shared learner](../qlearning.py) omits future-value bootstrapping on true terminal transitions.

After 25,000 training episodes, evaluation uses the same 500 starting positions for both policies:

| Policy | Games won | Games lost | Timeouts | Win rate |
| --- | ---: | ---: | ---: | ---: |
| Random walk | 16 | 484 | 0 | 3.2% |
| Q-learning | 500 | 0 | 0 | 100.0% |

The [summary](resource-world-results.csv), [random episodes](resource-random-episodes.csv), [learned episodes](resource-learned-episodes.csv), [policy](resource-policy.npz), and [route/training plot](resource-world.png) preserve the experiment. The notebook prints a successful route from the origin with energy, fatigue, and remaining apples after every move. Random games can end quickly because of death, so a shorter unconditional duration is not automatically better.

## Challenge and limitations

### Task 1 — limit the walk

The shared [walk implementation](../world.py) defaults to **100 attempted moves**, returning `timeout` at the limit. The returned path contains the starting cell, so its move count is `len(path) - 1`. A focused test repeatedly chooses the left wall from `(0, 0)` and verifies that this otherwise endless behavior ends after exactly 100 attempts. Zero moves leave only the start; negative limits are rejected. Reaching an apple or hazard stops immediately.

### Task 2 — avoid previously visited cells

With `avoid_revisits=True`, the walk samples uniformly from actions whose resulting positions have not been visited. Wall attempts are excluded because they repeat the current position. If all neighboring destinations have already been visited, it returns `trapped` rather than looping or choosing from an empty collection.

The executed notebook compares both variants on the same **500 starting positions**, resetting the generator to episode seeds **400000–400499** for each variant. This is a separate experiment from the earlier Q-learning baseline, whose generator advances across episodes.

| Walk policy | Apples reached | Hazard losses | Trapped | Timeouts | Mean attempted moves | Games with revisits |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Ordinary random walk | 183 | 317 | 0 | 0 | 6.768 | 323 |
| No revisits | 155 | 328 | 17 | 0 | 3.202 | 0 |

See the [summary](walk-challenge-results.csv) and [all episode paths](walk-challenge-episodes.csv). One observed trapped path is `(1,4) → (1,3) → (0,3) → (0,4)`: its final cell has no unvisited in-bounds neighbor. All 500 no-revisit paths contain unique positions and remain within the move limit.

Removing loops does not teach the walker where apples or hazards are. On this map and these starts it wins less often, and shorter games include both early losses and traps. This rule alone is therefore not an improvement in success rate. The apple-seeking Q-learning results and the resource-world assignment results above are unchanged.

### Policy interpretation

Equal Q values support random choice only if ties or probabilities are handled accordingly; deterministic `argmax` alone chooses a fixed tied action. Epsilon means the **probability of exploration** in this portfolio. The original Gym lesson uses the opposite convention, so the notebook documents the change.

These results concern a fixed map and controlled starting conditions, not unseen layouts. Repeated evaluation episodes are not independent new worlds. Focused tests cover one-time food consumption, rest, exhaustion, water, post-move battle conditions, clipped discretization, and terminal/nonterminal Bellman targets. No external participant was involved.
