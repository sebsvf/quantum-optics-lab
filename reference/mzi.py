
import math

import perceval as pcvl


def build_circuit(phi: float) -> pcvl.Circuit:
    return pcvl.Circuit(2) // pcvl.BS() // (0, pcvl.PS(phi)) // pcvl.BS()


def phase_from_offset(delta_nm: float, wavelength_nm: float = 925.0) -> float:
    return 2 * math.pi * delta_nm / wavelength_nm


def output_probs(delta_nm: float, wavelength_nm: float = 925.0) -> tuple[float, float]:
    phi = phase_from_offset(delta_nm, wavelength_nm)
    backend = pcvl.SLOSBackend()
    backend.set_circuit(build_circuit(phi))
    backend.set_input_state(pcvl.BasicState([1, 0]))
    p0 = backend.probability(pcvl.BasicState([1, 0]))
    p1 = backend.probability(pcvl.BasicState([0, 1]))
    return float(p0), float(p1)


if __name__ == "__main__":
    lam = 925.0
    for delta in [0, lam / 4, lam / 2, 3 * lam / 4, lam]:
        p0, p1 = output_probs(delta, lam)
        print(f"delta = {delta:7.2f} nm   P0 = {p0:.4f}   P1 = {p1:.4f}")
