import re
import socket
import struct
import requests
import validators


def is_valid_mac_address(address, mac_address_format='colon'):
    try:
        if mac_address_format == 'colon':
            if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", address.lower()):
                return True
        if mac_address_format == 'dotted':
            if re.match("[0-9a-f]{4}([.]?)[0-9a-f]{4}([.]?)[0-9a-f]{4}$", address.lower()):
                return True
    except BaseException:
        pass
    return False


def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  # no inet_pton here, sorry
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  # not a valid address
        return False
    except BaseException:
        return False

    return True


def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:  # not a valid address
        return False
    return True


def is_valid_ipv6_cidr(cidr):
    valid = False
    try:
        network, net_bits = cidr.split('/')
        if is_valid_ipv6_address(network) and int(net_bits) < 129 and int(net_bits) > 8:
            valid = True
    except BaseException:
        pass

    return valid


def is_valid_ipv4_cidr(cidr):
    valid = False
    try:
        network, net_bits = cidr.split('/')
        if is_valid_ipv4_address(network) and int(
                net_bits) < 33 and int(net_bits) >= 8:
            valid = True
    except BaseException:
        pass

    return valid


def cidr_to_netmask(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return network, netmask


def netmask_to_prefix(mask):
    try:
        prefix = sum(bin(int(x)).count('1') for x in mask.split('.'))
        return prefix
    except BaseException:
        return None


def prefix_to_netmask(prefix):
    host_bits = 32 - prefix
    netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
    return netmask


def is_ipv4_in_cidr(address, cidr):
    if not is_valid_ipv4_address(address):
        return False

    netaddr, bits = cidr.split('/')
    if not is_valid_ipv4_address(netaddr):
        return False
    if int(bits) < 8 or int(bits) > 32:
        return False

    ip_address = struct.unpack('>L', socket.inet_aton(address))[0]
    ip_address_cidr = ip_address & (4294967295 << (32 - int(bits)))
    ip_network = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    ip_network_cidr = ip_network & (4294967295 << (32 - int(bits)))

    return ip_address_cidr == ip_network_cidr


def get_network_ipv4_in_cidr(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None

    netaddr, bits = cidr.split('/')

    if not is_valid_ipv4_address(netaddr):
        return None
    if int(bits) < 8 or int(bits) > 32:
        return None

    ip_network = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    ip_network_cidr = ip_network & (4294967295 << (32 - int(bits)))

    return socket.inet_ntoa(struct.pack('>L', ip_network_cidr))


def get_first_ipv4_in_cidr(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None

    netaddr, bits = cidr.split('/')
    address = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    address = address + 1
    return socket.inet_ntoa(struct.pack('>L', address))


def get_nth_ipv4_in_cidr(cidr, index):
    if not is_valid_ipv4_cidr(cidr):
        return None

    size = get_ipv4_cidr_size(cidr)
    if size is None:
        return None

    if index >= size:
        return None

    netaddr, bits = cidr.split('/')
    address = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    address = address + index
    return socket.inet_ntoa(struct.pack('>L', address))


def get_last_ipv4_in_cidr(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None

    netaddr, bits = cidr.split('/')
    address = struct.unpack('>L', socket.inet_aton(netaddr))[0]
    address = address + 2**int(bits) - 2
    return socket.inet_ntoa(struct.pack('>L', address))


def get_ipv4_cidr_size(cidr):
    if not is_valid_ipv4_cidr(cidr):
        return None
    netaddr, bits = cidr.split('/')
    return 2**(32 - int(bits)) - 2


def get_nth_ipv4_from_address(address, index):
    if not is_valid_ipv4_address(address):
        return None

    numeric_address = struct.unpack('>L', socket.inet_aton(address))[0]
    numeric_address = numeric_address + index
    return socket.inet_ntoa(struct.pack('>L', numeric_address))


def get_ipv4_address_count(start_address, end_address):
    if not is_valid_ipv4_address(start_address):
        return None

    if not is_valid_ipv4_address(end_address):
        return None

    numeric_start_address = struct.unpack('>L', socket.inet_aton(start_address))[0]
    numeric_end_address = struct.unpack('>L', socket.inet_aton(end_address))[0]
    if numeric_end_address < numeric_start_address:
        return None

    count = numeric_end_address - numeric_start_address + 1

    return count


def get_lower_ipv4(ip_a, ip_b):
    if not is_valid_ipv4_address(ip_a):
        return None

    if not is_valid_ipv4_address(ip_b):
        return None

    numeric_address_a = struct.unpack('>L', socket.inet_aton(ip_a))[0]
    numeric_address_b = struct.unpack('>L', socket.inet_aton(ip_b))[0]
    return min(numeric_address_a, numeric_address_b)


def get_next_ipv4_address(ip_address):
    return get_nth_ipv4_from_address(ip_address, 1)


def is_url_valid(value):
    return validators.url(value)


def is_url_accessible(url, timeout=1):
    try:
        if len(url.split(' ')) > 1:
            return False
        handler = requests.head(url, timeout=timeout)
        if 'Content-Type' in handler.headers:
            return True
    except BaseException:
        pass
    return False
