import os
import numpy as np
import pandas as pd
import shutil

def split4drp(
    patients: list, 
    drugs: list, 
    response: list, 
    split_type: str, 
    output_path: str,
    folds: int = 5,
    seed: int = 42,
    val_proportion: float = 0.2
) -> None:
    """
    Splits the drug response prediction (DRP) dataset into cross-validation folds 
    based on the specified strategy.

    Options for split_type:
      - 'random': Randomly splits the dataset.
      - 'cancer-blind': All samples from the same patient (or cancer type) are kept together.
      - 'drug-blind': All samples from the same drug are kept together.
      - 'completely-blind': Ensures that neither patients nor drugs in the test set appear in the training set.

    For each fold, three files are created:
       - drugcell_train.txt
       - drugcell_test.txt
       - drugcell_validate.txt

    The validation split is performed proportionally using a cumulative frequency 
    approach (for grouped splits) or a simple random proportion (for the random split).
    By default, approximately 20% of the training set is used for validation.

    :param patients: List of patient identifiers or feature representations.
    :param drugs: List of drug identifiers or feature representations.
    :param response: List of drug response values.
    :param split_type: Strategy for splitting the dataset.
    :param output_path: Path where the generated dataset splits will be saved.
    :param folds: Number of folds for cross-validation (default 5).
    :param seed: Random seed (optional).
    :param val_proportion: Fraction of training data used for validation (default 0.2).
    :return: None. The function saves the split datasets to disk.
    """
    if not (len(patients) == len(drugs) == len(response)):
        print("Warning: The lengths of the input lists (patients, drugs, response) are not the same.")
        return

    np.random.seed(seed)

    # Create the full DataFrame.
    data = pd.DataFrame({
        'patient': patients,
        'drug': drugs,
        'response': response
    })

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # -------------------------------------------------------------------
    def split_train_validate_proportional(train_data: pd.DataFrame, col: str, num_val_groups: int):
        """
        Splits the training data into new training and validation sets proportionally,
        grouping by the specified column.
        """
        counts = train_data[col].value_counts()
        items = list(counts.to_dict().items())  # list of (value, frequency) pairs
        np.random.shuffle(items)  # randomize the order
        total = sum(freq for _, freq in items)
        target = round(total / num_val_groups)
        groups = {}
        current_group = 0
        cumulative = 0
        for val, freq in items:
            groups[val] = current_group
            cumulative += freq
            if cumulative >= (current_group + 1) * target and current_group < num_val_groups - 1:
                current_group += 1
        # Use group 0 for validation.
        val_values = [val for val, grp in groups.items() if grp == 0]
        new_train = train_data[~train_data[col].isin(val_values)]
        validate = train_data[train_data[col].isin(val_values)]
        return new_train, validate

    # -------------------------------------------------------------------
    def split_train_validate_random(train_data: pd.DataFrame, proportion: float):
        """
        Splits training data into new training and validation sets using a simple random proportion.
        """
        train_shuffled = train_data.sample(frac=1, random_state=seed)
        n_val = int(len(train_shuffled) * proportion)
        validate = train_shuffled.iloc[:n_val]
        new_train = train_shuffled.iloc[n_val:]
        return new_train, validate

    # -------------------------------------------------------------------
    def assign_groups_by_freq(data: pd.DataFrame, col: str, num_folds: int) -> list:
        """
        Assigns unique values in the specified column to num_folds groups, 
        aiming to balance the total number of samples in each fold.
        """
        freq = data[col].value_counts()
        unique_vals = list(freq.index)
        np.random.shuffle(unique_vals)
        total_samples = data.shape[0]
        target = total_samples / num_folds
        fold_groups = [[] for _ in range(num_folds)]
        cumulative = 0
        fold_index = 0
        for val in unique_vals:
            fold_groups[fold_index].append(val)
            cumulative += freq[val]
            if cumulative >= (fold_index + 1) * target and fold_index < num_folds - 1:
                fold_index += 1
        return fold_groups

    # -------------------------------------------------------------------
    if split_type == 'random':
        # Random split: shuffle the entire dataset and divide into folds.
        shuffled_data = data.sample(frac=1, random_state=seed).reset_index(drop=True)
        groups = np.array_split(shuffled_data, folds)

        for i in range(folds):
            print(f"Creating fold number: {i+1} - test group: {i+1} - train groups: {list(range(1, folds+1))}")
            test = groups[i]
            train_data = pd.concat([groups[j] for j in range(folds) if j != i])
            new_train, validate = split_train_validate_random(train_data, proportion=val_proportion)

            fold_folder = os.path.join(output_path, f"samples{str(i+1)}")
            if not os.path.exists(fold_folder):
                os.makedirs(fold_folder)

            new_train.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
            test.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
            validate.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

        # Save all samples.
        all_samples_folder = os.path.join(output_path, "allsamples")
        if not os.path.exists(all_samples_folder):
            os.makedirs(all_samples_folder)
        shuffled_data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
        shuffled_data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
        shuffled_data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

    elif split_type == 'cancer-blind':
        # Cancer-blind: all samples from the same patient remain together.
        fold_groups = assign_groups_by_freq(data, 'patient', folds)
        num_val_groups = int(round(1 / val_proportion))
        for i in range(folds):
            print(f"Creating fold number: {i+1} - test group (patients): {fold_groups[i]}")
            test = data[data['patient'].isin(fold_groups[i])]
            train_data = data[~data['patient'].isin(fold_groups[i])]
            new_train, validate = split_train_validate_proportional(train_data, 'patient', num_val_groups)

            fold_folder = os.path.join(output_path, f"samples{str(i+1)}")
            if not os.path.exists(fold_folder):
                os.makedirs(fold_folder)

            new_train.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
            test.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
            validate.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

        all_samples_folder = os.path.join(output_path, "allsamples")
        if not os.path.exists(all_samples_folder):
            os.makedirs(all_samples_folder)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

    elif split_type == 'drug-blind':
        # Drug-blind: all samples from the same drug remain together.
        fold_groups = assign_groups_by_freq(data, 'drug', folds)
        num_val_groups = int(round(1 / val_proportion))
        for i in range(folds):
            print(f"Creating fold number: {i+1} - test group (drugs): {fold_groups[i]}")
            test = data[data['drug'].isin(fold_groups[i])]
            train_data = data[~data['drug'].isin(fold_groups[i])]
            new_train, validate = split_train_validate_proportional(train_data, 'drug', num_val_groups)

            fold_folder = os.path.join(output_path, f"samples{str(i+1)}")
            if not os.path.exists(fold_folder):
                os.makedirs(fold_folder)

            new_train.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
            test.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
            validate.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

        all_samples_folder = os.path.join(output_path, "allsamples")
        if not os.path.exists(all_samples_folder):
            os.makedirs(all_samples_folder)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

    elif split_type == 'completely-blind':
        # Completely-blind: ensure that neither patients nor drugs in the test set appear in training.
        patient_groups = assign_groups_by_freq(data, 'patient', folds)
        drug_groups = assign_groups_by_freq(data, 'drug', folds)
        num_val_groups = int(round(1 / val_proportion))
        for i in range(folds):
            print(f"Creating fold number: {i+1} - test group (patients): {patient_groups[i]}, test group (drugs): {drug_groups[i]}")
            test = data[(data['patient'].isin(patient_groups[i])) & (data['drug'].isin(drug_groups[i]))]
            train_data = data[~(data['patient'].isin(patient_groups[i]) | data['drug'].isin(drug_groups[i]))]
            new_train, validate = split_train_validate_proportional(train_data, 'patient', num_val_groups)

            fold_folder = os.path.join(output_path, f"samples{str(i+1)}")
            if not os.path.exists(fold_folder):
                os.makedirs(fold_folder)

            new_train.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
            test.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
            validate.sample(frac=1, random_state=seed).to_csv(
                os.path.join(fold_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

        all_samples_folder = os.path.join(output_path, "allsamples")
        if not os.path.exists(all_samples_folder):
            os.makedirs(all_samples_folder)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_train.txt"), sep='\t', header=False, index=False)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_test.txt"), sep='\t', header=False, index=False)
        data.sample(frac=1, random_state=seed).to_csv(
            os.path.join(all_samples_folder, "drugcell_validate.txt"), sep='\t', header=False, index=False)

    else:
        print("Unsupported split_type. Options are: 'random', 'cancer-blind', 'drug-blind', 'completely-blind'.")
        return
