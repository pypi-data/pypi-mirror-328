import pandas as pd
import synapseclient
import synapseutils

syn = synapseclient.login()

"""
Due to GEN-1458, we need to compare these curated BPC files against the main GENIE files
to see the difference in cpt_seq_date
"""

import synapseclient
import pandas as pd


def get_main_genie_clinical_sample_file(
    syn: synapseclient.Synapse, release: str, release_files_table_synid: str
) -> pd.DataFrame:
    """This retrieves the main genie clinical sample file from consortium release

    Args:
        release (str): release version to pull from for main genie
        release_files_table_synid (str): synapse id of the data relese files table
        from main genie

    Returns:
        pandas.DataFrame: the read in clinical file as dataframe
    """
    release_files = syn.tableQuery(
        f"SELECT * FROM {release_files_table_synid}"
    ).asDataFrame()

    import pdb

    pdb.set_trace()
    clinical_link_synid = release_files[
        (release_files["release"] == release)
        & (release_files["name"] == "data_clinical_sample.txt")
    ]["fileSynId"].values[0]
    clinical_link_ent = syn.get(clinical_link_synid)
    clinical_ent = syn.get(
        clinical_link_ent["linksTo"]["targetId"],
        version=clinical_link_ent["linksTo"]["targetVersionNumber"],
    )
    clinical_df = pd.read_csv(clinical_ent.path, sep="\t")
    assert (
        not clinical_df.empty
    ), f"Clinical file pulled from {clinical_link_synid} link is empty."
    assert set(["SAMPLE_ID", "SEQ_YEAR"]) < set(
        clinical_df.columns
    ), f"Clinical file pulled from {clinical_link_synid} link"
    "is missing expected columns: ['SAMPLE_ID', 'SEQ_YEAR']"
    return clinical_df


# read the project config file
import json

with open("/Users/rxu/Genie/config.json") as config_file:
    config = json.load(config_file)
get_main_genie_clinical_sample_file(
    syn,
    release=config["main_genie_release_version"],
    release_files_table_synid=config["main_genie_data_release_files"],
)


curated_files = {
    "NSCLC": "syn23285494",
    "CRC": "syn23285418",
    "BrCa": "syn23286608",
    "PANC": "syn24175803",
    "Prostate": "syn25610393",
    "BLADDER": "syn26721150",
    "NSCLC2": "syn51318735",
    "CRC2": "syn52943208",
    "RENAL": "syn59474241",
}

syn = synapseclient.login()


# Define a function to determine the year
def extract_year(date_str):
    if date_str[0].isdigit():
        # If the date starts with a number, extract the first part
        return int(date_str.split("-")[0])
    else:
        # If the date does not start with a number, extract the last part
        return int(date_str.split("-")[-1])


for cohort, syn_id in curated_files.items():
    print("Cohort:", cohort)
    export_file_entity = syn.get(syn_id)
    export_file_df = pd.read_csv(export_file_entity.path, low_memory=False)
    print("Total N Unique records:", export_file_df["record_id"].nunique())
    seq_date_df = export_file_df[
        ["record_id", "genie_patient_id", "cpt_genie_sample_id", "cpt_seq_date"]
    ]
    seq_date_df["cohort"] = cohort
    seq_date_df = seq_date_df[~seq_date_df["cpt_seq_date"].isnull()]

    # seq_date_df[seq_date_df['cpt_seq_date'].]
    seq_date_df["SEQ_YEAR"] = seq_date_df["cpt_seq_date"].apply(extract_year)

    print("N Unique Records with SEQ_DATE:", seq_date_df["record_id"].nunique())
    print("SEQ_DATE count for BPC input:")
    print(seq_date_df["SEQ_YEAR"].value_counts())

    sample_ent = syn.get("syn61211961", followLink=True)
    sample_df = pd.read_csv(sample_ent.path, low_memory=False, sep="\t", comment="#")
    sample_df["SEQ_YEAR"] = sample_df["SEQ_YEAR"].fillna(0).astype(int)
    compare_df = seq_date_df.merge(
        sample_df[["SAMPLE_ID", "SEQ_YEAR"]],
        right_on="SAMPLE_ID",
        left_on="cpt_genie_sample_id",
        how="left",
    )
    print(
        "Do all SEQ_YEAR match?",
        all(compare_df["SEQ_YEAR_x"] == compare_df["SEQ_YEAR_y"]),
    )
    import pdb

    pdb.set_trace()
    compare_df[compare_df["SEQ_YEAR_x"] != compare_df["SEQ_YEAR_y"]]
import pdb

pdb.set_trace()


CONSORTIUM_RELEASE_FOLDER = "syn61875143"
DATA_CLINICAL_FILE_ID = "syn9734573"
# Step 1. get list of all all SEQ_ASSAY_IDs in sample clinical file have gene panel data file
clinical_ent = syn.get(DATA_CLINICAL_FILE_ID)
clinical = pd.read_csv(clinical_ent.path, sep="\t", skiprows=4)
seq_assay_ids = list(clinical.SEQ_ASSAY_ID.unique())


# Step 2: List all gene panel files within my project
gene_panel_assay_ids = []
for directory_path, directory_names, file_name in synapseutils.walk(
    syn=syn, synId=CONSORTIUM_RELEASE_FOLDER, includeTypes=["file", "link"]
):
    for file in file_name:
        if file[0].startswith("data_gene_panel"):
            seq_assay_id = file[0].split("data_gene_panel_")[1].replace(".txt", "")
            gene_panel_assay_ids.append(seq_assay_id)
            print(f"File ({file[1]}): {directory_path[0]}/{file[0]}")

# Step 3: Make sure none missing
assert set(seq_assay_ids) == set(
    gene_panel_assay_ids
), "There are gene panels that are missing"


import pdb

pdb.set_trace()
# check dup variants in maf files
MAF_SYN_ID = "syn5571527"
maf_ent = syn.get(MAF_SYN_ID)
mutationDF = pd.read_csv(maf_ent.path, sep="\t")

# get centers with dups
primary_cols = [
    "Chromosome",
    "Start_Position",
    "Reference_Allele",
    "Tumor_Sample_Barcode",
    "Tumor_Seq_Allele2",
]
mutationDF[mutationDF.duplicated(primary_cols)].Center.unique()


# check if SNV variants annotated as DNP or ONP
# This is commonly `Variant_Type`, but it may differ depending on the MAF version
variant_type_column = "Variant_Type"

# Check for variants classified as DNP or ONP
dnp_onp_variants = mutationDF[mutationDF[variant_type_column].isin(["DNP", "ONP"])]

# Further filter to identify potential SNVs misclassified
# Assuming 'Reference_Allele' and 'Tumor_Seq_Allele2' contain the reference and variant sequence
potential_misclassified = dnp_onp_variants[
    (dnp_onp_variants["Reference_Allele"].apply(len) == 1)
    & (dnp_onp_variants["Tumor_Seq_Allele2"].apply(len) == 1)
]


mutationDF[
    (mutationDF["Reference_Allele"] == mutationDF["Tumor_Seq_Allele2"])
    & (mutationDF["Tumor_Seq_Allele2"] == mutationDF["Tumor_Seq_Allele1"])
]
