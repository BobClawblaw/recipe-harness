"""The stats report as a typeset PDF, stdlib only: Helvetica text, headed and striped tables, running header and footer.

``render(md, title, stamp)`` lays out the markdown STATS.md is made of (``#``/``##``/``###`` headings, paragraphs,
``- `` bullets and pipe tables, ``---:`` columns right-aligned) on landscape letter pages. The fonts are PDF's
standard Helvetica and Helvetica-Bold, measured with their AFM widths, so nothing is embedded.
"""

from __future__ import annotations

import re

W, H, M = 792.0, 612.0, 42.0          # landscape letter, margin
TOP, BOTTOM = H - M - 22, M + 20      # the body's box, inside the running header and footer
INK = (0.13, 0.15, 0.18)
MUTED = (0.42, 0.45, 0.50)
ACCENT = (0.10, 0.27, 0.47)           # headings, table heads, rules
STRIPE = (0.945, 0.953, 0.965)
RULE = (0.82, 0.84, 0.87)
FAIL = (0.70, 0.13, 0.13)            # a failed check's result

# AFM advance widths (1/1000 em) for WinAnsi 32..126
_REG = [278, 278, 355, 556, 556, 889, 667, 191, 333, 333, 389, 584, 278, 333, 278, 278] + [556] * 10 + \
    [278, 278, 584, 584, 584, 556, 1015, 667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778,
     667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 278, 278, 278, 469, 556, 333, 556, 556, 500, 556, 556,
     278, 556, 556, 222, 222, 500, 222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 334,
     260, 334, 584]
_BOLD = [278, 333, 474, 556, 556, 889, 722, 238, 333, 333, 389, 584, 278, 333, 278, 278] + [556] * 10 + \
    [333, 333, 584, 584, 584, 611, 975, 722, 722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778,
     667, 778, 722, 667, 611, 722, 667, 944, 667, 667, 611, 333, 278, 333, 584, 556, 333, 556, 611, 556, 611, 556,
     333, 611, 611, 278, 278, 556, 278, 889, 611, 611, 611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 389,
     280, 389, 584]


def width(s: str, size: float, bold: bool = False) -> float:
    table = _BOLD if bold else _REG
    return sum(table[ord(c) - 32] if 32 <= ord(c) <= 126 else 556 for c in s) * size / 1000


def _plain(s: str) -> str:
    return s.replace("`", "").replace("**", "").strip()


def wrap(s: str, size: float, room: float, bold: bool = False) -> list[str]:
    """Words onto lines no wider than `room`; a word wider than a line is cut where it must be."""
    lines, cur = [], ""
    for word in s.split():
        while width(word, size, bold) > room:  # a hash or a URL: cut it across lines
            n = len(word)
            while n > 1 and width((cur + " " if cur else "") + word[:n], size, bold) > room:
                n -= 1
            if cur and n < 4:
                lines.append(cur)
                cur = ""
                continue
            lines.append((cur + " " if cur else "") + word[:n])
            cur, word = "", word[n:]
        trial = f"{cur} {word}" if cur else word
        if width(trial, size, bold) <= room:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur or not lines:
        lines.append(cur)
    return lines


def _esc(s: str) -> str:
    return s.encode("cp1252", "replace").decode("latin-1").replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class _Pages:
    """Content streams, one a page, with the cursor `y` falling from TOP."""

    def __init__(self):
        self.pages: list[list[str]] = []
        self.new()

    def new(self):
        self.pages.append([])
        self.y = TOP

    def room(self, need: float):
        if self.y - need < BOTTOM:
            self.new()

    def text(self, x, y, s, size, bold=False, color=INK):
        self.pages[-1].append(f"BT /{'F2' if bold else 'F1'} {size:.2f} Tf {color[0]} {color[1]} {color[2]} rg "
                              f"{x:.2f} {y:.2f} Td ({_esc(s)}) Tj ET")

    def rect(self, x, y, w, h, color):
        self.pages[-1].append(f"{color[0]} {color[1]} {color[2]} rg {x:.2f} {y:.2f} {w:.2f} {h:.2f} re f")

    def line(self, x1, y1, x2, y2, color, lw=0.6):
        self.pages[-1].append(f"{color[0]} {color[1]} {color[2]} RG {lw} w {x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")


def _blocks(md: str):
    """(kind, payload) blocks: h1/h2/h3 with their text, para with its text, bullets with items, table with rows."""
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif m := re.match(r"(#{1,3}) (.*)", line):
            yield f"h{len(m.group(1))}", _plain(m.group(2))
            i += 1
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = re.split(r"(?<!\\)\|", lines[i].strip().strip("|"))
                rows.append([c.strip().replace("\\|", "|") for c in cells])
                i += 1
            yield "table", rows
        elif line.startswith("- "):
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("  ")):
                if lines[i].startswith("- "):
                    items.append(lines[i][2:])
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            yield "bullets", [_plain(x) for x in items]
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(("|", "#", "- ")):
                para.append(lines[i].strip())
                i += 1
            yield "para", _plain(" ".join(para))


def _table(p: _Pages, rows: list[list[str]], left: float, room: float):
    head, rule, body = rows[0], rows[1] if len(rows) > 1 else [], rows[2:]
    n = len(head)
    right = [c.strip().endswith(":") for c in rule] + [False] * n
    body = [[_plain(c) for c in (r + [""] * n)[:n]] for r in body]
    head = [_plain(c) for c in head]
    size, pad, lead = 7.6, 4.0, 9.6
    # each column its natural width, then the widest shrink (and wrap) until the table fits
    natural = [max([width(head[j], size, True)] + [width(r[j], size) for r in body]) + 2 * pad + 1 for j in range(n)]
    floor = [min(natural[j], max(width(w, size, True) for w in (head[j].split() or [""])) + 2 * pad, 120) for j in range(n)]
    cols = natural[:]
    while sum(cols) > room:
        j = max(range(n), key=lambda k: cols[k] - floor[k])
        if cols[j] - floor[j] < 1:
            break
        cols[j] = max(floor[j], cols[j] - max(4.0, (sum(cols) - room) / 4))
    scale = room / sum(cols) if sum(cols) > room else 1.0
    cols = [c * scale for c in cols]

    def cells(r, bold):
        return [wrap(r[j], size, cols[j] - 2 * pad, bold) for j in range(n)]

    def draw(r, bold, fill, color):
        cl = cells(r, bold)
        h = max(len(c) for c in cl) * lead + 2 * pad - (lead - size)
        if fill:
            p.rect(left, p.y - h, sum(cols), h, fill)
        x = left
        for j, lines in enumerate(cl):
            for k, s in enumerate(lines):
                tx = x + cols[j] - pad - width(s, size, bold) if right[j] else x + pad
                ink = FAIL if color is INK and r[j].startswith("FAIL") else color
                p.text(tx, p.y - pad - size + 1.2 - k * lead, s, size, bold, ink)
            x += cols[j]
        p.y -= h
        return h

    def header():
        draw(head, True, ACCENT, (1, 1, 1))

    first = cells(body[0], False) if body else [[""]]
    p.room(2 * (max(len(c) for c in first) * lead + 2 * pad) + 4)
    header()
    for i, r in enumerate(body):
        need = max(len(c) for c in cells(r, False)) * lead + 2 * pad
        if p.y - need < BOTTOM:
            p.new()
            header()
        draw(r, False, STRIPE if i % 2 else None, INK)
    p.line(left, p.y, left + sum(cols), p.y, RULE)
    p.y -= 12


def render(md: str, title: str, stamp: str) -> bytes:
    p = _Pages()
    left, room = M, W - 2 * M
    first_h2 = True
    for kind, payload in _blocks(md):
        if kind == "h1":
            p.rect(0, H - 128, W, 128, ACCENT)
            p.text(M, H - 72, payload, 26, True, (1, 1, 1))
            sub = "Throughput, latency and quality of each served recipe, by model and hardware"
            p.text(M, H - 96, sub, 11, False, (0.82, 0.87, 0.93))
            p.text(W - M - width(stamp, 9), H - 96, stamp, 9, False, (0.82, 0.87, 0.93))
            p.y = H - 150
        elif kind == "h2":
            if not first_h2 and p.y < TOP - 1:
                p.new()
            first_h2 = False
            p.room(60)
            p.text(left, p.y - 15, payload, 14.5, True, ACCENT)
            p.y -= 22
            p.line(left, p.y, left + room, p.y, ACCENT, 1.0)
            p.y -= 12
        elif kind == "h3":
            p.room(48)
            p.y -= 4
            p.text(left, p.y - 10, payload[:1].upper() + payload[1:], 10.5, True, INK)
            p.y -= 18
        elif kind == "para":
            small = payload.startswith("Serving:")  # the run's identity: hashes and ids, set small and grey
            size, lead = (7.5, 10.0) if small else (9.0, 12.4)
            for s in wrap(payload, size, room):
                p.room(lead)
                p.text(left, p.y - size, s, size, False, MUTED if small else INK)
                p.y -= lead
            p.y -= 6
        elif kind == "bullets":
            for item in payload:
                for k, s in enumerate(wrap(item, 9, room - 14)):
                    p.room(12)
                    if k == 0:
                        p.text(left + 3, p.y - 9, "-", 9, True, ACCENT)
                    p.text(left + 14, p.y - 9, s, 9)
                    p.y -= 12.4
            p.y -= 6
        elif kind == "table":
            _table(p, payload, left, room)
    return _assemble(p.pages, title, stamp)


def _assemble(pages: list[list[str]], title: str, stamp: str) -> bytes:
    objs: list[bytes] = [b"<< /Type /Catalog /Pages 2 0 R >>", b"",
                         b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>",
                         b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>",
                         f"<< /Title ({_esc(title)}) /Producer (recipe-harness) >>".encode("latin-1")]
    kids = []
    total = len(pages)
    for n, body in enumerate(pages, 1):
        run = _Pages()
        run.pages = [[]]
        if n > 1:  # the running header; the first page has the title band
            run.text(M, H - M + 4, title, 8, True, ACCENT)
            run.text(W - M - width(stamp, 8), H - M + 4, stamp, 8, False, MUTED)
            run.line(M, H - M - 2, W - M, H - M - 2, RULE)
        run.line(M, M + 8, W - M, M + 8, RULE)
        run.text(M, M - 4, "recipe-harness served stats", 7.5, False, MUTED)
        folio = f"Page {n} of {total}"
        run.text(W - M - width(folio, 7.5), M - 4, folio, 7.5, False, MUTED)
        stream = "\n".join(body + run.pages[0]).encode("latin-1")
        objs.append(b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream")
        content = len(objs)
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.0f} {H:.0f}] /Resources << /Font << /F1 3 0 R "
                    f"/F2 4 0 R >> >> /Contents {content} 0 R >>".encode())
        kids.append(len(objs))
    objs[1] = f"<< /Type /Pages /Kids [{' '.join(f'{k} 0 R' for k in kids)}] /Count {len(kids)} >>".encode()
    out, offsets = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"), []
    for i, o in enumerate(objs, 1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + o + b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode() + b"".join(f"{o:010d} 00000 n \n".encode() for o in offsets)
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R /Info 5 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
    return bytes(out)
