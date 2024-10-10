import os
import config

from pfac import fac


def default_fname(elem: str, n_elec: int, uta: int) -> str:
    match uta:
        case 0:
            return f"{elem}_{n_elec:02}_DLA"
        case 1:
            return f"{elem}_{n_elec:02}_DCA"
        case _:
            raise Exception(f"{uta} is not a valid UTA flag.")


def read_default_econfig(n_elec: int) -> list[str]:
    with open(os.path.join(config.ions_path, f"ion{n_elec}.dat")) as f:
        return [line.rstrip("\n") for line in f.readlines()]


def compute_lev(elem: str, nelec: int, uta_flag: 0 | 1, ci_flag: int) -> None:
    fac.Reinit(0)

    fac.SetAtom(elem)
    fac.SetCILevel(ci_flag)

    fac.SetUTA(uta_flag)

    e_config = read_default_econfig(nelec)

    glist = []
    for ind, config in enumerate(e_config):
        fac.Config(config, group=f"n{ind}")
        glist.append(f"n{ind}")

    fac.ConfigEnergy(0)
    fac.OptimizeRadial("n1")
    fac.ConfigEnergy(1)

    fname = default_fname(elem, nelec, uta_flag)
    fpath = os.path.join(os.getcwd(), fname)

    fac.Structure(fpath + ".lev.b", glist)
    fac.MemENTable(fpath + ".lev.b")
    fac.PrintTable(fpath + ".lev.b", fpath + ".lev", 1)


def compute_tr(elem: str, nelec: int, uta_flag: 0 | 1, ci_flag: int) -> None:
    fac.Reinit(0)

    fac.SetAtom(elem)
    fac.SetCILevel(ci_flag)

    fac.SetUTA(uta_flag)

    e_config = read_default_econfig(nelec)

    glist = []
    for ind, config in enumerate(e_config):
        fac.Config(config, group=f"n{ind}")
        glist.append(f"n{ind}")

    fac.ConfigEnergy(0)
    fac.OptimizeRadial("n1")
    fac.ConfigEnergy(1)

    fname = default_fname(elem, nelec, uta_flag)
    fpath = os.path.join(os.getcwd(), fname)

    fac.Structure(fpath + ".lev.b", glist)
    fac.MemENTable(fpath + ".lev.b")
    fac.PrintTable(fpath + ".lev.b", fpath + ".lev", 1)
    fac.TransitionTable(fpath + ".tr.b", glist, glist)
    fac.PrintTable(fpath + ".tr.b", fpath + ".tr")
