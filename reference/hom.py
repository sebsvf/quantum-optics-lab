
import perceval as pcvl
from perceval.algorithm import Analyzer

OUTPUTS = {
    "11": pcvl.BasicState([1, 1]),
    "20": pcvl.BasicState([2, 0]),
    "02": pcvl.BasicState([0, 2]),
}


def output_probs(indistinguishability: float = 1.0) -> dict[str, float]:
    experiment = pcvl.Experiment(
        pcvl.BS(), noise=pcvl.NoiseModel(indistinguishability=indistinguishability)
    )
    computer = pcvl.SimulatedComputer("SLOS")
    with computer.acquire():
        analyzer = Analyzer(
            computer, experiment, [pcvl.BasicState([1, 1])], list(OUTPUTS.values())
        )
        analyzer.compute()
    row = analyzer.distribution[0]
    return {key: float(abs(row[i])) for i, key in enumerate(OUTPUTS)}


if __name__ == "__main__":
    for m in [1.0, 0.9, 0.5, 0.0]:
        p = output_probs(m)
        print(f"M = {m:.1f}   P(1,1) = {p['11']:.4f}   P(2,0) = {p['20']:.4f}   P(0,2) = {p['02']:.4f}")
