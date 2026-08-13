import importlib


DEPENDENCIES: tuple[tuple[str, str], ...] = (
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
    ("matplotlib", "Visualization ready"),
)


def compare_package_versions() -> bool:
    print("Checking dependencies:")
    all_available = True

    for package_name, description in DEPENDENCIES:
        try:
            package = importlib.import_module(package_name)
        except ImportError:
            print(f"[MISSING] {package_name} - {description}")
            all_available = False
        else:
            version = getattr(package, "__version__", "unknown")
            print(f"[OK] {package_name} ({version}) - {description}")

    return all_available


def show_package_management() -> None:
    print("Package management:")
    print("pip: requirements.txt installs into the active environment")
    print("Poetry: pyproject.toml manages dependencies and its environment")


def show_install_instructions() -> None:
    print("Missing dependencies detected.")
    print("Install with pip:")
    print("python -m pip install -r requirements.txt")
    print("Or install with Poetry:")
    print("poetry install")


def analyze_matrix_data() -> None:
    import matplotlib  # type: ignore[import-not-found]
    import numpy as np  # type: ignore[import-not-found]
    import pandas as pd  # type: ignore[import-not-found, import-untyped]

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore[import-not-found]

    print("Analyzing Matrix data...")
    random_generator = np.random.default_rng(42)
    signal_values = random_generator.normal(50, 15, 1000)
    matrix_data = pd.DataFrame({"signal_strength": signal_values})
    summary = matrix_data["signal_strength"].describe()

    print(f"Processing {len(matrix_data)} data points...")
    print("Generating visualization...")
    figure, axis = plt.subplots()
    axis.hist(matrix_data["signal_strength"], bins=30, color="green")
    axis.axvline(
        summary["mean"],
        color="black",
        linestyle="--",
        label="Mean signal",
    )
    axis.set_title("Matrix Signal Distribution")
    axis.set_xlabel("Signal strength")
    axis.set_ylabel("Frequency")
    axis.legend()
    figure.tight_layout()
    figure.savefig("matrix_analysis.png")
    plt.close(figure)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    show_package_management()
    if not compare_package_versions():
        show_install_instructions()
        return
    analyze_matrix_data()


if __name__ == "__main__":
    main()
