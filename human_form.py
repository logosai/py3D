import numpy as np
import trimesh
from trimesh.primitives import Sphere, Cylinder

# Head (a sphere)
head = Sphere(radius=0.5, subdivisions=2)
head.apply_translation([0, 0, 3.5])

# Body (a cylinder)
body = Cylinder(radius=0.25, height=2)
body.apply_translation([0, 0, 1.5])

# Left arm (a cylinder)
left_arm = Cylinder(radius=0.125, height=1.5)
left_arm.apply_translation([-0.75, 0, 2.5])
left_arm.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 6, (0, 1, 0), (0, 0, 2.5)))

# Right arm (a cylinder)
right_arm = Cylinder(radius=0.125, height=1.5)
right_arm.apply_translation([0.75, 0, 2.5])
right_arm.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 6, (0, 1, 0), (0, 0, 2.5)))

# Left leg (a cylinder)
left_leg = Cylinder(radius=0.125, height=2)
left_leg.apply_translation([-0.25, 0, 0.5])
left_leg.apply_transform(trimesh.transformations.rotation_matrix(-np.pi / 6, (0, 1, 0), (0, 0, 0.5)))

# Right leg (a cylinder)
right_leg = Cylinder(radius=0.125, height=2)
right_leg.apply_translation([0.25, 0, 0.5])
right_leg.apply_transform(trimesh.transformations.rotation_matrix(np.pi / 6, (0, 1, 0), (0, 0, 0.5)))

# Combine all parts into one mesh
human_form = trimesh.util.concatenate([
    head,
    body,
    left_arm,
    right_arm,
    left_leg,
    right_leg
])

# Scale the object to have a height of 10 cm
scale = 0.1 / (human_form.bounds[:, 2].ptp())
human_form.apply_scale(scale)

# Save the mesh to an STL file
human_form.export('human_form.stl')