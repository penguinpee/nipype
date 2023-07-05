"""Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator."""

from nipype.interfaces.base import (
    CommandLine,
    CommandLineInputSpec,
    SEMLikeCommandLine,
    TraitedSpec,
    File,
    Directory,
    traits,
    isdefined,
    InputMultiPath,
    OutputMultiPath,
)
import os


class SphericalCoordinateGenerationInputSpec(CommandLineInputSpec):
    inputAtlasImage = File(
        desc="Input atlas image", exists=True, argstr="--inputAtlasImage %s"
    )
    outputPath = traits.Str(
        desc="Output path for rho, phi and theta images", argstr="--outputPath %s"
    )


class SphericalCoordinateGenerationOutputSpec(TraitedSpec):
    pass


class SphericalCoordinateGeneration(SEMLikeCommandLine):
    """title: Spherical Coordinate Generation

    category: Testing.FeatureDetection

    description: get the atlas image as input and generates the rho, phi and theta images.

    version: 0.1.0.$Revision: 1 $(alpha)

    contributor: Ali Ghayoor
    """

    input_spec = SphericalCoordinateGenerationInputSpec
    output_spec = SphericalCoordinateGenerationOutputSpec
    _cmd = " SphericalCoordinateGeneration "
    _outputs_filenames = {}
    _redirect_x = False
