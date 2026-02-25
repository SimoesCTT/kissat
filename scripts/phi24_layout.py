import gdspy
import numpy as np

def generate_phi24_blueprint():
    lib = gdspy.GdsLibrary()
    cell = lib.new_cell('PHI24_RESONATOR')
    
    # α = log(phi) / (2*pi) ≈ 0.0765872
    alpha = 0.0765872
    base_unit = 1e-9 # 1nm
    
    # 21-layer Fibonacci superlattice (S21)
    sequence = "ABAABABAABAABABAABAAB"
    y = 0
    for char in sequence:
        thick = 1.618 if char == 'A' else 1.0
        rect = gdspy.Rectangle((0, y), (5000, y + thick), layer=1)
        cell.add(rect)
        y += thick
    
    lib.write_gds('phi24_core.gds')
    print("GDSII Blueprint generated: phi24_core.gds")

if __name__ == "__main__":
    generate_phi24_blueprint()
