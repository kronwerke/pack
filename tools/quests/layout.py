"""
Lays a chapter out from its dependency graph, the way the big packs do it (All the Mods).

Every section of a chapter (a heading banner and the quests under it) becomes one cluster:
a tree that grows left to right, one column per step, every parent level with the middle of
its children, so lines are short, straight where there is one child and fan out evenly where
there are more. A quest with many children that lead nowhere (glyphs, upgrades, a list of
machines) gets them as a tight block right next to it, without a web of lines; the position
tells the story. Quests without any link in their section form a small grid of their own.

The clusters are then packed like a map, row after row in the order of the headings, to a
shape that fits the quest screen (wider than tall), instead of one long column. Lines that
come from another cluster are hidden, so every cluster starts clean.

The hand placed coordinates in the chapter files only decide which heading a quest belongs
to and the order of siblings; the final positions come from here.
"""

COL_W = 2.0        # one step to the right
ROW_H = 1.5        # one row
BLOCK_W = 1.35     # cells of a block of leaves
BLOCK_H = 1.35
BLOCK_MIN = 4      # this many leaf children or more become a block
BLOCK_ROWS = 3     # a block is at most this tall, it grows to the right
GRID_COLS = 4      # quests without links
CLUSTER_GAP_X = 2.0
CLUSTER_GAP_Y = 1.2
BANNER_GAP = 0.5   # between a heading and its cluster
ASPECT = 1.7       # wanted width : height of the whole chapter
MAX_W = 17.0       # a cluster wider than this folds into a second row


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


def _assign_members(quests, sections, by_name):
    member = {}
    for q in quests:
        member[q["name"]] = _nearest_section(q, sections) if sections else -1
    root = quests[0]
    member[root["name"]] = -1 if sections else -1
    # a quest that names its section goes there, whatever its coordinates and links say
    fixed = set()
    for q in quests:
        sec = q.get("section")
        if sec:
            hit = [i for i, b in enumerate(sections) if b["image"].endswith("/" + sec + ".png")]
            if not hit:
                raise ValueError(f"quest {q['name']}: no section banner named {sec}")
            member[q["name"]] = hit[0]
            fixed.add(q["name"])
    succs_all = {q["name"]: [] for q in quests}
    for q in quests:
        for d in q["deps"]:
            if d in succs_all:
                succs_all[d].append(q["name"])
    # a quest with no link inside its own band but links into exactly one other band
    # was placed by eye near the wrong heading; it moves to the band it is linked to
    for _ in range(3):
        moved = False
        for q in quests:
            if q is root or q["name"] in fixed:
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
    return member


class _Cluster:
    """The quests of one section, laid out around (0, 0); w and h are its extent."""

    def __init__(self, members, root):
        self.members = members
        self.pos = {}
        self.hide = set()
        self.w = self.h = 0.0
        self._lay(root)

    def _lay(self, root):
        names = {q["name"] for q in self.members}
        by = {q["name"]: q for q in self.members}
        preds = {n: [d for d in by[n]["deps"] if d in names] for n in names}
        succs = {n: [] for n in names}
        for n in names:
            for p in preds[n]:
                succs[p].append(n)
        order = {q["name"]: i for i, q in enumerate(self.members)}
        # longest path depth inside the cluster
        depth = {}

        def dep(n, seen=()):
            if n in depth:
                return depth[n]
            if n in seen:
                return 0
            d = 0 if not preds[n] else 1 + max(dep(p, seen + (n,)) for p in preds[n])
            depth[n] = d
            return d

        for n in names:
            dep(n)
        floating = [n for n in names if not preds[n] and not succs[n] and by[n] is not root]
        linked = [n for n in names if n not in floating]
        # the tree: each quest hangs under its deepest parent (the last step before it)
        parent = {}
        for n in linked:
            if preds[n]:
                parent[n] = max(preds[n], key=lambda p: (depth[p], -order[p]))
        kids = {n: [] for n in linked}
        for n, p in parent.items():
            kids[p].append(n)
        for n in kids:
            kids[n].sort(key=lambda k: (by[k]["y"], by[k]["x"], order[k]))
        roots = sorted([n for n in linked if n not in parent], key=lambda n: (order[n] if by[n] is not root else -1))

        # a parent with many children that have no children of their own: a block
        block = {}
        for n in linked:
            leaves = [k for k in kids[n] if not kids[k] and _size(by[k]) <= 1.0]
            if len(leaves) >= BLOCK_MIN:
                block[n] = leaves
                kids[n] = [k for k in kids[n] if k not in leaves]

        def block_dims(n):
            m = len(block.get(n, []))
            if not m:
                return 0, 0
            rows = min(BLOCK_ROWS, m)
            cols = -(-m // rows)
            return cols, rows

        # x of each depth: wide quests push the next column further, and a block (which sits
        # in the column after its parent) pushes the column after that
        col_w = {}
        for n in linked:
            d = depth[n]
            col_w[d] = max(col_w.get(d, COL_W), COL_W + (_size(by[n]) - 1.0) * 0.8)
        block_right = {}
        for n in block:
            cols, _ = block_dims(n)
            d = depth[n]
            block_right[d] = max(block_right.get(d, 0.0), (cols - 1) * BLOCK_W)
        col_x = {}
        x = 0.0
        for d in range(0, max(col_w) + 2 if col_w else 1):
            col_x[d] = x
            x += max(col_w.get(d, COL_W), COL_W + block_right.get(d - 1, 0.0) if d >= 1 else 0.0)

        desc = {}

        def size_of(n):
            if n not in desc:
                desc[n] = 1 + len(block.get(n, [])) + sum(size_of(k) for k in kids[n])
            return desc[n]

        for r in roots:
            size_of(r)

        override = {}

        def arranged(n):
            """The children in row order: the biggest branch level with n, so the main line
            runs straight; the others fan out above and below it."""
            ks = kids[n]
            if n in override:
                order_ = override[n]
                main = max(order_, key=lambda k: (desc[k], -order_.index(k)))
                return order_, main
            if len(ks) <= 1:
                return ks, (ks[0] if ks else None)
            main = max(ks, key=lambda k: (desc[k], -ks.index(k)))
            rest = [k for k in ks if k != main]
            half = len(rest) // 2
            return rest[:half] + [main] + rest[half:], main

        GAP = 0.5

        def slots(x, w):
            return range(int(round((x - w / 2) * 2)), int(round((x + w / 2) * 2)) + 1)

        def shape(items):
            """Contour of placed items [(name, x, y, size)]: slot -> (top, bottom)."""
            c = {}
            for _, x, y, sz in items:
                for sl in slots(x, sz):
                    t, b = c.get(sl, (y - sz / 2, y + sz / 2))
                    c[sl] = (min(t, y - sz / 2), max(b, y + sz / 2))
            return c

        def stack(parts):
            """Puts subtrees (lists of items around y 0) one under the other as tight as their
            contours allow; returns the shifted parts and their offsets."""
            out, offs, acc = [], [], {}
            for part in parts:
                c = shape(part)
                off = 0.0
                if acc:
                    need = [acc[sl][1] - c[sl][0] + GAP for sl in c if sl in acc]
                    off = max(need) if need else max(b for _, b in acc.values()) - min(t for t, _ in c.values()) + GAP
                moved = [(nm, x, y + off, sz) for nm, x, y, sz in part]
                for sl, (t, b) in shape(moved).items():
                    if sl in acc:
                        acc[sl] = (min(acc[sl][0], t), max(acc[sl][1], b))
                    else:
                        acc[sl] = (t, b)
                out.append(moved)
                offs.append(off)
            return out, offs

        def block_items(n):
            cols, rows = block_dims(n)
            x0 = col_x[depth[n]] + COL_W
            items = []
            for i, leaf in enumerate(block[n]):
                c, r = divmod(i, rows)
                items.append((leaf, x0 + c * BLOCK_W, r * BLOCK_H, 1.0))
            return items

        def tree(n):
            """The subtree of n as items with n at y 0."""
            me = (n, col_x[depth[n]], 0.0, _size(by[n]))
            row_list, main = arranged(n)
            parts = [tree(k) for k in row_list]
            idx_main = row_list.index(main) if main else -1
            if block.get(n):
                bl = block_items(n)
                if parts:
                    # the block hangs right under the main line
                    parts.insert(idx_main + 1, bl)
                else:
                    h = (block_dims(n)[1] - 1) * BLOCK_H
                    parts = [[(nm, x, y - h / 2, sz) for nm, x, y, sz in bl]]
                    idx_main = -1
            if not parts:
                return [me]
            placed, offs = stack(parts)
            anchor = offs[idx_main] if idx_main >= 0 else 0.0
            items = [it for p_ in placed for it in p_]
            items = [(nm, x, y - anchor, sz) for nm, x, y, sz in items]
            # n must not sit on anything of its own column
            return [me] + items

        block_leaves = {l for ls in block.values() for l in ls}
        edges = [(p_, n) for n in linked for p_ in preds[n] if n not in block_leaves]

        def run(root_order):
            placed, _ = stack([tree(r) for r in root_order])
            return placed

        def cost(placed):
            pos = {nm: (x, y) for p_ in placed for nm, x, y, _ in p_}
            segs = [(pos[a], pos[b]) for a, b in edges if a in pos and b in pos]
            cross = 0
            for i in range(len(segs)):
                (a1, a2) = segs[i]
                for j in range(i + 1, len(segs)):
                    (b1, b2) = segs[j]
                    if {a1, a2} & {b1, b2}:
                        continue
                    if _crosses(a1, a2, b1, b2):
                        cross += 1
            length = sum(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 for a, b in segs)
            height_ = max((y for p_ in placed for _, _, y, _ in p_), default=0) - min((y for p_ in placed for _, _, y, _ in p_), default=0)
            return cross * 10 + length + height_ * 0.5

        # the orders of roots and of siblings that cross the fewest lines
        import itertools
        best_roots = list(roots)
        best = cost(run(best_roots))
        if 1 < len(roots) <= 6:
            for perm in itertools.permutations(roots):
                c_ = cost(run(list(perm)))
                if c_ < best - 1e-9:
                    best, best_roots = c_, list(perm)
        for n in sorted(linked, key=lambda n: depth[n]):
            ks = kids[n]
            if not 2 <= len(ks) <= 5:
                continue
            base = arranged(n)[0]
            best_k = base
            for perm in itertools.permutations(ks):
                override[n] = list(perm)
                c_ = cost(run(best_roots))
                if c_ < best - 1e-9:
                    best, best_k = c_, list(perm)
            override[n] = best_k
        placed = run(best_roots)
        top = 0.0
        for p_ in placed:
            for nm, x, y, sz in p_:
                self.pos[nm] = (x, y)
                if nm in [l for ls in block.values() for l in ls]:
                    self.hide.add(nm)
        top = max((y + sz / 2 for p_ in placed for _, _, y, sz in p_), default=0.0) / ROW_H if placed else 0.0

        # lines that are not the tree's own: keep them, they are few; quests with many parents hide theirs
        for n in linked:
            if len(preds[n]) > 3:
                self.hide.add(n)
            # FTB Quests hides all of a quest's lines or none: a second parent far away would
            # draw a long line across the cluster, so such a quest shows none (it sits next to
            # its main parent, and its panel lists what it needs)
            for p_ in preds[n]:
                if p_ != parent.get(n) and p_ in self.pos and n in self.pos:
                    dx = self.pos[p_][0] - self.pos[n][0]
                    dy = self.pos[p_][1] - self.pos[n][1]
                    if (dx * dx + dy * dy) ** 0.5 > 4.5 or dx > 0.1:
                        self.hide.add(n)
        # what still crosses: hide the lines of the quest whose line is not its tree line
        for _ in range(40):
            vis = [(p_, n) for p_, n in edges if n not in self.hide and p_ in self.pos and n in self.pos]
            hit = None
            for i in range(len(vis)):
                for j in range(i + 1, len(vis)):
                    (a1, a2), (b1, b2) = vis[i], vis[j]
                    if {a1, a2} & {b1, b2}:
                        continue
                    if _crosses(self.pos[a1], self.pos[a2], self.pos[b1], self.pos[b2]):
                        hit = (vis[i], vis[j])
                        break
                if hit:
                    break
            if not hit:
                break
            cands = [e for e in hit if e[0] != parent.get(e[1])] or list(hit)
            victim = max(cands, key=lambda e: len(preds[e[1]]))[1]
            self.hide.add(victim)

        # quests without a link: a grid under the tree
        if floating:
            floating.sort(key=lambda n: (by[n]["y"], by[n]["x"]))
            big = max(_size(by[n]) for n in floating)
            gy0 = (top * ROW_H + 0.6 + big / 2) if linked else 0.0
            gx0 = min((p[0] for p in self.pos.values()), default=0.0)
            step = max(1.6, big + 0.6)
            for i, n in enumerate(floating):
                r, c = divmod(i, GRID_COLS)
                self.pos[n] = (gx0 + c * step, gy0 + r * step)
                self.hide.add(n)
        # normalise to start at (0, 0)
        self._fold(by, parent)
        xs = [p[0] - _size(by[n]) / 2 for n, p in self.pos.items()]
        ys = [p[1] - _size(by[n]) / 2 for n, p in self.pos.items()]
        x0, y0 = min(xs), min(ys)
        self.pos = {n: (p[0] - x0, p[1] - y0) for n, p in self.pos.items()}
        self.w = max(p[0] + _size(by[n]) / 2 for n, p in self.pos.items())
        self.h = max(p[1] + _size(by[n]) / 2 for n, p in self.pos.items())

    def _fold(self, by, parent):
        """A cluster much wider than tall (a long chain) folds: what lies past MAX_W continues
        in a second row below, so a chapter does not become one endless line. The one line
        that would run back across the fold is hidden."""
        if not self.pos:
            return
        xs = [p[0] for p in self.pos.values()]
        ys = [p[1] for p in self.pos.values()]
        x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        if x1 - x0 <= MAX_W:
            return
        cut = x0 + MAX_W
        drop = (y1 - y0) + 1.6
        for n, (x, y) in list(self.pos.items()):
            if x > cut + 0.01:
                self.pos[n] = (x - MAX_W - COL_W * 0.5, y + drop)
        for n in self.pos:
            p_ = parent.get(n)
            if p_ in self.pos:
                a, b = self.pos[p_], self.pos[n]
                if ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5 > 4.5:
                    self.hide.add(n)

    def _block(self, parent, leaves, x0, y0, cols, rows):
        """Leaves of one parent in a tight block, filled column by column, lines hidden."""
        for i, n in enumerate(leaves):
            c, r = divmod(i, rows)
            self.pos[n] = (x0 + c * BLOCK_W, y0 + r * BLOCK_H + BLOCK_H / 2)
            self.hide.add(n)


def _crosses(p1, p2, p3, p4):
    """Whether the segments p1p2 and p3p4 cross (touching ends do not count)."""
    def orient(a, b, c):
        v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)
    o1, o2, o3, o4 = orient(p1, p2, p3), orient(p1, p2, p4), orient(p3, p4, p1), orient(p3, p4, p2)
    return o1 * o2 < 0 and o3 * o4 < 0


def _pack(boxes, width):
    """Shelf packing in order: (w, h) boxes into rows no wider than width; returns (x, y) each."""
    out, x, y, row_h = [], 0.0, 0.0, 0.0
    for w, h in boxes:
        if x > 0 and x + w > width:
            x, y, row_h = 0.0, y + row_h + CLUSTER_GAP_Y, 0.0
        out.append((x, y))
        x += w + CLUSTER_GAP_X
        row_h = max(row_h, h)
    total_w = max((p[0] + b[0] for p, b in zip(out, boxes)), default=0.0)
    total_h = max((p[1] + b[1] for p, b in zip(out, boxes)), default=0.0)
    return out, total_w, total_h


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
    note_of = {}
    for n in notes:
        note_of.setdefault(_nearest_section(n, sections) if sections else -1, []).append(n)
    if title:
        for n in notes:
            if n["y"] < title[0]["y"] + title[0]["height"]:
                note_of[_nearest_section(n, sections) if sections else -1].remove(n)
                note_of.setdefault("title", []).append(n)

    member = _assign_members(quests, sections, by_name)
    root = quests[0]
    groups = {}
    for q in quests:
        groups.setdefault(member[q["name"]], []).append(q)

    # every group is a cluster; its heading and notes become part of its box
    clusters = []
    for gi in sorted(groups.keys()):
        members = groups[gi]
        c = _Cluster(members, root)
        head = sections[gi] if gi >= 0 else None
        head_h = head["height"] + BANNER_GAP if head else 0.0
        band_notes = sorted(note_of.get(gi, []), key=lambda n: (n["y"], n["x"]))
        notes_h = (max(n["height"] for n in band_notes) + 0.5) if band_notes else 0.0
        notes_w = sum(n["width"] + 0.5 for n in band_notes)
        w = max(c.w, head["width"] if head else 0.0, notes_w)
        h = head_h + c.h + notes_h
        clusters.append((gi, c, head, band_notes, head_h, w, h))

    area = sum(w * h for *_, w, h in clusters)
    widest = max((w for *_, w, h in clusters), default=1.0)
    width = max(widest, (area * ASPECT) ** 0.5 * 1.15)
    # the strip before the first heading (the root) sits to the left of the first row
    spots, total_w, total_h = _pack([(w, h) for *_, w, h in clusters], width)

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
        y_top = t["height"] / 2 + 1.0

    for (gi, c, head, band_notes, head_h, w, h), (cx, cy) in zip(clusters, spots):
        ox, oy = cx - 0.5, y_top + cy
        if head:
            head["x"], head["y"] = ox + head["width"] / 2, oy + head["height"] / 2
            out_images.append(head)
        for q in c.members:
            px, py = c.pos[q["name"]]
            q["x"] = ox + px
            q["y"] = oy + head_h + py
            names = {m["name"] for m in c.members}
            cross = [d for d in q["deps"] if d not in names]
            if q["name"] in c.hide or (cross and len(cross) >= len(q["deps"]) - len(cross)):
                q["hide_lines"] = True
        nx = ox
        for n in band_notes:
            n["x"], n["y"] = nx + n["width"] / 2, oy + head_h + c.h + 0.5 + n["height"] / 2
            out_images.append(n)
            nx += n["width"] + 0.5
    # a line from another cluster that runs far across the map goes; the quest's panel lists it
    for gi, c, *_ in clusters:
        names = {m["name"] for m in c.members}
        for q in c.members:
            for d in q["deps"]:
                if d in names or d not in by_name:
                    continue
                o = by_name[d]
                if ((o["x"] - q["x"]) ** 2 + (o["y"] - q["y"]) ** 2) ** 0.5 > 5.0:
                    q["hide_lines"] = True
    # a line that runs through another quest or a banner reads as a link to it: such a quest
    # shows no lines
    allq = [m for _, c, *_ in clusters for m in c.members]
    for q in allq:
        if q.get("hide_lines"):
            continue
        for d in q["deps"]:
            o = by_name.get(d)
            if o is None or "x" not in o:
                continue
            if any(_through(o, q, (k["x"], k["y"]), _size(k) * 0.5 + 0.05) for k in allq if k is not o and k is not q) \
                    or any(_through(o, q, (im["x"], im["y"]), None, im) for im in out_images):
                q["hide_lines"] = True
                break
    ch["images"] = out_images


def _through(a, b, c, r, box=None):
    """Whether the segment a-b passes over the point c (within r) or over the box."""
    ax, ay, bx, by = a["x"], a["y"], b["x"], b["y"]
    dx, dy = bx - ax, by - ay
    L = dx * dx + dy * dy
    if L == 0:
        return False
    if box is not None:
        steps = 24
        for i in range(1, steps):
            t = i / steps
            px, py = ax + t * dx, ay + t * dy
            if abs(px - box["x"]) < box["width"] / 2 and abs(py - box["y"]) < box["height"] / 2:
                return True
        return False
    t = ((c[0] - ax) * dx + (c[1] - ay) * dy) / L
    if not 0.0 < t < 1.0:
        return False
    px, py = ax + t * dx, ay + t * dy
    return (px - c[0]) ** 2 + (py - c[1]) ** 2 < r * r
