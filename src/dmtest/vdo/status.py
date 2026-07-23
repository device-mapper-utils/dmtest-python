import re

from dmtest.device_mapper.dev import Dev


def _parse_vdo_status(status_str: str) -> dict[str, str]:
    tokens = re.split(r"\s+", status_str)

    h: dict[str, str] = {}
    h["storage-device"] = tokens[3]
    h["mode"] = tokens[4]
    h["recovery-mode"] = tokens[5]
    h["index-state"] = tokens[6]
    h["compress-state"] = tokens[7]
    h["blocks-used"] = tokens[8]
    h["blocks-available"] = tokens[9]

    return h

def vdo_status(dev: Dev) -> dict[str, str]:
    return _parse_vdo_status(dev.status())
