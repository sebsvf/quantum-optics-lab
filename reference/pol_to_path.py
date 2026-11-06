
import math

import perceval as pcvl


def build_circuit(xi_rad: float) -> pcvl.Circuit:
    return pcvl.Circuit(2) // (0, pcvl.HWP(xi_rad)) // pcvl.PBS()


def output_probs(xi_deg: float) -> tuple[float, float]:
    simulator = pcvl.SimulatorFactory.build(build_circuit(math.radians(xi_deg)))
    dist = simulator.probs(pcvl.BasicState("|{P:H},0>"))
    p0 = sum(float(p) for state, p in dist.items() if state[0] == 1)
    p1 = sum(float(p) for state, p in dist.items() if state[1] == 1)
    return p0, p1


if __name__ == "__main__":
    for xi in [0, 11.25, 22.5, 33.75, 45]:
        p0, p1 = output_probs(xi)
        print(f"xi = {xi:6.2f} deg   P0 (V) = {p0:.4f}   P1 (H) = {p1:.4f}")
