"""Main object to start drawing."""
# SPDX-FileCopyrightText: 2022-2025 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging
import math
import pathlib
from typing import TYPE_CHECKING

from .config import config_manager
from .drawing import Drawing
from .plane import Plane, ReferencePlane
from .trihedron import Trihedron
from .utils import save_svg, show_paths, visualize

if TYPE_CHECKING:
    from compas.geometry import CVector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Axonometry(Plane):
    """Represents an axonometric projection with given angles.

    Not mouch operations happen on this level, this class is more
    like a collection from which to access Trihedron and ReferencePlane
    objects. But this class also inherits Plane, therefore can be used
    as well to add geometries to the Drawing instance.

    .. note::

        When adding objects, and they have only two of the x y z, it means they are projecitons
        in a reference plane.

    """

    def __init__(
        self,
        *angles: float,
        trihedron_position: tuple = (0, 0),
        ref_planes_distance: float = 100.0,
        trihedron_size: float = 100.0,
    ) -> None:
        super().__init__()  # Call the parent class constructor if necessary
        self.drawing = Drawing()  #: The wrapped object
        self.key = "xyz"
        logger.info(f"[{self.key.upper()}] {angles[0]}°/{angles[1]}°")
        self._trihedron = Trihedron(
            tuple(angles),
            position=trihedron_position,
            size=trihedron_size,
            ref_planes_distance=ref_planes_distance,
        )

        """Access the different reference planes by key."""
        for plane in self._trihedron.reference_planes.values():
            plane.axo = self  # necessary to evaluate the geometry objects' membership
            plane.drawing = self.drawing  # necessary to draw in plane
        # Add Trihedron to Drawing
        self.drawing.add_compas_geometry(
            self._trihedron.axes.values(),
            layer_id=config_manager.config["layers"]["axo_system"]["id"],
        )
        for plane in self._trihedron.reference_planes.values():
            self.drawing.add_compas_geometry(
                plane.axes,
                layer_id=config_manager.config["layers"]["axo_system"]["id"],
            )

    @property
    def x(self) -> "CVector":
        """X coordinate vector."""
        return self._trihedron.axes["x"].direction

    @property
    def y(self) -> "CVector":
        """Y coordinate vector."""
        return self._trihedron.axes["y"].direction

    @property
    def z(self) -> "CVector":
        """Z coordinate vector."""
        return self._trihedron.axes["z"].direction

    @property
    def xy(self) -> ReferencePlane:
        """XY reference plane."""
        return self._trihedron.reference_planes["xy"]

    @property
    def yz(self) -> ReferencePlane:
        """YZ reference plane."""
        return self._trihedron.reference_planes["yz"]

    @property
    def zx(self) -> ReferencePlane:
        """ZX reference plane."""
        return self._trihedron.reference_planes["zx"]

    def show_paths(self) -> None:
        """Display drawing."""
        show_paths(self)

    def visualize(self) -> None:
        """Display geometry."""
        visualize(self)

    def save_svg(self, filename: str, directory: str = "./output/") -> None:
        """Save drawing to file.

        TODO: check best pracatice for file location.

        :param filename: Name of the SVG file.
        :param directory: Path to directory, defaults to ``./output/``.
        """
        try:
            with pathlib.Path.open(directory + filename + ".svg", "w") as f:
                save_svg(self, f)
        except FileExistsError:
            logger.info("Already exists.")

    def save_json(self, filename: str, directory: str = "./output/") -> None:
        """Save drawing data to json file."""
        try:
            with pathlib.Path.open(directory + filename + ".json", "w") as f:
                self.drawing.save_json(f)
        except FileExistsError:
            logger.info("Already exists.")

    def __repr__(self) -> str:
        """Get axonometry values in standard horizon angle notation."""
        return f"Axonometry {math.degrees(self._trihedron.axo_angles[0])}°/{math.degrees(self._trihedron.axo_angles[1])}°"

    def __getitem__(self, item: str) -> ReferencePlane:
        """Select a reference plane by key."""
        if item in self._trihedron.reference_planes:
            return self._trihedron.reference_planes[item]
        return self
