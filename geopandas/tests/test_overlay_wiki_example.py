from shapely.geometry import box

from geopandas import GeoDataFrame, overlay

import pytest


# Issue #305

class TestOverlayWikiExample:

    def setup_method(self):
        self.layer_a = GeoDataFrame([{'geometry': box(0, 2, 6, 6)}])

        self.layer_b = GeoDataFrame([{'geometry': box(4, 0, 10, 4)}])

        self.intersection = GeoDataFrame([{'geometry': box(4, 2, 6, 4)}])

        self.union = GeoDataFrame(
            [{'geometry': box(0, 2, 6, 6)}, {'geometry': box(4, 0, 10, 4)}])

        self.a_difference_b = GeoDataFrame(
            [{'geometry': box(0, 2, 4, 6)}, {'geometry': box(4, 4, 6, 6)}])

        self.b_difference_a = GeoDataFrame(
            [{'geometry': box(4, 0, 6, 2)}, {'geometry': box(6, 0, 10, 4)}])

        self.symmetric_difference = GeoDataFrame(
            [{'geometry': box(0, 2, 4, 6)}, {'geometry': box(4, 4, 6, 6)},
             {'geometry': box(4, 0, 6, 2)}, {'geometry': box(6, 0, 10, 4)}])

        self.a_identity_b = GeoDataFrame([{'geometry': box(0, 2, 6, 6)}])

        self.b_identity_a = GeoDataFrame([{'geometry': box(4, 0, 10, 4)}])

    def test_intersection(self):
        df_result = overlay(self.layer_a, self.layer_b, how="intersection")
        assert df_result.geom_equals(self.intersection).bool()

    def test_union(self):
        df_result = overlay(self.layer_a, self.layer_b, how="union")
        assert df_result.geom_equals(self.union).bool()

    def test_a_difference_b(self):
        df_result = overlay(self.layer_a, self.layer_b, how="difference")
        assert df_result.geom_equals(self.a_difference_b).bool()

    def test_b_difference_a(self):
        df_result = overlay(self.layer_b, self.layer_a, how="difference")
        assert df_result.geom_equals(self.b_difference_a).bool()

    def test_symmetric_difference(self):
        df_result = overlay(self.layer_a, self.layer_b,
                            how="symmetric_difference")
        assert df_result.geom_equals(self.symmetric_difference).bool()
