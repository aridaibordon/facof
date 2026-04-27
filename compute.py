import os
from pfac import fac

from label import get_ion_states_config_list


def default_fname(elem: str, n_elec: int, uta: int) -> str:
    match uta:
        case 0:
            return f"{elem}_{n_elec:02}_DLA"
        case 1:
            return f"{elem}_{n_elec:02}_DCA"
        case _:
            raise Exception(f"{uta} is not a valid UTA flag.")


def add_levels_to_econfig(config_list: list[str]) -> None:
    for config, label in config_list:
        print(config, label)
        fac.Config(config, group=label)


def prepare_fac_setup(elem: str, uta_flag: 0 | 1, ci_flag: int):
    fac.Reinit(0)

    fac.SetAtom(elem)
    fac.SetCILevel(ci_flag)
    fac.SetUTA(uta_flag)


def compute_lev(elem: str, nelec: int, uta_flag: 0 | 1, ci_flag: int) -> None:
    config_list = get_ion_states_config_list(nelec)
    label_list = [label for _, label in config_list]

    prepare_fac_setup(elem, uta_flag, ci_flag)
    add_levels_to_econfig(config_list)

    fac.ConfigEnergy(0)
    fac.OptimizeRadial(label_list[0])
    fac.ConfigEnergy(1)

    fname = default_fname(elem, nelec, uta_flag)
    fpath = os.path.join(os.getcwd(), fname)

    fac.Structure(fpath + ".lev.b", label_list)
    fac.MemENTable(fpath + ".lev.b")
    fac.PrintTable(fpath + ".lev.b", fpath + ".lev", 1)


def compute_tr(elem: str, nelec: int, uta_flag: 0 | 1, ci_flag: int) -> None:
    config_list = get_ion_states_config_list(nelec)
    label_list = [label for _, label in config_list]

    prepare_fac_setup(elem, uta_flag, ci_flag)
    add_levels_to_econfig(config_list)

    fac.ConfigEnergy(0)
    fac.OptimizeRadial(label_list[0])
    fac.ConfigEnergy(1)

    fname = default_fname(elem, nelec, uta_flag)
    fpath = os.path.join(os.getcwd(), fname)

    fac.Structure(fpath + ".lev.b", label_list)
    fac.MemENTable(fpath + ".lev.b")
    fac.PrintTable(fpath + ".lev.b", fpath + ".lev", 1)

    fac.TransitionTable(fpath + ".tr.b", label_list, label_list)
    fac.PrintTable(fpath + ".tr.b", fpath + ".tr")


def compute_rr(elem: str, nelec: int, uta_flag: 0 | 1, ci_flag: int) -> None:
    upp_config_list = get_ion_states_config_list(nelec - 1)
    low_config_list = get_ion_states_config_list(nelec)

    upp_label_list = [label for _, label in upp_config_list]
    low_label_list = [label for _, label in low_config_list]

    prepare_fac_setup(elem, uta_flag, ci_flag)
    add_levels_to_econfig(upp_config_list)
    add_levels_to_econfig(low_config_list)

    fac.ConfigEnergy(0)
    fac.OptimizeRadial(low_label_list[0])
    fac.ConfigEnergy(1)

    fname = default_fname(elem, nelec, uta_flag)
    fpath = os.path.join(os.getcwd(), fname)

    fac.Structure(fpath + ".lev.b", upp_label_list)
    fac.Structure(fpath + ".lev.b", low_label_list)
    fac.MemENTable(fpath + ".lev.b")
    fac.PrintTable(fpath + ".lev.b", fpath + ".lev", 1)

    fac.RRTable(fpath + ".pi.b", low_label_list, upp_label_list)
    fac.PrintTable(fpath + ".pi.b", fpath + ".pi", 1)


def compute_ai(elem: str, nelec: int, uta_flag: 0 | 1, ci_flag: int) -> None:
    upp_config_list = get_ion_states_config_list(nelec - 1)
    low_config_list = get_ion_states_config_list(nelec)

    upp_label_list = [label for _, label in upp_config_list]
    low_label_list = [label for _, label in low_config_list]

    prepare_fac_setup(elem, uta_flag, ci_flag)
    add_levels_to_econfig(upp_config_list)
    add_levels_to_econfig(low_config_list)

    fac.ConfigEnergy(0)
    fac.OptimizeRadial(low_label_list[0])
    fac.ConfigEnergy(1)

    fname = default_fname(elem, nelec, uta_flag)
    fpath = os.path.join(os.getcwd(), fname)

    fac.ConfigEnergy(0)
    fac.OptimizeRadial(low_label_list[0])
    fac.ConfigEnergy(1)

    fac.Structure(fpath + ".lev.b", upp_label_list)
    fac.Structure(fpath + ".lev.b", low_label_list)
    fac.MemENTable(fpath + ".lev.b")
    # fac.PrintTable(fpath + ".lev.b", fpath + ".lev", 1)

    fac.AITable(fpath + ".ai.b", low_label_list, upp_label_list)
    fac.PrintTable(fpath + ".ai.b", fpath + ".ai", 1)
