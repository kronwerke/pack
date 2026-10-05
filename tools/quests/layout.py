"""
Lays a chapter out from its dependency graph, the way the big packs do it: sections stacked
top to bottom, each a band with its heading on the left, quests inside a band in columns by
depth (left to right) and rows chosen so lines cross as little as possible. Quests without
links inside their section (checklists) form a grid at the right of the band.

The hand placed coordinates in the chapter files only decide which heading a quest belongs
to and the order of rows; the final positions come from here. Lines that would cross from
one band into another are hidden for quests that have no link inside their own band, so a
band starts clean.
"""

COL_W = 2.25      # one column, quest size 1 plus the gap
ROW_H = 1.6
BAND_GAP = 1.4    # room for the heading above a band
GRID_COLS = 6     # checklist grid at the right of a band
MAX_ROWS = 6      # a taller column wraps
SUB_W = 1.7       # distance between wrapped sub columns


def _size(q):
    return float(q.get("size") or 1.0)


def _nearest_section(q, sections):
    """The heading a quest sits under: the closest one above it, by its old coordinates."""
    best, score = None, None
    for i, b in enumerate(sections):
        dy = q["y"] - b["y"]
        dx = abs(q["x"] - b["x"]) - b["width"] / 2
        s = (dy if dy >= -0.6 else 100 + abs(dy)) + 0.6 * max(0.0, dx)
        if score is None or s < score:
            best, score = i, s
    return best


def layout(ch, banner_kind):
    """Rewrites x, y of every quest and every heading of the chapter in place.
    banner_kind(texture) -> "title" | "section" | "note"."""
    quests = ch["quests"]
    by_name = {q["name"]: q for q in quests}
    images = ch["images"]
    title = [im for im in images if banner_kind(im["image"]) == "title"]
    sections = [im for im in images if banner_kind(im["image"]) == "section"]
    sections.sort(key=lambda b: (round(b["y"] / 3.0), b["x"]))
    notes = [im for im in images if banner_kind(im["image"]) == "note"]
    # notes above the first heading sit next to the title, the others under their band
    note_of = {}
    for n in notes:
        note_of.setdefault(_nearest_section(n, sections) if sections else -1, []).append(n)
    if title:
        for n in notes:
            if n["y"] < title[0]["y"] + title[0]["height"]:
                note_of[_nearest_section(n, sections) if sections else -1].remove(n)
                note_of.setdefault("title", []).append(n)

    # which heading each quest belongs to; -1 is the strip before the first heading
    member = {}
    for q in quests:
        member[q["name"]] = _nearest_section(q, sections) if sections else -1
    root = quests[0]
    member[root["name"]] = -1
    # a quest with no link inside its own band but links into exactly one other band
    # was placed by eye near the wrong heading; it moves to the band it is linked to
    succs_all = {q["name"]: [] for q in quests}
    for q in quests:
        for d in q["deps"]:
            if d in succs_all:
                succs_all[d].append(q["name"])
    for _ in range(3):
        moved = False
        for q in quests:
            if q is root:
                continue
            linked = [d for d in q["deps"] if d in by_name] + succs_all[q["name"]]
            if not linked:
                continue
            bands = {member[n] for n in linked}
            if member[q["name"]] not in bands and len(bands) == 1:
                member[q["name"]] = bands.pop()
                moved = True
        if not moved:
            break

    # the root and anything that sits with it go into the first strip
    groups = {}
    for q in quests:
        groups.setdefault(member[q["name"]], []).append(q)

    y_top = 0.0
    out_images = []
    if title:
        t = title[0]
        t["x"], t["y"] = t["width"] / 2 - 0.5, 0.0
        out_images.append(t)
        nx = t["width"] + 0.6
        for n in note_of.get("title", []):
            n["x"], n["y"] = nx + n["width"] / 2 - 0.5, t["height"] / 2 - n["height"] / 2
            out_images.append(n)
            nx += n["width"] + 0.6
        y_top = t["height"] / 2 + 1.2

    order = sorted(groups.keys())
    for gi in order:
        members = groups[gi]
        names = {q["name"] for q in members}
        if gi >= 0:
            b = sections[gi]
            b["x"], b["y"] = b["width"] / 2 - 0.5, y_top + b["height"] / 2
            out_images.append(b)
            y_top += b["height"] + 0.9
        # links inside the band
        preds = {q["name"]: [d for d in q["deps"] if d in names] for q in members}
        succs = {q["name"]: [] for q in members}
        for n, ps in preds.items():
            for p in ps:
                succs[p].append(n)
        floating = [q for q in members if not preds[q["name"]] and not succs[q["name"]] and q is not root]
        tree = [q for q in members if q not in floating]
        # depth by longest path inside the band
        depth = {}

        def dep_of(n, seen=()):
            if n in depth:
                return depth[n]
            if n in seen:
                return 0
            ps = preds[n]
            d = 0 if not ps else 1 + max(dep_of(p, seen + (n,)) for p in ps)
            depth[n] = d
            return d

        for q in tree:
            dep_of(q["name"])
        cols = {}
        for q in tree:
            cols.setdefault(depth[q["name"]], []).append(q)
        rows = {}
        for c in sorted(cols):
            col = cols[c]
            if c == 0:
                col.sort(key=lambda q: (q["y"], q["x"]))
            else:
                def bary(q):
                    ps = [rows[p] for p in preds[q["name"]] if p in rows]
                    return (sum(ps) / len(ps) if ps else 0.0, q["y"], q["x"])
                col.sort(key=bary)
            for r, q in enumerate(col):
                rows[q["name"]] = r
        # a column taller than MAX_ROWS wraps into side by side sub columns
        sub = {}
        for c in sorted(cols):
            col = sorted(cols[c], key=lambda q: rows[q["name"]])
            if len(col) > MAX_ROWS:
                n_sub = -(-len(col) // MAX_ROWS)
                per = -(-len(col) // n_sub)
                for i, q in enumerate(col):
                    sub[q["name"]] = i // per
                    rows[q["name"]] = i % per
            else:
                for q in col:
                    sub[q["name"]] = 0
        # a parent sits level with its first child where that row is free
        for c in sorted(cols)[:-1]:
            for q in cols[c]:
                kids = [k for k in succs[q["name"]] if k in rows]
                if not kids:
                    continue
                want = min(rows[k] for k in kids)
                taken = {rows[o["name"]] for o in cols[c] if o is not q and sub[o["name"]] == sub[q["name"]]}
                if want not in taken and want > rows[q["name"]]:
                    rows[q["name"]] = want
        # column widths follow the biggest quest in them
        x = 0.0
        col_x = {}
        for c in sorted(cols):
            w = max(_size(q) for q in cols[c])
            n_sub = max(sub[q["name"]] for q in cols[c]) + 1
            col_x[c] = x + (w - 1.0) / 2
            x += COL_W + (w - 1.0) + (n_sub - 1) * SUB_W
        band_rows = max([rows[q["name"]] for q in tree], default=-1) + 1
        row_h = ROW_H + 0.5 * max([_size(q) - 1.0 for q in tree], default=0.0)
        for q in tree:
            q["x"] = col_x[depth[q["name"]]] + sub[q["name"]] * SUB_W
            q["y"] = y_top + rows[q["name"]] * row_h + (_size(q) - 1.0) / 2
            # lines from another band are hidden; the band order tells the story
            cross = len(q["deps"]) - len(preds[q["name"]])
            if cross and (not preds[q["name"]] or cross >= len(preds[q["name"]])):
                q["hide_lines"] = True
        # checklist grid to the right
        if floating:
            floating.sort(key=lambda q: (q["y"], q["x"]))
            gx0 = x + 0.5 if tree else 0.0
            grid_rows = 0
            for i, q in enumerate(floating):
                r, c = divmod(i, GRID_COLS)
                q["x"] = gx0 + c * 1.6
                q["y"] = y_top + r * 1.5
                q["hide_lines"] = bool(q["deps"])
                grid_rows = r + 1
            band_rows = max(band_rows, grid_rows)
        y_top += max(band_rows, 1) * row_h
        band_notes = note_of.get(gi, [])
        if band_notes:
            band_notes.sort(key=lambda n: (n["y"], n["x"]))
            nx = 0.0
            for n in band_notes:
                n["x"], n["y"] = nx + n["width"] / 2 - 0.5, y_top + n["height"] / 2
                out_images.append(n)
                nx += n["width"] + 0.6
            y_top += max(n["height"] for n in band_notes) + 0.6
        y_top += BAND_GAP
    ch["images"] = out_images
