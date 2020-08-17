import open3d as o3d
import numpy as np

def test_identically_colored_connected_components():
    mesh = o3d.geometry.TriangleMesh()
    mesh.vertices = o3d.utility.Vector3dVector(
        np.array([
        [0, 1, 0], [0, 2, 0],
        [1, 0, 0], [1, 1.5, 0], [1, 3, 0],
        [2, 1, 0], [2, 2, 0]
        ]))
    mesh.triangles = o3d.utility.Vector3iVector(
        np.array([
            [0, 2, 3], [0, 3, 1], [1, 3, 4], [2, 5, 3], [3, 5, 6], [3, 6, 4]
            ]))
    red = [1, 0, 0]
    green = [0, 1, 0]
    blue = [0, 0, 1]
    mesh.vertex_colors = o3d.utility.Vector3dVector(
            np.array([red, green,
                      blue, red, green,
                      red, red]))
    
    truth = [[0, 3, 5, 6], [1, 4], [2]]
    result = mesh.identically_colored_connected_components()
    size = 3
    for i in range(size):
        assert truth[i] == list(result[i])
