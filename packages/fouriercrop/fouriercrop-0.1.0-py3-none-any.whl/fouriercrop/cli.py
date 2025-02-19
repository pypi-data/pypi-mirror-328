"""Console script for fouriercrop."""

from typing import Annotated, Optional

import typer

from fouriercrop import __version__, load_mrc, save_mrc, FourierCrop
import torch

app = typer.Typer()


def version_callback(value: bool) -> None:
    """Callback function for the --version option."""
    if value:
        typer.echo(f"fouriercrop, version {__version__}")
        raise typer.Exit()


@app.command()
def main(
    input_path: str,
    output_path: str = None,
    bin_factor: int = 2,
    pad_mode: int = 0,
    norm_flag: bool = False,
    version: Annotated[Optional[bool], typer.Option("--version", callback=version_callback, is_eager=True)] = None,
) -> None:
    """Console script for fouriercrop."""
    x = torch.tensor(load_mrc(input_path), dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    print(f"input shape: {x.shape}")

    fc_func = FourierCrop(pad_mode=pad_mode)
    x = fc_func(x, bin_factor=bin_factor, norm_flag=norm_flag)
    print(f"output shape: {x.shape}")

    if output_path:
        save_mrc(output_path, x.squeeze().numpy())


if __name__ == "__main__":
    app()  # pragma: no cover
