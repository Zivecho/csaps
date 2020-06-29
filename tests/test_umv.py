# -*- coding: utf-8 -*-

from itertools import chain, product, permutations

import numpy as np
from scipy.interpolate import CubicSpline
import pytest

import csaps


@pytest.mark.parametrize('x,y,w', [
    ([1], [2], None),
    ([1, 2, 3], [1, 2], None),
    ([(1, 2, 3), (1, 2, 3)], [1, 2, 3], None),
    ([1, 2, 3], [1, 2, 3], [1, 1]),
    ([1, 2, 3], [1, 2, 3], [1, 1, 1, 1]),
    ([1, 2, 3], [1, 2, 3], [(1, 1, 1), (1, 1, 1)]),
    ([1, 2, 3], [(1, 2, 3, 4), (1, 2, 3, 4)], None),
    ([1, 2, 3], np.ones((2, 4, 5)), None),
    ([1, 2, 3], np.ones((2, 4, 3)), np.ones((2, 4, 4))),
    ([1, 2, 3], [(1, 2, 3), (1, 2, 3)], [(1, 1, 1, 1), (1, 1, 1, 1)]),
    ([1, 2, 3], [(1, 2, 3), (1, 2, 3)], [(1, 1, 1), (1, 1, 1), (1, 1, 1)])
])
def test_invalid_data(x, y, w):
    with pytest.raises(ValueError):
        csaps.CubicSmoothingSpline(x, y, weights=w)


@pytest.mark.parametrize('y', [
    # 1D (2, )
    [2, 4],

    # 2D (2, 2)
    [(2, 4), (3, 5)],

    # 2D (3, 2)
    [(2, 4), (3, 5), (4, 6)],

    # 3D (2, 2, 2)
    [[(1, 2), (3, 4)],
     [(5, 6), (7, 8)]],

    # 1D (3, )
    [2, 4, 6],

    # 2D (2, 5)
    [(1, 2, 3, 4, 5), (3, 4, 5, 6, 7)],

    # 2D (3, 3)
    [(2, 4, 6), (3, 5, 7), (4, 6, 8)],

    # 3D (2, 2, 3)
    [[(2, 4, 6), (3, 5, 7)],
     [(2, 4, 6), (3, 5, 7)]],

    # 1D (4, )
    [2, 4, 6, 8],

    # 2D (2, 4)
    [(2, 4, 6, 8), (3, 5, 7, 9)],

    # 2D (3, 4)
    [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],

    # 3D (2, 2, 4)
    [[(2, 4, 6, 8), (3, 5, 7, 9)],
     [(2, 4, 6, 8), (3, 5, 7, 9)]],

    # 3D (2, 3, 4)
    [[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
     [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]],

    # 3D (3, 2, 4)
    [[(2, 4, 6, 8), (3, 5, 7, 9)],
     [(2, 4, 6, 8), (3, 5, 7, 9)],
     [(2, 4, 6, 8), (3, 5, 7, 9)]],

    # 3D (3, 3, 4)
    [[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
     [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
     [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]],

    # 4D (2, 2, 2, 4)
    [[[(2, 4, 6, 8), (3, 5, 7, 9)], [(2, 4, 6, 8), (3, 5, 7, 9)]],
     [[(2, 4, 6, 8), (3, 5, 7, 9)], [(2, 4, 6, 8), (3, 5, 7, 9)]]],

    # 4D (3, 2, 2, 4)
    [[[(2, 4, 6, 8), (3, 5, 7, 9)], [(2, 4, 6, 8), (3, 5, 7, 9)]],
     [[(2, 4, 6, 8), (3, 5, 7, 9)], [(2, 4, 6, 8), (3, 5, 7, 9)]],
     [[(2, 4, 6, 8), (3, 5, 7, 9)], [(2, 4, 6, 8), (3, 5, 7, 9)]]],

    # 4D (3, 2, 3, 4)
    [[[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)], [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]],
     [[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)], [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]],
     [[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)], [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]]],

    # 4D (3, 3, 3, 4)
    [[[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
      [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
      [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]],

     [[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
      [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
      [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]],

     [[(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
      [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)],
      [(2, 4, 6, 8), (3, 5, 7, 9), (4, 6, 8, 10)]]],

])
def test_vectorize(y):
    x = np.arange(np.array(y).shape[-1])

    ys = csaps.CubicSmoothingSpline(x, y)(x)
    np.testing.assert_allclose(ys, y)


@pytest.mark.parametrize('shape, axis', chain(
    *map(product, [
        # shape
        [(2,), (4,)],
        permutations((2, 4), 2),
        permutations((3, 4, 5), 3),
        permutations((3, 4, 5, 6), 4)
    ], [
        # axis
        range(-1, 1),
        range(-2, 2),
        range(-3, 3),
        range(-4, 4),
    ])
))
def test_axis(shape, axis):
    y = np.arange(int(np.prod(shape))).reshape(shape)
    x = np.arange(np.array(y).shape[axis])

    s = csaps.CubicSmoothingSpline(x, y, axis=axis)

    ys = s(x)
    np.testing.assert_allclose(ys, y)

    ss = s.spline
    axis = len(shape) + axis if axis < 0 else axis

    assert ss.axis == axis
    assert ss.order == 2 if len(x) < 3 else 4
    assert ss.pieces == len(x) - 1
    assert ss.shape == shape


def test_zero_smooth():
    x = [1., 2., 4., 6.]
    y = [2., 4., 5., 7.]

    sp = csaps.CubicSmoothingSpline(x, y, smooth=0.)

    assert sp.smooth == pytest.approx(0.)

    ys = sp(x)

    assert ys == pytest.approx([2.440677966101695,
                                3.355932203389830,
                                5.186440677966102,
                                7.016949152542373])


def test_auto_smooth():
    np.random.seed(1234)

    x = np.linspace(0, 2 * np.pi, 21)
    y = np.sin(x) + (np.random.rand(21) - .5) * .1

    sp = csaps.CubicSmoothingSpline(x, y)

    xi = np.linspace(x[0], x[-1], 120)
    yi = sp(xi)

    np.testing.assert_almost_equal(sp.smooth, 0.996566686)

    desired_yi = [
        -0.0235609972734076, 0.0342554130011887, 0.0917604768962524,
        0.148642848032251, 0.204591180029653, 0.259294126508924,
        0.312440351240669, 0.363812477806949, 0.413516746584544,
        0.461729017734914, 0.508625151419519, 0.554381007799819,
        0.59917235322775, 0.643050468816528, 0.685696744725134,
        0.726724183969348, 0.765745789564952, 0.802374564527724,
        0.836223661222756, 0.866972935842014, 0.894473725242276,
        0.918604542323229, 0.939243899984561, 0.956270311125961,
        0.969562963467305, 0.979144106608908, 0.985355180101302,
        0.988580811987222, 0.989205630309408, 0.987614263110598,
        0.984190455154498, 0.979211074442117, 0.972745418402277,
        0.964838935929978, 0.955537075920216, 0.944885287267991,
        0.932927490881626, 0.919589386774692, 0.904596282338286,
        0.88765407387356, 0.868468657681665, 0.846745930063754,
        0.822194253635299, 0.794653654806466, 0.76415937272086,
        0.73076244387651, 0.694513904771452, 0.655464791903716,
        0.613667457460308, 0.569225401037061, 0.522308564522944,
        0.473091330257213, 0.421748080579123, 0.368453197827928,
        0.313386409949078, 0.256884901954999, 0.199465270307742,
        0.141653871417018, 0.0839770616925367, 0.0269611975440111,
        -0.0288790108903068, -0.0832967177157068, -0.136312941281018,
        -0.187960346206531, -0.238271597112534, -0.287279358619317,
        -0.335016296758048, -0.381515103495269, -0.426808493559216,
        -0.47092918245087, -0.513909885671217, -0.555783318721242,
        -0.596577904130849, -0.636257828862702, -0.674737831212602,
        -0.711931377484918, -0.74775193398402, -0.782112967014277,
        -0.814916147256374, -0.845917383266534, -0.874774272419685,
        -0.901142570534573, -0.92467803342995, -0.945036416924564,
        -0.961906593475871, -0.975319318974765, -0.985507042193372,
        -0.99270481875293, -0.997147704274675, -0.999070754379844,
        -0.998693087710525, -0.996095112164348, -0.991285814362011,
        -0.984273590665723, -0.975066837437697, -0.963673951040142,
        -0.95006546257481, -0.933932055202886, -0.914838983410284,
        -0.892350910038224, -0.86603249792793, -0.835448409920623,
        -0.800282146364173, -0.76096707154776, -0.718228237424455,
        -0.672791349033563, -0.625382111414392, -0.576726229606248,
        -0.527490657611685, -0.478024578050658, -0.428570228926154,
        -0.379369767649891, -0.330665351633583, -0.282699138288946,
        -0.23565484652653, -0.189444552928148, -0.143901464676976,
        -0.098858780436212, -0.0541496988690512, -0.00960741863869263,
    ]

    np.testing.assert_allclose(yi, desired_yi)


@pytest.mark.parametrize('x,y,xi,yid', [
    ([1., 2.], [3., 4.], [1., 1.5, 2.], [3., 3.5, 4.]),
    ([1., 2., 3.], [3., 4., 5.], [1., 1.5, 2., 2.5, 3.], [3., 3.5, 4., 4.5, 5.]),
    ([1., 2., 4., 6.], [2., 4., 5., 7.], np.linspace(1., 6., 10), [
        2.2579392157892, 3.0231172855707, 3.6937304019483,
        4.21971044584031, 4.65026761247821, 5.04804510368134,
        5.47288175793241, 5.94265482897362, 6.44293945952166,
        6.95847986982311
    ]),
])
def test_npoints(x, y, xi, yid):
    sp = csaps.CubicSmoothingSpline(x, y)
    yi = sp(xi)

    np.testing.assert_allclose(yi, yid)


@pytest.mark.parametrize('w,yid', [
    ([0.5, 1, 0.7, 1.2], [
        2.39572102230177, 3.13781163365086, 3.78568993197139,
        4.28992448591238, 4.7009959256016, 5.08290363789967,
        5.49673867759808, 5.9600748344541, 6.45698622142886,
        6.97068522346297
    ])
])
def test_weighted(w, yid):
    x = [1., 2., 4., 6.]
    y = [2., 4., 5., 7.]
    xi = np.linspace(1., 6., 10)

    sp = csaps.CubicSmoothingSpline(x, y, weights=w)
    yi = sp(xi)

    np.testing.assert_allclose(yi, yid)


@pytest.mark.skip(reason='It may take a long time')
def test_big_vectorized():
    x = np.linspace(0, 10000, 10000)
    y = np.random.rand(1000, 10000)
    xi = np.linspace(0, 10000, 20000)

    csaps.CubicSmoothingSpline(x, y)(xi)


def test_cubic_bc_natural():
    np.random.seed(1234)
    x = np.linspace(0, 5, 20)
    xi = np.linspace(0, 5, 100)
    y = np.sin(x) + np.random.randn(x.size) * 0.3

    cs = CubicSpline(x, y, bc_type='natural')
    ss = csaps.CubicSmoothingSpline(x, y, smooth=1.0)

    y_cs = cs(xi)
    y_ss = ss(xi)

    assert cs.c == pytest.approx(ss.spline.c)
    assert y_cs == pytest.approx(y_ss)
