import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from datetime import datetime

print("=" * 55)
print("  QUANTUM NEURAL NETWORK & BRAIN SIMULATOR")
print("  Quantum Computing meets Neuroscience")
print("=" * 55)

simulator = AerSimulator()

print("\n-- PART 1: QUANTUM NEURON SIMULATION --\n")
print("Classical neuron: Fires or doesn't fire (0 or 1)")
print("Quantum neuron:   exists in superposition of both\n")

neuron_inputs = [0.2, 0.5, 0.8, 1.0]

print("Simulating neuron firing probability:\n")
for strength in neuron_inputs:
    qc = QuantumCircuit(1, 1)
    qc.ry(strength * np.pi, 0)
    qc.measure(0, 0)

    job = simulator.run(qc, shots=100)
    counts = job.result().get_counts()

    fired = counts.get("1", 0)
    resting = counts.get("0", 0)

    bar = "#" * (fired // 5)
    status = "FIRING" if fired > 50 else "RESTING"
    print(f"  Signal {strength:.1f} -> [{status}] {bar} {fired}% probability")


print("-- PART 2: QUANTUM NEURAL NETWORK --\n")
print("Simulating a 3 layer quantum neural network\n")

layers = [
    ("Input Layer",  3, "Receives sensory data"),
    ("Hidden Layer", 3, "Processes quantum states"),
    ("Output Layer", 2, "Makes decisions")
]

for layer_name, qubits, desc in layers:
    qc = QuantumCircuit(qubits, qubits)

    for i in range(qubits):
        qc.h(i)

    for i in range(qubits-1):
        qc.ry(np.pi/4 * (i+i), i)

    qc.measure_all()

    job = simulator.run(qc, shots=100)
    counts = job.result().get_counts()

    top_state = max(counts, key=counts.get)
    confidence = counts[top_state]

    print(f"  Layer:        {layer_name}")
    print(f"  Neurons:      {qubits} quantum neurons")
    print(f"  Function:     {desc}")
    print(f"  Output:       |{top_state}> with {confidence}% confidence")
    print()

print("-- PART 3: BRAIN REGION QUANTUM STATES --\n")
print("Modeling different brain regions as quantum systems\n")

brain_regions = [
    {
        "name": "Prefrontal Cortex",
        "function": "Decision making and planning",
        "qubits": 3,
        "complexity": 0.9,
        "disease_risk": "Schizophrenia, ADHD"
    },
    {
        "name": "Hippocampus",
        "function": "Memory formation and storage",
        "qubits": 3,
        "complexity": 0.7,
        "disease_risk": "Alzheimer's disease"
    },
    {
        "name": "Amygdala",
        "function": "Emotion and fear processing",
        "qubits": 2,
        "complexity": 0.6,
        "disease_risk": "Anxiety, PTSD"
    },
    {
        "name": "Cerebellum",
        "function": "Motor control and coordination",
        "qubits": 2,
        "complexity": 0.5,
        "disease_risk": "Ataxia, tremors"
    }
]

for region in brain_regions:
    qc = QuantumCircuit(region["qubits"], region["qubits"])

    for i in range(region["qubits"]):
        qc.h(i)
        qc.ry(region["complexity"] * np.pi, i)

    for i in range(region["qubits"]-1):
        qc.cx(i, i+1)

    qc.measure_all()

    job = simulator.run(qc, shots=100)
    counts = job.result().get_counts()

    active_states = sum(v for k,v in counts.items() if "1" in k)
    activity = "HIGH" if active_states > 60 else "NORMAL" if active_states > 30 else "LOW"

    print(f"  Region:   {region['name']}")
    print(f"  Function: {region['function']}")
    print(f"  Activity: {activity} ({active_states}%)")
    print(f"  Risk:     {region['disease_risk']}")
    print()

print("-- PART 4: SYNTHETIC BIOMARKER DEMO --\n")
print("Toy demo: synthetic biomarker values, not real patient data\n")

patients = [
    ("Patient A", 0.9, 0.8, "HIGH RISK"),
    ("Patient B", 0.3, 0.2, "LOW RISK"),
    ("Patient C", 0.7, 0.6, "MODERATE RISK"),
    ("Patient D", 0.95, 0.9, "HIGH RISK"),
]
for patient, tau_level, amyloid_level, expected in patients:
    qc = QuantumCircuit(2, 2)
    qc.ry(tau_level * np.pi, 0)
    qc.ry(amyloid_level * np.pi, 1)
    qc.measure([0,1],[0,1])

    job = simulator.run(qc, shots=1000)
    counts = job.result().get_counts()

    risk_signal = counts.get("11", 0) / 1000
    risk = "HIGH RISK" if risk_signal > 0.75 else \
           "MODERATE RISK" if risk_signal > 0.25 else "LOW RISK"

    match = "CORRECT" if risk.split()[0] == expected.split()[0] else "REVIEW"

    print(f"  {patient}")
    print(f"  Tau protein:    {tau_level*100:.0f}% elevated")
    print(f"  Amyloid beta:   {amyloid_level*100:.0f}% elevated")
    print(f"  Quantum result: {risk}")
    print(f"  Accuracy:       [{match}]\n")

print("-- SUMMARY --")
print(f"  Quantum neurons simulated:  {len(neuron_inputs)}")
print(f"  Brain regions modeled:      {len(brain_regions)}")
print(f"  Patients analyzed:          {len(patients)}")
print(f"  Neural network layers:      {len(layers)}")
print()
print("  Note: this is a classical simulation with synthetic toy data.")
print("  No speedup is measured and no medical conclusions are drawn.")
