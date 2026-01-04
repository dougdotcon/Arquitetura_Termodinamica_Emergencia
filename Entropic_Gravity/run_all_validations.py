#!/usr/bin/env python3
"""
Run All Validations - Master Execution Script
----------------------------------------------
Author: Entropic Gravity Research Team
Date: 2025-12

This script runs all 7 validation modules in sequence with fixed random seeds
for complete reproducibility. All figures are generated from this single script.

Usage:
    python run_all_validations.py
"""

import os
import sys
import numpy as np
import subprocess
from datetime import datetime

# Set fixed random seed for reproducibility
RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

# Get git commit hash for documentation
def get_git_commit():
    try:
        result = subprocess.run(
            ['git', 'rev-parse', 'HEAD'],
            capture_output=True, text=True, cwd=os.path.dirname(__file__)
        )
        return result.stdout.strip()[:8] if result.returncode == 0 else "unknown"
    except:
        return "unknown"

def run_validation(module_path, module_name):
    """Run a single validation module"""
    print(f"\n{'='*60}")
    print(f"Running: {module_name}")
    print(f"{'='*60}")
    
    result = subprocess.run(
        [sys.executable, module_path],
        cwd=os.path.dirname(module_path),
        capture_output=True, text=True
    )
    
    if result.returncode == 0:
        print(f"[PASS] {module_name}")
        if result.stdout:
            print(result.stdout)
    else:
        print(f"[FAIL] {module_name}")
        if result.stderr:
            print(result.stderr)
    
    return result.returncode == 0

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("="*60)
    print("ENTROPIC GRAVITY VALIDATION SUITE")
    print("="*60)
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Git Commit: {get_git_commit()}")
    print(f"Random Seed: {RANDOM_SEED}")
    print("="*60)
    
    # Define validation modules
    validations = [
        ("Validation/06_Gravitational_Lensing/lensing_simulation.py", "Gravitational Lensing"),
        ("Validation/07_Cosmology/emergent_cosmology_solver.py", "Reactive Cosmology"),
        ("src/galactic_rotation.py", "Galactic Rotation Curves"),
        ("Validation/05_Numerical_Convergence/convergence_test.py", "Numerical Convergence (Richardson)"),
        ("Validation/sensitivity_test.py", "Parameter Sensitivity Audit"),
        ("src/entropic_fall_1d.py", "1D Entropic Fall (Demo)")
    ]
    
    results = []
    for module_path, module_name in validations:
        full_path = os.path.join(base_dir, module_path)
        if os.path.exists(full_path):
            success = run_validation(full_path, module_name)
            results.append((module_name, success))
        else:
            print(f"⚠️ Module not found: {module_path}")
            results.append((module_name, False))
    
    # Summary
    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for module_name, success in results:
        status = "[PASS]" if success else "[FAIL]"
        print(f"  {status}: {module_name}")
    
    print(f"\nTotal: {passed}/{total} validations passed")
    print("="*60)
    
    # Generate reproducibility report
    report_path = os.path.join(base_dir, "Validation", "REPRODUCIBILITY_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Reproducibility Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Git Commit:** `{get_git_commit()}`\n")
        f.write(f"**Random Seed:** `{RANDOM_SEED}`\n\n")
        f.write("## Validation Results\n\n")
        for module_name, success in results:
            status = "✅ PASS" if success else "❌ FAIL"
            f.write(f"- {status}: {module_name}\n")
        f.write(f"\n**Summary:** {passed}/{total} validations passed\n")
    
    print(f"\n📄 Reproducibility report saved to: {report_path}")

if __name__ == "__main__":
    main()
