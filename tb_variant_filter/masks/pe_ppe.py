from .. import Location, doc_inherit
from io import StringIO
import pandas as pd
from py2neo import Graph
import requests

from ..region_list import RegionList


# noinspection PyPep8Naming
class PE_PPE_Regions(RegionList):
    url = "https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.12981"
    name = "PE_PPE"
    description = 'PE/PPE genes'
    project_url = url  # URL of the Fishbein et al paper
    regions = [
        Location(locus="Rv0096", start=105324, end=106715, strand=1),
        Location(locus="Rv0109", start=131382, end=132872, strand=1),
        Location(locus="Rv0124", start=149533, end=150996, strand=1),
        Location(locus="Rv0151c", start=177543, end=179309, strand=-1),
        Location(locus="Rv0152c", start=179319, end=180896, strand=-1),
        Location(locus="Rv0159c", start=187433, end=188839, strand=-1),
        Location(locus="Rv0160c", start=188931, end=190439, strand=-1),
        Location(locus="Rv0256c", start=307877, end=309547, strand=-1),
        Location(locus="Rv0278c", start=333437, end=336310, strand=-1),
        Location(locus="Rv0279c", start=336560, end=339073, strand=-1),
        Location(locus="Rv0280", start=339364, end=340974, strand=1),
        Location(locus="Rv0285", start=349624, end=349932, strand=1),
        Location(locus="Rv0286", start=349935, end=351476, strand=1),
        Location(locus="Rv0297", start=361334, end=363109, strand=1),
        Location(locus="Rv0304c", start=366150, end=372764, strand=-1),
        Location(locus="Rv0305c", start=372820, end=375711, strand=-1),
        Location(locus="Rv0335c", start=399535, end=400050, strand=-1),
        Location(locus="Rv0354c", start=424269, end=424694, strand=-1),
        Location(locus="Rv0355c", start=424777, end=434679, strand=-1),
        Location(locus="Rv0388c", start=467459, end=468001, strand=-1),
        Location(locus="Rv0442c", start=530751, end=532214, strand=-1),
        Location(locus="Rv0453", start=543174, end=544730, strand=1),
        Location(locus="Rv0532", start=622793, end=624577, strand=1),
        Location(locus="Rv0578c", start=671996, end=675916, strand=-1),
        Location(locus="Rv0742", start=832981, end=833508, strand=1),
        Location(locus="Rv0746", start=835701, end=838052, strand=1),
        Location(locus="Rv0747", start=838451, end=840856, strand=1),
        Location(locus="Rv0754", start=846159, end=847913, strand=1),
        Location(locus="Rv0755c", start=848103, end=850040, strand=-1),
        Location(locus="Rv0832", start=924951, end=925364, strand=1),
        Location(locus="Rv0833", start=925361, end=927610, strand=1),
        Location(locus="Rv0834c", start=927837, end=930485, strand=-1),
        Location(locus="Rv0872c", start=968424, end=970244, strand=-1),
        Location(locus="Rv0878c", start=976872, end=978203, strand=-1),
        Location(locus="Rv0915c", start=1020058, end=1021329, strand=-1),
        Location(locus="Rv0916c", start=1021344, end=1021643, strand=-1),
        Location(locus="Rv0977", start=1090373, end=1093144, strand=1),
        Location(locus="Rv0978c", start=1093361, end=1094356, strand=-1),
        Location(locus="Rv0980c", start=1095078, end=1096451, strand=-1),
        Location(locus="Rv1039c", start=1161297, end=1162472, strand=-1),
        Location(locus="Rv1040c", start=1162549, end=1163376, strand=-1),
        Location(locus="Rv1067c", start=1188421, end=1190424, strand=-1),
        Location(locus="Rv1068c", start=1190757, end=1192148, strand=-1),
        Location(locus="Rv1087", start=1211560, end=1213863, strand=1),
        Location(locus="Rv1088", start=1214513, end=1214947, strand=1),
        Location(locus="Rv1089", start=1214769, end=1215131, strand=1),
        Location(locus="Rv1091", start=1216469, end=1219030, strand=1),
        Location(locus="Rv1135c", start=1262272, end=1264128, strand=-1),
        Location(locus="Rv1168c", start=1298764, end=1299804, strand=-1),
        Location(locus="Rv1169c", start=1299822, end=1300124, strand=-1),
        Location(locus="Rv1172c", start=1301755, end=1302681, strand=-1),
        Location(locus="Rv1195", start=1339003, end=1339302, strand=1),
        Location(locus="Rv1196", start=1339349, end=1340524, strand=1),
        Location(locus="Rv1214c", start=1357293, end=1357625, strand=-1),
        Location(locus="Rv1243c", start=1384989, end=1386677, strand=-1),
        Location(locus="Rv1325c", start=1488154, end=1489965, strand=-1),
        Location(locus="Rv1361c", start=1532443, end=1533633, strand=-1),
        Location(locus="Rv1386", start=1561464, end=1561772, strand=1),
        Location(locus="Rv1387", start=1561769, end=1563388, strand=1),
        Location(locus="Rv1396c", start=1572127, end=1573857, strand=-1),
        Location(locus="Rv1430", start=1606386, end=1607972, strand=1),
        Location(locus="Rv1441c", start=1618209, end=1619684, strand=-1),
        Location(locus="Rv1450c", start=1630638, end=1634627, strand=-1),
        Location(locus="Rv1452c", start=1636004, end=1638229, strand=-1),
        Location(locus="Rv1468c", start=1655609, end=1656721, strand=-1),
        Location(locus="Rv1548c", start=1751297, end=1753333, strand=-1),
        Location(locus="Rv1646", start=1855764, end=1856696, strand=1),
        Location(locus="Rv1651c", start=1862347, end=1865382, strand=-1),
        Location(locus="Rv1705c", start=1931497, end=1932654, strand=-1),
        Location(locus="Rv1706c", start=1932694, end=1933878, strand=-1),
        Location(locus="Rv1753c", start=1981614, end=1984775, strand=-1),
        Location(locus="Rv1759c", start=1989833, end=1992577, strand=-1),
        Location(locus="Rv1768", start=2000614, end=2002470, strand=1),
        Location(locus="Rv1787", start=2025301, end=2026398, strand=1),
        Location(locus="Rv1788", start=2026477, end=2026776, strand=1),
        Location(locus="Rv1789", start=2026790, end=2027971, strand=1),
        Location(locus="Rv1790", start=2028425, end=2029477, strand=1),
        Location(locus="Rv1791", start=2029904, end=2030203, strand=1),
        Location(locus="Rv1800", start=2039453, end=2041420, strand=1),
        Location(locus="Rv1801", start=2042001, end=2043272, strand=1),
        Location(locus="Rv1802", start=2043384, end=2044775, strand=1),
        Location(locus="Rv1803c", start=2044923, end=2046842, strand=-1),
        Location(locus="Rv1806", start=2048072, end=2048371, strand=1),
        Location(locus="Rv1807", start=2048398, end=2049597, strand=1),
        Location(locus="Rv1808", start=2049921, end=2051150, strand=1),
        Location(locus="Rv1809", start=2051282, end=2052688, strand=1),
        Location(locus="Rv1818c", start=2061178, end=2062674, strand=-1),
        Location(locus="Rv1840c", start=2087971, end=2089518, strand=-1),
        Location(locus="Rv1917c", start=2162932, end=2167311, strand=-1),
        Location(locus="Rv1918c", start=2167649, end=2170612, strand=-1),
        Location(locus="Rv1983", start=2226244, end=2227920, strand=1),
        Location(locus="Rv2098c", start=2356729, end=2358033, strand=-1),
        Location(locus="Rv2099c", start=2358033, end=2358206, strand=-1),
        Location(locus="Rv2107", start=2367359, end=2367655, strand=1),
        Location(locus="Rv2108", start=2367711, end=2368442, strand=1),
        Location(locus="Rv2123", start=2381071, end=2382492, strand=1),
        Location(locus="Rv2126c", start=2387202, end=2387972, strand=-1),
        Location(locus="Rv2162c", start=2423240, end=2424838, strand=-1),
        Location(locus="Rv2328", start=2600731, end=2601879, strand=1),
        Location(locus="Rv2340c", start=2617667, end=2618908, strand=-1),
        Location(locus="Rv2352c", start=2632923, end=2634098, strand=-1),
        Location(locus="Rv2353c", start=2634528, end=2635592, strand=-1),
        Location(locus="Rv2356c", start=2637688, end=2639535, strand=-1),
        Location(locus="Rv2371", start=2651753, end=2651938, strand=1),
        Location(locus="Rv2396", start=2692799, end=2693884, strand=1),
        Location(locus="Rv2408", start=2706017, end=2706736, strand=1),
        Location(locus="Rv2430c", start=2727336, end=2727920, strand=-1),
        Location(locus="Rv2431c", start=2727967, end=2728266, strand=-1),
        Location(locus="Rv2487c", start=2795301, end=2797385, strand=-1),
        Location(locus="Rv2490c", start=2801254, end=2806236, strand=-1),
        Location(locus="Rv2519", start=2835785, end=2837263, strand=1),
        Location(locus="Rv2591", start=2921551, end=2923182, strand=1),
        Location(locus="Rv2608", start=2935046, end=2936788, strand=1),
        Location(locus="Rv2615c", start=2943600, end=2944985, strand=-1),
        Location(locus="Rv2634c", start=2960105, end=2962441, strand=-1),
        Location(locus="Rv2741", start=3053914, end=3055491, strand=1),
        Location(locus="Rv2768c", start=3076894, end=3078078, strand=-1),
        Location(locus="Rv2769c", start=3078158, end=3078985, strand=-1),
        Location(locus="Rv2770c", start=3079309, end=3080457, strand=-1),
        Location(locus="Rv2853", start=3162268, end=3164115, strand=1),
        Location(locus="Rv2892c", start=3200794, end=3202020, strand=-1),
        Location(locus="Rv3018c", start=3376939, end=3378243, strand=-1),
        Location(locus="Rv3018A", start=3378329, end=3378415, strand=-1),
        Location(locus="Rv3021c", start=3379376, end=3380452, strand=-1),
        Location(locus="Rv3022c", start=3380440, end=3380682, strand=-1),
        Location(locus="Rv3022A", start=3380679, end=3380993, strand=-1),
        Location(locus="Rv3097c", start=3465778, end=3467091, strand=-1),
        Location(locus="Rv3125c", start=3490476, end=3491651, strand=-1),
        Location(locus="Rv3135", start=3501334, end=3501732, strand=1),
        Location(locus="Rv3136", start=3501794, end=3502936, strand=1),
        Location(locus="Rv3144c", start=3510088, end=3511317, strand=-1),
        Location(locus="Rv3159c", start=3527391, end=3529163, strand=-1),
        Location(locus="Rv3343c", start=3729364, end=3736935, strand=-1),
        Location(locus="Rv3344c", start=3736984, end=3738438, strand=-1),
        Location(locus="Rv3345c", start=3738158, end=3742774, strand=-1),
        Location(locus="Rv3347c", start=3743711, end=3753184, strand=-1),
        Location(locus="Rv3350c", start=3755952, end=3767102, strand=-1),
        Location(locus="Rv3367", start=3778568, end=3780334, strand=1),
        Location(locus="Rv3388", start=3801653, end=3803848, strand=1),
        Location(locus="Rv3425", start=3842239, end=3842769, strand=1),
        Location(locus="Rv3426", start=3843036, end=3843734, strand=1),
        Location(locus="Rv3429", start=3847165, end=3847701, strand=1),
        Location(locus="Rv3477", start=3894093, end=3894389, strand=1),
        Location(locus="Rv3478", start=3894426, end=3895607, strand=1),
        Location(locus="Rv3507", start=3926569, end=3930714, strand=1),
        Location(locus="Rv3508", start=3931005, end=3936710, strand=1),
        Location(locus="Rv3511", start=3939617, end=3941761, strand=1),
        Location(locus="Rv3512", start=3941724, end=3944963, strand=1),
        Location(locus="Rv3514", start=3945794, end=3950263, strand=1),
        Location(locus="Rv3532", start=3969343, end=3970563, strand=1),
        Location(locus="Rv3533c", start=3970705, end=3972453, strand=-1),
        Location(locus="Rv3539", start=3978059, end=3979498, strand=1),
        Location(locus="Rv3558", start=3997980, end=3999638, strand=1),
        Location(locus="Rv3590c", start=4031404, end=4033158, strand=-1),
        Location(locus="Rv3595c", start=4036731, end=4038050, strand=-1),
        Location(locus="Rv3621c", start=4060648, end=4061889, strand=-1),
        Location(locus="Rv3622c", start=4061899, end=4062198, strand=-1),
        Location(locus="Rv3650", start=4091233, end=4091517, strand=1),
        Location(locus="Rv3652", start=4093632, end=4093946, strand=1),
        Location(locus="Rv3653", start=4093940, end=4094527, strand=1),
        Location(locus="Rv3738c", start=4189285, end=4190232, strand=-1),
        Location(locus="Rv3739c", start=4190284, end=4190517, strand=-1),
        Location(locus="Rv3746c", start=4196171, end=4196506, strand=-1),
        Location(locus="Rv3812", start=4276571, end=4278085, strand=1),
        Location(locus="Rv3872", start=4350745, end=4351044, strand=1),
        Location(locus="Rv3873", start=4351075, end=4352181, strand=1),
        Location(locus="Rv3892c", start=4374484, end=4375683, strand=-1),
        Location(locus="Rv3893c", start=4375762, end=4375995, strand=-1),
    ]

    @doc_inherit
    def load_from_web_and_db(self, bolt_url: str):
        response = requests.get(self.url)
        if response.status_code == 200:
            tables = pd.read_html(StringIO(response.text))
            pe_ppe_data = tables[0]
            graph = Graph(uri=bolt_url)
            self.regions = RegionList.locus_list_to_locations(
                graph, pe_ppe_data, "Rv number"
            )
