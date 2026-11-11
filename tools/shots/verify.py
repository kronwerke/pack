#!/usr/bin/env python3
"""Checks that need the world to tick, run against the local test server over RCON.

build.py leaves them in verify.json: a Mekanism multiblock that has to form by itself, a
wheel that has to turn. The test world's chunks only tick with a player or a forced chunk, so
this loads the area first, waits, and asks.

Usage: verify.py [seconds to wait, default 8]   (server on 127.0.0.1:25575, see srv/server.properties)
"""
import json
import os
import socket
import struct
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))


class Rcon:
    def __init__(self, host="127.0.0.1", port=25575, password="localtest"):
        self.s = socket.create_connection((host, port), timeout=60)
        self._send(3, password)

    def _send(self, kind, body):
        data = struct.pack("<ii", 1, kind) + body.encode() + b"\x00\x00"
        self.s.sendall(struct.pack("<i", len(data)) + data)
        n = struct.unpack("<i", self._read(4))[0]
        return self._read(n)[8:-2].decode(errors="replace")

    def _read(self, n):
        d = b""
        while len(d) < n:
            d += self.s.recv(n - len(d))
        return d

    def run(self, cmd):
        return self._send(2, cmd)


def main():
    wait = float(sys.argv[1]) if len(sys.argv) > 1 else 8
    spec = json.load(open(os.path.join(HERE, "verify.json")))
    r = Rcon()
    x0, z0, x1, z1 = spec["area"]
    # forceload takes at most 256 chunks a call
    for cx in range(x0, x1 + 1, 16 * 14):
        for cz in range(z0, z1 + 1, 16 * 14):
            r.run(f"execute in kronwerke:testworld run forceload add {cx} {cz} {min(x1, cx + 16 * 14 - 1)} {min(z1, cz + 16 * 14 - 1)}")
    time.sleep(wait)
    bad = 0
    for scene, cmd in spec["checks"]:
        answer = r.run(cmd)
        if "passed" not in answer:
            bad += 1
            print(f"FAILED {scene}: {cmd} -> {answer.strip()}")
    print(f"{len(spec['checks'])} checks, {bad} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
