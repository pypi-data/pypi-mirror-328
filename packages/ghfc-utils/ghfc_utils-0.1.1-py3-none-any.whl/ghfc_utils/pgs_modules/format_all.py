import argparse
import os

from tqdm import tqdm

from . import format


def setup_args(subparsers: "argparse._SubParsersAction") -> None:
    """register arguments for this submodule of the argparse

    Args:
        subparsers (argparse._SubParsersAction): the subparsers to register into
    """
    subformat = subparsers.add_parser("format-all")
    subformat.add_argument(
        metavar="root",
        dest="root",
        help="collection of summaries to format",
        type=str,
    )
    subformat.add_argument(
        "--force", "-f", help="force the processing", action="store_true"
    )


def run(args):
    list_pgs = []
    # loop over all entity.yaml file in the args.root directory
    for root, _, files in os.walk(args.root):
        if "entity.yaml" in files:
            pgs_name = root[len(args.root) :]
            if pgs_name.startswith("/"):
                pgs_name = pgs_name[1:]
            list_pgs.append(pgs_name)
    list_pgs.sort()

    # with open(args.yaml, "r") as f:
    #     data = yaml.load(f, Loader=yaml.SafeLoader)

    # df = pd.DataFrame(data["summaries"])
    # write_dataframe_to_docx(df, args.yaml[:-5] + ".docx")

    for p in (pbar := tqdm(list_pgs, desc="processing summaries")):
        pbar.set_description("processing " + p)
        format.format(root=args.root, name=p, force=args.force)
