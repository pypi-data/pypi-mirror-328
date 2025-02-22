import pandas as pd
import numpy as np
from Levenshtein import distance
from itertools import combinations
from typing import List, Dict, Tuple
import warnings
import seaborn as sns
import matplotlib.pyplot as plt
import os

def trim_sequence(seq: str, max_length: int = 9) -> str:
    """Trim sequence to specified maximum length."""
    return seq[:max_length] if len(seq) > max_length else seq

def are_sequences_similar(seq1: str, seq2: str, threshold: int = 1, max_length: int = 9) -> bool:
    """
    Compare two sequences using Levenshtein distance after trimming.

    Args:
        seq1: First sequence
        seq2: Second sequence
        threshold: Maximum allowed Levenshtein distance (default: 1)
        max_length: Maximum sequence length to consider (default: 9)

    Returns:
        bool: True if sequences are similar within threshold
    """
    seq1_trimmed = trim_sequence(seq1, max_length)
    seq2_trimmed = trim_sequence(seq2, max_length)
    return distance(seq1_trimmed, seq2_trimmed) <= threshold

def compare_prediction_sets(preds1: List[str], preds2: List[str],
                          threshold: int = 1, max_length: int = 9) -> bool:
    """
    Compare two sets of predictions for similarity.
    Returns True if any prediction from set1 is similar to any prediction from set2.

    Args:
        preds1: First set of predictions
        preds2: Second set of predictions
        threshold: Maximum allowed Levenshtein distance
        max_length: Maximum sequence length to consider

    Returns:
        bool: True if any predictions are similar
    """
    for p1 in preds1:
        for p2 in preds2:
            if are_sequences_similar(p1, p2, threshold, max_length):
                return True
    return False

def align_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Align two dataframes based on common TCRs.

    Args:
        df1: First dataframe
        df2: Second dataframe

    Returns:
        Tuple of aligned dataframes
    """
    # Get common TCRs
    common_tcrs = set(df1['tcr']).intersection(set(df2['tcr']))

    if not common_tcrs:
        raise ValueError("No common TCRs found between the files")

    # Filter both dataframes to only include common TCRs
    df1_aligned = df1[df1['tcr'].isin(common_tcrs)].copy()
    df2_aligned = df2[df2['tcr'].isin(common_tcrs)].copy()

    # Sort both dataframes by TCR sequence
    df1_aligned.sort_values('tcr', inplace=True)
    df2_aligned.sort_values('tcr', inplace=True)

    # Reset indices
    df1_aligned.reset_index(drop=True, inplace=True)
    df2_aligned.reset_index(drop=True, inplace=True)

    return df1_aligned, df2_aligned

def compare_tcr_predictions(file_paths: List[str], top_k: int = 3,
                          threshold: int = 1, max_length: int = 9) -> Dict[Tuple[str, str], Dict]:
    """
    Compare TCR predictions between multiple files.

    Args:
        file_paths: List of paths to CSV files containing TCR predictions
        top_k: Number of top predictions to consider (default: 3)
        threshold: Maximum allowed Levenshtein distance (default: 1)
        max_length: Maximum sequence length to consider (default: 9)

    Returns:
        Dict with file pairs as keys and dictionaries containing similarity scores and TCR counts
    """
    # Input validation
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    # Read all files
    dataframes = {}
    for file_path in file_paths:
        df = pd.read_csv(file_path)

        # Verify required columns exist
        required_cols = ['tcr'] + [f'pred_{i}' for i in range(top_k)]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns in {file_path}: {missing_cols}")

        dataframes[file_path] = df

    # Compare file pairs
    results = {}
    for (file1, file2) in combinations(file_paths, 2):
        df1 = dataframes[file1]
        df2 = dataframes[file2]

        # Align dataframes based on common TCRs
        df1_aligned, df2_aligned = align_dataframes(df1, df2)
        total_tcrs = len(df1_aligned)

        similar_count = 0
        for i in range(total_tcrs):
            preds1 = [df1_aligned[f'pred_{j}'].iloc[i] for j in range(top_k)]
            preds2 = [df2_aligned[f'pred_{j}'].iloc[i] for j in range(top_k)]

            if compare_prediction_sets(preds1, preds2, threshold, max_length):
                similar_count += 1

        similarity_score = similar_count / total_tcrs
        results[(file1, file2)] = {
            'similarity_score': similarity_score,
            'common_tcrs': total_tcrs,
            'total_tcrs_file1': len(df1),
            'total_tcrs_file2': len(df2)
        }

    return results

def get_child_node_name(file_path: str) -> str:
    """
    Extract the child node name from the file path.
    Assumes the child node name is the file name without extension.
    """
    return os.path.splitext(os.path.basename(file_path))[0]

def create_similarity_heatmap(results: Dict[Tuple[str, str], Dict],
                            file_paths: List[str],
                            output_path: str = "similarity_heatmap.png") -> None:
    """
    Create and save a heatmap visualization of the pairwise similarities.
    """
    # Get child node names for labels
    labels = [get_child_node_name(f) for f in file_paths]
    n = len(labels)

    # Create similarity matrix
    similarity_matrix = np.ones((n, n))
    for (file1, file2), result in results.items():
        i = file_paths.index(file1)
        j = file_paths.index(file2)
        similarity_matrix[i, j] = result['similarity_score']
        similarity_matrix[j, i] = result['similarity_score']

    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(similarity_matrix,
                annot=True,
                fmt='.2%',
                cmap='YlOrRd',
                xticklabels=labels,
                yticklabels=labels,
                vmin=0,
                vmax=1)

    plt.title('Pairwise TCR Prediction Similarity')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"Heatmap saved as: {output_path}")

def print_comparison_results(results: Dict[Tuple[str, str], Dict]) -> None:
    """
    Print comparison results in a readable format.
    """
    print("\nPairwise Comparison Results:")
    print("-" * 80)
    for (file1, file2), result in results.items():
        print(f"Files: {get_child_node_name(file1)} vs {get_child_node_name(file2)}")
        print(f"Similarity Score: {result['similarity_score']:.2%}")
        print(f"Common TCRs: {result['common_tcrs']}")
        print(f"Total TCRs in {get_child_node_name(file1)}: {result['total_tcrs_file1']}")
        print(f"Total TCRs in {get_child_node_name(file2)}: {result['total_tcrs_file2']}")
        print("-" * 80)


if __name__ == "__main__":
    # Example file paths
    files = [
        "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu/wu_formatted_small_0.csv",
        "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu_new_code_ckpt_3/wu_formatted_small_ckpt_3_new_code_0.csv",
        "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu_new_code_ckpt_4/wu_formatted_small_ckpt_4_new_code_0.csv",
        "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu_new_code_ckpt_5/wu_formatted_small_ckpt_5_new_code_0.csv",
        # "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/random/random_predictions.csv"
        # "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu_new_code/wu_formatted_small_new_code_2.csv",
        # "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu_new_code/wu_formatted_small_new_code_3.csv",
        # "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen/predictions/250208_example_run/cancer_wu_new_code/wu_formatted_small_new_code_4.csv",
    ]

    # Compare files with top 3 predictions
    results = compare_tcr_predictions(files, top_k=8)

    # Print results and create heatmap
    print_comparison_results(results)
    create_similarity_heatmap(results, files, "similarity_heatmap.png")
