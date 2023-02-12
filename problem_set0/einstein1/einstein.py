def mass_to_energy(mass):
    energy = mass * (3*10**8)**2
    return energy

input = int(input("What mass do you want to input?"))

print(mass_to_energy(input))

