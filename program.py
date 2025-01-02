import numpy as np

M = np.array([[2.33e8, 0, 0],
              [0, 2.33e8, 0],
              [0, 0, 2.33e8]])

K = np.array([[2e9, -1e9, 0],
              [-1e9, 2e9, -1e9],
              [0, -1e9, 1e9]])

eigenvalues, eigenvectors = np.linalg.eig(np.linalg.inv(M) @ K)

frequencies = np.sqrt(eigenvalues) / (2 * np.pi)

filtered_indices = (frequencies >= 0.5) & (frequencies <= 5)
filtered_frequencies = frequencies[filtered_indices]
filtered_mode_shapes = eigenvectors[:, filtered_indices]

print("Eigenvalues (λ):", eigenvalues)
print("Eigenvectors (Mode Shapes):")
print(eigenvectors)
print("-" * 50)
print("Frekuensi Alami dalam rentang 0.5 - 5 Hz:")

for i, freq in enumerate(filtered_frequencies):
    print(f"Frekuensi: {freq:.2f} Hz")
    print("Mode Bentukan (Eigenvector):")
    print(filtered_mode_shapes[:, i])
    print("-" * 50)