from ttlinks.macservice.mac_address import MACAddr
from ttlinks.macservice.mac_classifiers import MACAddrClassifier
from ttlinks.macservice.mac_converters import *
from ttlinks.macservice.mac_factory import MACFactory
from ttlinks.macservice.mac_utils import MACType

# mac_classifier = MACAddrClassifier()
# mac_in_bytes = MACConverter.convert_mac('021111111110')
# print(mac_in_bytes)
# hex_fmt = '021111111110'
# print(NumeralConverter.bytes_to_hexadecimal(mac_in_bytes))
# print(MACAddrClassifier.classify_mac(mac_in_bytes))
# print([hex_fmt[i:i+2] for i in range(0, len(hex_fmt), 2)])



# print(NumeralConverter.hexadecimal_to_decimal('A00000'))
# print(NumeralConverter.hexadecimal_to_decimal('AFFFFF'))

# base_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources\\')
# print(os.path.realpath(__file__))
# print(base_folder)
# handler = OuiFileParser()
# file = IEEEOuiCsvFile(os.path.join(base_folder, 'default_mal.txt'))
# parsed_result = handler.parse_oui_file(file)
# oui_units = parsed_result['oui_units']
# for unit in oui_units:
#     print('------------')
#     print(unit.record)
#
#
# mac = '08-bf-B8-34-C6-A4'
# mac_addr = MACAddr(mac)
# print(mac_addr)
# print(mac_addr.binary_string)
# print(mac_addr.mac_type)

# mac_as_bytes = MACConverter.convert_oui("08-BF-B8")
# print(mac)
# mac = MACAddr(mac_as_bytes)
# print(mac.as_decimal)
# loader = OUIDBLoader()
# updater = OUIDBUpdater(loader)
# searcher = OUIDBSearcher(loader)
# oui_units = searcher.search_by_decimal(mac.as_decimal)
# for unit in oui_units:
#     print(unit.record)
# print(mac.oui)


# oui_units = [oui_unit.record for oui_unit in oui_units]
# print(oui_units)
# updater._parse_oui_file()
# updater.batch_upsert()

# mac_factory = MACFactory()

# macs = mac_factory.batch_macs([
#     '18:64:72:C5:D3:0E', '18:64:72:C5:D3:DC', '01:80:A3:B6:BF:D3',
# ], keep_dup=True)

# macs = mac_factory.random_macs_batch(MACType.UNICAST, 1000000)
# print(len(macs))
# for mac in macs:
#     if mac.oui:
#         for oui in mac.oui:
#             print(oui.record)


# mac = MACAddr("08-BF-B8-34-00-00")
# result = {'oui_id': '08BFB8', 'start_hex': '000000', 'end_hex': 'FFFFFF', 'start_decimal': 9619518783488, 'end_decimal': 9619535560703, 'block_size': 16777215, 'oui_type': 'MA_L', 'organization': 'ASUSTek COMPUTER INC.', 'address': 'No.15,Lide Rd., Beitou, Dist.,Taipei 112,Taiwan Taipei Taiwan TW 112'}
# print(mac.oui[0].record == result)


# mac_factory = MACFactory()
# mac_addr = mac_factory.mac("08-BF-B8-34-b0-03")
# print('MAC Type: ', mac_addr.mac_type.name)
# print('Bit-level representation: ', mac_addr.binary_string)
# print('OUI', mac_addr.oui[0].record)
# print('Standardized output', str(mac_addr))


# mac1 = MACAddr("08-BF-B8-34-b0-03")
# mac2 = MACAddr("AA-BB-CC-DD-EE-FF")
# mac3 = MACAddr("08.BF.B8.34.b0.03")
# mac4 = MACAddr("08BFB834b003")
#
# print(str(mac1))
# print(str(mac2))
# print(str(mac3))
# print(str(mac4))
# print(mac1.binary_string)
# print(mac1.binary_digits)
# print(mac1.as_decimal)
#
# if mac1.oui:
#     print('mac1: ', mac1.oui[0].record)
# else:
#     print('No OUI record for mac1')
#
# if mac2.oui:
#     print('mac2: ', mac2.oui[0].record)
# else:
#     print('No OUI record for mac2')



factory = MACFactory()
multicast_macs = factory.random_macs_batch(mac_type=MACType.MULTICAST, num_macs=3)

for mac in multicast_macs:
    print(mac.binary_string)