import argparse
import pathlib
from dataclasses import dataclass

from lnas import LnasFormat

from cfdmod.logger import logger
from cfdmod.use_cases.pressure.path_manager import CePathManager
from cfdmod.use_cases.pressure.shape.Ce_config import CeCaseConfig
from cfdmod.use_cases.pressure.shape.Ce_data import CeOutput, process_Ce
from cfdmod.utils import save_yaml


@dataclass
class ArgsModel:
    """Command line arguments for client app"""

    output: str
    cp: str
    mesh: str
    config: str


def get_args_process(args: list[str]) -> ArgsModel:
    """Get arguments model from list of command line args

    Args:
        args (List[str]): List of command line arguments passed

    Returns:
        ArgsModel: Arguments model for client app
    """
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--output",
        required=True,
        help="Output path for generated files",
        type=str,
    )
    ap.add_argument(
        "--cp",
        required=True,
        help="Path to body pressure coefficient series .hdf",
        type=str,
    )
    ap.add_argument(
        "--mesh",
        required=True,
        help="Path to LNAS normalized mesh file",
        type=str,
    )
    ap.add_argument(
        "--config",
        required=True,
        help="Path to config .yaml file",
        type=str,
    )
    parsed_args = ap.parse_args(args)
    args_model = ArgsModel(**vars(parsed_args))
    return args_model


def main(*args):
    args_use = get_args_process(*args)
    path_manager = CePathManager(output_path=pathlib.Path(args_use.output))

    cfg_path = pathlib.Path(args_use.config)
    mesh_path = pathlib.Path(args_use.mesh)
    cp_path = pathlib.Path(args_use.cp)

    post_proc_cfg = CeCaseConfig.from_file(cfg_path)

    logger.info("Reading mesh description...")
    mesh = LnasFormat.from_file(mesh_path)
    logger.info("Mesh description loaded successfully!")

    for cfg_label, cfg in post_proc_cfg.shape_coefficient.items():
        logger.info(f"Processing {cfg_label} ...")

        Ce_output: CeOutput = process_Ce(mesh=mesh, cfg=cfg, cp_path=cp_path)

        Ce_output.save_region_info(cfg_label=cfg_label, path_manager=path_manager)
        Ce_output.save_outputs(cfg_label=cfg_label, path_manager=path_manager)
        Ce_output.export_mesh(cfg_label=cfg_label, path_manager=path_manager)
        save_yaml(cfg.model_dump(), path_manager.get_config_path(cfg_lbl=cfg_label))

        logger.info(f"Processed {cfg_label}!")
