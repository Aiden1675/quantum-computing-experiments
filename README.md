# Quantum Computing Experiments

Learning projects with Qiskit on a classical simulator.

## Scripts
- superposition_dna_demo.py: toy DNA, protein, drug and mutation circuits
- qubit_neuron_demo.py: toy quantum neurons and a synthetic biomarker demo
- pqc_threat_assessment.py: classical vs post-quantum algorithm table

## Limitations
- All data is synthetic or hardcoded. Nothing here is medical or diagnostic.
- No speedup over classical methods is measured or claimed.
- Mutation flags are hardcoded. The measured percentages do not decide them.
- The biomarker risk score is the chance of measuring 11 on two rotated qubits.
- PQC attack times and the 2030/2035 rows are illustrative, not predictions.
- The factoring demo is classical trial division, not Shor's algorithm.

## Setup
pip install qiskit qiskit-aer numpy

## Run
- python3 superposition_dna_demo.py
- python3 qubit_neuron_demo.py
- python3 pqc_threat_assessment.py
