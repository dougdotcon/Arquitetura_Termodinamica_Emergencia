"""
Tests for the entropic gravity simulations
"""

import sys
import os
import unittest
import numpy as np

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import only the modules that exist
from galactic_rotation import newtonian_force, verlinde_force, stable_orbital_velocity, simulate_orbit


class TestGalacticRotation(unittest.TestCase):
    """Tests for galactic rotation simulation"""

    def test_newtonian_force(self):
        """Test Newtonian force calculation"""
        # Force should be positive and decrease with square of distance
        f_10 = newtonian_force(10.0)
        f_20 = newtonian_force(20.0)

        self.assertGreater(f_10, 0)
        self.assertGreater(f_20, 0)
        self.assertGreater(f_10, f_20)  # Force smaller at larger distances

        # Verify inverse square law
        ratio = f_10 / f_20
        expected_ratio = (20.0 / 10.0) ** 2  # 4
        self.assertAlmostEqual(ratio, expected_ratio, places=1)

    def test_verlinde_force(self):
        """Test Verlinde force with phase transition"""
        # Near center: should be similar to Newton
        f_newton_near = newtonian_force(5.0)
        f_verlinde_near = verlinde_force(5.0)
        self.assertAlmostEqual(f_verlinde_near, f_newton_near, places=1)

        # Far from center: should be stronger than Newton
        # For r=100, Newton acceleration = 1*1000/10000 = 0.1 < A_0=2.0
        f_newton_far = newtonian_force(100.0)
        f_verlinde_far = verlinde_force(100.0)
        self.assertGreater(f_verlinde_far, f_newton_far)

    def test_orbital_velocity(self):
        """Test orbital velocity calculation"""
        # Test at distance where there's difference
        r = 100.0  # Far, where Verlinde is different

        v_newton = stable_orbital_velocity(r, 'newton')
        v_verlinde = stable_orbital_velocity(r, 'verlinde')

        # Both should be positive
        self.assertGreater(v_newton, 0)
        self.assertGreater(v_verlinde, 0)

        # Verlinde should have higher velocity at large distances
        self.assertGreater(v_verlinde, v_newton)

    def test_basic_orbit_simulation(self):
        """Test basic orbit simulation"""
        tx, ty, v_avg = simulate_orbit('newton', initial_radius=10.0, steps=100)

        # Should return lists of same size
        self.assertEqual(len(tx), len(ty))
        self.assertEqual(len(tx), 101)  # initial + 100 steps

        # Average velocity should be positive
        self.assertGreater(v_avg, 0)

        # Should start at correct radius
        r_initial = np.sqrt(tx[0]**2 + ty[0]**2)
        self.assertAlmostEqual(r_initial, 10.0, places=1)

    def test_flat_rotation_curve(self):
        """Test if Verlinde produces flatter rotation curve"""
        radii = np.linspace(50, 150, 5)  # Larger radii where difference exists

        v_newton = [stable_orbital_velocity(r, 'newton') for r in radii]
        v_verlinde = [stable_orbital_velocity(r, 'verlinde') for r in radii]

        # Calculate variations
        var_newton = np.std(v_newton) / np.mean(v_newton)
        var_verlinde = np.std(v_verlinde) / np.mean(v_verlinde)

        # Verlinde should have lower variation (flatter)
        self.assertLess(var_verlinde, var_newton)

        # Basic verifications
        for v in v_newton + v_verlinde:
            self.assertGreater(v, 0)


class TestPhysicalConstraints(unittest.TestCase):
    """Tests for physical constraints and edge cases"""
    
    def test_force_at_zero(self):
        """Test force at r=0 returns 0 (no singularity)"""
        f_newton = newtonian_force(0.0)
        f_verlinde = verlinde_force(0.0)
        
        self.assertEqual(f_newton, 0.0)
        self.assertEqual(f_verlinde, 0.0)
    
    def test_model_validation(self):
        """Test that invalid models raise errors"""
        with self.assertRaises(ValueError):
            stable_orbital_velocity(10.0, 'invalid_model')
    
    def test_energy_conservation_approx(self):
        """Test approximate energy conservation in orbit"""
        # Simulate a circular orbit
        tx, ty, v_avg = simulate_orbit('verlinde', initial_radius=30.0, steps=500)
        
        # Calculate initial and final radius
        r_initial = np.sqrt(tx[0]**2 + ty[0]**2)
        r_final = np.sqrt(tx[-1]**2 + ty[-1]**2)
        
        # Orbit should remain roughly stable (within 50% of initial radius)
        self.assertLess(abs(r_final - r_initial) / r_initial, 0.5)


if __name__ == '__main__':
    unittest.main()
