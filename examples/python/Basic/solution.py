import open3d as o3d

if __name__ == "__main__":
    path = "/home/amirok/Documents/Open3D/examples/test_data/test_mesh.ply";
    mesh = o3d.io.read_triangle_mesh(path)
    connected_components = mesh.identically_colored_connected_components()
    ofile = open("/home/amirok/Documents/Open3D/results_python.txt", "w")
    for row in connected_components:
        ofile.write(str(row).replace("[", "").replace("]", ""))
        ofile.write("\n")
    ofile.close()
