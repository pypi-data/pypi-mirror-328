from .optimizer import optimize, best_variety, sowing_date_from_best_variety

import os, sys
from pathlib import Path
import click

os.environ["CMD_MODE"] = "1"
__version__ = "1.0.1"

@click.group()
@click.version_option(version=__version__, prog_name="optimal_sowingdate")
def cli():
    pass

@click.command("optim")
@click.argument("modelout")
@click.argument("resultpath")
@click.option("--start", default=10, help="Start date for optimization")
@click.option("--end", default=360, help="End date for optimization")
@click.option("--step", default=10, help="Step for optimization")
def cmd_optimize(modelout, resultpath, start=10, end=360, step=10):
    """Optimize sowing date for given model outputs.
    
    modelout: the path of the folder containing the model outputs
    resultpath: the path of the folder where sowing date netcdf files will be saved
    """
    optimize(modelout, resultpath, start, end, step)

@click.command("bestvar")
@click.argument("yieldfolder")
@click.argument("resultpath")
def cmd_optimvar(yieldfolder, resultpath):
    """Find the best cultivar from a list of cultivars.
    
    yieldfolder: the path of the folder containing the yield data for different cultivars
    resultpath: the path of the folder where the best cultivars netcdf files will be saved
    """
    best_variety(yieldfolder,resultpath) 
    
@click.command("varsow")
@click.argument("best_variety_file")
@click.argument("variety_sowing_folder")
@click.argument("resultpath")
def cmd_sowvar(best_variety_file, variety_sowing_folder, resultpath):
    """Create a sowing date netcdf file based on the cultivar map.
    
    best_variety_file: the path of the file containing the best cultivar
    variety_sowing_folder: the path of the folder containing the sowing date netcdf file for different cultivars
    
    resultpath: the path of the folder where the best cultivars netcdf files will be saved
    """
    sowing_date_from_best_variety(best_variety_file, variety_sowing_folder, resultpath)
    
       
cli.add_command(cmd_optimize)
cli.add_command(cmd_optimvar)
cli.add_command(cmd_sowvar)

if __name__ == "__main__":
    cli()
