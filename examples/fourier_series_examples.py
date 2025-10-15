"""Fourier series examples using CalculusKit."""

import math

from calculuskit.fourier_series.fourier_series import FourierSeries


def example_1_square_wave():
    """Example 1: Fourier series of square wave."""
    print("=" * 60)
    print("Example 1: Square wave approximation")
    print("=" * 60)

    def square_wave(x):
        """Square wave with period 2π."""
        x_mod = x % (2 * math.pi)
        return 1.0 if x_mod < math.pi else -1.0

    # Create Fourier series with increasing harmonics
    for n in [3, 5, 10]:
        fourier = FourierSeries(square_wave, period=2 * math.pi, n=n)

        # Evaluate at x = π/2 (should be close to 1)
        x = math.pi / 2
        result = fourier.at(x)

        print(f"With {n:2d} harmonics at x=π/2: {result:.6f} (expected: 1.0)")

    print()


def example_2_sawtooth_wave():
    """Example 2: Fourier series of sawtooth wave."""
    print("=" * 60)
    print("Example 2: Sawtooth wave approximation")
    print("=" * 60)

    def sawtooth(x):
        """Sawtooth wave with period 2π."""
        x_mod = x % (2 * math.pi)
        return x_mod / math.pi - 1  # Ranges from -1 to 1

    fourier = FourierSeries(sawtooth, period=2 * math.pi, n=10)

    print("x/π | Actual | Fourier (n=10) | Error")
    print("-" * 50)

    test_points = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
    for ratio in test_points:
        x = ratio * math.pi
        actual = sawtooth(x)
        approx = fourier.at(x)
        error = abs(actual - approx)
        print(f"{ratio:4.2f} | {actual:6.3f} | {approx:14.6f} | {error:.6f}")

    print()


def example_3_triangular_wave():
    """Example 3: Fourier series of triangular wave."""
    print("=" * 60)
    print("Example 3: Triangular wave approximation")
    print("=" * 60)

    def triangular(x):
        """Triangular wave with period 2π."""
        x_mod = x % (2 * math.pi)
        if x_mod < math.pi:
            return (2 * x_mod / math.pi) - 1
        else:
            return 3 - (2 * x_mod / math.pi)

    fourier = FourierSeries(triangular, period=2 * math.pi, n=15)

    # Peak should be at π (value = 1)
    x = math.pi
    result = fourier.at(x)
    print(f"At peak (x=π): {result:.6f} (expected: 1.0)")

    # Trough should be at 0 (value = -1)
    x = 0
    result = fourier.at(x)
    print(f"At trough (x=0): {result:.6f} (expected: -1.0)")

    print()


def example_4_sine_function():
    """Example 4: Fourier series of pure sine (should converge exactly)."""
    print("=" * 60)
    print("Example 4: Pure sine wave f(x) = sin(x)")
    print("=" * 60)

    def sine_wave(x):
        return math.sin(x)

    fourier = FourierSeries(sine_wave, period=2 * math.pi, n=5)

    print("Testing Fourier approximation of pure sine:")
    print("x/π | sin(x) | Fourier | Error")
    print("-" * 50)

    for ratio in [0, 0.25, 0.5, 0.75, 1.0]:
        x = ratio * math.pi
        actual = sine_wave(x)
        approx = fourier.at(x)
        error = abs(actual - approx)
        print(f"{ratio:4.2f} | {actual:6.4f} | {approx:7.4f} | {error:.8f}")

    print()


def example_5_coefficients():
    """Example 5: Extracting Fourier coefficients."""
    print("=" * 60)
    print("Example 5: Fourier coefficients of square wave")
    print("=" * 60)

    def square_wave(x):
        x_mod = x % (2 * math.pi)
        return 1.0 if x_mod < math.pi else -1.0

    fourier = FourierSeries(square_wave, period=2 * math.pi, n=7)

    print(f"a0 (DC component): {fourier.a0():.6f}")
    print("\nCosine coefficients (an):")
    for n in range(1, 8):
        an = fourier.an(n)
        if abs(an) > 1e-6:
            print(f"  a{n} = {an:.6f}")

    print("\nSine coefficients (bn):")
    for n in range(1, 8):
        bn = fourier.bn(n)
        if abs(bn) > 1e-6:
            print(f"  b{n} = {bn:.6f}")

    # For square wave: a0=0, all an=0, bn = 4/(nπ) for odd n, 0 for even n
    print("\nExpected for square wave:")
    print("  an = 0 for all n")
    print("  bn = 4/(nπ) for odd n, 0 for even n")
    print(f"  b1 should be ≈ {4 / math.pi:.6f}")
    print(f"  b3 should be ≈ {4 / (3 * math.pi):.6f}")
    print()


def example_6_custom_period():
    """Example 6: Function with custom period."""
    print("=" * 60)
    print("Example 6: Periodic function with period 4")
    print("=" * 60)

    def periodic_func(x):
        """Function with period 4."""
        x_mod = x % 4
        return x_mod**2  # From 0 to 16

    fourier = FourierSeries(periodic_func, period=4, n=10)

    print("Testing at various points:")
    print("x   | f(x)  | Fourier | Error")
    print("-" * 50)

    for x in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5]:
        actual = periodic_func(x)
        approx = fourier.at(x)
        error = abs(actual - approx)
        print(f"{x:3.1f} | {actual:5.2f} | {approx:7.4f} | {error:.4f}")

    print()


def example_7_cosine_function():
    """Example 7: Pure cosine wave."""
    print("=" * 60)
    print("Example 7: Pure cosine wave f(x) = cos(x)")
    print("=" * 60)

    def cosine_wave(x):
        return math.cos(x)

    fourier = FourierSeries(cosine_wave, period=2 * math.pi, n=5)

    # For pure cosine, we should get a1 = 1, all other coefficients ≈ 0
    a0 = fourier.a0()
    a1 = fourier.an(1)
    b1 = fourier.bn(1)

    print(f"a0 = {a0:.8f} (expected: 0)")
    print(f"a1 = {a1:.8f} (expected: 1)")
    print(f"b1 = {b1:.8f} (expected: 0)")

    # Test approximation
    x = math.pi / 3
    actual = cosine_wave(x)
    approx = fourier.at(x)

    print("\nAt x=π/3:")
    print(f"  cos(π/3) = {actual:.6f}")
    print(f"  Fourier  = {approx:.6f}")
    print(f"  Error    = {abs(actual - approx):.8f}")
    print()


def example_8_half_wave_rectifier():
    """Example 8: Half-wave rectified sine."""
    print("=" * 60)
    print("Example 8: Half-wave rectified sine wave")
    print("=" * 60)

    def half_wave_rectified(x):
        """Half-wave rectified sine: f(x) = sin(x) if sin(x) > 0, else 0."""
        sin_val = math.sin(x)
        return sin_val if sin_val > 0 else 0.0

    fourier = FourierSeries(half_wave_rectified, period=2 * math.pi, n=10)

    # DC component (average value)
    a0 = fourier.a0()
    print(f"DC component (a0): {a0:.6f}")
    print(f"Expected: {1 / math.pi:.6f}")  # Average = 1/π

    # Test at various points
    print("\nApproximation quality:")
    print("x/π | Actual | Fourier")
    print("-" * 40)

    for ratio in [0.25, 0.5, 0.75, 1.0]:
        x = ratio * math.pi
        actual = half_wave_rectified(x)
        approx = fourier.at(x)
        print(f"{ratio:4.2f} | {actual:6.4f} | {approx:7.4f}")

    print()


def example_9_step_function():
    """Example 9: Step function."""
    print("=" * 60)
    print("Example 9: Step function")
    print("=" * 60)

    def step_function(x):
        """Step function: 0 for x in [0, π), 1 for x in [π, 2π)."""
        x_mod = x % (2 * math.pi)
        return 1.0 if x_mod >= math.pi else 0.0

    # Compare with different numbers of harmonics
    print("Effect of number of harmonics:")
    print("n  | At x=π/2 (expected 0) | At x=3π/2 (expected 1)")
    print("-" * 60)

    for n in [5, 10, 20, 30]:
        fourier = FourierSeries(step_function, period=2 * math.pi, n=n)
        val_low = fourier.at(math.pi / 2)
        val_high = fourier.at(3 * math.pi / 2)
        print(f"{n:2d} | {val_low:20.6f} | {val_high:20.6f}")

    print()


def example_10_convergence_analysis():
    """Example 10: Analyzing convergence with increasing harmonics."""
    print("=" * 60)
    print("Example 10: Convergence analysis for square wave")
    print("=" * 60)

    def square_wave(x):
        x_mod = x % (2 * math.pi)
        return 1.0 if x_mod < math.pi else -1.0

    # Test point
    x_test = math.pi / 2
    expected = square_wave(x_test)

    print("Number of harmonics vs. approximation error:")
    print("n   | Approximation | Error")
    print("-" * 40)

    for n in [3, 5, 10, 15, 20, 30, 50]:
        fourier = FourierSeries(square_wave, period=2 * math.pi, n=n)
        approx = fourier.at(x_test)
        error = abs(approx - expected)
        print(f"{n:3d} | {approx:13.8f} | {error:.8f}")

    print(f"\nExpected value: {expected}")
    print()


def example_11_harmonic_content():
    """Example 11: Analyzing harmonic content."""
    print("=" * 60)
    print("Example 11: Harmonic content analysis")
    print("=" * 60)

    def sawtooth(x):
        x_mod = x % (2 * math.pi)
        return x_mod / math.pi - 1

    fourier = FourierSeries(sawtooth, period=2 * math.pi, n=10)

    print("Harmonic | an (cosine) | bn (sine) | Magnitude")
    print("-" * 60)

    for n in range(1, 11):
        an = fourier.an(n)
        bn = fourier.bn(n)
        magnitude = math.sqrt(an**2 + bn**2)
        if magnitude > 1e-6:
            print(f"{n:8d} | {an:11.6f} | {bn:9.6f} | {magnitude:9.6f}")

    print()


def example_12_gibbs_phenomenon():
    """Example 12: Demonstrating Gibbs phenomenon at discontinuity."""
    print("=" * 60)
    print("Example 12: Gibbs phenomenon at discontinuity")
    print("=" * 60)

    def square_wave(x):
        x_mod = x % (2 * math.pi)
        return 1.0 if x_mod < math.pi else -1.0

    # Discontinuity at x = π
    print("Values near discontinuity at x = π:")
    print("(Shows overshoot characteristic of Gibbs phenomenon)")
    print()

    for n in [10, 20, 50]:
        fourier = FourierSeries(square_wave, period=2 * math.pi, n=n)

        print(f"With {n} harmonics:")
        print("x/π  | Fourier")
        print("-" * 30)

        # Sample points near π
        for offset in [-0.1, -0.05, 0, 0.05, 0.1]:
            x = math.pi + offset * math.pi
            approx = fourier.at(x)
            print(f"{(x / math.pi):5.2f} | {approx:7.4f}")

        print()


if __name__ == "__main__":
    example_1_square_wave()
    example_2_sawtooth_wave()
    example_3_triangular_wave()
    example_4_sine_function()
    example_5_coefficients()
    example_6_custom_period()
    example_7_cosine_function()
    example_8_half_wave_rectifier()
    example_9_step_function()
    example_10_convergence_analysis()
    example_11_harmonic_content()
    example_12_gibbs_phenomenon()

    print("=" * 60)
    print("All Fourier series examples completed!")
    print("=" * 60)
