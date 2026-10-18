import importlib.util
import sys
import unittest
from pathlib import Path
from unittest.mock import Mock

import numpy as np


ROOT = Path(__file__).resolve().parents[1] / "8-Reinforcement"


class ReinforcementTests(unittest.TestCase):
    def load_module(self, name):
        path = ROOT / f"{name}.py"
        self.assertTrue(path.is_file(), f"Missing reinforcement implementation: {path}")
        spec = importlib.util.spec_from_file_location(name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        return module

    def test_discretization_clips_bounds_and_rejects_nonfinite_observations(self):
        module = self.load_module("qlearning")
        bounds = ((-1.2, 0.6), (-0.07, 0.07))
        self.assertEqual(module.discretize([-1.2, -0.07], bounds, (20, 20)), (0, 0))
        self.assertEqual(module.discretize([0.6, 0.07], bounds, (20, 20)), (19, 19))
        self.assertEqual(module.discretize([10, -10], bounds, (20, 20)), (19, 0))
        with self.assertRaises(ValueError):
            module.discretize([np.nan, 0], bounds, (20, 20))

    def test_q_update_does_not_bootstrap_after_termination(self):
        module = self.load_module("qlearning")
        q = np.array([[2.0, 0.0], [10.0, 4.0]])
        module.update_q(q, (0,), 0, 1.0, (1,), True, 0.5, 0.9)
        self.assertAlmostEqual(q[0, 0], 1.5)

    def test_q_update_bootstraps_a_nonterminal_transition(self):
        module = self.load_module("qlearning")
        q = np.array([[2.0, 0.0], [10.0, 4.0]])
        module.update_q(q, (0,), 0, 1.0, (1,), False, 0.5, 0.9)
        self.assertAlmostEqual(q[0, 0], 6.0)

    def test_apples_restore_energy_only_once(self):
        world = self.load_module("world")
        state, _, done, outcome = world.step((0, 0, 6, 0, 3), 1)
        self.assertEqual(state, (1, 0, 11, 1, 2))
        self.assertFalse(done)
        self.assertEqual(outcome, "ongoing")
        state, _, _, _ = world.step(state, 0)
        state, _, _, _ = world.step(state, 1)
        self.assertEqual(state, (1, 0, 9, 3, 2))

    def test_resting_reduces_fatigue_but_still_costs_energy(self):
        world = self.load_module("world")
        state, _, done, _ = world.step((1, 0, 9, 5, 2), 1)
        self.assertEqual(state, (2, 0, 8, 2, 2))
        self.assertFalse(done)

    def test_wolf_battle_checks_resources_after_the_move(self):
        world = self.load_module("world")
        _, reward, done, outcome = world.step((4, 3, 6, 3, 0), 3)
        self.assertTrue(done)
        self.assertEqual(outcome, "won")
        self.assertGreater(reward, 0)
        for energy, fatigue in [(5, 3), (6, 4)]:
            with self.subTest(energy=energy, fatigue=fatigue):
                _, reward, done, outcome = world.step((4, 3, energy, fatigue, 0), 3)
                self.assertTrue(done)
                self.assertEqual(outcome, "lost")
                self.assertLess(reward, 0)

    def test_exhaustion_and_water_terminate(self):
        world = self.load_module("world")
        cases = [((0, 0, 1, 0, 3), 3), ((0, 1, 8, 0, 3), 1), ((0, 0, 8, 7, 3), 3)]
        for state, action in cases:
            with self.subTest(state=state):
                _, reward, done, outcome = world.step(state, action)
                self.assertTrue(done)
                self.assertEqual(outcome, "lost")
                self.assertLess(reward, 0)

    def test_random_walk_enforces_the_move_limit(self):
        world = self.load_module("world")
        rng = Mock()
        rng.choice.return_value = 0
        for limit in (0, 1, 100):
            with self.subTest(limit=limit):
                path, outcome = world.walk((0, 0), rng, max_steps=limit)
                self.assertEqual(path, [(0, 0)] * (limit + 1))
                self.assertEqual(outcome, "timeout")
        with self.assertRaises(ValueError):
            world.walk((0, 0), rng, max_steps=-1)

    def test_walk_without_revisits_reports_a_trap(self):
        world = self.load_module("world")
        rng = Mock()
        rng.choice.side_effect = [3, 3, 3, 1, 3, 0]
        path, outcome = world.walk((0, 0), rng, avoid_revisits=True)
        self.assertEqual(
            path, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (0, 4)]
        )
        self.assertEqual(len(path), len(set(path)))
        self.assertEqual(outcome, "trapped")

    def test_walk_stops_at_an_apple_or_hazard(self):
        world = self.load_module("world")
        for start, action, finish, expected in (
            ((0, 0), 1, (1, 0), "won"),
            ((0, 1), 1, (1, 1), "lost"),
            ((4, 3), 3, (4, 4), "lost"),
        ):
            with self.subTest(start=start):
                rng = Mock()
                rng.choice.side_effect = [action]
                path, outcome = world.walk(start, rng, avoid_revisits=True)
                self.assertEqual(path, [start, finish])
                self.assertEqual(outcome, expected)


if __name__ == "__main__":
    unittest.main()
