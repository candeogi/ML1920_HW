#perceptron hand made test

test with custom matrix
X_prova = np.array([
    [-2,2],
    [-2,-3],
    [2,-1],
    [1,-4],
    [2,2],
    [3,-1]
])
Y_prova = np.array([1,-1,+1,-1,+1,-1])
print(Y_prova)
X_permuted = X_prova[permutation]
print(permutation)
print(X_permuted)
w_found,training_error=perceptron(X_prova,Y_prova,100)
print('w_found: ',w_found)
print('training_error: ',training_error)