

# ΔΔCt calculation example

def delta_ct(target_ct, reference_ct):
    return target_ct - reference_ct

def delta_delta_ct(sample_delta_ct, control_delta_ct):
    return sample_delta_ct - control_delta_ct

sample = delta_ct(23.5, 18.2)
control = delta_ct(25.1, 18.0)

ddct = delta_delta_ct(sample, control)

fold_change = 2 ** (-ddct)

print("Fold Change:", round(fold_change, 3))
