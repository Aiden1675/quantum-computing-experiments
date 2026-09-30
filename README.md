# Quantum Computing Experiments

Learning projects at the intersection of quantum computing and security, built in a home lab.

## Post-Quantum Cryptography Assessment

`pqc_threat_assessment.py` prints an educational assessment of how quantum computing affects common cryptography:

- A table of widely used algorithms with a hardcoded status (vulnerable or partially safe)
- How Grover's algorithm effectively halves symmetric key strength (for example, a 128-bit key gives roughly 64-bit quantum security)
- NIST's post-quantum standards: ML-KEM (FIPS 203, formerly Kyber), ML-DSA (FIPS 204, formerly Dilithium), SLH-DSA (FIPS 205, formerly SPHINCS+), and FALCON
- Recommended actions: inventory cryptography in use, find RSA and ECC, plan migration, build crypto-agility
- A timeline based on the NIST IR 8547 draft, which proposes deprecating RSA and elliptic-curve algorithms after 2030 and disallowing them after 2035
- A summary report saved as `quantum_report.txt`

### Usage

```bash
python3 pqc_threat_assessment.py
```

Uses only the Python standard library.

### Limitations

- The algorithm table and statuses are static, typed into the script. It does not scan real systems for the cryptography they use.
- Standard names and dates reflect NIST publications at the time of writing. IR 8547 is a draft, so check NIST for current status.
- It's a learning tool, not a migration planner or a compliance check.

## Planned

Qiskit simulator experiments (single-qubit measurement demos), once their write-ups are cleaned up.
