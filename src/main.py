# NOTE: Code is based off the following blog:
# https://towardsdatascience.com/building-your-own-quantum-circuits-in-python-e9031b548fa7

import qiskit as qk


from utils.runner import Runner

if __name__ == '__main__':
    # Instantioate runner class
    runner = Runner()

    # HACK: Only need to run this line once
    # runner.save_and_load_IBMQ_account()

    # Run experiment to get results of binary circuit
    runner.run_experiment()


    # TODO: Modualize this into the runner class
    
    '''
    `n` is the number of Qubits needed to 
    generate a a random number between
    0 and 2^n - 1
    '''
    n = 3

    '''
    Creating a Quantum Register with `n` Qubits and 
    `n` Classical Bits where n=3
    '''
    q = qk.QuantumRegister(n)
    c = qk.ClassicalRegister(n)
    circ = qk.QuantumCircuit(q, c)

    '''
    Applying a Hadamard Gate on the n Qubits
    to get a final bitstring of size n 
    The bitstring will be converted to a
    decimal number (integer) between 0 and 2^3 - 1 (7)
    '''
    for i in range(n):
        circ.h(q[i])
        
    circ.measure(q,c)

    # FIXME: IBMQFactory object has no attribute 'get_backend'
    # The backend simulator available to me
    backend = qk.IBMQ.get_backend('ibmqx4')

    rand_int = runner.rand_int()
    print(a)