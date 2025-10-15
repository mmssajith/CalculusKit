"""
Demonstration of 3D Surface Plot Features in CalculusKit

This script demonstrates the comprehensive 3D surface plotting capabilities
available in the FunctionPlotter class for visualizing 2-variable functions.
"""

import math

from calculuskit.plotter import FunctionPlotter


def demo_basic_surface():
    """Demo 1: Basic 3D surface plot - Paraboloid."""
    print("Demo 1: Basic 3D Paraboloid Surface")
    print("-" * 50)

    def paraboloid(x: float, y: float) -> float:
        """z = x² + y²"""
        return x**2 + y**2

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        paraboloid,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Paraboloid: z = x² + y²",
        colormap="viridis",
    )
    print("✓ Displayed basic paraboloid surface\n")


def demo_saddle_point():
    """Demo 2: Saddle point visualization."""
    print("Demo 2: Saddle Point Surface")
    print("-" * 50)

    def saddle(x: float, y: float) -> float:
        """z = x² - y²"""
        return x**2 - y**2

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        saddle,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Saddle Point: z = x² - y²",
        colormap="coolwarm",
        elevation=20,
        azimuth=60,
    )
    print("✓ Displayed saddle point surface\n")


def demo_wave_function():
    """Demo 3: Wave function with contour projection."""
    print("Demo 3: Wave Function with Contour Lines")
    print("-" * 50)

    def wave(x: float, y: float) -> float:
        """z = sin(√(x² + y²))"""
        r = math.sqrt(x**2 + y**2)
        return math.sin(r) if r != 0 else 1.0

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        wave,
        x_range=(-10, 10),
        y_range=(-10, 10),
        title="Wave Function: z = sin(√(x² + y²))",
        colormap="plasma",
        show_contour=True,  # Shows contour projection at bottom
        elevation=30,
        azimuth=45,
    )
    print("✓ Displayed wave function with contour projection\n")


def demo_gaussian_surface():
    """Demo 4: 2D Gaussian (bell curve)."""
    print("Demo 4: 2D Gaussian Surface")
    print("-" * 50)

    def gaussian_2d(x: float, y: float) -> float:
        """z = e^(-(x² + y²))"""
        return math.exp(-(x**2 + y**2))

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        gaussian_2d,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="2D Gaussian: z = e^(-(x² + y²))",
        colormap="hot",
        alpha=0.9,
        elevation=35,
        azimuth=135,
    )
    print("✓ Displayed 2D Gaussian surface\n")


def demo_mexican_hat():
    """Demo 5: Mexican hat (Ricker wavelet) function."""
    print("Demo 5: Mexican Hat Wavelet")
    print("-" * 50)

    def mexican_hat(x: float, y: float) -> float:
        """z = (1 - r²) * e^(-r²/2) where r² = x² + y²"""
        r_squared = x**2 + y**2
        return (1 - r_squared) * math.exp(-r_squared / 2)

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        mexican_hat,
        x_range=(-3, 3),
        y_range=(-3, 3),
        title="Mexican Hat Wavelet: z = (1 - r²)e^(-r²/2)",
        colormap="seismic",
        show_contour=True,
        elevation=25,
        azimuth=120,
    )
    print("✓ Displayed Mexican hat wavelet\n")


def demo_trig_surface():
    """Demo 6: Trigonometric surface."""
    print("Demo 6: Trigonometric Surface")
    print("-" * 50)

    def trig_surface(x: float, y: float) -> float:
        """z = sin(x) * cos(y)"""
        return math.sin(x) * math.cos(y)

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        trig_surface,
        x_range=(-2 * math.pi, 2 * math.pi),
        y_range=(-2 * math.pi, 2 * math.pi),
        title="Trigonometric Surface: z = sin(x)·cos(y)",
        colormap="RdBu",
        elevation=30,
        azimuth=45,
    )
    print("✓ Displayed trigonometric surface\n")


def demo_custom_viewing_angles():
    """Demo 7: Same function with different viewing angles."""
    print("Demo 7: Custom Viewing Angles")
    print("-" * 50)

    def peaks(x: float, y: float) -> float:
        """Complex surface with multiple peaks"""
        return (
            3 * (1 - x) ** 2 * math.exp(-(x**2) - (y + 1) ** 2)
            - 10 * (x / 5 - x**3 - y**5) * math.exp(-(x**2) - y**2)
            - 1 / 3 * math.exp(-((x + 1) ** 2) - y**2)
        )

    plotter = FunctionPlotter(lambda x: x)

    # View from different angles
    angles = [
        (30, 45, "Standard View"),
        (60, 30, "High Elevation View"),
        (15, 120, "Low Angle View"),
    ]

    for elev, azim, description in angles:
        print(f"  → {description} (elevation={elev}°, azimuth={azim}°)")
        plotter.surface_plot_3d(
            peaks,
            x_range=(-3, 3),
            y_range=(-3, 3),
            title=f"Peaks Function - {description}",
            colormap="terrain",
            elevation=elev,
            azimuth=azim,
            show_contour=False,
        )

    print("✓ Displayed multiple viewing angles\n")


def demo_transparency_effect():
    """Demo 8: Surface with transparency."""
    print("Demo 8: Transparent Surface")
    print("-" * 50)

    def hemisphere(x: float, y: float) -> float:
        """Upper hemisphere: z = √(r² - x² - y²)"""
        r = 5.0
        val = r**2 - x**2 - y**2
        return math.sqrt(val) if val > 0 else 0

    plotter = FunctionPlotter(lambda x: x)
    plotter.surface_plot_3d(
        hemisphere,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Hemisphere with Transparency (α=0.6)",
        colormap="ocean",
        alpha=0.6,  # Semi-transparent
        elevation=20,
        azimuth=45,
    )
    print("✓ Displayed transparent hemisphere\n")


def main():
    """Run all 3D surface plot demonstrations."""
    print("\n" + "=" * 60)
    print("CalculusKit 3D Surface Plot Demonstrations")
    print("Visualizing 2-Variable Functions")
    print("=" * 60 + "\n")

    demos = [
        demo_basic_surface,
        demo_saddle_point,
        demo_wave_function,
        demo_gaussian_surface,
        demo_mexican_hat,
        demo_trig_surface,
        demo_custom_viewing_angles,
        demo_transparency_effect,
    ]

    print("Available demonstrations:")
    for i, demo in enumerate(demos, 1):
        print(f"  {i}. {demo.__doc__.split(':')[1].strip()}")

    print("\nRunning all demonstrations...")
    print("Close each plot window to see the next demonstration.\n")

    for demo in demos:
        try:
            demo()
        except Exception as e:
            print(f"Error in {demo.__name__}: {e}\n")

    print("=" * 60)
    print("All demonstrations completed!")
    print("=" * 60)
    print("\nKey Features Demonstrated:")
    print("  ✓ Basic 3D surface plotting")
    print("  ✓ Custom colormaps (viridis, coolwarm, plasma, etc.)")
    print("  ✓ Contour projection at the base")
    print("  ✓ Adjustable viewing angles (elevation & azimuth)")
    print("  ✓ Transparency control")
    print("  ✓ Complex mathematical surfaces")
    print("  ✓ Automatic colorbar scaling")


if __name__ == "__main__":
    main()
