import os
import config
import wizard


from parser import PARSER_ARGS, get_facof_parser


def main() -> None:
    parser = get_facof_parser()
    args = vars(parser.parse_args())

    # run default wizard if not args are provided
    if not any(args.values()):
        wizard.main()

    # otherwise run flag specific command
    flag_cmd_dict = {key: arg[-1] for key, arg in zip(args, PARSER_ARGS)}
    for key in args:
        kargs = args.get(key, None)
        if not kargs:
            continue

        elem, nelec = kargs

        flag_cmd = flag_cmd_dict[key]
        flag_cmd(elem, int(nelec), config.uta_flag, config.ci_flag)


if __name__ == "__main__":
    main()
