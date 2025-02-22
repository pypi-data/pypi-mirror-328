
from ttlinks.ipservice.ip_configs import IPv4SubnetConfig, IPv6SubnetConfig
from ttlinks.ipservice.ip_subnet_type_classifiers import IPSubnetTypeClassifier
from ttlinks.ipservice.ip_utils import IPv4TypeAddrBlocks
from ttlinks.ipservice.wildcard_calculator import calculate_minimum_ipv4_wildcard, calculate_minimum_ipv6_wildcard

# ip_subnet_type_classifier = IPSubnetTypeClassifier
#
# print('IPv4 subnet types:'.center(50, '-'))
# ipv4_subnet1 = IPv4SubnetConfig("192.168.0.0/16")
# ipv4_subnet2 = IPv4SubnetConfig("192.168.0.0/15")
# ipv4_subnet3 = IPv4SubnetConfig("224.0.0.0/4")
# print('IPv4 subnet 1 belongs to:', [subnet_type.name for subnet_type in ip_subnet_type_classifier.classify_ipv4_subnet_types(ipv4_subnet1)])
# print('IPv4 subnet 2 belongs to:', [subnet_type.name for subnet_type in ip_subnet_type_classifier.classify_ipv4_subnet_types(ipv4_subnet2)])
# print('IPv4 subnet 3 belongs to:', [subnet_type.name for subnet_type in ip_subnet_type_classifier.classify_ipv4_subnet_types(ipv4_subnet3)])
#
# print('IPv6 subnet types:'.center(50, '-'))
# ipv6_subnet1 = IPv6SubnetConfig("2001:db8::/32")
# ipv6_subnet2 = IPv6SubnetConfig("fe80::/64")
# ipv6_subnet3 = IPv6SubnetConfig("2002::/16")
# print('IPv6 subnet 1 belongs to:', [subnet_type.name for subnet_type in ip_subnet_type_classifier.classify_ipv6_subnet_types(ipv6_subnet1)])
# print('IPv6 subnet 2 belongs to:', [subnet_type.name for subnet_type in ip_subnet_type_classifier.classify_ipv6_subnet_types(ipv6_subnet2)])
# print('IPv6 subnet 3 belongs to:', [subnet_type.name for subnet_type in ip_subnet_type_classifier.classify_ipv6_subnet_types(ipv6_subnet3)])

# ipv4_subnet = IPv4SubnetConfig("192.168.1.0/24")
# print(ipv4_subnet.total_hosts)
# print(ipv4_subnet.usable_hosts)
# print(ipv4_subnet.subnet_range)


# print(calculate_minimum_ipv4_wildcard("0.0.0.0/24"))

def get_ipv4_type_blocks():
    return {block.name: block.value for block in IPv4TypeAddrBlocks}

print(get_ipv4_type_blocks())
