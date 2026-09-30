import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from datetime import datetime

print("=" * 55)
print(" QUANTUM MOLECULAR SIMULATION")
print(" Drug Discovery & DNA Analysis")
print(f"  {datetime.now()}")
print("=" * 55)

simulator = AerSimulator()

print("\n-- PART 1: DNA BASE PAIR QUANTUM STATE --\n")
print("DNA has 4 bases: Adenine, Thymine, Guanine, Cytosine")
print("A superposition gives each base an equal chance when measures\n")

dna_bases = {
    "Adenine":  "00",
    "Thymine":  "01",
    "Guanine":  "10",
    "Cytosine": "11",
}

qc_dna = QuantumCircuit(2, 2)
qc_dna.h(0)
qc_dna.h(1)
qc_dna.measure([0,1],[0,1])

job = simulator.run(qc_dna, shots=1000)
counts = job.result().get_counts()

print("sampled measurement outcomes (1000 shots):")
for state, count in sorted(counts.items()):
    base = {v:k for k,v in dna_bases.items()}.get(state, "Unknown")
    bar = "#" * (count // 20)
    print(f"  |{state}> {base:<12} {bar} {count/10:.1f}%")

print("  Note: this is uniform random sampling, which a classical RNG also produces\n")

print("-- PART 2: PROTEIN FOLDING SIMULATION --\n")
print("Protein folding determines drug binding sites")
print("Misfolded proteins are linked to several diseases\n")

amino_acids = [
    ("Glycine",    0.0,  "Simplest amino acid"),
    ("Alanine",    0.25, "Common in proteins"),
    ("Valine",     0.5,  "Essential amino acid"),
    ("Leucine",    0.75, "Most common in proteins"),
]

print("Simulating protein chain folding angles:\n")
for acid, angle, desc in amino_acids:
    qc_protein = QuantumCircuit(1, 1)
    qc_protein.ry(angle * np.pi, 0)
    qc_protein.measure(0, 0)

    job = simulator.run(qc_protein, shots=100)
    counts = job.result().get_counts()

    folded = counts.get("1", 0)
    unfolded = counts.get("0", 0)

    state = "FOLDED" if folded > unfolded else "UNFOLDED"
    print(f"  {acid:<12} {desc}")
    print(f"  State: {state} | Folded:{folded}% Unfolded:{unfolded}%\n")

print("  Real world: Google DeepMind AlphaFold uses similar")
print("  approach to model protein structures\n")

print("-- PART 3: DRUG MOLECULE BINDING SIMULATION --\n")
print("Simulating how drug molecules bind to target proteins\n")

drugs = [
    {
        "name": "Aspirin",
        "target": "COX enzyme",
        "qubits": 2,
        "binding_strength": 0.7,
        "use": "Pain relief anti-inflammatory"
    },
    {
        "name": "Penicillin",
        "target": "Bacterial cell wall",
        "qubits": 2,
        "binding_strength": 0.9,
        "use": "Antibiotic"
    },
    {
        "name": "Experimental-QX1",
        "target": "Cancer cell receptor",
        "qubits": 2,
        "binding_strength": 0.85,
        "use": "Simulated cancer drug"
    }
]

for drug in drugs:
    qc_drug = QuantumCircuit(drug["qubits"], drug["qubits"])

    qc_drug.h(0)
    qc_drug.ry(drug["binding_strength"] * np.pi, 1)
    qc_drug.cx(0, 1)
    qc_drug.measure_all()

    job = simulator.run(qc_drug, shots=500)
    counts = job.result().get_counts()

    bound_states = sum(v for k,v in counts.items() if k.count("1") >= 1)
    binding_prob = bound_states / 500 * 100

    efficacy = "HIGH" if binding_prob > 60 else " MEDIUM" if binding_prob > 40 else "LOW"

    print(f"  Drug:        {drug['name']}")
    print(f"  Target:      {drug['target']}")
    print(f"  Use:         {drug['use']}")
    print(f"  Binding:     {binding_prob:.1f}% probability")
    print(f"  Efficacy:    {efficacy}")
    print()

print("-- PART 4: DNA MUTATION DEMO --\n")
print("Toy demo: flagging mutations in synthetic data\n")

mutations = [
    ("BRCA1", "Breast cancer gene",    True,  "High risk mutation"),
    ("TP53",  "Tumor suppressor",      True,  "Cancer risk elevated"),
    ("CFTR",  "Cystic fibrosis gene",  False, "Normal sequence"),
    ("APOE4", "Alzheimer's risk gene", True,  "Elevated risk"),
]

print("Scanning DNA sequences for mutations:\n")
for gene, role, mutated, desc in mutations:
    qc_mut = QuantumCircuit(2, 2)

    if mutated:
        qc_mut.x(0)
        qc_mut.h(1)
        qc_mut.cx(0, 1)
    else:
        qc_mut.h(0)
        qc_mut.h(1)

    qc_mut.measure([0,1],[0,1])

    job = simulator.run(qc_mut, shots=100)
    counts = job.result().get_counts()

    mutation_signal = counts.get("11", 0) + counts.get("10", 0)
    tag = "[MUTATION FLAGGED]" if mutated else "[NORMAL]"

    print(f"  {tag} Gene: {gene}")
    print(f"  Role: {role}")
    print(f"  Finding: {desc}")
    print(f"  Simulated measurement: {mutation_signal}%\n")

print("-- SUMMARY --")
print(f"  DNA bases simulated:   {len(dna_bases)}")
print(f"  Protein states modeled: {len(amino_acids)}")
print(f"  Drug candidates tested: {len(drugs)}")
print(f"  Mutations scanned:     {len(mutations)}")
print()
print("  Note: this is a classical simulation with illustrative toy data.")
print("  No speedup is measured here.")
