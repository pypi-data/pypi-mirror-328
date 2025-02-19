import pathlib
from typing import Sequence

import pandas as pd
from lnas import LnasGeometry
from vtk import (
    vtkAppendPolyData,
    vtkCellArray,
    vtkFloatArray,
    vtkIdList,
    vtkPoints,
    vtkPolyData,
    vtkXMLPolyDataReader,
    vtkXMLPolyDataWriter,
)

from cfdmod.utils import create_folders_for_file


def _mkVtkIdList(it) -> vtkIdList:
    """Makes a vtkIdList from a Python iterable. I'm kinda surprised that
     this is necessary, since I assumed that this kind of thing would
     have been built into the wrapper and happen transparently, but it
     seems not.

    Args:
        it (Iterable): A python iterable.

    Returns:
        vtkIdList: A vtkIdList
    """
    vil = vtkIdList()
    for i in it:
        vil.InsertNextId(int(i))
    return vil


def create_polydata_for_cell_data(data: pd.DataFrame, mesh: LnasGeometry) -> vtkPolyData:
    """Creates a vtkPolyData for cell data combined with mesh description

    Args:
        data (pd.DataFrame): Compiled cell data. It supports table and matrix data formats.
            In matrix form, each column represents a point, and each row identifies the scalar label.
            In table form, there is a column with point indexes, and other columns for scalar data.
        mesh (LnasGeometry): Mesh description

    Returns:
        vtkPolyData: Extracted polydata
    """
    # We'll create the building blocks of polydata including data attributes.
    polyData = vtkPolyData()
    points = vtkPoints()
    polys = vtkCellArray()

    # Load the point, cell, and data attributes.
    for i, xi in enumerate(mesh.vertices):
        points.InsertPoint(i, xi)
    for pt in mesh.triangles:
        polys.InsertNextCell(_mkVtkIdList(pt))

    # We now assign the pieces to the vtkPolyData.
    polyData.SetPoints(points)
    polyData.SetPolys(polys)

    scalars_lbls, point_idx = None, None
    if "point_idx" in data.columns:
        # Table form dataframe
        scalars_lbls = [c for c in data.columns if c != "point_idx"]
        point_idx = data["point_idx"].to_numpy()
    else:
        # Matrix form dataframe
        scalars_lbls = data["scalar"]
        point_idx = [int(c) for c in data.columns if c != "scalar"]
    for scalar_index, scalar_lbl in enumerate(scalars_lbls):
        scalars = vtkFloatArray()
        scalars.SetName(scalar_lbl)
        scalar_data = None

        if "point_idx" in data.columns:
            # Table form dataframe, scalar is in columns
            scalar_data = data[scalar_lbl].to_numpy()
        else:
            # Matrix form dataframe, scalar is in rows
            scalar_data = data.iloc[scalar_index][
                [col for col in data.columns if col != "scalar"]
            ].to_numpy()
        for i, value in zip(point_idx, scalar_data):
            scalars.InsertTuple1(i, value)
        polyData.GetCellData().AddArray(scalars)

    return polyData


def merge_polydata(polydata_list: Sequence[vtkPolyData | vtkAppendPolyData]) -> vtkAppendPolyData:
    """Merges a list of polydata into a vtkAppendPolyData

    Args:
        polydata_list (list[vtkPolyData]): List of vtkPolyData

    Returns:
        vtkAppendPolyData: Appended polydata object
    """
    append_poly_data = vtkAppendPolyData()

    for polydata in polydata_list:
        append_poly_data.AddInputData(polydata)

    append_poly_data.Update()
    return append_poly_data


def read_polydata(file_path: pathlib.Path) -> vtkPolyData:
    """Reads polydata from file

    Args:
        file_path (pathlib.Path): File path

    Returns:
        vtkPolyData: Read polydata
    """
    reader = vtkXMLPolyDataReader()
    reader.SetFileName(file_path)
    reader.Update()

    polydata = reader.GetOutput()

    return polydata


def write_polydata(output_filename: pathlib.Path, poly_data: vtkPolyData | vtkAppendPolyData):
    """Writes a polydata object to file output

    Args:
        output_filename (pathlib.Path): Output file path
        poly_data (vtkPolyData | vtkAppendPolyData): Polydata object
    """
    writer = vtkXMLPolyDataWriter()
    create_folders_for_file(output_filename)
    writer.SetFileName(output_filename.as_posix())
    if isinstance(poly_data, vtkPolyData):
        writer.SetInputData(poly_data)
    else:
        writer.SetInputData(poly_data.GetOutput())
    writer.SetDataModeToAscii()
    writer.Write()
