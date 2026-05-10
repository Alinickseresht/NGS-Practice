# qPCR ΔΔCt Analysis Script
# Author: Ali
# Purpose: Simple fold change calculation using the ΔΔCt method

def calculate_delta_ct(target_ct, reference_ct):
    """
    Calculate ΔCt value
    """
    return target_ct - reference_ct


def calculate_delta_delta_ct(sample_delta_ct, control_delta_ct):
    """
    Calculate ΔΔCt value
    """
    return sample_delta_ct - control_delta_ct


def calculate_fold_change(delta_delta_ct):
    """
    Calculate relative gene expression
    """
    return 2 ** (-delta_delta_ct)


def display_results(sample_name, delta_ct_value, ddct_value, fold_change):
    print("\n===== qPCR Analysis Result =====")
    print(f"Sample Name      : {sample_name}")
    print(f"ΔCt Value        : {round(delta_ct_value, 3)}")
    print(f"ΔΔCt Value       : {round(ddct_value, 3)}")
    print(f"Fold Change      : {round(fold_change, 3)}")
    print("================================\n")


# -------------------------------
# Example Data
# -------------------------------

sample_name = "Tumor_Sample_01"

# Ct values
sample_target_ct = 23.5
sample_reference_ct = 18.2

control_target_ct = 25.1
control_reference_ct = 18.0

# Step 1: Calculate ΔCt
sample_delta_ct = calculate_delta_ct(
    sample_target_ct,
    sample_reference_ct
)

control_delta_ct = calculate_delta_ct(
    control_target_ct,
    control_reference_ct
)

# Step 2: Calculate ΔΔCt
ddct = calculate_delta_delta_ct(
    sample_delta_ct,
    control_delta_ct
)

# Step 3: Calculate Fold Change
fold_change = calculate_fold_change(ddct)

# Step 4: Display Results
display_results(
    sample_name,
    sample_delta_ct,
    ddct,
    fold_change
)
