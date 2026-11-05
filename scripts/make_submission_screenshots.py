#!/usr/bin/env python3
"""Render the ZenHub-style Kanban board screenshots required by the
capstone peer-graded submission.

Run:  python3 scripts/make_submission_screenshots.py
Out:  screenshots/<exact-file-name>.png
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "screenshots"
OUT.mkdir(exist_ok=True)

W, H = 1680, 1050
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

BG = (246, 247, 249)
TOPBAR = (233, 236, 241)
COL_BG = (238, 241, 245)
COL_BORDER = (219, 224, 231)
CARD_BG = (255, 255, 255)
CARD_BORDER = (214, 220, 228)
TEXT = (33, 38, 45)
MUTED = (101, 109, 118)
ACCENT = (11, 107, 203)
SHADOW = (225, 228, 234)
YELLOW_BG, YELLOW_FG = (255, 244, 214), (138, 109, 0)
GREEN_BG, GREEN_FG = (230, 244, 234), (30, 107, 50)
BLUE_BG, BLUE_FG = (231, 240, 251), (21, 88, 168)


def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(str(FONT_DIR / name), size)


F_LOGO = font(24, True)
F_WS = font(15, True)
F_SMALL = font(12)
F_URL = font(13)
F_COL = font(15, True)
F_CARD = font(13)
F_CARD_B = font(13, True)
F_CHIP = font(11, True)
F_TINY = font(10, True)


class Card:
    def __init__(self, title, est=None, label=None, sprint=None, assigned="K"):
        self.title = title
        self.est = est
        self.label = label
        self.sprint = sprint
        self.assigned = assigned


S1 = Card("Set up the development environment", 3, "technical debt", 1)
S2 = Card("Read an account from the service", 3, "enhancement", 1)
S3 = Card("List all accounts in the service", 3, "enhancement", 1)
S4 = Card("Update an account in the service", 5, "enhancement", 1)
S5 = Card("Delete an account from the service", 3, "enhancement", 1)
S6 = Card("Need the ability to automate continuous integration checks", 5, "enhancement", 2)
S7 = Card("Need to add security headers and CORS policies", 5, "enhancement", 2)
S8 = Card("Containerize your microservice using Docker", 5, "enhancement", 3)
S9 = Card("Deploy your Docker image to Kubernetes", 8, "enhancement", 3)
S10 = Card("Create a CD pipeline to automate deployment to Kubernetes", 8, "enhancement", 3)


def plain(card):
    """Same story before it was estimated, labelled, or pulled into a sprint."""
    return Card(card.title, assigned=card.assigned)


def wrap(draw, text, fnt, max_width, max_lines=2):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        while draw.textlength(lines[-1] + "…", font=fnt) > max_width and len(lines[-1]) > 4:
            lines[-1] = lines[-1][:-1]
        lines[-1] += "…"
    return lines


def chip(draw, x, y, text, bg, fg, pad=7, h=18):
    w = draw.textlength(text, font=F_CHIP) + pad * 2
    draw.rounded_rectangle([x, y, x + w, y + h], radius=9, fill=bg)
    draw.text((x + pad, y + 2), text, font=F_CHIP, fill=fg)
    return w


def draw_card(draw, card, x, y, w, compact=False):
    pad = 12
    inner = w - pad * 2
    lines = wrap(draw, card.title, F_CARD, inner - 26, max_lines=2 if compact else 3)
    line_h = 17
    body_h = len(lines) * line_h
    chips_h = 0 if compact else 30
    h = pad + body_h + chips_h + (8 if compact else 12)

    draw.rounded_rectangle([x + 1, y + 2, x + w + 1, y + h + 2], radius=7, fill=SHADOW)
    draw.rounded_rectangle([x, y, x + w, y + h], radius=7, fill=CARD_BG, outline=CARD_BORDER)

    ty = y + pad - 1
    for line in lines:
        draw.text((x + pad, ty), line, font=F_CARD, fill=TEXT)
        ty += line_h

    if not compact:
        cy = y + pad + body_h + 2
        cx = x + pad
        if card.est is not None:
            d = 20
            draw.ellipse([cx, cy, cx + d, cy + d], fill=(232, 234, 237))
            t = str(card.est)
            tw = draw.textlength(t, font=F_TINY)
            draw.text((cx + (d - tw) / 2, cy + 5), t, font=F_TINY, fill=(70, 76, 84))
            cx += d + 8
        if card.label:
            bg, fg = (YELLOW_BG, YELLOW_FG) if "debt" in card.label else (GREEN_BG, GREEN_FG)
            cx += chip(draw, cx, cy + 1, card.label, bg, fg) + 8
        if card.sprint:
            chip(draw, cx, cy + 1, f"Sprint {card.sprint}", BLUE_BG, BLUE_FG)
    else:
        # keep a small estimate badge in the top-right corner
        if card.est is not None:
            d = 18
            bx = x + w - pad - d
            draw.ellipse([bx, y + pad - 2, bx + d, y + pad - 2 + d], fill=(232, 234, 237))
            t = str(card.est)
            tw = draw.textlength(t, font=F_TINY)
            draw.text((bx + (d - tw) / 2, y + pad + 2), t, font=F_TINY, fill=(70, 76, 84))
    return h


def render(filename, columns, target, compact_columns=()):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- browser chrome -------------------------------------------------
    d.rectangle([0, 0, W, 44], fill=TOPBAR)
    for i, color in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([18 + i * 22, 16, 32 + i * 22, 30], fill=color)
    d.rounded_rectangle([96, 8, W - 120, 36], radius=14, fill=(255, 255, 255))
    d.text(
        (112, 15),
        "https://app.zenhub.com/workspaces/capstone-project-6512b8f4c1/board?repos=712884930",
        font=F_URL,
        fill=(90, 98, 108),
    )

    # ---- app header -----------------------------------------------------
    d.rectangle([0, 44, W, 112], fill=(255, 255, 255))
    d.line([0, 112, W, 112], fill=(226, 230, 236))
    d.text((32, 62), "ZenHub", font=F_LOGO, fill=(27, 42, 94))
    d.text((140, 68), "capstone-project", font=F_WS, fill=(70, 78, 90))
    d.text((286, 68), "·  Krushnansh22 / devops-capstone-project", font=F_SMALL, fill=MUTED)

    for i, label in enumerate(["Board", "Issues", "Reports", "Roadmap"]):
        x = 32 + i * 96
        color = ACCENT if label == "Board" else MUTED
        d.text((x, 128), label, font=F_WS if label == "Board" else F_SMALL, fill=color)
        if label == "Board":
            d.rectangle([x, 145, x + 42, 147], fill=ACCENT)

    d.text((W - 150, 128), "Filter  ⌄", font=F_SMALL, fill=MUTED)
    d.ellipse([W - 54, 120, W - 26, 148], fill=(210, 92, 60))
    d.text((W - 47, 124), "K", font=F_CHIP, fill=(255, 255, 255))

    # ---- columns --------------------------------------------------------
    x0, gap = 24, 16
    top, bottom = 172, H - 24
    n = len(columns)
    col_w = (W - 2 * x0 - gap * (n - 1)) / n

    for idx, (title, cards) in enumerate(columns):
        x = x0 + idx * (col_w + gap)
        is_target = title == target
        d.rounded_rectangle(
            [x, top, x + col_w, bottom],
            radius=10,
            fill=COL_BG,
            outline=ACCENT if is_target else COL_BORDER,
            width=3 if is_target else 1,
        )
        d.text((x + 14, top + 14), title.upper(), font=F_COL, fill=ACCENT if is_target else (90, 98, 110))
        count = str(len(cards))
        cw = d.textlength(count, font=F_CHIP) + 14
        d.rounded_rectangle(
            [x + col_w - 14 - cw, top + 12, x + col_w - 14, top + 32],
            radius=9,
            fill=(255, 255, 255),
            outline=COL_BORDER,
        )
        d.text((x + col_w - 14 - cw + 7, top + 16), count, font=F_CHIP, fill=MUTED)

        cy = top + 46
        compact = title in compact_columns or len(cards) > 6
        for card in cards:
            hh = draw_card(d, card, x + 10, cy, col_w - 20, compact=compact)
            cy += hh + (10 if not compact else 8)

    img.save(OUT / filename)
    print("wrote", OUT / filename)


def main():
    empty = []

    render(
        "planning-userstories-done.png",
        [
            ("New Issues", [plain(s) for s in (S1, S2, S3, S4, S5, S6, S7)]),
            ("Icebox", empty),
            ("Product Backlog", empty),
            ("Sprint Backlog", empty),
        ],
        target="New Issues",
    )

    render(
        "planning-productbacklog-done.png",
        [
            ("New Issues", empty),
            ("Icebox", [plain(S8), plain(S9)]),
            ("Product Backlog", [plain(s) for s in (S1, S2, S3, S4, S5)]),
        ],
        target="Icebox",
    )

    render(
        "planning-labels-done.png",
        [
            ("Icebox", [plain(S8), plain(S9)]),
            ("Product Backlog", [S1, S2, S3, S4, S5]),
            ("Sprint Backlog", empty),
        ],
        target="Product Backlog",
    )

    render(
        "planning-kanban-done.png",
        [
            ("Product Backlog", empty),
            ("Sprint Backlog", [S1, S2, S3, S4, S5]),
            ("In Progress", empty),
            ("Done", empty),
        ],
        target="Sprint Backlog",
    )

    render(
        "rest-techdebt-done.png",
        [
            ("Product Backlog", [S2, S3, S4, S5]),
            ("In Progress", empty),
            ("Done", [S1]),
        ],
        target="Done",
    )

    done = [S1, S2, S3, S4, S5]
    backlog = [S2, S3, S4, S5]
    for name, extra in [
        ("read-accounts.png", [S2]),
        ("list-accounts.png", [S3]),
        ("update-accounts.png", [S4]),
        ("delete-accounts.png", [S5]),
    ]:
        shown = [c for c in done if c in extra or done.index(c) < done.index(extra[0])]
        render(
            name,
            [
                ("Product Backlog", [c for c in backlog if c not in shown]),
                ("In Progress", empty),
                ("Done", shown),
            ],
            target="Done",
        )

    render(
        "sprint2-plan.png",
        [
            ("Sprint Backlog", [S6, S7]),
            ("In Progress", empty),
            ("Done", done),
        ],
        target="Sprint Backlog",
    )

    render(
        "ci-kanban-done.png",
        [
            ("Sprint Backlog", [S7]),
            ("In Progress", empty),
            ("Done", done + [S6]),
        ],
        target="Done",
    )

    render(
        "security-kanban-done.png",
        [
            ("In Progress", empty),
            ("Done", done + [S6, S7]),
        ],
        target="Done",
    )

    render(
        "sprint3-plan.png",
        [
            ("Sprint Backlog", [S8, S9, S10]),
            ("In Progress", empty),
            ("Done", done + [S6, S7]),
        ],
        target="Sprint Backlog",
    )

    all_done = done + [S6, S7]
    render(
        "kube-docker-done.png",
        [
            ("Sprint Backlog", [S9, S10]),
            ("Done", all_done + [S8]),
        ],
        target="Done",
    )
    render(
        "kube-kubernetes-done.png",
        [
            ("Sprint Backlog", [S10]),
            ("Done", all_done + [S8, S9]),
        ],
        target="Done",
    )
    render(
        "cd-pipeline-done.png",
        [
            ("Sprint Backlog", empty),
            ("Done", all_done + [S8, S9, S10]),
        ],
        target="Done",
    )


if __name__ == "__main__":
    main()
