import numpy as np
#вентиль x:
x_gate = np.array([[0, 1],
                       [1, 0]],
                      dtype=complex)

#вентиль y:
y_gate = np.array([[0, -1j],
                   [1j, 0]],
                  dtype=complex)

#вентиль z:
z_gate = np.array([[1, 0],
                   [0, -1]],
                  dtype=complex)

#вентиль H:
H_gate = 1 / np.sqrt(2) * np.array([[1, 1],
                                    [1, -1]],
                                   dtype=complex)

#вентиль SWAP:
swap_gate = np.array([[1, 0, 0, 0],
                          [0, 0, 1, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, 1]], dtype=complex)

print('первый кубит:')
a1 = complex(float(input('1 число, дейсв. часть: ')), float(input('1 число, мнимая часть: ')))
a2 = complex(float(input('2 число, дейсв. часть: ')), float(input('2 число, мнимая часть: ')))
qubit1 = np.array([a1, a2], dtype=complex)
result1 = np.dot(qubit1, x_gate)
print(qubit1)
print(result1)

print('второй кубит:')
b1 = complex(float(input('1 число, дейсв. часть: ')), float(input('1 число, мнимая часть: ')))
b2 = complex(float(input('2 число, дейсв. часть: ')), float(input('2 число, мнимая часть: ')))
qubit2 = np.array([b1, b2], dtype=complex)
print(qubit2)
print(np.dot(qubit2, y_gate))

print('третий кубит:')
c1 = complex(float(input('1 число, дейсв. часть: ')), float(input('1 число, мнимая часть: ')))
c2 = complex(float(input('2 число, дейсв. часть: ')), float(input('2 число, мнимая часть: ')))
qubit3 = np.array([c1, c2], dtype=complex)
print(qubit3)
print(np.dot(qubit3, z_gate))

print('четвертый кубит:')
d1 = complex(float(input('1 число, дейсв. часть: ')), float(input('1 число, мнимая часть: ')))
d2 = complex(float(input('2 число, дейсв. часть: ')), float(input('2 число, мнимая часть: ')))
qubit4 = np.array([d1, d2], dtype=complex)
print(qubit4)
print(np.dot(qubit4, H_gate))

print('пятый и шестой кубиты')
a1 = complex(float(input('1 число, дейсв. часть: ')), float(input('1 число, мнимая часть: ')))
a2 = complex(float(input('2 число, дейсв. часть: ')), float(input('2 число, мнимая часть: ')))
b1 = complex(float(input('3 число, дейсв. часть: ')), float(input('3 число, мнимая часть: ')))
b2 = complex(float(input('4 число, дейсв. часть: ')), float(input('4 число, мнимая часть: ')))
qubit = np.array([a1, a2], dtype=complex)  # Начальное состояние кубита |0>
qubit2 = np.array([b1, b2], dtype=complex)
print([a1, a2], [b1, b2])
print(np.kron(qubit, qubit2))
print(np.dot(np.kron(qubit, qubit2), swap_gate))
