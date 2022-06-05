primes = [39839, 39983, 40127, 40499, 40739, 40787, 40823, 40883, 41387, 41507, 41519, 41543, 41579, 41759, 41843, 41879, 41927, 42023, 42179, 42299, 42359, 42443, 42683, 42767, 42839]
 
# indexes for the safe primes' list - can be randomized for testing
i0 = 1
i1 = 12
i2 = -1
 
# both the multiple of primes and their Euler's totient can be public,
# because there are 3 large prime factors to be identified in both, yet
# there are only two equations for the three unknown variables
mult_of_primes = primes[i0] * primes[i1] * primes[i2]
phi_of_primes = (primes[i0]-1) * (primes[i1]-1) * (primes[i2]-1)

# must work for it is odd, and smaller than any prime factor
encrypt0 = 8765
#encrypt0 = 7653 # uncomment or randomize for further testing!

# shouldn't work, because it is even, thus not coprime with Euler's totient,
# whose factors include the Sophie-German primes of the safe primes, and 8 
encrypt1 = 2578
#encrypt1 = 5782 # uncomment or randomize for further testing!

# FROM HERE THE COMPUTATIONS SHOULD BE KEPT SECRET

# inverting with help of Fermat's theorem: needs the knowlegde of the separate prime factors
phi_of_phi = 4 * ((primes[i0]-1)//2-1) * ((primes[i1]-1)//2-1) * ((primes[i2]-1)//2-1)
Fermat_exp = phi_of_phi-1

decrypt0 = pow(encrypt0, Fermat_exp, phi_of_primes) # calculate modular inverse
decrypt1 = pow(encrypt1, Fermat_exp, phi_of_primes) # calculate modular inverse

# test decryption of encryption at work
plain = 1234
print(' odd exponents work:', plain == pow(pow(plain, encrypt0, mult_of_primes), decrypt0, mult_of_primes))
print('even exponents work:', plain == pow(pow(plain, encrypt1, mult_of_primes), decrypt1, mult_of_primes))

plain = 2345
print(' odd exponents work:', plain == pow(pow(plain, encrypt0, mult_of_primes), decrypt0, mult_of_primes))
print('even exponents work:', plain == pow(pow(plain, encrypt1, mult_of_primes), decrypt1, mult_of_primes))

