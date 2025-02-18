from __future__ import annotations

import html
from abc import ABC, abstractmethod
from typing import Optional

import folium
import geopandas as gpd
import numpy as np
import osmnx as ox
import pandas as pd
from folium.plugins import Fullscreen
from networkx import MultiDiGraph


class BaseOsmMap(ABC):
    # Define available tile options for the map
    tile_options = {
        "OpenStreetMap": "OpenStreetMap",
        "CartoDB": "cartodbpositron",
        "CartoDB Voyager": "cartodbvoyager"
    }
    # Default geographical bounds (Costa Rica)
    bounds = [[8.0340, -85.9417], [11.2192, -82.5566]]

    def __init__(
            self,
            osmnx_graph: MultiDiGraph,
            df: pd.DataFrame,
            lat_col: str = "latitude",
            lon_col: str = "longitude",
            map_html_title: str = "OSM Basemap",
            zoom_start: int = 13,
            fullscreen: bool = True,
            fullscreen_position: str = "topright",
            tiles: str = "OpenStreetMap",
            verbose: bool = False,
            sort_keys: Optional[list[str]] = None,
            dt_field: Optional[str] = None,
            calc_nearest_nodes: bool = False,
            max_bounds: bool = False,
    ):
        if df.empty:
            raise ValueError("df must not be empty")

        # Store attributes
        self.df = df.copy()
        self.osmnx_graph = osmnx_graph
        self.lat_col = lat_col
        self.lon_col = lon_col
        self.map_html_title = self._sanitize_html(map_html_title)
        self.zoom_start = zoom_start
        self.fullscreen = fullscreen
        self.fullscreen_position = fullscreen_position
        self.tiles = tiles
        self.verbose = verbose
        self.sort_keys = sort_keys
        self.dt_field = dt_field
        self.calc_nearest_nodes = calc_nearest_nodes
        self.max_bounds = max_bounds
        self.dt = self.df[self.dt_field].to_list() if self.dt_field else None
        self.nearest_nodes = None
        self.G = None
        self.osm_map = None

        self._prepare_df()
        self._initialize_map()

    def _prepare_df(self):
        """Sort and preprocess the DataFrame."""
        if self.sort_keys:
            self.df.sort_values(by=self.sort_keys, inplace=True, ignore_index=True)
        self.gps_points = self.df[[self.lat_col, self.lon_col]].to_numpy()

        # Compute nearest nodes if required
        if self.calc_nearest_nodes and not self.df.empty:
            self.nearest_nodes = ox.distance.nearest_nodes(
                self.osmnx_graph, X=self.df[self.lon_col], Y=self.df[self.lat_col]
            )

    def _initialize_map(self):
        """Initialize the folium map centered around the dataset."""
        if self.gps_points.size == 0:
            raise ValueError("No valid GPS points available for map initialization")

        center = self.gps_points.mean(axis=0).tolist()
        if self.osm_map is None:
            self.osm_map = folium.Map(
                location=center, zoom_start=self.zoom_start, tiles=self.tiles, max_bounds=self.max_bounds
            )
        self.G = self._extract_subgraph(*self._get_bounding_box_from_points())

    def _get_bounding_box_from_points(self, margin: float = 0.001) -> tuple[float, float, float, float]:
        """Compute bounding box for the dataset with margin."""
        latitudes, longitudes = self.gps_points[:, 0], self.gps_points[:, 1]
        return max(latitudes) + margin, min(latitudes) - margin, max(longitudes) + margin, min(longitudes) - margin

    def _extract_subgraph(self, north: float, south: float, east: float, west: float) -> MultiDiGraph:
        """Extract a subgraph from OSM data within the bounding box."""
        bbox_poly = gpd.GeoSeries([ox.utils_geo.bbox_to_poly((west, south, east, north))])
        nodes_gdf = ox.graph_to_gdfs(self.osmnx_graph, nodes=True, edges=False)
        nodes_within_bbox = gpd.sjoin(nodes_gdf, gpd.GeoDataFrame(geometry=bbox_poly), predicate="within")
        return self.osmnx_graph.subgraph(nodes_within_bbox.index)

    def _post_process_map(self):
        """Perform final adjustments to the map."""
        self._attach_supported_tiles()
        self.add_tile_layer()
        self._add_fullscreen()
        self._add_map_title()
        if self.max_bounds and self.bounds:
            self.osm_map.fit_bounds(self.bounds)

    def _attach_supported_tiles(self):
        """Attach additional tile layers to the map."""
        for name, tile in self.tile_options.items():
            if tile.lower() != self.tiles.lower():
                folium.TileLayer(name=name, tiles=tile, show=False).add_to(self.osm_map)

    def _add_fullscreen(self):
        """Enable fullscreen control if required."""
        if self.fullscreen:
            Fullscreen(position=self.fullscreen_position).add_to(self.osm_map)

    def _add_map_title(self):
        """Add a title to the map if provided."""
        if self.map_html_title:
            self.osm_map.get_root().html.add_child(folium.Element(self.map_html_title))

    @staticmethod
    def _sanitize_html(input_html: str) -> str:
        """Sanitize HTML input to prevent script injection."""
        return html.escape(input_html)

    @abstractmethod
    def process_map(self):
        """Abstract method to define map processing logic in subclasses."""
        pass

    def pre_process_map(self):
        """Optional preprocessing step before main processing."""
        pass

    def add_tile_layer(self):
        """Add a layer control to the map."""
        folium.LayerControl().add_to(self.osm_map)

    def generate_map(self) -> folium.Map:
        """Generate and return the processed map."""
        self.pre_process_map()
        self.process_map()
        self._post_process_map()
        return self.osm_map
