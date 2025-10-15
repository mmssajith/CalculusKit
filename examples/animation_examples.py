"""
Animation Examples for Series Convergence and Limits

This script demonstrates the animation capabilities for visualizing
how series approximations converge and sequences approach their limits.
"""

import math

from calculuskit.plotter import FunctionPlotter


def demo_taylor_exp():
    """Demo 1: Taylor series convergence for e^x."""
    print("Demo 1: Taylor Series for e^x")
    print("-" * 50)

    def f(x: float) -> float:
        return math.exp(x)

    def taylor_approx(x: float, n: int) -> float:
        """Taylor series approximation of e^x"""
        return sum(x**k / math.factorial(k) for k in range(n + 1))

    plotter = FunctionPlotter(f, x_range=(-2, 2))
    print("  Animating Taylor series convergence...")
    print("  Watch as more terms are added to approximate e^x")

    anim = plotter.animate_series_approximation(
        f,
        taylor_approx,
        max_terms=15,
        title_func=lambda n: f"Taylor Series for e^x: {n} terms",
        func_label="e^x",
        approx_label="Taylor Series",
        interval=500,
    )

    print("✓ Animation complete\n")
    return anim


def demo_taylor_sin():
    """Demo 2: Taylor series convergence for sin(x)."""
    print("Demo 2: Taylor Series for sin(x)")
    print("-" * 50)

    def f(x: float) -> float:
        return math.sin(x)

    def taylor_sin(x: float, n: int) -> float:
        """Taylor series for sin(x)"""
        result = 0.0
        for k in range(n + 1):
            sign = (-1) ** k
            result += sign * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        return result

    plotter = FunctionPlotter(f, x_range=(-2 * math.pi, 2 * math.pi))
    print("  Animating Taylor series for sine...")
    print("  Notice how it converges better near x=0")

    anim = plotter.animate_series_approximation(
        f,
        taylor_sin,
        max_terms=10,
        title_func=lambda n: f"Taylor Series for sin(x): {n} terms",
        func_color="blue",
        approx_color="red",
        interval=600,
    )

    print("✓ Animation complete\n")
    return anim


def demo_taylor_cos():
    """Demo 3: Taylor series convergence for cos(x)."""
    print("Demo 3: Taylor Series for cos(x)")
    print("-" * 50)

    def f(x: float) -> float:
        return math.cos(x)

    def taylor_cos(x: float, n: int) -> float:
        """Taylor series for cos(x)"""
        result = 0.0
        for k in range(n + 1):
            sign = (-1) ** k
            result += sign * (x ** (2 * k)) / math.factorial(2 * k)
        return result

    plotter = FunctionPlotter(f, x_range=(-2 * math.pi, 2 * math.pi))
    print("  Animating Taylor series for cosine...")

    anim = plotter.animate_series_approximation(
        f,
        taylor_cos,
        max_terms=10,
        title_func=lambda n: f"Taylor Series for cos(x): {n} terms",
        func_color="green",
        approx_color="orange",
        interval=600,
    )

    print("✓ Animation complete\n")
    return anim


def demo_fourier_square_wave():
    """Demo 4: Fourier series for square wave."""
    print("Demo 4: Fourier Series for Square Wave")
    print("-" * 50)

    def square_wave(x: float) -> float:
        """Square wave function"""
        return 1.0 if (x % (2 * math.pi)) < math.pi else -1.0

    def fourier_square(x: float, n: int) -> float:
        """Fourier series approximation of square wave"""
        result = 0.0
        for k in range(1, n + 1):
            result += (4 / math.pi) * math.sin((2 * k - 1) * x) / (2 * k - 1)
        return result

    plotter = FunctionPlotter(square_wave, x_range=(0, 4 * math.pi))
    print("  Animating Fourier series for square wave...")
    print("  Observe the Gibbs phenomenon at discontinuities")

    anim = plotter.animate_series_approximation(
        square_wave,
        fourier_square,
        max_terms=20,
        title_func=lambda n: f"Fourier Series for Square Wave: {n} terms",
        func_label="Square Wave",
        approx_label="Fourier Approx",
        func_color="black",
        approx_color="red",
        interval=400,
    )

    print("✓ Animation complete\n")
    return anim


def demo_limit_1_over_n():
    """Demo 5: Sequence convergence: 1/n → 0."""
    print("Demo 5: Sequence Convergence: 1/n → 0")
    print("-" * 50)

    def seq(n: int) -> float:
        return 1 / n

    plotter = FunctionPlotter(lambda x: x)
    print("  Animating sequence convergence...")
    print("  Watch as 1/n approaches 0")

    anim = plotter.animate_limit_convergence(
        seq,
        limit_value=0.0,
        max_n=50,
        title="Convergence of 1/n to 0",
        sequence_color="blue",
        limit_color="red",
        interval=100,
    )

    print("✓ Animation complete\n")
    return anim


def demo_limit_to_e():
    """Demo 6: Sequence convergence: (1 + 1/n)^n → e."""
    print("Demo 6: Sequence Convergence to e")
    print("-" * 50)

    def seq(n: int) -> float:
        return (1 + 1 / n) ** n

    plotter = FunctionPlotter(lambda x: x)
    print("  Animating convergence to Euler's number e...")
    print("  Famous limit: (1 + 1/n)^n → e as n → ∞")

    anim = plotter.animate_limit_convergence(
        seq,
        limit_value=math.e,
        max_n=100,
        title="Convergence to e: (1 + 1/n)^n",
        ylabel="(1 + 1/n)^n",
        sequence_color="green",
        limit_color="red",
        interval=50,
    )

    print("✓ Animation complete\n")
    return anim


def demo_limit_alternating():
    """Demo 7: Alternating sequence with decay."""
    print("Demo 7: Alternating Sequence: (-1)^n / n")
    print("-" * 50)

    def seq(n: int) -> float:
        return ((-1) ** n) / n

    plotter = FunctionPlotter(lambda x: x)
    print("  Animating alternating sequence...")
    print("  Oscillates but converges to 0")

    anim = plotter.animate_limit_convergence(
        seq,
        limit_value=0.0,
        max_n=50,
        title="Alternating Sequence: (-1)^n / n → 0",
        ylabel="(-1)^n / n",
        sequence_color="purple",
        limit_color="red",
        marker="o",
        interval=150,
    )

    print("✓ Animation complete\n")
    return anim


def demo_limit_sin_over_n():
    """Demo 8: Squeeze theorem example: sin(n)/n → 0."""
    print("Demo 8: Squeeze Theorem: sin(n)/n → 0")
    print("-" * 50)

    def seq(n: int) -> float:
        return math.sin(n) / n

    plotter = FunctionPlotter(lambda x: x)
    print("  Animating sequence with oscillating numerator...")
    print("  Despite oscillations, still converges to 0")

    anim = plotter.animate_limit_convergence(
        seq,
        limit_value=0.0,
        max_n=60,
        title="Squeeze Theorem Example: sin(n)/n → 0",
        ylabel="sin(n)/n",
        sequence_color="orange",
        limit_color="red",
        interval=100,
    )

    print("✓ Animation complete\n")
    return anim


def main():
    """Run all animation demonstrations."""
    print("\n" + "=" * 60)
    print("CalculusKit Animation Demonstrations")
    print("Series Convergence & Limit Visualization")
    print("=" * 60 + "\n")

    # Series approximation demos
    series_demos = [
        demo_taylor_exp,
        demo_taylor_sin,
        demo_taylor_cos,
        demo_fourier_square_wave,
    ]

    # Limit convergence demos
    limit_demos = [
        demo_limit_1_over_n,
        demo_limit_to_e,
        demo_limit_alternating,
        demo_limit_sin_over_n,
    ]

    print("SERIES APPROXIMATION ANIMATIONS:")
    for i, demo in enumerate(series_demos, 1):
        print(f"  {i}. {demo.__doc__.split(':')[1].strip()}")

    print("\nLIMIT CONVERGENCE ANIMATIONS:")
    for i, demo in enumerate(limit_demos, 1):
        print(f"  {i + len(series_demos)}. {demo.__doc__.split(':')[1].strip()}")

    print("\nRunning all demonstrations...")
    print("Close each animation window to see the next one.\n")

    all_demos = series_demos + limit_demos
    animations = []

    for demo in all_demos:
        try:
            anim = demo()
            animations.append(anim)
        except Exception as e:
            print(f"Error in {demo.__name__}: {e}\n")

    print("=" * 60)
    print("All demonstrations completed!")
    print("=" * 60)
    print("\nKey Features Demonstrated:")
    print("  ✓ Taylor series convergence (e^x, sin(x), cos(x))")
    print("  ✓ Fourier series approximation (square wave)")
    print("  ✓ Limit convergence visualization")
    print("  ✓ Famous limits (convergence to e)")
    print("  ✓ Alternating sequences")
    print("  ✓ Squeeze theorem examples")
    print("  ✓ Custom animation timing and styling")

    print("\nNote: Animations can be saved as GIF or MP4 files")
    print("using the save_path parameter.")


if __name__ == "__main__":
    main()
