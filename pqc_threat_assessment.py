import math
from datetime import datetime

print("== QUANTUM COMPUTING THREAT ANALYZER ==")
print("Post-Quantum Cryptography Assessment")
print(f"Time: {datetime.now()}\n")

algorithms = [
    {
        "name": "RSA-2048",
        "type": "Asymmetric",
        "classical_crack": "Billions of years",
        "quantum_crack": "Needs big quantum computer",
        "algorithm_used": "Shor's Algorithm",
        "status": "VULNERABLE",
        "used_for": "SSL/TLS, Email encryption",
        "replacement": "ML-KEM (Kyber) (NIST approved)"
    },
    {
        "name": "AES-256",
        "type": "Symmetric",
        "classical_crack": "Impossible",
        "quantum_crack": "Weakened - needs AES-512",
        "algorithm_used": "Grover's Algorithm",
        "status": "PARTIALLY SAFE",
        "used_for": "File encryption, VPNs",
        "replacement": "AES-256 with larger keys"
    },
    {
        "name": "SHA-256",
        "type": "Hashing",
        "classical_crack": "Impossible",
        "quantum_crack": "Weakened but still usable",
        "algorithm_used": "Grover's Algorithm",
        "status": "PARTIALLY SAFE",
        "used_for": "Password hashing, Blockchain",
        "replacement": "SHA-384 or SHA-512"
    },
    {
        "name": "ECC-256",
        "type": "Asymmetric",
        "classical_crack": "Billions of years",
        "quantum_crack": "Needs big quantum computer",
        "algorithm_used": "Shor's Algorithm",
        "status": "VULNERABLE",
        "used_for": "Bitcoin, mobile encryption",
        "replacement": "CRSTALS-Dilithim"
    },
    {
        "name": "Diffie-Hellman",
        "type": "Key Exchange",
        "classical_crack": "Very difficult",
        "quantum_crack": "Needs big quantum computer",
        "algorithm_used": "Shor's Algorithm",
        "status": "CRITICAL",
        "used_for": "HTTPS key exchange",
        "replacement": "ML-KEM (Kyber)"
    },
]

print("-- ENCRYPTION VULNERABILITY ASSESSMENT --\n")
for a in algorithms:
    tag = "[CRITICAL]" if a["status"] == "CRITICAL" else \
          "[VULNERABLE]" if a["status"] == "VULNERABLE" else \
          "[PARTIAL]"
    print(f"  {tag} {a['name']} ({a['type']})")
    print(f"  Classical crack:  {a['classical_crack']}")
    print(f"  Quantum crack:    {a['quantum_crack']}")
    print(f"  Quantum method:   {a['algorithm_used']}")
    print(f"  Used for:         {a['used_for']}")
    print(f"  Replace with:     {a['replacement']}")
    print()

print("--QUANTUM THREAT TIMELINE --\n")
timeline = [
    ("2024", "Current", "Quantum computers have ~1000 qubits - not yet threatening"),
    ("2027", "Near",    "Scenario only"),
    ("2030", "Medium",  "Scenario: Large-scale quantum computer threatens RSA and ECC"),
    ("2035", "Far",     "Scenario: broad exposure of public-key cryptography")
]

for year, term, desc in timeline:
    print(f"  {year} [{term:<7}] {desc}")

print("\n--CLASSICAL FACTORING DEMO --")
print("Classical demo, no quantum\n")

def factor(n):
    print(f"  Target number to factor: {n}")
    print(f"  Classical computer: Trail division")
    print(f"  Result:")

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print(f"  Found factors: {i} x {n//i} = {n}")
            print(f"  Toy number only")
            return i, n//i
    return None

result = factor(15)

print("\n-- GROVER'S ALGORITHM IMPACT --")
print("Shows how quantum weakens symmetric encryption\n")

key_sizes = [
    (128, 64,  "AES-128 reduced to 64-bit security"),
    (256, 128, "AES-256 reduced to 128-bit security"),
    (512, 256, "AES-512 would maintain 256-bit security")
]
for original, quantum, desc in key_sizes:
    print(f"  {original}-bit key -> {quantum}-bit quantum security")
    print(f"  {desc}\n")

print("-- NIST POST_QUANTUM STANDARDS (2024) --\n")
standards = [
    ("ML-KEM (Kyber)",     "Key Encapsulation", "Replaces RSA/ECC"),
    ("ML-DSA (Dilithium)", "Digital Signatures", "Replaces RSA signatures"),
    ("FALCON",             "Digital Signatures", "Compact signatures"),
    ("SLH-DSA (SPHINCS+)",           "Digital Signatures", "Hash based - most secure")
]

for name, use, desc in standards:
    print(f"  [APPROVED] {name}")
    print(f"             Use: {use}")
    print(f"             Why: {desc}\n")

print(f"""
-- RECOMMENDATIONS --

  Immediate actions:
  1. Inventory all encryption algorithms in use
  2. Identify systems using RSA or ECC
  3. Plan migration to NIST approved algorithms
  4. Implement crypto-agile architecture

  Timeline:
  - Start planning NOW
  - Begin migration now
  - NIST IR 8547 draft: deprecate after 2030, disallow after 2035
  - Reference: NIST IR 8547 (draft), FIPS 203/204/205

-- SUMMARY --
  Vulnerable algorithms:  {sum(1 for a in algorithms if a['status'] in ['VULNERABLE','CRITICAL'])}
  Safe algorithms:        {sum(1 for a in algorithms if a['status'] == 'PARTIALLY SAFE')}
  Action required:        URGENT PLANNING
""")

with open("quantum_report.txt","w") as f:
    f.write(f"Quantum Threat Report - {datetime.now()}\n")
    for a in algorithms:
        f.write(f"{a['name']}: {a['status']}\n")

print("[+] Report saved: quantum_report.txt")
