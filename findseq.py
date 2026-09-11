import re
from pymol import cmd


AA3_TO_AA1 = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D",
    "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G",
    "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
    "MET": "M", "PHE": "F", "PRO": "P", "SER": "S",
    "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V",

    # Common modified residues
    "MSE": "M",
    "SEC": "U",
    "PYL": "O",

    # Nucleic Acids
    "A":"A",
    "C":"C",
    "G":"G",
    "T":"T",
    "U":"U"
}


def get_sequence(pymol_obj):
    model = cmd.get_model(pymol_obj)

    chains = {}
    seen = set()

    for atom in model.atom:

        key = (
            atom.chain,
            atom.resi,
            atom.resn,
        )

        if key in seen:
            continue

        seen.add(key)

        chain = atom.chain

        if chain not in chains:
            chains[chain] = {
                "sequence": [],
                "residues": [],
            }

        aa = AA3_TO_AA1.get(atom.resn.upper(), "X")

        chains[chain]["sequence"].append(aa)
        chains[chain]["residues"].append(atom.resi)

    for chain in chains:
        chains[chain]["sequence"] = "".join(
            chains[chain]["sequence"]
        )

    return chains


def findseq(pymol_obj, motif):

    cmd.delete("findseq_*")

    if not cmd.get_object_list(pymol_obj):
        print(f"findseq: object '{pymol_obj}' not found")
        return 0

    try:
        regex = re.compile(motif)
    except re.error as e:
        print(f"findseq: invalid regular expression: {e}")
        return 0

    chains = get_sequence(pymol_obj)

    match_number = 0

    for chain, data in chains.items():

        sequence = data["sequence"]
        residues = data["residues"]

        for match in regex.finditer(sequence):

            start = match.start()
            end = match.end()

            if start == end:
                continue

            matched_residues = residues[start:end]

            residue_selection = "+".join(
                str(resi) for resi in matched_residues
            )

            match_number += 1

            selection_name = f"findseq_{match_number}"

            selection = (
                f"({pymol_obj} and "
                f"chain {chain} and "
                f"resi {residue_selection})"
            )

            cmd.select(selection_name, selection)

            print(
                f"{selection_name}: "
                f"chain {chain}, "
                f"resi {matched_residues[0]}-{matched_residues[-1]}, "
                f"match '{match.group()}'"
            )

    print(f"findseq: {match_number} match(es) found")

    return match_number


cmd.extend("findseq", findseq)
cmd.findseq = findseq
