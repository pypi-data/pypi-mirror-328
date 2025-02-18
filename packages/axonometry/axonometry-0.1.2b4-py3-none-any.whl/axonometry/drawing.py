"""Where all operations are recorded."""

# SPDX-FileCopyrightText: 2022-2025 Julien Rippinger
#
# SPDX-License-Identifier: GPL-3.0-or-later
import logging
from typing import TYPE_CHECKING

from compas.geometry import Geometry as CGeometry
from compas.scene import Scene as CScene
from vpype import Document

from .config import config_manager
from .utils import convert_compas_to_vpype_lines

if TYPE_CHECKING:
    from .axonometry import Axonometry


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Drawing:
    """I record all what is happening.

    Basically a wrapper for vpype.Document and compas.scene.Scene objects.
    The various add_* functions at the Axonometry/Reference Plane level
    interact mostly with this object.
    """

    def __init__(self) -> None:
        self.dimensions = (
            config_manager.config["sizes"]["A1"]["portrait"][0]
            * config_manager.config["css_pixel"],
            config_manager.config["sizes"]["A1"]["portrait"][1]
            * config_manager.config["css_pixel"],
        )
        self.document = Document(
            page_size=self.dimensions,
        )  #: Wrapper for a vpype.Document
        self.scene = CScene()

    def resize_page(self, page_format: str, page_layout: str) -> None:
        """Not implemented."""
        raise NotImplementedError

    def add(self, item, layer_id: int | None = None) -> None:
        """Adding geometries to the drawing."""
        compas_data = [item.data]  # it's the compas data which is being drawn
        logger.info(f"[{item.key.upper()}] {item} added to {self}.")
        self.add_compas_geometry(compas_data, layer_id=layer_id)

    def add_axonometry(self, axo: "Axonometry", position: tuple | None = None) -> None:
        """Combine several axonometries in a single drawing."""
        if position:
            axo.drawing.document.translate()  # TODO compute translate from new position
        self.document.extend(axo.drawing.document)

    def add_compas_geometry(
        self,
        compas_data: list[CGeometry],
        layer_id: int | None = None,
    ) -> None:
        """Add directly compas geometries to the drawing."""
        # no traces ?
        logger.debug(f"[{self}] Add compas data objects to drawing: {compas_data}")
        # for item in compas_data:
        #     self.scene.add(item)
        geometry = convert_compas_to_vpype_lines(compas_data)
        if geometry:
            self.document.add(geometry, layer_id=layer_id)

    def __repr__(self) -> str:
        """Identify drawing."""
        return "Drawing"  # + hex(id(self)) ?
