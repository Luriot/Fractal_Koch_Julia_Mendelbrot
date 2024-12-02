import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# === VARIABLES MODIFIABLES ===
# Flocon de Koch
order = 10  # Ordre du flocon de Koch

# Ensemble de Julia
julia_c = complex(-0.7, 0.27015)  # Constante complexe pour l'ensemble de Julia
julia_resolution = 3000  # Résolution (pixels par dimension)
julia_iterations = 500  # Nombre maximum d'itérations

# Fractale de Mandelbrot
mandelbrot_resolution = 3000  # Résolution (pixels par dimension)
mandelbrot_iterations = 500  # Nombre maximum d'itérations


# === FONCTIONS ===
def koch_snowflake(order):
    def koch_segment(p1, p2):
        delta = (p2 - p1) / 3
        p3 = p1 + delta
        p5 = p1 + 2 * delta
        angle = np.pi / 3
        rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        p4 = p3 + np.dot(rotation, delta)
        return np.array([p1, p3, p4, p5, p2])

    def koch_recursive(points, depth):
        if depth == 0:
            return points
        new_points = []
        for i in range(len(points) - 1):
            segment = koch_segment(points[i], points[i + 1])
            new_points.extend(segment[:-1])
        new_points.append(points[-1])
        return koch_recursive(np.array(new_points), depth - 1)

    triangle = np.array([
        [0, 0],
        [0.5, np.sqrt(3) / 2],
        [1, 0],
        [0, 0]
    ])
    return koch_recursive(triangle, order)


def julia_set(c, resolution, max_iter):
    x = np.linspace(-1.5, 1.5, resolution)
    y = np.linspace(-1.5, 1.5, resolution)
    z = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    fractal = np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(z) < 2
        fractal[mask] = i
        z[mask] = z[mask]**2 + c

    return fractal, x, y


def mandelbrot_set(resolution, max_iter):
    x = np.linspace(-2.0, 1.0, resolution)
    y = np.linspace(-1.5, 1.5, resolution)
    c = x[np.newaxis, :] + 1j * y[:, np.newaxis]
    z = np.zeros(c.shape, dtype=complex)
    fractal = np.zeros(c.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(z) < 2
        fractal[mask] = i
        z[mask] = z[mask]**2 + c[mask]

    return fractal, x, y


# === VISUALISATION FUNCTIONS ===
def display_koch_snowflake(points):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=points[:, 0], y=points[:, 1], mode='lines', line=dict(color='black')))
    fig.update_layout(title=f"Flocon de Koch (Ordre {order})", xaxis_title="X", yaxis_title="Y", showlegend=False)
    fig.show()


def display_julia_set(fractal, x, y):
    fig = go.Figure(data=go.Heatmap(z=fractal, x=x, y=y, colorscale='Inferno'))
    fig.update_layout(
        title="Ensemble de Julia",
        xaxis=dict(title="Re"),
        yaxis=dict(title="Im"),
        coloraxis_colorbar=dict(title="Itérations")
    )
    fig.show()


def display_mandelbrot_set(fractal, x, y):
    fig = go.Figure(data=go.Heatmap(z=fractal, x=x, y=y, colorscale='Hot'))
    fig.update_layout(
        title="Fractale de Mandelbrot",
        xaxis=dict(title="Re"),
        yaxis=dict(title="Im"),
        coloraxis_colorbar=dict(title="Itérations")
    )
    fig.show()


def three_in_one_graph(koch_points, julia_data, mandelbrot_data):
    plt.figure(figsize=(15, 5))

    # Flocon de Koch
    plt.subplot(1, 3, 1)
    plt.plot(koch_points[:, 0], koch_points[:, 1], color="black")
    plt.title(f"Flocon de Koch (Ordre {order})")
    plt.axis("equal")

    # Ensemble de Julia
    julia_fractal, x, y = julia_data
    plt.subplot(1, 3, 2)
    plt.imshow(julia_fractal, cmap="inferno", extent=[x[0], x[-1], y[0], y[-1]])
    plt.title("Ensemble de Julia")
    plt.colorbar()

    # Fractale de Mandelbrot
    mandelbrot_fractal, x, y = mandelbrot_data
    plt.subplot(1, 3, 3)
    plt.imshow(mandelbrot_fractal, cmap="hot", extent=[x[0], x[-1], y[0], y[-1]])
    plt.title("Fractale de Mandelbrot")
    plt.colorbar()

    plt.tight_layout()
    plt.show()


# === CALCULS ET EXÉCUTION ===
# Precompute fractals
koch_points = koch_snowflake(order)
print("Koch snowflake points calculated.")
julia_data = julia_set(julia_c, julia_resolution, julia_iterations)
print("Julia set data calculated.")
mandelbrot_data = mandelbrot_set(mandelbrot_resolution, mandelbrot_iterations)
print("Mandelbrot set data calculated.")

# Combined graph
three_in_one_graph(koch_points, julia_data, mandelbrot_data)
print("Combined graph displayed.")

# Individual visualizations
display_koch_snowflake(koch_points)
print("Koch snowflake displayed.")
display_julia_set(*julia_data)
print("Julia set displayed.")
display_mandelbrot_set(*mandelbrot_data)
print("Mandelbrot set displayed.")
