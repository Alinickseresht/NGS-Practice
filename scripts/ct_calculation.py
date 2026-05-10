
# Simple ΔΔCt concept demonstration

def delta_ct(ct_target, ct_reference):
    return ct_target - ct_reference

def delta_delta_ct(sample, control):
    return sample - control

# Example values
sample = delta_ct(23, 18)
control = delta_ct(25, 18)

fold_change = 2 ** -(delta_delta_ct(sample, control))

print("Fold change:", fold_change)
