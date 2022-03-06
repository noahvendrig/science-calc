import math
from turtle import distance

x = 0

pi = math.pi

# Given Constants
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

# Motion, Forces, Gravity
mass = {'value': None, 'unit': 'kg', 'type': 'variable'}
velocity = {'value': None, 'unit': 'm s^-1', 'type': 'variable'}
velocity_avg = {'value': None, 'unit': 'm s^-1', 'type': 'variable'}
acceleration = {'value': None, 'unit': 'm s^-2', 'type': 'variable'}
t = {'value': None, 'unit': 'degrees', 's': 'variable'}
displacement = {'value': None, 'unit': 'm', 'type': 'variable'}
radius = {'value': None, 'unit': 'm', 'type': 'variable'}
velocity_angular = {'value': None, 'rad s^-1': 'degrees', 'type': 'variable'}
energy_kinetic = {'value': None, 'unit': 'J', 'type': 'variable'}
energy_potential = {'value': None, 'unit': 'J', 'type': 'variable'}
force_net = {'value': None, 'unit': 'N', 'type': 'variable'}
force_centripetal = {'value': None, 'unit': 'N', 'type': 'variable'}
theta = {'value': None, 'unit': 'degrees', 'type': 'variable'}

# Waves and Thermodynamics
frequency = {'value': None, 'unit': 'Hz', 'type': 'variable'}
period = {'value': None, 'unit': 's', 'type': 'variable'}

# Electricity and Magnetism
charge_1 = {'value': None, 'unit': 's', 'type': 'variable'}
charge_2 = {'value': None, 'unit': 's', 'type': 'variable'}
voltage = {'value': None, 'unit': 's', 'type': 'variable'}
work = {'value': None, 'unit': 's', 'type': 'variable'}
magnetic_flux_density = {'value': None, 'unit': 's', 'type': 'variable'}
current = {'value': None, 'unit': 's', 'type': 'variable'}
length = {'value': None, 'unit': 's', 'type': 'variable'}
number_turns = {'value': None, 'unit': 's', 'type': 'variable'}
torque = {'value': None, 'unit': 's', 'type': 'variable'}
electric_field_strength = {'value': None, 'unit': 's', 'type': 'variable'}
resistance = {'value': None, 'unit': 's', 'type': 'variable'}
power = {'value': None, 'unit': 's', 'type': 'variable'}
Area = {'value': None, 'unit': 's', 'type': 'variable'}



