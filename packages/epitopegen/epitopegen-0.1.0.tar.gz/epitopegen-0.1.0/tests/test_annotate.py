import os
import numpy as np
import pandas as pd
from pathlib import Path
from multiprocessing import Pool, cpu_count
from itertools import combinations_with_replacement, combinations
from functools import partial
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_match_overlap(file1_path: str, file2_path: str, top_k: int = 1,
                         tcr_col: str = 'cdr3', total_population: int = None) -> dict:
    """
    Analyze overlap between matched TCRs in two files considering top K matches.
    A TCR is considered matched if any of its match_0 to match_{K-1} equals 1.

    Args:
        file1_path: Path to first CSV file
        file2_path: Path to second CSV file
        top_k: Number of top matches to consider
        tcr_col: Name of column containing TCR sequences
        total_population: Total size of TCR population (if None, uses length of input data)

    Returns:
        Dictionary containing overlap statistics
    """
    # Read CSVs and drop NA values in TCR column
    df1 = pd.read_csv(file1_path).dropna(subset=[tcr_col])
    df2 = pd.read_csv(file2_path).dropna(subset=[tcr_col])

    # Get total population size
    total_tcrs = total_population or len(df1)

    # Create masks for TCRs with matches in top K predictions
    match_cols = [f'match_{k}' for k in range(top_k)]
    df1_match_mask = df1[match_cols].eq(1).any(axis=1)
    df2_match_mask = df2[match_cols].eq(1).any(axis=1)

    # Get matched TCRs
    df1_matched = df1[df1_match_mask]
    df2_matched = df2[df2_match_mask]

    # Get unique TCRs and calculate overlap
    matched_tcrs_1 = set(df1_matched[tcr_col])
    matched_tcrs_2 = set(df2_matched[tcr_col])
    overlap = matched_tcrs_1 & matched_tcrs_2

    # Calculate expected random overlap
    size1, size2 = len(matched_tcrs_1), len(matched_tcrs_2)
    expected_matches = size1 * (size2 / total_tcrs)
    expected_overlap_pct = expected_matches / min(size1, size2) * 100 if min(size1, size2) > 0 else 0

    # Calculate actual overlap percentages
    overlap_pct_1 = (len(df1_matched[df1_matched[tcr_col].isin(overlap)]) / len(df1_matched)) * 100 if len(df1_matched) > 0 else 0
    overlap_pct_2 = (len(df2_matched[df2_matched[tcr_col].isin(overlap)]) / len(df2_matched)) * 100 if len(df2_matched) > 0 else 0

    # Print results
    print(f"\n*** Between {Path(file1_path).name} & {Path(file2_path).name} (top {top_k} matches)")
    print(f"- Total TCRs: {total_tcrs}")
    print(f"- Expected random overlap: {expected_overlap_pct:.2f}%")
    print(f"- File 1 matched TCRs: {size1}")
    print(f"- File 2 matched TCRs: {size2}")
    print(f"- Overlap percentage in File 1: {overlap_pct_1:.2f}%")
    print(f"- Overlap percentage in File 2: {overlap_pct_2:.2f}%")

    return {
        'file1': Path(file1_path).name,
        'file2': Path(file2_path).name,
        'total_tcrs': total_tcrs,
        'file1_matches': size1,
        'file2_matches': size2,
        'overlap_size': len(overlap),
        'overlap_pct_file1': overlap_pct_1,
        'overlap_pct_file2': overlap_pct_2,
        'expected_overlap_pct': expected_overlap_pct
    }

def merge_annotations(
    site_file: str,
    annotation_file: str,
    output_dir: str = "merged",
    randomize: bool = False,
    random_seed: int = 42
):
    """Merge site data with new annotations by matching TCR sequences.

    Args:
        site_file: Path to site_added.csv
        annotation_file: Path to annotation_ens_th0.5.csv
        output_dir: Directory to save output file
        randomize: Whether to randomize annotation matches
        random_seed: Seed for reproducible randomization
    """
    print("\n=== Starting Annotation Merge ===")
    print(f"• Mode: {'Randomized' if randomize else 'Normal'}")

    # Read input files
    print("• Reading input files...")
    site_df = pd.read_csv(site_file)
    annot_df = pd.read_csv(annotation_file)

    if randomize:
        print("• Randomizing annotation matches...")
        np.random.seed(random_seed)

        # Identify columns to shuffle
        match_cols = [col for col in annot_df.columns if any(x in col for x in ['match_', 'ref_epitope_', 'ref_protein_'])]

        # Group columns by their index (e.g., match_0, ref_epitope_0, ref_protein_0)
        col_groups = {}
        for col in match_cols:
            idx = col.split('_')[-1]
            if idx.isdigit():
                if idx not in col_groups:
                    col_groups[idx] = []
                col_groups[idx].append(col)

        # Shuffle each group of columns together
        for idx, cols in col_groups.items():
            shuffle_idx = np.random.permutation(len(annot_df))
            annot_df[cols] = annot_df[cols].iloc[shuffle_idx].values

    # Get columns to keep from site_df
    keep_cols = []
    drop_patterns = ['pred_', 'ref_epitope_', 'ref_protein_', 'match_']
    for col in site_df.columns:
        if not any(pattern in col for pattern in drop_patterns):
            keep_cols.append(col)

    # Create clean site dataframe
    print("• Removing old predictions and annotations...")
    site_clean = site_df[keep_cols].copy()

    # Rename columns for merging
    annot_df = annot_df.rename(columns={'tcr': 'cdr3'})

    # Merge dataframes
    print("• Merging with new annotations...")
    merged_df = site_clean.merge(annot_df, on='cdr3', how='left')

    # Create output directory
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Generate output filename
    site_stem = Path(site_file).stem
    annot_stem = Path(annotation_file).stem
    random_suffix = "_randomized" if randomize else ""
    output_file = output_dir / f"{site_stem}_merged_{annot_stem}{random_suffix}.csv"

    # Save merged file
    merged_df.to_csv(output_file, index=False)

    # Print statistics
    print("\n=== Merge Summary ===")
    print(f"• Total cells in site file: {len(site_df)}")
    print(f"• Total TCRs in annotation file: {len(annot_df)}")
    print(f"• Cells matched with annotations: {merged_df['pred_0'].notna().sum()}")
    print(f"• Cells without matches: {merged_df['pred_0'].isna().sum()}")

    # Print match statistics
    match_cols = [col for col in merged_df.columns if col.startswith('match_')]
    for k in range(min(4, len(match_cols))):  # Show first 4 positions
        matches = merged_df[f'match_{k}'].sum()
        total = merged_df[f'match_{k}'].notna().sum()
        if total > 0:
            print(f"• Match rate at k={k}: {matches/total*100:.1f}%")

    print(f"\n• Results saved to: {output_file}")
    print("===========================")

    return merged_df


def check_PA_same(path1: str, path2: str):
    """Compare match patterns between two annotation files.

    Args:
        path1: Path to first annotation file
        path2: Path to second annotation file
    """
    print("\n=== Comparing Match Patterns ===")
    print(f"File 1: {Path(path1).name}")
    print(f"File 2: {Path(path2).name}")

    # Read files
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)

    # Identify match columns present in both files
    match_cols = [col for col in df1.columns if col.startswith('match_') and col in df2.columns]
    match_cols.sort()  # Ensure ordered comparison
    # for col in match_cols:
    #     df1 = df1[df1[col].notna()]
    #     df2 = df2[df2[col].notna()]

    print(f"\nAnalyzing {len(match_cols)} match columns...")
    # Compare each match column
    for col in match_cols:
        # Basic equality check
        exact_matches = (df1[col] == df2[col]).sum()
        total_rows = len(df1)
        match_rate = (exact_matches / total_rows) * 100

        # Detailed pattern analysis
        pattern = {
            '0->0': ((df1[col] == 0) & (df2[col] == 0)).sum(),
            '0->1': ((df1[col] == 0) & (df2[col] == 1)).sum(),
            '1->0': ((df1[col] == 1) & (df2[col] == 0)).sum(),
            '1->1': ((df1[col] == 1) & (df2[col] == 1)).sum()
        }

        # Calculate positive rates
        pos_rate1 = (df1[col] == 1).mean() * 100
        pos_rate2 = (df2[col] == 1).mean() * 100

        print(f"\n• {col}:")
        print(f"  - Match rate: {match_rate:.1f}% ({exact_matches:,}/{total_rows:,} entries)")
        print(f"  - Positive rate in File 1: {pos_rate1:.1f}%")
        print(f"  - Positive rate in File 2: {pos_rate2:.1f}%")
        print("  - Transition patterns:")
        print(f"    * 0->0: {pattern['0->0']:,} entries")
        print(f"    * 0->1: {pattern['0->1']:,} entries")
        print(f"    * 1->0: {pattern['1->0']:,} entries")
        print(f"    * 1->1: {pattern['1->1']:,} entries")

    # Compare cumulative matches
    print("\n• Cumulative match comparison:")
    for k in range(len(match_cols)):
        cols_to_k = [f'match_{i}' for i in range(k + 1)]
        cum_match1 = df1[cols_to_k].any(axis=1).mean() * 100
        cum_match2 = df2[cols_to_k].any(axis=1).mean() * 100

        print(f"  - Up to k={k}:")
        print(f"    * File 1: {cum_match1:.1f}% positive")
        print(f"    * File 2: {cum_match2:.1f}% positive")
        print(f"    * Difference: {abs(cum_match1 - cum_match2):.1f}%")

    print("===========================")


def analyze_pair(args, top_k=1):
    """
    Helper function to analyze a single pair of files.

    Args:
        args (tuple): Tuple containing (file1_path, file2_path)
        top_k (int): Number of top matches to consider
    """
    try:
        file1_path, file2_path = args
        result = analyze_match_overlap(file1_path, file2_path, top_k=top_k, tcr_col='tcr')
        overlap_value = (result['overlap_pct_file1'] + result['overlap_pct_file2']) / 2
        return (Path(file1_path).parts[-1],
                Path(file2_path).parts[-1],
                overlap_value)
    except Exception as e:
        print(f"Error processing {file1_path} and {file2_path}: {str(e)}")
        return None

def visualize_match_overlaps_parallel(files_list, outdir, top_k=1, n_processes=None):
    """
    Generate a heatmap of match overlaps between all pairs of files using multiprocessing.

    Args:
        files_list (list): List of file paths to analyze
        outdir (str): Output directory for saving the visualization
        top_k (int): Number of top matches to consider (default: 1)
        n_processes (int): Number of processes to use (default: None, uses CPU count - 1)
    """
    # Create output directory if it doesn't exist
    os.makedirs(outdir, exist_ok=True)

    # Determine number of processes
    if n_processes is None:
        n_processes = max(1, cpu_count() - 1)  # Leave one CPU free

    # Generate all pairs of files
    file_pairs = list(combinations_with_replacement(files_list, 2))

    # Create partial function with fixed top_k
    analyze_pair_fixed = partial(analyze_pair, top_k=top_k)

    # Process pairs in parallel
    print(f"Starting parallel processing with {n_processes} processes...")
    with Pool(processes=n_processes) as pool:
        results = pool.map(analyze_pair_fixed, file_pairs)

    # Filter out any failed results
    results = [r for r in results if r is not None]

    # Initialize empty matrix
    file_names = [Path(f).parts[-1] for f in files_list]

    # Initialize matrix with float type instead of default
    overlap_matrix = pd.DataFrame(0.0, index=file_names, columns=file_names)

    # Fill matrix with explicit type conversion
    for file1, file2, value in results:
        overlap_matrix.loc[file1, file2] = float(value)
        overlap_matrix.loc[file2, file1] = float(value)

    # Create heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(overlap_matrix,
                annot=True,
                cmap='YlOrRd',
                square=True,
                cbar_kws={'label': 'Overlap %'})

    plt.title(f'TCR Match Overlap Percentages (top_{top_k})')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)

    # Adjust layout to prevent label cutoff
    plt.tight_layout()

    # Save plot
    output_path = os.path.join(outdir, f'match_overlap_heatmap_top{top_k}.pdf')
    plt.savefig(output_path)
    plt.close()

    print(f"Heatmap saved to: {output_path}")

    return overlap_matrix, file_names


def find_best_triplets(similarity_matrix: np.ndarray, file_names: list, k: int = 5) -> list:
    """
    Find the top K triplets of models with highest agreement based on similarity matrix.

    Parameters:
    -----------
    similarity_matrix : np.ndarray
        NxN matrix where each element [i,j] represents similarity between models i and j
    file_names : list
        List of model names corresponding to the similarity matrix indices
    k : int, optional
        Number of top triplets to return (default: 5)

    Returns:
    --------
    list
        List of tuples, each containing (triplet_score, (model1, model2, model3))
        ordered by score from highest to lowest
    """
    n = len(file_names)
    if n != similarity_matrix.shape[0] or n != similarity_matrix.shape[1]:
        raise ValueError("Number of file names must match similarity matrix dimensions")

    # Get all possible triplet combinations
    triplet_indices = list(combinations(range(n), 3))

    # Store results as (score, (model1, model2, model3))
    triplet_scores = []

    for i, j, k in triplet_indices:
        # Get the three pairwise similarities for this triplet
        sim_ij = similarity_matrix[i, j]
        sim_ik = similarity_matrix[i, k]
        sim_jk = similarity_matrix[j, k]

        # Calculate aggregate score for the triplet
        # We use the minimum similarity as it represents the worst agreement in the triplet
        # You could also use mean or other aggregation methods
        triplet_score = min(sim_ij, sim_ik, sim_jk)

        # Store the score and model names
        triplet = (file_names[i], file_names[j], file_names[k])
        triplet_scores.append((triplet_score, triplet))

    # Sort by score in descending order
    triplet_scores.sort(reverse=True)

    # Return top K triplets
    return triplet_scores[:k]

def analyze_triplets(triplet_results: list, similarity_matrix: np.ndarray, file_names: list, log_file: str = None):
    """
    Analyze selected triplets and optionally save to a log file.

    Parameters:
    -----------
    triplet_results : list
        Output from find_best_triplets function
    similarity_matrix : np.ndarray
        Original similarity matrix
    file_names : list
        List of model names
    log_file : str, optional
        Path to save the analysis log (default: None)
    """
    # Prepare the analysis text
    analysis_lines = []
    analysis_lines.append("Detailed Triplet Analysis:")
    analysis_lines.append("-" * 80)
    for rank, (score, triplet) in enumerate(triplet_results, 1):
        analysis_lines.append(f"\nRank {rank}:")
        analysis_lines.append(f"Models: {triplet}")
        analysis_lines.append(f"Minimum similarity score: {score:.3f}")

        # Get indices for detailed similarity analysis
        indices = [file_names.index(model) for model in triplet]
        i, j, k = indices

        # Add all pairwise similarities
        analysis_lines.append("Pairwise similarities:")
        analysis_lines.append(f"  {triplet[0]} - {triplet[1]}: {similarity_matrix[i,j]:.3f}")
        analysis_lines.append(f"  {triplet[0]} - {triplet[2]}: {similarity_matrix[i,k]:.3f}")
        analysis_lines.append(f"  {triplet[1]} - {triplet[2]}: {similarity_matrix[j,k]:.3f}")

        # Calculate mean similarity for this triplet
        mean_sim = (similarity_matrix[i,j] + similarity_matrix[i,k] + similarity_matrix[j,k]) / 3
        analysis_lines.append(f"Mean similarity: {mean_sim:.3f}")

    # Join all lines with newlines
    analysis_text = '\n'.join(analysis_lines)

    # Print to console
    print(analysis_text)

    # Save to log file if specified
    if log_file:
        with open(log_file, 'w') as f:
            f.write(analysis_text)


if __name__ == "__main__":
    root = "/ubc/cs/research/beaver/projects/minukma/Research/clean_code/EpiGen"
    # analyze_match_overlap(
    #     file1_path=f"{root}/results/old_predictions_with_new_code/annotation_ckpt_3.csv",
    #     file2_path=f"{root}/results/old_predictions_with_new_code/annotation_ckpt_4.csv",
    #     top_k=4,
    #     tcr_col="tcr"
    # )

    ### Merge old code's annotation to cancer_wu site_added.csv
    for idx in [1, 2, 3, 4, 5]:
        desc = "attn"
        merged_df = merge_annotations(
            # site_file=f"{root}/predictions/250209_validate_new_codes/old_predictions/241107_GPT2_principled_ACF_seed2025/cancer_wu/site_added.csv",
            # annotation_file=f"{root}/predictions/250209_validate_new_codes/old_predictions_annotated/substring/annotation_seed2025.csv",
            site_file=f"{root}/research/cancer_wu/predictions/241225_seed_models/ensemble_2023_2024_2025/site_added_th0.5.csv",
            annotation_file=f"{root}/predictions/250209_validate_new_codes/seed_models_inferred_{desc}_{idx}/annotation_ens_all_th0.5.csv",
            output_dir=f"{root}/predictions/250209_validate_new_codes/seed_models_inferred_{desc}_{idx}",
            randomize=False
        )

    # check_PA_same(
    #     # path1=f"{root}/predictions/250209_validate_new_codes/old_predictions_annotated/substring/site_added_merged_annotation_seed2024.csv",
    #     # path2=f"{root}/predictions/250209_validate_new_codes/old_predictions/241107_GPT2_principled_ACF_seed2024/cancer_wu/site_added.csv"
    #     path1=f"{root}/predictions/250209_validate_new_codes/old_predictions_annotated/substring/site_added_th0.5_merged_annotation_ens_th0.5.csv",
    #     path2=f"{root}/research/cancer_wu/predictions/241225_seed_models/ensemble_2023_2024_2025/site_added_th0.5.csv"
    # )

    # seeds = [42, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]
    # for k in [1, 2, 3, 4]:
    #     similarity_matrix, file_names = visualize_match_overlaps_parallel(
    #         files_list=[
    #             f"{root}/predictions/250209_validate_new_codes/seed_models_inferred_{idx}/annotation_ens_all_th0.5.csv" for idx in [1,2,3,4,5]
    #         ],
    #         outdir=f"{root}/predictions/250209_validate_new_codes/seed_models_inferred_1",
    #         top_k=k,
    #         n_processes=None
    #     )

    # similarity_matrix = np.array(similarity_matrix)

    # # Find top 5 triplets
    # best_triplets = find_best_triplets(similarity_matrix, file_names, k=5)

    # # Print detailed analysis
    # analyze_triplets(best_triplets, similarity_matrix, file_names, log_file="triplet_analysis.txt")
