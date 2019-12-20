import qiskit as qk

class Runner(object):
    def __init__(self):
        pass

    def run_experiment(self):
        # Qubit
        q = qk.QuantumRegister(2)

        # Classical bit
        c = qk.ClassicalRegister(2)

        # Creating ciruit
        circuit = qk.QuantumCircuit(q, c)

        # Hadamard Gate on first qubit
        circuit.h(q[0])

        # CNOT Gate on first and second qubit
        circuit.cx(q[0], q[1])
        # Measuring qubits
        circuit.measure(q, c)

        print(circuit)

        # Using Qiskit's Aer Qasm Simulator
        simulator = qk.BasicAer.get_backend('qasm_simulator')

        # Simulating circuit to get the result
        # NOTE: Runs simulation 1024 times by default, can change by
        # using parameter 'shots'.
        job = qk.execute(circuit, simulator)
        result = job.result()

        # Getting the aggregated results of the binary circuit
        counts = result.get_counts(circuit)
        print(counts)

    def save_and_load_IBMQ_account(self):
        # Saving IMBQ account
        qk.IBMQ.save_account('2758ea1d157065bb33fa677bd5e8c87f0cc19ad92c8d9ae1bef48c14ef59ae23f1200f45ac1d4f5f37fdaacdc79000c837cc4b9942e46ef61328e4352a8a72be')
        # qk.IBMQ.load_accounts()

    def rand_int(self):
        new_job = qk.execute(circ, backend, shots=1)
        
        # The output bitstring consists of 3 collapsed Qubits (bits)
        bitstring = new_job.results().get_counts()
        bitstring = list(bitstring.keys()[0])
        
        # Converting binary to Decimal integers
        random_integer = int(bitstring, 2)
        
        return random_integer