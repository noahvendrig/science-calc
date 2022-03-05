import math

x = 0

pi = math.pi

charge_electron = {'value': -1.602*10**-19, 'unit': 'C', 'type': 'constant'}
charge_proton = {'value': 1.602*10**-19, 'unit': 'C', 'type': 'constant'}
mass_electron = {'value': 9.109*10**-31, 'unit': 'kg', 'type': 'constant'}
mass_proton = {'value': 1.673*10**-27, 'unit': 'kg', 'type': 'constant'}
mass_neutron = {'value': 1.675*10**-27, 'unit': 'kg', 'type': 'constant'}
acceleration_gravity = {'value': 9.8, 'unit': 'm s^-2', 'type': 'constant'}
electric_permittivity = {'value': 8.854*10**-12, 'unit': 'A^2 s^4 kg^-1 m^-3', 'type': 'constant'}
magnetic_permeability = {'value': 4*pi*10**-7, 'unit': 'N A^-2', 'type': 'constant'}
gravitational_constant = {'value': 6.67*10**-11, 'unit': 'N m^2 kg^-2', 'type': 'constant'}
mass_earth = {'value': 6*10**24, 'unit': 'kg', 'type': 'constant'}
radius_earth = {'value': 6.371*10**6, 'unit': 'm', 'type': 'constant'}
speed_sound = {'value': 340, 'unit': 'm s^-1', 'type': 'constant'}

mass = {'value': f'{x}', 'unit': 'kg', 'type': 'variable'}
velocity = {'value': f'{x}', 'unit': 'm s^-1', 'type': 'variable'}
velocity_avg = {'value': f'{x}', 'unit': 'm s^-1', 'type': 'variable'}
acceleration = {'value': f'{x}', 'unit': 'm s^-2', 'type': 'variable'}
t = {'value': f'{x}', 'unit': 'degrees', 's': 'variable'}
displacement = {'value': f'{x}', 'unit': 'm', 'type': 'variable'}
radius = {'value': f'{x}', 'unit': 'm', 'type': 'variable'}
velocity_angular = {'value': f'{x}', 'rad s^-1': 'degrees', 'type': 'variable'}
energy_kinetic = {'value': f'{x}', 'unit': 'J', 'type': 'variable'}
energy_potential = {'value': f'{x}', 'unit': 'J', 'type': 'variable'}
force_net = {'value': f'{x}', 'unit': 'N', 'type': 'variable'}
force_centripetal = {'value': f'{x}', 'unit': 'N', 'type': 'variable'}
theta = {'value': f'{x}', 'unit': 'degrees', 'type': 'variable'}

