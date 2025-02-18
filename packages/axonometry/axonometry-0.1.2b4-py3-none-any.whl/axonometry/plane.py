"""Build an axonometry picture with this class."""

# SPDX-FileCopyrightText: 2022-2025 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
from typing import TYPE_CHECKING

from compas.geometry import Line as CLine
from compas.geometry import Point as CPoint
from compas.geometry import Vector as CVector
from compas.geometry import intersection_line_line_xy

from .config import config_manager
from .line import Line
from .point import Point
from .utils import pair_projections_lines, pair_projections_points, random_axo_ref_plane_keys

if TYPE_CHECKING:
    from .trihedron import Trihedron


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Plane:
    """Base class for axonometric and reference planes."""

    def __init__(self) -> None:
        self.key = None
        self.drawing = None  # Initialize the drawing attribute if needed
        self._points = []
        self._lines = []

    @property
    def points(self) -> list[Point]:
        """All points contained in the current plane."""
        return self._points

    @points.setter
    def points(self, value: list[Point] | Point) -> None:
        """Store points which got added to the current plane."""
        if isinstance(value, list):
            if not all(isinstance(item, Point) for item in value):
                raise ValueError("All elements must be instances of Point")
            self._points.extend(value)
        elif isinstance(value, Point):
            self._points.append(value)
        else:
            raise TypeError("Points must be a list of Points or a single Point")

    @property
    def lines(self) -> list[Line]:
        """All lines contained in the current plane."""
        return self._lines

    @lines.setter
    def lines(self, value: list[Line] | Line) -> None:
        """Store lines which got added to the current plane."""
        if isinstance(value, list):
            if not all(isinstance(item, Line) for item in value):
                raise ValueError("All elements must be instances of Line")
            self._lines.extend(value)
        elif isinstance(value, Line):
            self._lines.append(value)
        else:
            raise TypeError("Lines must be a list of Lines or a single Line")

        # Add the line points to the plane attributes as well
        if value.start not in self._points:
            self._points.append(value.start)
        if value.end not in self._points:
            self._points.append(value.end)

    @property
    def objects(self) -> dict[str, list[Point | Line]]:
        """Collection of geometries in current plane."""
        return {"points": self._points, "lines": self._lines}

    def add_point(self, point: Point, ref_plane_keys: list[str] | None = None) -> Point:
        """Add a point to the current plane.

        TODO: check if point already exists. Return existing point in case.
        """
        assert point.key == self.key, (
            f"Point coordinates must follow containing plane coordinates. Plane:{self.key} & Point:{point.key}"
        )
        logger.info(f"[{self.key.upper()}] Add {point}")
        if point in self.objects["points"]:  # point already exists in plane
            index = self.objects["points"].index(point)
            point = self.objects["points"][index]
        else:  # make a new point
            if self.key == "xyz":
                # Point data could not exist
                logger.debug(
                    f"[{self.key.upper()}] Adding {point} by auxilary projection.",
                )
                if point.data is None:
                    point.data = self._decompose_xyz_point(point, ref_plane_keys)

            else:
                if point.matrix_applied:
                    # Reuse the original when repeating operation.
                    point.reset_data()
                point.data = point.data.transformed(self.matrix)
                point.matrix_applied = True

            logger.debug(f"[{self.key.upper()}] Add {point}")
            self.points = point
            self.drawing.add(point)
            point.plane = self  # add self as parent
        logger.debug(f"[{self.key.upper()}] Current objects in {self}: {self.objects}.")
        return point

    def add_line(self, line: Line, ref_plane_keys: list[str] | None = None) -> Line:
        """Add a line to the current reference plane.

        These are the various cases:
        In XYZ space:
            - The line has no data: it's a new line and auxilary projections are necessary.
            - The line has data set: data was computed by the projection function.
        In a reference plane:
            -
        """
        if line in self.objects["lines"]:  # line already exists in plane
            logger.info(
                f"[{self.key.upper()}] Adding {line} by using existing line from {self.objects['lines']}",
            )
            index = self.objects["lines"].index(line)
            line = self.objects["lines"][index]

        else:
            logger.info(f"[{self.key.upper()}] Add {line}")
            line.plane = self

            if self.key == "xyz":  # stop recursivity with "and line.data is not None" ?
                self._add_line_to_xyz_plane(line, ref_plane_keys)
                self._add_projected_lines_in_ref_plane(line)

            elif self.key in ["xy", "yz", "zx"]:
                self._add_line_to_ref_plane(line)
                self._add_projected_line_in_axo_plane(line)
                # TODO: add line to xyz plane without recursivity error.

            self.lines = line
            self.drawing.add(line, layer_id=config_manager.config["layers"]["geometry"]["id"])

        return line

    def _add_line_to_xyz_plane(
        self,
        line: Line,
        ref_plane_keys: list[str] | None = None,
    ) -> None:
        """Compute line data when added to XYZ plane.

        Add the start and end point to the XYZ plane and use their data to update the
        current line data.

        First add the lines' start and end point to the XYZ space. Get the data from these
        points in order to update the line data. Finally add lines where the two XYZ made
        auxilary projections.
        """
        # Randomize reference plane projections at this level in order
        # to make start and end points project in the same planes.
        if ref_plane_keys is None:
            # Make sure not to use perpendicular plane as auxilary plane
            if line.start.x == line.end.x and line.start.y == line.end.y:
                ref_plane_keys = ["zx", "yz"]
            elif line.start.y == line.end.y and line.start.z == line.end.z:
                ref_plane_keys = ["xy", "zx"]
            elif line.start.z == line.end.z and line.start.x == line.end.x:
                ref_plane_keys = ["xy", "yz"]
            # For all other scenarios
            else:
                # Favour XY plane because of architecture customs
                ref_plane_keys = random_axo_ref_plane_keys(privilege_xy_plane=True)

        line.start = self.add_point(
            line.start,
            ref_plane_keys=ref_plane_keys,
        )
        line.end = self.add_point(
            line.end,
            ref_plane_keys=ref_plane_keys,
        )
        # Update the line data with the projection
        line.data = CLine(line.start.data, line.end.data)

    def _add_line_to_ref_plane(self, line: Line) -> None:
        """Compute the line data when added to a reference plane."""
        # Compute the start and end points when added to the reference plane.
        line.start = self.add_point(line.start)
        line.end = self.add_point(line.end)
        # Get and update the line data from the new points.
        line.data = CLine(line.start.data, line.end.data)

    def _add_projected_lines_in_ref_plane(self, line: Line) -> None:
        """Check in which plane two points have both a projection and draw a line if so."""
        for ref_plane_key in self._common_projections(
            line.start.projections,
            line.end.projections,
        ):
            auxilary_line = Line(
                line.start.projections[ref_plane_key],
                line.end.projections[ref_plane_key],
                data=CLine(
                    line.start.projections[ref_plane_key].data,
                    line.end.projections[ref_plane_key].data,
                ),
                plane=self[ref_plane_key],
            )
            self.drawing.add(
                auxilary_line,
                layer_id=config_manager.config["layers"]["geometry"]["id"],
            )
            self[ref_plane_key].lines = auxilary_line
            pair_projections_lines(line, auxilary_line)

    def _add_projected_line_in_axo_plane(self, line: Line) -> None:
        """Add line in axo projection if points (projection) already exists there.

        Check if line start and end points have a axo projection.
        Draw a line if projections exists, add it to axo plane, pair lines.
        Check remaining planes for start end projections of new line.
        """
        if (
            len(line.start.projections["xyz"]) >= 1 and len(line.end.projections["xyz"]) >= 1
        ):  # TODO: get all points
            logger.info(
                f"Line points have axo projections and line ? {line.start.projections["xyz"][0].data=}; {line.end.projections["xyz"][0].data=}",
            )

            # Make new line
            new_axo_line = Line(
                line.start.projections["xyz"][0],
                line.end.projections["xyz"][0],
                data=CLine(
                    line.start.projections["xyz"][0].data,
                    line.end.projections["xyz"][0].data,
                ),
                plane=self.axo,
            )
            self.drawing.add(
                new_axo_line,
                layer_id=config_manager.config["layers"]["geometry"]["id"],
            )
            self.axo.lines = new_axo_line
            pair_projections_lines(line, new_axo_line)

            # Propagate axo line projections
            for key in self._common_projections(
                new_axo_line.start.projections,
                new_axo_line.end.projections,
                exclude=[self.key, "xyz"],
            ):
                logger.info(
                    f"Line points have other ref plane projections ? {new_axo_line.start.projections[key]=}; {new_axo_line.end.projections[key]=}",
                )
                new_ref_plane_line = Line(
                    new_axo_line.start.projections[key],
                    new_axo_line.end.projections[key],
                    data=CLine(
                        new_axo_line.start.projections[key].data,
                        new_axo_line.end.projections[key].data,
                    ),
                    plane=self.axo[key],
                )
                self.drawing.add(
                    new_ref_plane_line,
                    layer_id=config_manager.config["layers"]["geometry"]["id"],
                )
                self.axo[key].lines = new_ref_plane_line
                pair_projections_lines(new_axo_line, new_ref_plane_line)

    def _common_projections(self, dict1, dict2, exclude: list[str] = ["xyz"]):
        """Find which projected points are on the same reference plane."""
        for key in dict1:
            if key in exclude:  # Exclude this specific key from comparison
                continue
            if key in dict2 and dict1[key] is not None and dict2[key] is not None:
                yield key

    def _decompose_xyz_point(
        self,
        axo_point: Point,
        ref_plane_keys: list[str] | None = None,
    ) -> CPoint:
        """Directly added point in XYZ space becomes the intersection of two projected points.

        Basically adding points in two reference planes and intersecting them
        in the xyz space. The two planes can be provided as a parameter.

        :param: The axonometric point to be found by intersection of two projections.
        :param ref_plane_keys: The two reference, default to XY and random YZ or ZX.
        :return: Intersection coordinates from projected points.
        """
        logger.debug(f"Decompose {axo_point=}")

        if (
            ref_plane_keys
            and len(ref_plane_keys) != 2
            and (
                ref_plane_keys != ["xy", "yz"]
                or ref_plane_keys != ["xy", "zx"]
                or ref_plane_keys != ["yz", "zx"]
            )
        ):
            raise ValueError(f"{ref_plane_keys} are invalid.")

        if not ref_plane_keys:
            ref_plane_keys = random_axo_ref_plane_keys()

        if "xy" in ref_plane_keys and "yz" in ref_plane_keys:
            p1 = Point(x=axo_point.x, y=axo_point.y)
            p2 = Point(y=axo_point.y, z=axo_point.z)
            plane1 = self["xy"]
            plane2 = self["yz"]

        if "zx" in ref_plane_keys and "yz" in ref_plane_keys:
            p1 = Point(y=axo_point.y, z=axo_point.z)
            p2 = Point(z=axo_point.z, x=axo_point.x)
            plane1 = self["yz"]
            plane2 = self["zx"]

        if "xy" in ref_plane_keys and "zx" in ref_plane_keys:
            p1 = Point(z=axo_point.z, x=axo_point.x)
            p2 = Point(x=axo_point.x, y=axo_point.y)
            plane1 = self["zx"]
            plane2 = self["xy"]

        logger.debug(f"Two auxilary points computed {p1=}, {p2=}")

        plane1.add_point(p1)
        plane2.add_point(p2)
        pair_projections_points(axo_point, p1)
        pair_projections_points(axo_point, p2)

        # add them in respective ReferencePlanes
        axo_point_data = intersection_line_line_xy(
            CLine.from_point_and_vector(p1.data, plane1.projection_vector),
            CLine.from_point_and_vector(p2.data, plane2.projection_vector),
        )
        axo_point_data = CPoint(*axo_point_data)
        logger.debug(f"New {axo_point_data=}")
        # Add points in reference planes to the
        # axo point projections collection

        # draw intersection
        self.drawing.add_compas_geometry(
            [CLine(p1.data, axo_point_data), CLine(p2.data, axo_point_data)],
            layer_id=config_manager.config["layers"]["projection_traces"]["id"],
        )
        return axo_point_data


class ReferencePlane(Plane):
    """Represents a reference plane in an axonometric projection.

    :param lines: The two lines making up the reference plane axes.

    """

    def __init__(self, line_pair: list[CLine], projection_vector: CVector) -> None:
        super().__init__()  # Call the parent class constructor if necessary
        self.trihedron: Trihedron | None = None
        self.matrix = None
        self.axes = line_pair
        self.projection_vector = projection_vector
        self.matrix_to_coord_plane = None  # TODO

    def __repr__(self) -> str:
        """Get axes keys."""
        return f"Reference Plane {self.key.upper()}"

    def add_svg_file(self, svg_file: str):
        """Get an external svg and add it to current reference plane.

        An SVG is treated as a collection of lines. The steps to follow are extracting the line
        coordinates and adding each line to the current plane. Roughly the code should be as
        follow::

            for line in collection:
                self.add_line(Line(line))  # this will call the matrix
            doc = self.drawing.convert_svg_vpype_doc(svg_file)
        """
        raise NotImplementedError
