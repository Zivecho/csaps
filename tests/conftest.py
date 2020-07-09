# -*- coding: utf-8 -*-

from typing import NamedTuple, Tuple

import pytest
import numpy as np


class UnivariateData(NamedTuple):
    x: np.ndarray
    y: np.ndarray
    xi: np.ndarray
    yi: np.ndarray
    yi_d1: np.ndarray
    yi_d2: np.ndarray
    yi_ad1: np.ndarray
    integral: float
    smooth: float


@pytest.fixture(scope='session')
def univariate_data() -> UnivariateData:
    """Univariate exponential noisy data sample
    """

    x = np.linspace(-5., 5., 25)
    y = np.array([
        0.015771474002402, 0.161329316958106, 0.133494845724251, 0.281006799675995, 0.343006057841707,
        0.278153538271205, 0.390818717714371, 0.679913441859782, 0.868622194535066, 0.981580573494033,
        0.942184497801730, 1.062903014773386, 1.145038880551641, 1.126415085211218, 0.945914543251488,
        0.887159638891092, 0.732105338022297, 0.443482323476481, 0.539727427655155, 0.461168113877247,
        0.218479110576478, 0.230018078091912, 0.024790896515009, 0.085343887446749, 0.238257669483491,
    ])

    xi = np.linspace(-5., 5., 100)
    yi = np.array([
        0.027180620841235, 0.055266722842603, 0.081889893919483, 0.105587203147386, 0.124895719601823,
        0.138845028755704, 0.149340839533796, 0.159329894062361, 0.171760370375527, 0.189200881318870,
        0.210916416800576, 0.234470952365328, 0.257414405587860, 0.277378327575793, 0.293102526279226,
        0.304125512134026, 0.310003428419162, 0.310378253365020, 0.306866169084541, 0.303057561573221,
        0.302628651777970, 0.309224604926640, 0.325083877194873, 0.350493015304832, 0.385594789501554,
        0.430522770904909, 0.484297436489629, 0.543777468816333, 0.605573174066145, 0.666295736381613,
        0.723192861937517, 0.775270813640449, 0.821836995165352, 0.862198810187169, 0.895800934807012,
        0.922637134830661, 0.942838448490065, 0.956535914017174, 0.964201067822575, 0.968293836555378,
        0.971993858758319, 0.978481765680190, 0.990589029304687, 1.008108142826666, 1.029266848660349,
        1.052279957395322, 1.075372085392223, 1.096900972159461, 1.115320296869396, 1.129085856740936,
        1.136683629726760, 1.137293750656333, 1.130790511235904, 1.117078383905495, 1.096086194963815,
        1.068845910308547, 1.037920180955498, 1.005984407266240, 0.975701613072527, 0.948237262097737,
        0.921848333557257, 0.894457640361302, 0.863988793631958, 0.828944108099870, 0.789424716879042,
        0.745805539756215, 0.698461496518133, 0.648486500475627, 0.599850439035886, 0.557242193130187,
        0.525350643689810, 0.507735527292642, 0.501362772528695, 0.500811632605449, 0.500658068764342,
        0.495835799645429, 0.484392358284163, 0.465978560872775, 0.440258473877521, 0.407065767289394,
        0.368536648551231, 0.328466725991911, 0.290688242301654, 0.258885509945327, 0.233340446204702,
        0.210932573178451, 0.188393482739897, 0.162519263868190, 0.133027485558460, 0.103689479346398,
        0.078575174479879, 0.061741087177262, 0.055620757085748, 0.059495661916820, 0.072285127585087,
        0.092908288203052, 0.120145221354215, 0.152391824997807, 0.187978208969687, 0.225234483105709,
    ])

    yi_d1 = np.array([
        0.280466245838951, 0.273224737762734, 0.251500213534080, 0.215292673152991, 0.164602116619466,
        0.116145957650883, 0.096535589511642, 0.106112183910259, 0.144875740846734, 0.197795478854448,
        0.228129487681658, 0.234207680498741, 0.216030057305698, 0.177475843585326, 0.133130927152951,
        0.084391829182380, 0.031258549673615, -0.021170315259270, -0.042303188931811, -0.027041475229932,
        0.024614825846369, 0.110206101347581, 0.204043060467737, 0.299293445013758, 0.395957254985645,
        0.492941634313625, 0.566203749462694, 0.605907895804895, 0.612054073340229, 0.584850885702982,
        0.540569416367585, 0.489431243414127, 0.431436366842608, 0.366584786653029, 0.298953493902567,
        0.232619479648399, 0.167582743890526, 0.103843286628946, 0.052958588898598, 0.033326273571420,
        0.045182207607307, 0.088526391006262, 0.149532116870303, 0.194400768337705, 0.221596044642023,
        0.231117945783259, 0.223432442001698, 0.200291581400812, 0.161863113267105, 0.108147037600576,
        0.040936089987355, -0.029013316055774, -0.099908444942684, -0.171749296673372, -0.242607045639946,
        -0.292336179937763, -0.315578850656009, -0.312335057794686, -0.284075133096558, -0.263146374902438,
        -0.262781768897203, -0.282981315080855, -0.323555358312161, -0.369710797575063, -0.412154530949217,
        -0.450886558434622, -0.485906880031279, -0.495861388073734, -0.459395974896536, -0.376510640499682,
        -0.247205384883174, -0.109806593527812, -0.025323614749973, 0.005461380318084, -0.017451608323641,
        -0.079895387689795, -0.147239041593955, -0.217908437482194, -0.291903575354511, -0.361164895715347,
        -0.395388454861403, -0.391672811374275, -0.350017965253966, -0.279210971886386, -0.231974163587015,
        -0.217094595741764, -0.234572268350635, -0.279299010631809, -0.297922816641862, -0.276254323097967,
        -0.214293530000122, -0.113633905254560, -0.009331742798295, 0.084271746212620, 0.167176561778182,
        0.239337131717303, 0.297198825904872, 0.338528607467420, 0.363326476404950, 0.371592432717459,
    ])

    yi_d2 = np.array([
        0.0, -0.143381859909114, -0.286763719818227, -0.430145579727340, -0.573527439636453, -0.338618109140893,
        -0.049667180016091, 0.239283749108707, 0.528234678233509, 0.420372976639513, 0.180240398139254,
        -0.059892180361004, -0.300024758861262, -0.417263474066444, -0.460765871294580, -0.504268268522715,
        -0.547770665750851, -0.389368656861538, -0.029062241854775, 0.331244173151988, 0.691550588158752,
        0.921989439431505, 0.935982351147577, 0.949975262863648, 0.963968174579720, 0.891406885569776,
        0.559182994381786, 0.226959103193797, -0.105264787994194, -0.404445863511035, -0.472327229329834,
        -0.540208595148634, -0.608089960967433, -0.675971326786232, -0.663128269672918, -0.650285212559604,
        -0.637442155446290, -0.624599098332976, -0.350226756086249, -0.038493087391889, 0.273240581302470,
        0.584974249996826, 0.531682856584531, 0.356716442470013, 0.181750028355495, 0.006783614240977,
        -0.153420862661300, -0.304768177236235, -0.456115491811170, -0.607462806386105, -0.687817791750278,
        -0.697180447903692, -0.706543104057105, -0.715905760210518, -0.623426424267251, -0.361210434829511,
        -0.098994445391772, 0.163221544045968, 0.308987259456777, 0.105402152786806, -0.098182953883166,
        -0.301768060553138, -0.475311792852036, -0.438565904553427, -0.401820016254817, -0.365074127956207,
        -0.328328239657597, 0.131228980416978, 0.590786200491558, 1.050343420566138, 1.509900640640717,
        1.102186509264039, 0.570576470537193, 0.038966431810342, -0.492643606916509, -0.650239750830002,
        -0.683164596472375, -0.716089442114750, -0.749014287757124, -0.526612288580197, -0.151014182511690,
        0.224583923556814, 0.600182029625318, 0.627812742411677, 0.307476061915880, -0.012860618579924,
        -0.333197299075721, -0.383822562291567, 0.015071203292524, 0.413964968876607, 0.812858734460697,
        1.085549841871512, 0.979632974762537, 0.873716107653561, 0.767799240544586, 0.654663739950773,
        0.490997804963078, 0.327331869975386, 0.163665934987692, 0.0,
    ])

    yi_ad1 = np.array([
        0, 0.004170164373445, 0.011115737580173, 0.020615063419503, 0.032298714890302, 0.045660376813401,
        0.060231892427910, 0.075813180885901, 0.092501952567935, 0.110686524880963, 0.130868677637032,
        0.153357821207108, 0.178215971638707, 0.205258950314118, 0.234108819065114, 0.264313291890776,
        0.295375081800281, 0.326753151565222, 0.357945080592172, 0.388736333089680, 0.419282624940839,
        0.450110713389674, 0.482066710123764, 0.516105768238528, 0.553199731265708, 0.594334805898634,
        0.640475555315434, 0.692364771746437, 0.750407558205033, 0.814666627160915, 0.884880469463989,
        0.960603933483209, 1.041315254368523, 1.126422708045129, 1.215268077688877, 1.307164784955765,
        1.401436021211426, 1.497418214006542, 1.594468550710834, 1.692085995899572, 1.790070243397785,
        1.888542259780677, 1.987937674642304, 2.088843826542736, 2.191718430510039, 2.296838961049921,
        2.404302725268220, 2.514033161345466, 2.625794182200862, 2.739193700617453, 2.853684030369255,
        2.968590847531448, 3.083200836550669, 3.196790651555201, 3.308627528048506, 3.418009815729590,
        3.524431905730442, 3.627656652140256, 3.727717073374330, 3.824867908686134, 3.919316366135970,
        4.011066165813679, 4.099911213450951, 4.185452118972609, 4.267224006141539, 4.344793819826894,
        4.417766375583358, 4.485802516053269, 4.548818831389975, 4.607187379681194, 4.661753843351136,
        4.713812579632492, 4.764705308291650, 4.815294002191847, 4.865892761884743, 4.916274580927416,
        4.965838312719173, 5.013896930882124, 5.059729392707482, 5.102583399629591, 5.141784337510146,
        5.176983368905221, 5.208218404675820, 5.235912583098308, 5.260732316617858, 5.283157696497049,
        5.303340539569319, 5.321103131201137, 5.336045569661458, 5.347982548219602, 5.357135151392904,
        5.364135482984910, 5.369974165591079, 5.375708539464273, 5.382293644794382, 5.390575362167333,
        5.401286443327005, 5.415015799831229, 5.432185121115394, 5.453047420840733,
    ])

    integral = 5.453047420840733
    smooth = 0.992026535689226

    return UnivariateData(x, y, xi, yi, yi_d1, yi_d2, yi_ad1, integral, smooth)


class NdGrid2dData(NamedTuple):
    xy: Tuple[np.ndarray, np.ndarray]
    z: np.ndarray
    zi: np.ndarray
    zi_d1: np.ndarray
    zi_d2: np.ndarray
    zi_ad1: np.ndarray
    integral: float
    smooth: Tuple[float, float]


@pytest.fixture(scope='session')
def ndgrid_2d_data() -> NdGrid2dData:
    xy = (np.linspace(-3.0, 3.0, 5), np.linspace(-3.5, 3.5, 7))

    z = np.array(
        [[-0.153527183790132, 0.360477327564227, -0.400800187993851, -0.661751768834967,
          1.39827150034968, 1.044246054228617, 0.069681364921588],
         [0.211217178485871, 0.592683030706752, 1.294599451385471, -4.924883983709012,
          -2.641771353280953, 0.245330967159293, 0.171928943618129],
         [1.012132959440344, 0.132792505223302, -3.970096642307903, 0.702129940268655,
          4.729521910567126, 0.208213433055832, -0.40275495492284],
         [0.35749708646856, 2.409904780478664, 0.892801916808247, 7.563804764350773,
          2.510824654279176, 0.317303593544217, 0.393080231785911],
         [0.000706314884567, 1.009080744382149, -0.45874273220015, -0.323494125914201,
          -1.700362064179427, -1.394209767885332, -0.645566364768713]
         ])

    zi = np.array(
        [[-0.055377680470166, 0.195656616225213, -0.295030253111251, -0.830533929888634,
          0.193176060095987, 0.770374649757329, 0.252865339751650],
         [0.471994652733459, 0.293417006151304, -0.758106516247562, -1.960431309380293,
          -0.781936045165379, 0.216341632490716, 0.180333235920312],
         [0.875919224697303, 0.067344259041702, -0.735889940425535, 0.882313890047783,
          2.056305063365266, 0.896850201038262, -0.190314083560006],
         [0.606245376082951, 0.941947682137626, 1.225331206624579, 3.379540894700002,
          2.581257432070516, 0.581783850872262, -0.187728390603794],
         [0.183397630824828, 0.805748594104382, 0.503605325241657, 0.264260721868410,
          -0.874052860773297, -1.188420383689933, -0.617919628357980]
         ])

    zi_d1 = np.array(
        [[-0.121812472223565, -0.157326929297246, -0.828962829944406, -0.640465943383180,
          0.503884652683063, 0.662549465069741, 0.501482011524879],
         [-0.470497745190257, -0.466533613272337, 0.403062598673842, 0.767903075058928,
          -0.334118185393139, -0.545086449738045, -0.154825057274055],
         [0.194607321700336, 0.192434581435788, 1.293210437573223, 0.562712202846881,
          -1.370259457802591, -0.823157992133989, -0.176531696944242],
         [0.607431089728563, 0.510938352696447, -0.237734672001804, -1.058160086418725,
          -0.269494123744448, 0.632430110330214, 0.577443254979813],
         [0.006464517899505, -0.138732754726110, -1.426802191857966, -1.065472485030174,
          1.029409644646945, 1.158453840382574, 0.696817777775121]
         ])

    zi_d2 = np.array(
        [[0., 0., 0., 0., 0., 0., 0.],
         [0., 0.090236774837945, 3.432579482518258, -3.029508420063717,
          -2.105055823406707, 1.260180219448802, 0.],
         [0., -0.104263911255016, -2.890141730806884, -0.016560671330926,
          3.251809714350141, -0.674203298932788, 0.],
         [0., -0.111324652785139, -1.121581432777390, 3.822735995622450,
          -0.837099042473098, -0.929483902301833, 0.],
         [0., 0., 0., 0., 0., 0., 0.]
         ])

    zi_ad1 = np.array(
        [[0., 0., 0., 0., 0., 0., 0.],
         [0., 0.509395864624591, 0.476401125691113, -1.598603993938397,
          -3.760699480840437, -3.750794105947393, -3.076469947082991],
         [0., 1.318187655218603, 0.563946491827388, -3.255188072198998,
          -5.625801866969895, -4.504932326883326, -3.364137445816383],
         [0., 2.511070517473814, 2.161223166080562, 0.664448782633726,
          3.261109214575526, 7.566477396430049, 9.182402413317154],
         [0., 3.799550963870154, 5.127806810771760, 6.567161731071815,
          12.269550101243563, 17.158134933110624, 18.133537415972746]
         ])

    integral = 18.133537415972746
    smooth = (0.727272727272727, 0.850021862702230)

    return NdGrid2dData(xy, z, zi, zi_d1, zi_d2, zi_ad1, integral, smooth)


class SurfaceData(NamedTuple):
    xy: Tuple[np.ndarray, np.ndarray]
    z: np.ndarray


@pytest.fixture(scope='session')
def surface_data() -> SurfaceData:
    """2-d surface data sample
    """
    np.random.seed(12345)

    xy = (np.linspace(-3.0, 3.0, 61), np.linspace(-3.5, 3.5, 51))
    i, j = np.meshgrid(*xy, indexing='ij')

    z = (3 * (1 - j) ** 2. * np.exp(-(j ** 2) - (i + 1) ** 2)
         - 10 * (j / 5 - j ** 3 - i ** 5) * np.exp(-j ** 2 - i ** 2)
         - 1 / 3 * np.exp(-(j + 1) ** 2 - i ** 2))

    z += (np.random.randn(*z.shape) * 0.75)

    return SurfaceData(xy, z)