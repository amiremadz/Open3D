#include <fstream>

#include "open3d/Open3D.h"

int main() {
    open3d::geometry::TriangleMesh mesh;
    const std::string ply_name = "/home/amirok/Documents/Open3D/examples/test_data/test_mesh.ply";

    if (open3d::io::ReadTriangleMesh(ply_name, mesh)) {
        open3d::utility::LogInfo("Successfully read {}\n", ply_name);
    } else {
        open3d::utility::LogError("Failed to read {}\n", ply_name);
        return 1;
    }

    const std::string txt_name = "/home/amirok/Documents/Open3D/results_cpp.txt";
    std::vector<std::vector<int>> connected_components = mesh.IdenticallyColoredConnectedComponents();
    std::ofstream ofile(txt_name);
    if (ofile) {
        for (size_t row = 0; row < connected_components.size(); ++row) {
            for (size_t col = 0; col < connected_components[row].size(); ++col) {
                ofile << connected_components[row][col] << " ";
            }
            ofile << "\n";
        }
    } 
    ofile.close();
    open3d::utility::LogInfo("Successfully wrote {}\n", txt_name);
 
    return 0;
}
