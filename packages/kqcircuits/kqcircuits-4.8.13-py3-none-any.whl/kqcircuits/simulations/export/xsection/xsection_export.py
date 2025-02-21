# This code is part of KQCircuits
# Copyright (C) 2022 IQM Finland Oy
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see
# https://www.gnu.org/licenses/gpl-3.0.html.
#
# The software distribution should follow IQM trademark policy for open-source software
# (meetiqm.com/iqm-open-source-trademark-policy). IQM welcomes contributions to the code.
# Please see our contribution agreements for individuals (meetiqm.com/iqm-individual-contributor-license-agreement)
# and organizations (meetiqm.com/iqm-organization-contributor-license-agreement).


import ast
import json
import os
import logging
import subprocess
from itertools import product
from pathlib import Path
from typing import Callable
from kqcircuits.defaults import STARTUPINFO, XSECTION_PROCESS_PATH
from kqcircuits.pya_resolver import pya, klayout_executable_command
from kqcircuits.util.load_save_layout import load_layout, save_layout
from kqcircuits.simulations.cross_section_simulation import CrossSectionSimulation
from kqcircuits.simulations.simulation import Simulation, to_1d_list
from kqcircuits.util.geometry_json_encoder import GeometryJsonEncoder


def xsection_call(
    input_oas: Path,
    output_oas: Path,
    cut1: pya.DPoint,
    cut2: pya.DPoint,
    process_path: Path = XSECTION_PROCESS_PATH,
    parameters_path: Path = None,
) -> None:
    """Calls on KLayout to run the XSection plugin

    Args:
        input_oas: Input OAS file (top-down geometry)
        output_oas: Output OAS file (Cross-section of input geometry)
        cut1: DPoint of first endpoint of the cross-section cut
        cut2: DPoint of second endpoint of the cross-section cut
        process_path: XSection process file that defines cross-section etching depths etc
        parameters_path: If process_path points to kqc_process.xs,
            parameters_path should point to the XSection parameters json file
            containing sweeped parameters and layer information.
    """
    if os.name == "nt":
        klayout_dir_name = "KLayout"
    elif os.name == "posix":
        klayout_dir_name = ".klayout"
    else:
        raise SystemError("Error: unsupported operating system")
    xsection_plugin_path = os.path.join(os.path.expanduser("~"), klayout_dir_name, "salt/xsection/macros/xsection.lym")
    cut_string = f"{cut1.x},{cut1.y};{cut2.x},{cut2.y}"

    if not klayout_executable_command():
        raise Exception("Can't find klayout executable command!")
    if not Path(xsection_plugin_path).is_file():
        raise Exception("The 'xsection' plugin is missing in KLayout! Go to 'Tools->Manage Packages' to install it.")

    # Hack: Weird prefix keeps getting added when path is converted to string which breaks the ruby plugin
    xs_run = str(process_path).replace("\\\\?\\", "")
    xs_params = str(parameters_path).replace("\\\\?\\", "")
    # When debugging, remove '-z' argument to see ruby error messages
    subprocess.run(
        [
            klayout_executable_command(),
            input_oas.absolute(),
            "-z",
            "-nc",
            "-rx",
            "-r",
            xsection_plugin_path,
            "-rd",
            f"xs_run={xs_run}",
            "-rd",
            f"xs_params={xs_params}",
            "-rd",
            f"xs_cut={cut_string}",
            "-rd",
            f"xs_out={output_oas.absolute()}",
        ],
        check=True,
        startupinfo=STARTUPINFO,
    )


def _oxidise_layers(simulation, ma_thickness, ms_thickness, sa_thickness):
    """Take the cross section geometry and add oxide layers between substrate, metal and vacuum.
    Will etch away substrate and metals to insert oxide geometry.
    """
    substrate_layers = [
        layer
        for layer in simulation.layout.layer_infos()
        if layer.name.startswith("substrate_") or layer.name == "substrate"
    ]
    substrate = _combine_region_from_layers(simulation, substrate_layers)
    used_faces = []
    for face_group in simulation.get_parameters()["face_stack"]:
        if isinstance(face_group, list):
            used_faces.extend(face_group)
        else:
            used_faces.append(face_group)
    metal_layers = [
        layer
        for layer in simulation.layout.layer_infos()
        if layer.name in [f"{f}_{l}" for f, l in product(used_faces, ["ground", "signal"])]
    ]
    for f in used_faces:
        metal_layers += [layer for layer in simulation.layout.layer_infos() if layer.name.startswith(f"{f}_signal_")]
    metals = _combine_region_from_layers(simulation, metal_layers)
    metal_edges = metals.edges()
    substrate_edges = substrate.edges()

    ma_edges = []
    for metal_edge in metal_edges:
        if not _edge_on_the_box_border(metal_edge.to_dtype(simulation.layout.dbu), simulation.box):
            ma_edges.extend(_remove_shared_points(metal_edge, substrate_edges, True))

    sa_edges, ms_edges = [], []
    for substrate_edge in substrate_edges:
        if not _edge_on_the_box_border(substrate_edge.to_dtype(simulation.layout.dbu), simulation.box):
            sa_edges.extend(_remove_shared_points(substrate_edge, metal_edges, True))
            ms_edges.extend(_remove_shared_points(substrate_edge, sa_edges, False))

    ma_layer = _thicken_edges(simulation, ma_edges, ma_thickness, False)
    ms_layer = _thicken_edges(simulation, ms_edges, ms_thickness, False)
    sa_layer = _thicken_edges(simulation, sa_edges, sa_thickness, False)
    ma_layer -= ms_layer  # MS layer takes precedence over both MA and SA layers
    sa_layer -= ms_layer
    sa_layer -= ma_layer  # MA layer takes precedence over SA layer

    # Etch and replace substrate layer regions
    if ms_thickness > 0.0 or sa_thickness > 0.0:
        for substrate_layer in substrate_layers:
            substrate_region = pya.Region(simulation.cell.shapes(simulation.layout.layer(substrate_layer)))
            simulation.cell.shapes(simulation.layout.layer(substrate_layer)).clear()
            simulation.cell.shapes(simulation.layout.layer(substrate_layer)).insert(
                substrate_region - ms_layer - sa_layer
            )

    # Etch and replace metal layer regions
    if ma_thickness > 0.0:
        for metal_layer in metal_layers:
            metal_region = pya.Region(simulation.cell.shapes(simulation.layout.layer(metal_layer)))
            simulation.cell.shapes(simulation.layout.layer(metal_layer)).clear()
            simulation.cell.shapes(simulation.layout.layer(metal_layer)).insert(metal_region - ma_layer)

    if ma_thickness > 0.0:
        simulation.cell.shapes(simulation.get_sim_layer("ma_layer")).insert(ma_layer)
    if ms_thickness > 0.0:
        simulation.cell.shapes(simulation.get_sim_layer("ms_layer")).insert(ms_layer)
    if sa_thickness > 0.0:
        simulation.cell.shapes(simulation.get_sim_layer("sa_layer")).insert(sa_layer)


def _check_metal_heights(simulation):
    for i, h in enumerate(to_1d_list(simulation.metal_height), 1):
        if h == 0:
            logging.warning(f"Encountered zero metal height in CrossSectionSimulation (face {i}).")


def create_xsections_from_simulations(
    simulations: list[Simulation],
    output_path: Path,
    cuts: tuple[pya.DPoint, pya.DPoint] | list[tuple[pya.DPoint, pya.DPoint]],
    process_path: Path = XSECTION_PROCESS_PATH,
    post_processing_function: Callable[[CrossSectionSimulation], None] = None,
    oxidise_layers_function: Callable[[CrossSectionSimulation, float, float, float], None] = _oxidise_layers,
    ma_permittivity: float = 0,
    ms_permittivity: float = 0,
    sa_permittivity: float = 0,
    ma_thickness: float = 0,
    ms_thickness: float = 0,
    sa_thickness: float = 0,
    vertical_cull: tuple[float, float] | None = None,
    mer_box: pya.DBox | list[pya.DBox] | None = None,
    london_penetration_depth: float | list = 0,
    magnification_order: int = 0,
    layout: pya.Layout | None = None,
) -> list[Simulation]:
    """Create cross-sections of all simulation geometries in the list.
    Will set 'box' and 'cell' parameters according to the produced cross-section geometry data.

    Args:
        simulations: List of Simulation objects, usually produced by a sweep
        output_path: Path for the exported simulation files
        cuts: 1. A tuple (p1, p2), where p1 and p2 are endpoints of a cross-section cut or
              2. a list of such tuples such that each Simulation object gets an individual cut
        process_path: XSection process file that defines cross-section etching depths etc
        post_processing_function: Additional function to post-process the cross-section geometry.
            Defaults to None, in which case no post-processing is performed.
            The function takes a CrossSectionSimulation object as argument
        oxidise_layers_function: Set this argument if you have a custom way of introducing
            oxidization layers to the cross-section metal deposits and substrate.
            See expected function signature from pyhints
        ma_permittivity: Permittivity of metal–vacuum (air) interface
        ms_permittivity: Permittivity of metal–substrate interface
        sa_permittivity: Permittivity of substrate–vacuum (air) interface
        ma_thickness: Thickness of metal–vacuum (air) interface
        ms_thickness: Thickness of metal–substrate interface
        sa_thickness: Thickness of substrate–vacuum (air) interface
        vertical_cull: Tuple of two y-coordinates, will cull all geometry not in-between the y-coordinates.
            None by default, which means all geometry is retained.
        mer_box: If set as pya.DBox, will create a specified box as metal edge region,
            meaning that the geometry inside the region are separated into different layers with '_mer' suffix
        london_penetration_depth: London penetration depth of the superconducting material
        magnification_order: Increase magnification of simulation geometry to accomodate more precise spacial units.
            0 =   no magnification with 1e-3 dbu
            1 =  10x magnification with 1e-4 dbu
            2 = 100x magnification with 1e-5 dbu etc
            Consider setting non-zero value when using oxide layers with < 1e-3 layer thickness or
            taking cross-sections of thin objects
        layout: predefined layout for the cross-section simulation (optional)

    Returns:
        List of CrossSectionSimulation objects for each Simulation object in simulations
    """
    if isinstance(cuts, tuple):
        cuts = [cuts] * len(simulations)
    cuts = [tuple(c if isinstance(c, pya.DPoint) else c.to_p() for c in cut) for cut in cuts]
    if len(simulations) != len(cuts):
        raise Exception("Number of cuts did not match the number of simulations")
    if any(len(simulation.get_parameters()["face_stack"]) not in (1, 2) for simulation in simulations):
        raise Exception("Only single face and flip chip cross section simulations currently supported")

    xsection_dir = output_path.joinpath("xsection_tmp")
    xsection_dir.mkdir(parents=True, exist_ok=True)

    if layout is None:
        layout = pya.Layout()
    xsection_cells = []
    for simulation, cut in zip(simulations, cuts):
        _check_metal_heights(simulation)
        xsection_parameters = _dump_xsection_parameters(xsection_dir, simulation)
        simulation_file = xsection_dir / f"original_{simulation.cell.name}.oas"
        xsection_file = xsection_dir / f"xsection_{simulation.cell.name}.oas"
        save_layout(simulation_file, simulation.layout, [simulation.cell], no_empty_cells=True)
        xsection_call(simulation_file, xsection_file, cut[0], cut[1], process_path, xsection_parameters)

        load_layout(xsection_file, layout)
        for i in layout.layer_indexes():
            if all(layout.begin_shapes(cell, i).at_end() for cell in layout.top_cells()):
                layout.delete_layer(i)  # delete empty layers caused by bug in klayout 0.29.0
        xsection_cells.append(layout.top_cells()[-1])
        xsection_cells[-1].name = simulation.cell.name

    _clean_tmp_xsection_directory(xsection_dir, simulations)
    # Collect cross-section simulation sweeps
    return [
        _construct_cross_section_simulation(
            layout,
            xsection_cell,
            simulations[idx],
            post_processing_function,
            oxidise_layers_function,
            ma_permittivity,
            ms_permittivity,
            sa_permittivity,
            ma_thickness,
            ms_thickness,
            sa_thickness,
            vertical_cull,
            mer_box,
            london_penetration_depth,
            magnification_order,
        )
        for idx, xsection_cell in enumerate(xsection_cells)
    ]


def separate_signal_layer_shapes(simulation: Simulation, sort_key: Callable[[pya.Shape], float] = None):
    """Separate shapes in signal layer to their own dedicated signal layers for each face

    Args:
        simulation: A Simulation object where the layer will be separated
        sort_key: A function that, given a Shape object, returns a number.
            Shapes are sorted according to the number in increasing order.
            If None, picks a point in shape polygon, sorts points top to bottom then tie-breaks left to right
    """
    if sort_key is None:

        def sort_key(shape):
            point_in_shape = list(shape.polygon.each_point_hull())[0]
            return (-point_in_shape.y, point_in_shape.x)

    signal_index = 1
    gen_free_layer_slots = free_layer_slots(simulation.layout)
    for face in simulation.face_ids:
        signal_layer = find_layer_by_name(f"{face}_signal", simulation.layout)
        if signal_layer is None:
            continue
        signal_layer_idx = simulation.layout.layer(signal_layer)
        for shape in sorted(simulation.cell.each_shape(signal_layer_idx), key=sort_key):
            # Reuse layer if it already used in layout
            signal_layer = find_layer_by_name(f"{face}_signal_{signal_index}", simulation.layout)
            # If no such layer, find next available layer index
            if signal_layer is None:
                layer_index = next(gen_free_layer_slots)
                signal_layer = pya.LayerInfo(layer_index, 0, f"{face}_signal_{signal_index}")
            simulation.cell.shapes(simulation.layout.layer(signal_layer)).insert(shape)
            signal_index += 1
        simulation.cell.clear(signal_layer_idx)


def find_layer_by_name(layer_name, layout):
    """Returns layerinfo if there already is a layer by layer_name in layout. None if no such layer exists"""
    for l in layout.layer_infos():
        if l.datatype == 0 and layer_name == l.name:
            return l
    return None


def free_layer_slots(layout):
    """A generator of available layer slots"""
    layer_index = 0
    reserved_layer_ids = [l.layer for l in layout.layer_infos() if l.datatype == 0]
    while True:
        layer_index += 1
        if layer_index in reserved_layer_ids:
            continue
        yield layer_index


def visualise_xsection_cut_on_original_layout(
    simulations: list[Simulation],
    cuts: tuple[pya.DPoint, pya.DPoint] | list[tuple[pya.DPoint, pya.DPoint]],
    cut_label: str = "cut",
    width_ratio: float = 0.0,
):
    """Visualise requested xsection cuts on the original simulation layout.

    Will add a rectangle between two points of the cut, and two text points into layer "xsection_cut"::

        * f"{cut_label}_1" representing the left side of the cross section simulation
        * f"{cut_label}_2" representing the right side of the cross section simulation

    In case the export takes xsections for one simulation multiple times, this function
    can be called on same simulation sweep multiple times so that multiple cuts can be visualised
    in the same layout. In such case it is recommended to differentiate the cuts using `cut_label`.

    Args:
        simulations: list of simulations from which xsections are taken. After this call these simulations
            will be modified to include the visualised cuts.
        cuts: 1. A tuple (p1, p2), where p1 and p2 are endpoints of a cross-section cut or
              2. a list of such tuples such that each Simulation object gets an individual cut
        cut_label: prefix of the two text points shown for the cut
        width_ratio: rectangles visualising cuts will have a width of length of the cut multiplied by width_ratio
    """
    if isinstance(cuts, tuple):
        cuts = [cuts] * len(simulations)
    cuts = [tuple(c if isinstance(c, pya.DPoint) else c.to_p() for c in cut) for cut in cuts]
    if len(simulations) != len(cuts):
        raise Exception("Number of cuts did not match the number of simulations")
    for simulation, cut in zip(simulations, cuts):
        cut_length = (cut[1] - cut[0]).length()
        marker_path = pya.DPath(cut, cut_length * width_ratio).to_itype(simulation.layout.dbu)
        # Prevent .OAS saving errors by rounding integer value of path width to even value
        marker_path.width -= marker_path.width % 2
        marker = pya.Region(marker_path)
        simulation.visualise_region(marker, cut_label, "xsection_cut", cut)


def _dump_xsection_parameters(xsection_dir, simulation):
    """If we're sweeping xsection specific parameters,
    dump them in external file for xsection process file to pick up
    """
    simulation_params = {
        param_name: param_value
        for param_name, param_value in simulation.get_parameters().items()
        if not isinstance(param_value, pya.DBox)
    }  # Hack: ignore non-serializable params
    simulation_params["chip_distance"] = to_1d_list(simulation_params["chip_distance"])
    # Also dump all used layers in the simulation cell
    simulation_params["sim_layers"] = {l.name: f"{l.layer}/{l.datatype}" for l in simulation.layout.layer_infos()}
    xsection_parameters_file = xsection_dir / f"parameters_{simulation.cell.name}.json"
    with open(xsection_parameters_file, "w", encoding="utf-8") as sweep_file:
        json.dump(simulation_params, sweep_file, cls=GeometryJsonEncoder)
    return xsection_parameters_file


def _clean_tmp_xsection_directory(xsection_dir, simulations):
    for simulation in simulations:
        if os.path.exists(xsection_dir / f"original_{simulation.cell.name}.oas"):
            os.remove(xsection_dir / f"original_{simulation.cell.name}.oas")
        if os.path.exists(xsection_dir / f"xsection_{simulation.cell.name}.oas"):
            os.remove(xsection_dir / f"xsection_{simulation.cell.name}.oas")
        if os.path.exists(xsection_dir / f"parameters_{simulation.cell.name}.json"):
            os.remove(xsection_dir / f"parameters_{simulation.cell.name}.json")
    if os.path.exists(xsection_dir):
        os.rmdir(xsection_dir)


def _combine_region_from_layers(simulation, layers):
    """Produce a region combined from regions in layers list"""
    region = pya.Region()
    for layer in layers:
        region += pya.Region(simulation.cell.shapes(simulation.layout.layer(layer)))
    return region


def _edge_on_the_box_border(edge, box):
    """True if edge is exactly at the rim of the box. edge must be of class pya.DEdge"""
    return (
        (edge.x1 == box.p1.x and edge.x2 == box.p1.x)
        or (edge.x1 == box.p2.x and edge.x2 == box.p2.x)
        or (edge.y1 == box.p1.y and edge.y2 == box.p1.y)
        or (edge.y1 == box.p2.y and edge.y2 == box.p2.y)
    )


def _cut_edge(target_edge, source_edge, extra_edges):
    """Cut an end of the target_edge with source_edge.

    If source_edge leaves behind two ends of the target_edge,
    the second edge bit is stored in extra_edges.

    Each edge should be in integer form (pya.Edge)
    """
    # Copy target_edge to not modify the original edge instance
    result_edge = pya.Edge(target_edge.p1.x, target_edge.p1.y, target_edge.p2.x, target_edge.p2.y)
    if result_edge.contains_excl(source_edge.p1):
        if result_edge.contains_excl(source_edge.p2) and source_edge.p2 != result_edge.p2:
            extra_edges.append(pya.Edge(source_edge.p2, result_edge.p2))
        result_edge.p2 = source_edge.p1
    elif result_edge.contains_excl(source_edge.p2):
        result_edge.p1 = source_edge.p2
    return result_edge


def _remove_shared_points(target_edge, acting_edges, is_adjacent):
    """Remove all points shared by target_edge and edges in acting_edges

    Returns a set of continuous edges that are not contained by acting_edges.
    Set is_adjacent to True if the shape of acting_edges is adjacent to the shape
    from which target_edge was taken. Set to False if the shapes are on top of eah other.

    Each edge should be in integer form (pya.Edge)
    """
    edge_bits = [target_edge]
    for acting_edge in acting_edges:
        # Set acting_edge to point to same direction as target_edge
        if is_adjacent:
            acting_edge = acting_edge.swapped_points()
        # Consider edges if they share points, which means they are parallel and have same displacement
        if acting_edge.is_parallel(target_edge):
            # Remove edge bits if they are completely covered by acting_edge
            edge_bits = [e for e in edge_bits if not (acting_edge.contains(e.p1) and acting_edge.contains(e.p2))]
            extra_edge_bits = []  # Collect extra edge bits here
            edge_bits = [_cut_edge(e, acting_edge, extra_edge_bits) for e in edge_bits]
            edge_bits.extend(extra_edge_bits)  # Add extra bits
            edge_bits = [e for e in edge_bits if e.p1 != e.p2]  # Remove zero length edge bits
    return edge_bits


def _normal_of_edge(simulation, p1, p2, scale):
    """Returns a normal of edge p1->p2.

    If (p1, p2) are in same polygon in given order,
    the returned normal will stick out of polygon.
    The magnitude of the normal will be set to `scale`.

    p1, p2 are pya.Point (integer) objects, however
    scale is scaled according to pya.DPoint domain.
    """
    edge_dir = p2 - p1
    normal = pya.Point(-edge_dir.y, edge_dir.x)
    dnormal = normal.to_dtype(simulation.layout.dbu)
    return (dnormal * (scale / dnormal.abs())).to_itype(simulation.layout.dbu)


def _thicken_edges(simulation, edges, thickness, grow):
    """Take edges and add thickness to produce a region.

    Set grow to True to grow the region outward, False to grow inward
    Each edge should be in integer form (pya.Edge)
    """
    if thickness <= 0.0:  # Don't do anything if no thickness
        return pya.Region()
    # Construct a graph from the edges to find paths
    # Start by finding start points for paths
    start_points = [e.p1 for e in edges if e.p1 not in [e2.p2 for e2 in edges]]
    path_graph = {}
    for edge in edges:
        path_graph[edge.p1] = edge

    result_region = pya.Region()
    processed_edges = []
    # Take each start_point and follow the path until the end
    for current_point in start_points:
        inner_path = [current_point]
        normals = []
        while True:
            current_edge = path_graph[current_point]
            processed_edges.append(current_edge)
            # First collect path points for the region polygon
            inner_path.append(current_edge.p2)
            # Also collect their normals
            normals.append(
                (1.0 if grow else -1.0) * _normal_of_edge(simulation, current_edge.p1, current_edge.p2, thickness)
            )
            # At the end point, terminate
            if current_edge.p2 not in path_graph:
                break
            # Otherwise proceed to next point in path
            current_point = current_edge.p2
        # Connect to the second layer of the path to add thickness
        outer_path = [inner_path[-1] + normals[-1]]
        # Backtrack the path for the second layer of the polygon
        for idx in range(len(normals) - 1, 0, -1):
            normal_sum = normals[idx] + normals[idx - 1]  # Sum normals of surrounding edges of the point
            outer_path.append(inner_path[idx] + normal_sum)
        outer_path.append(inner_path[0] + normals[0])
        result_region += pya.Region(pya.Polygon(inner_path + outer_path))

    # Handle edges in loops separately
    loop_edges = [e for e in edges if e not in processed_edges]
    processed_edges = []
    for start_edge in loop_edges:
        if start_edge in processed_edges:
            continue
        current_edge = start_edge
        loop = [current_edge.p1]
        while current_edge.p2 != start_edge.p1:
            loop.append(current_edge.p2)
            current_edge = path_graph[current_edge.p2]
            processed_edges.append(current_edge)
        loop_poly = pya.Polygon(loop)
        if grow:
            # We are growing on the rim of the loop. Take the rim, then copy the
            # shrinked rim, then subtract shrinked rim from original rim.
            # To shrink, we have to rely on normals
            loop_sized = []
            for i, p in enumerate(loop):
                j = 0 if i + 1 == len(loop) else i + 1
                normal_next = _normal_of_edge(simulation, p, loop[j], thickness)
                normal_prev = _normal_of_edge(simulation, loop[i - 1], p, thickness)
                loop_sized.append(p + normal_prev + normal_next)
            loop_sized = pya.Polygon(loop_sized)
        else:
            # We are "growing" out of the rim of the loop. Take the rim,
            # then copy the magnified rim, subtracting original rim from
            # the magnified rim. We can just use `sized` method.
            loop_sized = loop_poly.to_dtype(simulation.layout.dbu)
            loop_sized = loop_sized.sized(thickness)
            loop_sized = loop_sized.to_itype(simulation.layout.dbu)
        if grow:
            result_region += pya.Region(loop_poly) - pya.Region(loop_sized)
        else:
            result_region += pya.Region(loop_sized) - pya.Region(loop_poly)
    return result_region


def _iterate_layers_and_modify_region(xsection_cell, process_region):
    """Iterates over all (non-empty) layers in xsection_cell
    and replaces the region in that layer with process_region(region, layer)
    """
    for layer in xsection_cell.layout().layer_infos():
        region = pya.Region(xsection_cell.shapes(xsection_cell.layout().layer(layer)))
        if region.is_empty():
            continue
        xsection_cell.shapes(xsection_cell.layout().layer(layer)).clear()
        xsection_cell.shapes(xsection_cell.layout().layer(layer)).insert(process_region(region, layer))


def _construct_cross_section_simulation(
    layout,
    xsection_cell,
    simulation,
    post_processing_function,
    oxidise_layers_function,
    ma_permittivity,
    ms_permittivity,
    sa_permittivity,
    ma_thickness,
    ms_thickness,
    sa_thickness,
    vertical_cull,
    mer_box,
    london_penetration_depth,
    magnification_order,
):
    """Produce CrossSectionSimulation object"""
    if magnification_order > 0:
        layout.dbu = 10 ** (-3 - magnification_order)
        xsection_cell.transform(pya.DCplxTrans(10**magnification_order))
    xsection_parameters = simulation.get_parameters()
    xsection_parameters["london_penetration_depth"] = london_penetration_depth
    cell_bbox = xsection_cell.dbbox()
    # Disabled for single face and flip-chip cases
    # cell_bbox.p1 -= pya.DPoint(0, xsection_parameters['lower_box_height'])
    if len(xsection_parameters["face_stack"]) == 1:
        cell_bbox.p2 += pya.DPoint(0, xsection_parameters["upper_box_height"])
    if vertical_cull is not None:
        cell_bbox.p1 = pya.DPoint(cell_bbox.p1.x, min(vertical_cull))
        cell_bbox.p2 = pya.DPoint(cell_bbox.p2.x, max(vertical_cull))
    xsection_parameters["box"] = cell_bbox
    xsection_parameters["cell"] = xsection_cell
    xsection_simulation = CrossSectionSimulation(layout, **xsection_parameters, ignore_process_layers=True)
    # Keep all parameters given in simulations for JSON
    for k, v in xsection_parameters.items():
        setattr(xsection_simulation, k, v)
    xsection_simulation.xsection_source_class = type(simulation)
    xsection_simulation.register_cell_layers_as_sim_layers()

    material_dict = xsection_parameters["material_dict"]
    material_dict = ast.literal_eval(material_dict) if isinstance(material_dict, str) else material_dict
    substrate_material = xsection_parameters["substrate_material"]
    substrate_1_permittivity = material_dict[substrate_material[0]]["permittivity"]

    xsection_simulation.set_permittivity("substrate_1", substrate_1_permittivity)
    if len(xsection_parameters["face_stack"]) == 2:
        substrate_2_permittivity = substrate_1_permittivity
        if len(substrate_material) > 1:
            substrate_2_permittivity = material_dict[substrate_material[1]]["permittivity"]
        xsection_simulation.set_permittivity("substrate_2", substrate_2_permittivity)

    if post_processing_function:
        post_processing_function(xsection_simulation)

    if oxidise_layers_function:
        oxidise_layers_function(xsection_simulation, ma_thickness, ms_thickness, sa_thickness)

    if vertical_cull is not None:

        def _cull_region_vertically(region, layer):  # pylint: disable=unused-argument
            return region & cell_bbox.to_itype(xsection_cell.layout().dbu)

        _iterate_layers_and_modify_region(xsection_cell, _cull_region_vertically)

    if mer_box is not None:
        regions_to_update = {}
        if isinstance(mer_box, list):
            box_region = pya.Region()
            for mb in mer_box:
                box_region += pya.Region(mb.to_itype(xsection_cell.layout().dbu))
        else:
            box_region = pya.Region(mer_box.to_itype(xsection_cell.layout().dbu))

        def _separate_region_in_mer_box(region, layer):
            region_in_box = region & box_region
            regions_to_update[f"{layer.name}_mer"] = region_in_box
            return region - box_region

        _iterate_layers_and_modify_region(xsection_cell, _separate_region_in_mer_box)
        vacuum_in_box = box_region
        for layer, region in regions_to_update.items():
            vacuum_in_box -= region
            xsection_cell.shapes(xsection_simulation.get_sim_layer(layer)).insert(region)
        xsection_cell.shapes(xsection_simulation.get_sim_layer("vacuum_mer")).insert(vacuum_in_box)

    if ma_thickness > 0.0:
        xsection_simulation.set_permittivity("ma_layer", ma_permittivity)
    if ms_thickness > 0.0:
        xsection_simulation.set_permittivity("ms_layer", ms_permittivity)
    if sa_thickness > 0.0:
        xsection_simulation.set_permittivity("sa_layer", sa_permittivity)
    xsection_simulation.process_layers()
    return xsection_simulation
