Vin = 12 # Input voltage
Vout = 9 # Output voltage
Iout = 1.56 # Output current (max)
Vf = 0.525 # Diode forward voltage
Vsat = 1.3 # Saturation voltage
f = 500e3 # Design switching frequency
Vripple = 0.02 # Peak to peak output ripple voltage

Ipk = 2 * Iout
print(f"Peak Current: Ipk = {Ipk} A")

Rsc = 0.3 / Ipk
print(f"Calculated Rsc = {Rsc} Ohms")
Rsc = 0.1
print(f"Selected Rsc = {Rsc} Ohms")

tontoff = (Vout + Vf) / (Vin - Vsat - Vout)
toff = (1 / f) / (tontoff + 1)
ton = (1 / f) - toff
print(f"Design ton = {1e6 * ton} us")

Ct = 4e-5 * ton
print(f"Calculated Ct = {1e12 * Ct} pF")
Ct = 68e-12
print(f"Selected Ct = {1e12 * Ct} pF")

ton = Ct / 4e-5
print(f"Resulting ton = {1e6 * ton} us")
toff = (1 / f) - ton

L = ton * (Vin - Vsat - Vout) / Ipk
print(f"Minimum Inductance L = {1e6 * L} uH")
L = 1e-6
print(f"Selected Inductance L = {1e6 * L} uH")

Co = Ipk / (8 * f * Vripple)
print(f"Calculated Co = {1e6 * Co} uF")

R2R1 = (Vout / 1.25) - 1
R1 = 1e3
print(f"Selected R1 = {1e-3 * R1} kOhms")
R2 = R1 * R2R1
print(f"Calcuated R2 = {1e-3 * R2} kOhms")
