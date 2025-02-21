#! python
import os
import tempfile
import unittest
import warnings
import shutil
from pathlib import Path

import numpy as np
from jigsawpy import jigsaw_msh_t
from pyproj import CRS
from shapely import geometry

from ocsmesh import utils
from ocsmesh.mesh.mesh import Mesh, Raster



def edge_at (x, y):
    return geometry.Point(x, y).buffer(0.05)

class BoundaryExtraction(unittest.TestCase):

    def setUp(self):
        """
        Note:
            x = x-index
            y = y-index

            node-index(node-id)

              25(26)             29(30)
          5     *---*---*---*---*
                | \ | \ | \ | \ |
          4     *---*---*---*---*
                | \ | \ | \ | \ |
          3     *---*---*---*---*
                | \ |   | \ | \ |
          2     *---*---*---*---*
                | \ | \ | \ | \ |
          1     *---*---*---*---*
                | \ | \ | \ | \ |
          0     *---*---*---*---*
              0(1)               4(5)

                0   1   2   3   4
        """

        # x and y coords are the same as index (in value)
        mesh_msht = utils.create_rectangle_mesh(nx=5, ny=6, holes=[10])

        with warnings.catch_warnings():
            warnings.filterwarnings(
                'ignore', category=UserWarning, message='Input mesh has no CRS information'
            )

            self.mesh = Mesh(mesh_msht)

    def _chkEqualPermutations(self, a, b):
        # Make sure there are rings!
        assert a[0] == a[-1] and b[0] == b[-1]

        a = np.array(a[:-1])
        b = np.array(b[:-1])
        idx = np.nonzero(a == b[0])
        if len(idx) == 0:
            raise ValueError("One item in arg2 is not found in arg1")
        shift = -idx[0].item()
        self.assertTrue(np.all(np.roll(a, shift=shift) == np.array(b)))

    def test_auto_boundary_fails_if_na_elev(self):
        # Set one node to nan value
        self.mesh.msh_t.value[-1] = np.nan
        with self.assertRaises(ValueError):
            self.mesh.boundaries.auto_generate()


    def test_auto_boundary_1open_correctness(self):
        # Set right boundary to be open
        self.mesh.msh_t.value[self.mesh.msh_t.vert2['coord'][:, 0] > 3] = -10

        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        # Mesh has one segment of each boundary type
        self.assertEqual(len(bdry.open()), 1)
        self.assertEqual(len(bdry.land()), 1)
        self.assertEqual(len(bdry.interior()), 1)

        # Boundaries node ID list
        self.assertEqual(bdry.open().iloc[0]['index_id'], [30, 25, 20, 15, 10, 5])
        self.assertEqual(
            bdry.land().iloc[0]['index_id'],
            [5, 4, 3, 2, 1, 6, 11, 16, 21, 26, 27, 28, 29, 30]
        )
        self._chkEqualPermutations(bdry.interior().iloc[0]['index_id'], [12, 13, 18, 17, 12])


    def test_auto_boundary_2open_correctness(self):
        # Set left and right boundary to be open
        self.mesh.msh_t.value[self.mesh.msh_t.vert2['coord'][:, 0] > 3] = -10
        self.mesh.msh_t.value[self.mesh.msh_t.vert2['coord'][:, 0] < 1] = -10

        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        self.assertEqual(len(bdry.open()), 2)
        self.assertEqual(len(bdry.land()), 2)
        self.assertEqual(len(bdry.interior()), 1)

        # Boundaries node ID list
        self.assertEqual(bdry.open().iloc[0]['index_id'], [1, 6, 11, 16, 21, 26])
        self.assertEqual(bdry.open().iloc[1]['index_id'], [30, 25, 20, 15, 10, 5])
        self.assertEqual(bdry.land().iloc[0]['index_id'], [5, 4, 3, 2, 1])
        self.assertEqual(bdry.land().iloc[1]['index_id'], [26, 27, 28, 29, 30])
        self._chkEqualPermutations(bdry.interior().iloc[0]['index_id'], [12, 13, 18, 17, 12])


    def test_manual_boundary_specification_correctness(self):
        # Shape for wrapping bottom boundary
        shape1 = geometry.box(0.5, -0.5, 3.5, 0.5)
        shape2 = geometry.box(1.5, -0.5, 2.5, 0.5)

        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=shape1)
        bdry.set_land(region=shape2)

        self.assertEqual(len(bdry.open()), 2)
        self.assertEqual(len(bdry.land()), 2)
        self.assertEqual(len(bdry.interior()), 1)

        # Boundaries node ID list
        self.assertEqual(bdry.open().iloc[0]['index_id'], [1, 2])
        self.assertEqual(bdry.open().iloc[1]['index_id'], [4, 5])
        self.assertEqual(
            bdry.land().iloc[0]['index_id'],
            [1, 6, 11, 16, 21, 26, 27, 28, 29, 30, 25, 20, 15, 10, 5]
        )
        self.assertEqual(bdry.land().iloc[1]['index_id'], [2, 3, 4])
        self._chkEqualPermutations(bdry.interior().iloc[0]['index_id'], [12, 13, 18, 17, 12])


    def test_manual_boundary_notaffect_interior(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=geometry.box(0.5, 1.5, 2.5, 3.5))

        self.assertEqual(len(bdry.open()), 0)
        self.assertEqual(len(bdry.land()), 1)
        self.assertEqual(len(bdry.interior()), 1)


    def test_manual_boundary_convex_region(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=geometry.Polygon([
            (-1, 4.5),
            (0.5, 4.5),
            (0.5, 3.5),
            (-0.5, 3.5),
            (-0.5, 1.5),
            (0.5, 1.5),
            (0.5, 0.5),
            (-1, 0.5),
        ]))

        self.assertEqual(len(bdry.open()), 2)
        self.assertEqual(len(bdry.land()), 2)
        self.assertEqual(len(bdry.interior()), 1)

        self.assertEqual(bdry.open().iloc[0]['index_id'], [1, 6, 11])
        self.assertEqual(bdry.open().iloc[1]['index_id'], [16, 21, 26])
        self.assertEqual(bdry.land().iloc[0]['index_id'], [11, 16])
        self.assertEqual(
            bdry.land().iloc[1]['index_id'],
            [26, 27, 28, 29, 30, 25, 20, 15, 10, 5, 4, 3, 2, 1]
        )


    def test_specified_boundary_order_nomerge(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=edge_at(1, 0))
        bdry.set_open(region=edge_at(4, 1))
        bdry.set_open(region=edge_at(0, 5))
        bdry.set_open(region=edge_at(4, 5))

        self.assertEqual(len(bdry.open()), 4)
        self.assertEqual(len(bdry.land()), 4)
        self.assertEqual(len(bdry.interior()), 1)

        self.assertEqual(bdry.open().iloc[0]['index_id'], [1, 2, 3])
        self.assertEqual(bdry.open().iloc[1]['index_id'], [5, 10, 15])
        self.assertEqual(bdry.open().iloc[2]['index_id'], [21, 26, 27])
        self.assertEqual(bdry.open().iloc[3]['index_id'], [29, 30, 25])


    def test_manual_boundary_brokenring_stillconnected(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=edge_at(4, 5))

        # Mesh has one segment of each boundary type
        self.assertEqual(len(bdry.open()), 1)
        self.assertEqual(len(bdry.land()), 1)
        self.assertEqual(len(bdry.interior()), 1)


    def test_manual_boundary_merge_sametype(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_land(region=edge_at(1, 0), merge=True)
        bdry.set_open(region=edge_at(4, 3), merge=True)
        bdry.set_open(region=edge_at(4, 4), merge=True)


        # Mesh has one segment of each boundary type
        self.assertEqual(len(bdry.open()), 1)
        self.assertEqual(len(bdry.land()), 1)
        self.assertEqual(len(bdry.interior()), 1)


    def test_manual_boundary_connect_two_separate_segments(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=edge_at(0, 0), merge=True)
        bdry.set_open(region=edge_at(4, 0), merge=True)

        self.assertEqual(len(bdry.open()), 2)
        self.assertEqual(len(bdry.land()), 2)
        self.assertEqual(len(bdry.interior()), 1)

        self.mesh.boundaries.set_open(region=edge_at(2, 0), merge=True)

        self.assertEqual(len(bdry.open()), 1)
        self.assertEqual(len(bdry.land()), 1)
        self.assertEqual(len(bdry.interior()), 1)


    def test_specified_boundary_order_withmerge(self):
        self.mesh.boundaries.auto_generate()
        # bdry is referring to mesh object and can be mutated
        bdry = self.mesh.boundaries

        bdry.set_open(region=edge_at(1, 0))
        bdry.set_open(region=edge_at(4, 1))
        bdry.set_open(region=edge_at(0, 5))
        bdry.set_open(region=edge_at(4, 5))
        bdry.set_open(region=edge_at(4, 4))
        bdry.set_open(region=edge_at(0, 0), merge=True)
        bdry.set_open(region=edge_at(0, 4), merge=True)

        self.assertEqual(len(bdry.open()), 4)
        self.assertEqual(len(bdry.land()), 4)
        self.assertEqual(len(bdry.interior()), 1)

        self.assertEqual(bdry.open().iloc[0]['index_id'], [6, 1, 2, 3])
        self.assertEqual(bdry.open().iloc[1]['index_id'], [5, 10, 15])
        self.assertEqual(bdry.open().iloc[2]['index_id'], [16, 21, 26, 27])
        self.assertEqual(bdry.open().iloc[3]['index_id'], [20, 25, 30, 29])


    def test_specify_boundary_on_imported_mesh_with_boundary(self):
        self.mesh.boundaries.auto_generate()

        tmpfd, tmppath = tempfile.mkstemp(suffix='.grd')
        self.mesh.write(tmppath, format='grd', overwrite=True)
        imported_mesh = Mesh.open(tmppath)
        os.close(tmpfd)
        os.unlink(tmppath)

        bdry = imported_mesh.boundaries

        bdry.set_open(region=edge_at(1, 0))

        self.assertEqual(len(bdry.open()), 1)
        self.assertEqual(len(bdry.land()), 1)
        self.assertEqual(len(bdry.interior()), 1)

        self.assertEqual(bdry.open().iloc[0]['index_id'], [1, 2, 3])


    def test_auto_find_islands_only(self):
        bdry = self.mesh.boundaries

        self.assertEqual(len(bdry.interior()), 0)

        bdry.find_islands()

        self.assertEqual(len(bdry.interior()), 1)
        self._chkEqualPermutations(bdry.interior().iloc[0]['index_id'], [12, 13, 18, 17, 12])


    def test_specify_boundary_on_mesh_with_no_boundary(self):
        bdry = self.mesh.boundaries

        with self.assertWarns(UserWarning) as w:
            bdry.set_open(region=edge_at(1, 0))
        self.assertTrue('didn\'t have prior boundary' in str(w.warning))

        self.assertEqual(len(bdry.open()), 1)
        self.assertEqual(len(bdry.land()), 0)
        self.assertEqual(len(bdry.interior()), 0)

        self.assertEqual(bdry.open().iloc[0]['index_id'], [1, 2, 3])


class RasterInterpolation(unittest.TestCase):

    def setUp(self):
        self.tdir = Path(tempfile.mkdtemp())

        msht1 = utils.create_rectangle_mesh(
            nx=13, ny=5, x_extent=(-73.9, -71.1), y_extent=(40.55, 40.85),
            holes=[],
        )
        msht1.crs = CRS.from_user_input(4326)
        msht2 = utils.create_rectangle_mesh(
            nx=11, ny=7, x_extent=(-73.9, -71.1), y_extent=(40.55, 40.85),
            holes=[],
        )
        msht2.crs = CRS.from_user_input(4326)
        with warnings.catch_warnings():
            warnings.filterwarnings(
                'ignore', category=UserWarning,
                message='Input mesh has no CRS information'
            )
            self.mesh1 = Mesh(msht1)
            self.mesh2 = Mesh(msht2)

        self.rast = self.tdir / 'rast.tif'

        rast_xy = np.mgrid[-74:-71:0.1, 40.9:40.5:-0.01]
        rast_z = np.ones((rast_xy.shape[1], rast_xy.shape[2], 2))
        rast_z[:, :, 1] = 2
        utils.raster_from_numpy(
            self.rast, rast_z, rast_xy, 4326
        )


    def tearDown(self):
        shutil.rmtree(self.tdir)


    def test_interpolation_io(self):
        rast = Raster(self.rast)

        self.mesh1.interpolate(rast)
        self.assertTrue(np.isclose(self.mesh1.value, 1).all())

        # TODO: Improve the assertion!
        with self.assertRaises(Exception):
            self.mesh1.interpolate(self.mesh2)


    def test_interpolation_band(self):
        rast = Raster(self.rast)

        self.mesh1.interpolate(rast)
        self.assertTrue(np.isclose(self.mesh1.value, 1).all())

        self.mesh1.interpolate(rast, band=2)
        self.assertTrue(np.isclose(self.mesh1.value, 2).all())


    # TODO Add more interpolation tests


if __name__ == '__main__':
    unittest.main()
