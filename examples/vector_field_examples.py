"""
Vector Field (Quiver Plot) Examples

This script demonstrates the quiver plot functionality for visualizing
2D vector fields using the FunctionPlotter class.
"""

from calculuskit.plotter import FunctionPlotter


def demo_gradient_field():
    """Demo 1: Gradient field of a paraboloid."""
    print("Demo 1: Gradient Field of f(x,y) = x² + y²")
    print("-" * 50)

    # Gradient of f(x,y) = x² + y² is (2x, 2y)
    def u(x: float, _y: float) -> float:
        """x-component of gradient"""
        return 2 * x

    def v(_x: float, y: float) -> float:
        """y-component of gradient"""
        return 2 * y

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Gradient Field: ∇f = (2x, 2y)",
        show_magnitude=True,
        colormap="viridis",
    )
    print("✓ Displayed gradient field\n")


def demo_rotation_field():
    """Demo 2: Circular rotation field."""
    print("Demo 2: Rotation Field")
    print("-" * 50)

    def u(_x: float, y: float) -> float:
        """x-component: -y"""
        return -y

    def v(x: float, _y: float) -> float:
        """y-component: x"""
        return x

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Rotation Field: F = (-y, x)",
        normalize=True,  # Normalize to show direction clearly
        color="blue",
    )
    print("✓ Displayed rotation field\n")


def demo_radial_field():
    """Demo 3: Radial field (pointing outward)."""
    print("Demo 3: Radial Outward Field")
    print("-" * 50)

    def u(x: float, _y: float) -> float:
        """x-component: x"""
        return x

    def v(_x: float, y: float) -> float:
        """y-component: y"""
        return y

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Radial Field: F = (x, y)",
        show_magnitude=True,
        colormap="plasma",
    )
    print("✓ Displayed radial field\n")


def demo_saddle_gradient():
    """Demo 4: Gradient of saddle point function."""
    print("Demo 4: Saddle Point Gradient Field")
    print("-" * 50)

    # Gradient of f(x,y) = x² - y² is (2x, -2y)
    def u(x: float, _y: float) -> float:
        return 2 * x

    def v(_x: float, y: float) -> float:
        return -2 * y

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-4, 4),
        y_range=(-4, 4),
        title="Saddle Gradient: ∇(x² - y²)",
        show_magnitude=True,
        colormap="coolwarm",
        density=15,
    )
    print("✓ Displayed saddle gradient field\n")


def demo_vortex_field():
    """Demo 5: Vortex field with magnitude decay."""
    print("Demo 5: Vortex Field with Decay")
    print("-" * 50)

    def u(x: float, y: float) -> float:
        """Vortex with 1/r² decay"""
        r_squared = x**2 + y**2
        if r_squared < 0.1:
            return 0
        return -y / r_squared

    def v(x: float, y: float) -> float:
        """Vortex with 1/r² decay"""
        r_squared = x**2 + y**2
        if r_squared < 0.1:
            return 0
        return x / r_squared

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Vortex Field: F = (-y/r², x/r²)",
        show_magnitude=True,
        colormap="twilight",
        density=20,
    )
    print("✓ Displayed vortex field\n")


def demo_electric_dipole():
    """Demo 6: Electric dipole field."""
    print("Demo 6: Electric Dipole Field")
    print("-" * 50)

    def u(x: float, y: float) -> float:
        """x-component of dipole field"""
        # Two charges: +1 at (1,0) and -1 at (-1,0)
        r1_sq = (x - 1) ** 2 + y**2
        r2_sq = (x + 1) ** 2 + y**2

        if r1_sq < 0.1 or r2_sq < 0.1:
            return 0

        # Electric field from positive charge
        e1x = (x - 1) / (r1_sq**1.5)
        # Electric field from negative charge
        e2x = -(x + 1) / (r2_sq**1.5)

        return e1x + e2x

    def v(x: float, y: float) -> float:
        """y-component of dipole field"""
        r1_sq = (x - 1) ** 2 + y**2
        r2_sq = (x + 1) ** 2 + y**2

        if r1_sq < 0.1 or r2_sq < 0.1:
            return 0

        e1y = y / (r1_sq**1.5)
        e2y = -y / (r2_sq**1.5)

        return e1y + e2y

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Electric Dipole Field",
        show_magnitude=True,
        colormap="RdBu",
        density=18,
    )
    print("✓ Displayed electric dipole field\n")


def demo_shear_field():
    """Demo 7: Shear flow field."""
    print("Demo 7: Shear Flow Field")
    print("-" * 50)

    def u(_x: float, y: float) -> float:
        """Horizontal velocity proportional to height"""
        return y

    def v(_x: float, _y: float) -> float:
        """No vertical velocity"""
        return 0

    plotter = FunctionPlotter(lambda x: x)
    plotter.quiver_plot(
        u,
        v,
        x_range=(-5, 5),
        y_range=(-5, 5),
        title="Shear Flow: F = (y, 0)",
        color="green",
        density=12,
    )
    print("✓ Displayed shear flow field\n")


def main():
    """Run all vector field demonstrations."""
    print("\n" + "=" * 60)
    print("CalculusKit Vector Field (Quiver Plot) Demonstrations")
    print("=" * 60 + "\n")

    demos = [
        demo_gradient_field,
        demo_rotation_field,
        demo_radial_field,
        demo_saddle_gradient,
        demo_vortex_field,
        demo_electric_dipole,
        demo_shear_field,
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
    print("  ✓ Gradient fields")
    print("  ✓ Rotation and vortex fields")
    print("  ✓ Radial fields")
    print("  ✓ Magnitude-based coloring")
    print("  ✓ Vector normalization")
    print("  ✓ Custom arrow density")
    print("  ✓ Physical field visualizations (electric dipole, shear flow)")


if __name__ == "__main__":
    main()
