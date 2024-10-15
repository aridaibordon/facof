import itertools

from read import read_ion_data
from product import get_compatible_subshell_distributions


SPEC_NOT = "spdfghiklmnoqrtuvwxy"


def get_config_from_laviez(fac_susbhell: str) -> list[str]:
    n, nelec = (int(elem) for elem in fac_susbhell.split("*"))
    subshell_deg_list = [2 * (2 * l + 1) for l in range(n)]

    subshell_config = []
    for p in get_compatible_subshell_distributions(nelec, subshell_deg_list):
        subshell = ".".join(
            [f"{n}{SPEC_NOT[l]}{ocu}" for ocu, l in zip(p, range(n)) if ocu != 0]
        )
        subshell_config.append(subshell)

    return subshell_config


def get_config_from_nrel(fac_subshell: str):
    if not "[" in fac_subshell:
        return [fac_subshell]

    n = int(fac_subshell[: fac_subshell.index("[")])
    l_list = fac_subshell[fac_subshell.index("[") + 1 : fac_subshell.index("]")]
    nelec = int(fac_subshell[fac_subshell.index("]") + 1 :])

    max_ocu = [2 * (2 * SPEC_NOT.index(l) + 1) for l in l_list.split(",")]

    subshell_config = []
    for p in get_compatible_subshell_distributions(nelec, max_ocu):
        subshell = ".".join(
            [f"{n}{l}{ocu}" for ocu, l in zip(p, l_list.split(",")) if ocu != 0]
        )
        subshell_config.append(subshell)

    return subshell_config


def get_nrel_config_list(fac_state: str) -> list[str]:
    config = []
    for fac_subshell in fac_state.split():
        if "*" in fac_subshell:
            subshell_config = get_config_from_laviez(fac_subshell)

        else:
            subshell_config = get_config_from_nrel(fac_subshell)

        config.append(subshell_config)

    nrel_config_list = []
    for nrel_config in itertools.product(*config):
        nrel_config_list.append(".".join(nrel_config))

    return nrel_config_list


def get_ion_states_label_list(nion: int) -> list[str]:
    if nion == 0:
        # label for naked atom
        return ["naked"]

    ion_data = read_ion_data(nion)

    nrel_config_list = []
    for fac_state in ion_data:
        nrel_config = get_nrel_config_list(fac_state)
        nrel_config_list.extend(nrel_config)

    return nrel_config_list
