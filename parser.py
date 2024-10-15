import argparse

from compute import compute_lev, compute_tr, compute_rr

PARSER_ARGS = [
    (
        ["-l", "-lev"],
        2,
        str,
        ("ELEM", "N_ELEC"),
        "compute atomic level structure",
        compute_lev,
    ),
    (
        ["-tr"],
        2,
        str,
        ("ELEM", "N_ELEC"),
        "compute atomic transition rates",
        compute_tr,
    ),
    (
        ["-rr"],
        2,
        str,
        ("ELEM", "N_ELEC"),
        "compute atomic RR and PI cross-section",
        compute_rr,
    ),
]


def get_facof_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="FACOF v(1.0.0)",
        description="FAC on terminal framework.",
    )

    for args in PARSER_ARGS:
        flag, nargs, type, metavar, help, _ = args
        parser.add_argument(
            *flag,
            nargs=nargs,
            type=type,
            metavar=metavar,
            help=help
        )

    return parser
