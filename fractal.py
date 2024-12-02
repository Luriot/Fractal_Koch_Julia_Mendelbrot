import numpy as np
import matplotlib.pyplot as plt

# === VARIABLES MODIFIABLES ===
# Flocon de Koch
order = 6  # Ordre du flocon de Koch

# Ensemble de Julia
julia_c = complex(-0.7, 0.27015)  # Constante complexe pour l'ensemble de Julia
julia_resolution = 500  # Résolution (pixels par dimension)
julia_iterations = 300  # Nombre maximum d'itérations

# Fractale de Mandelbrot
mandelbrot_resolution = 500  # Résolution (pixels par dimension)
mandelbrot_iterations = 300  # Nombre maximum d'itérations


# === FONCTIONS ===
# Fonction pour générer le Flocon de Koch
def koch_snowflake(order):
    """
    Génère les points du Flocon de Koch pour un certain ordre.
    """
    def koch_segment(p1, p2):
        # Divise le segment en trois parties
        delta = (p2 - p1) / 3
        p3 = p1 + delta
        p5 = p1 + 2 * delta

        # Calcule le point de "pic"
        angle = np.pi / 3  # 60 degrés
        rotation = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        p4 = p3 + np.dot(rotation, delta)

        return np.array([p1, p3, p4, p5, p2])

    def koch_recursive(points, depth):
        if depth == 0:
            return points
        new_points = []
        for i in range(len(points) - 1):
            segment = koch_segment(points[i], points[i + 1])
            new_points.extend(segment[:-1])  # Exclut le dernier point pour éviter les doublons
        new_points.append(points[-1])  # Ajoute le dernier point pour fermer le flocon
        return koch_recursive(np.array(new_points), depth - 1)

    # Triangle équilatéral initial
    triangle = np.array([
        [0, 0],
        [0.5, np.sqrt(3) / 2],
        [1, 0],
        [0, 0]  # Fermer le triangle
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

    return fractal


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

    return fractal


# === VISUALISATION ===
plt.figure(figsize=(15, 5))

# Flocon de Koch
plt.subplot(1, 3, 1)
koch_points = koch_snowflake(order)
plt.plot(koch_points[:, 0], koch_points[:, 1], color="black")
plt.title(f"Flocon de Koch (Ordre {order})")
plt.axis("equal")

# Ensemble de Julia
plt.subplot(1, 3, 2)
julia = julia_set(julia_c, julia_resolution, julia_iterations)
plt.imshow(julia, cmap="inferno", extent=[-1.5, 1.5, -1.5, 1.5])
plt.title("Ensemble de Julia")
plt.colorbar()

# Fractale de Mandelbrot
plt.subplot(1, 3, 3)
mandelbrot = mandelbrot_set(mandelbrot_resolution, mandelbrot_iterations)
plt.imshow(mandelbrot, cmap="hot", extent=[-2.0, 1.0, -1.5, 1.5])
plt.title("Fractale de Mandelbrot")
plt.colorbar()

plt.tight_layout()
plt.show()