#!/usr/bin/env python3
"""Tiny RCON client. Usage: rcon.py <password> <port> <command...>  (one command per argument)"""
import socket, struct, sys

def _pkt(rid, typ, body):
    data = struct.pack("<ii", rid, typ) + body.encode() + b"\x00\x00"
    return struct.pack("<i", len(data)) + data

def _recv(s):
    ln = struct.unpack("<i", s.recv(4))[0]
    buf = b""
    while len(buf) < ln:
        buf += s.recv(ln - len(buf))
    rid, typ = struct.unpack("<ii", buf[:8])
    return rid, typ, buf[8:-2].decode(errors="replace")

def run(pw, port, cmds, host="127.0.0.1"):
    s = socket.create_connection((host, port), timeout=15)
    s.sendall(_pkt(1, 3, pw))
    rid, _, _ = _recv(s)
    if rid == -1:
        raise SystemExit("rcon auth failed")
    out = []
    for i, c in enumerate(cmds, start=2):
        s.sendall(_pkt(i, 2, c))
        _, _, body = _recv(s)
        out.append((c, body))
    s.close()
    return out

if __name__ == "__main__":
    pw, port, cmds = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
    for c, body in run(pw, port, cmds):
        print(f"> {c}\n{body}\n")
