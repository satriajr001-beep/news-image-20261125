#!/usr/bin/env python3
"""Render the 25 Nov 2026 world-news summary poster (1024x1024 PNG).

Eight stories (1 lead + 7 panels), all text drawn with PIL from DejaVu fonts —
no image model renders words. Livelier broadsheet look: drop shadows on cards,
coloured kicker pills, a bold lead with a side accent bar, gold rules with
diamond ornaments, and varied card sizes. Layout: masthead, lead card,
three panels, two wide panels, two wide panels, footer.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/home/hatch/workspace/news-image-20261125/entry.png"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

PAPER = (247, 243, 234)
NAVY = (20, 33, 61)
GOLD = (232, 163, 61)
INK = (26, 26, 26)
GRAY = (90, 90, 86)
CARD = (255, 255, 255)
BORDER = (214, 208, 194)
BODY = (60, 60, 60)
SHADOW = (226, 221, 208)
STEEL = (46, 90, 136)
TEAL = (30, 122, 90)
GREEN = (74, 122, 0)
RUST = (179, 64, 42)
MAROON = (150, 40, 80)
OCHRE = (176, 120, 20)
VIOLET = (110, 60, 150)
ORANGE = (205, 95, 20)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(text, fnt, x, y, max_w, fill, leading):
    ys = y
    for line in wrap(text, fnt, max_w):
        d.text((x, ys), line, font=fnt, fill=fill)
        ys += leading
    return ys


def diamond(cx, cy, r, fill):
    d.polygon([(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)], fill=fill)


def kicker_pill(x, y, text, color):
    """Coloured rounded pill with white bold text. Returns pill width."""
    kf = font(SANS_B, 17)
    tw = d.textlength(text, font=kf)
    pw, ph = int(tw) + 24, 28
    d.rounded_rectangle([x, y, x + pw, y + ph], radius=14, fill=color)
    d.text((x + 12, y + 5), text, font=kf, fill=(255, 255, 255))
    return pw


def card(x, y, w, h, band):
    """White card with drop shadow and a coloured top band."""
    d.rounded_rectangle([x + 4, y + 4, x + w + 4, y + h + 4], radius=10,
                        fill=SHADOW)
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD,
                        outline=BORDER, width=2)
    d.rectangle([x + 10, y, x + w - 10, y + 10], fill=band)


# ---------------- masthead ----------------
d.rectangle([0, 0, W, 128], fill=NAVY)
mast = font(SERIF_B, 60)
t = "THE WORLD TODAY"
d.text(((W - d.textlength(t, font=mast)) / 2, 16), t, font=mast, fill=(255, 255, 255))
date_f = font(SANS_B, 24)
t = "WEDNESDAY, 25 NOVEMBER 2026"
d.text(((W - d.textlength(t, font=date_f)) / 2, 84), t, font=date_f, fill=GOLD)
d.line([36, 124, W - 36, 124], fill=GOLD, width=3)
diamond(W // 2, 124, 8, GOLD)

# ---------------- lead story: Houthis / Saudi ----------------
LX, LY, LW, LH = 36, 142, 952, 198
d.rounded_rectangle([LX + 4, LY + 4, LX + LW + 4, LY + LH + 4], radius=10,
                    fill=SHADOW)
d.rounded_rectangle([LX, LY, LX + LW, LY + LH], radius=10, fill=CARD,
                    outline=BORDER, width=2)
d.rounded_rectangle([LX + 8, LY + 14, LX + 18, LY + LH - 14], radius=5, fill=RUST)
kicker_pill(LX + 34, LY + 16, "MIDDLE EAST  \u00b7  CONFLICT", RUST)
head = font(SERIF_B, 42)
d.text((LX + 34, LY + 54), "Houthis hit Saudi oil refinery", font=head, fill=INK)
body = font(SANS, 21)
lead = ("Yemen's Houthis said they struck Saudi Arabia's Ras Tanura oil refinery and "
        "Riyadh's financial district. Saudi defences said they shot down four drones, "
        "a day after a tower strike wounded 11 people.")
y_end = draw_wrapped(lead, body, LX + 34, LY + 106, LW - 62, INK, 29)
print("lead body ends at y =", y_end, "(card bottom =", LY + LH, ")")

# ---------------- "also today" header ----------------
lab = font(SANS_B, 20)
d.text((36, 356), "ALSO TODAY", font=lab, fill=NAVY)
d.rectangle([36, 382, 168, 386], fill=GOLD)
diamond(176, 384, 5, GOLD)
d.line([184, 384, 988, 384], fill=BORDER, width=2)

# ---------------- panels ----------------
panels_top = [
    dict(x=36, band=STEEL, kicker="MARKETS",
         headline="AI rally fades as stocks slide",
         body=("Nikkei fell 2.76% and Nvidia slid 6% as the AI rally faded "
               "and new US tariff threats loomed.")),
    dict(x=360, band=TEAL, kicker="SPACE",
         headline="Pakistan's first astronaut docks",
         body=("Shenzhou-24 docked at Tiangong with Muhammad Zeeshan Ali, "
               "the first foreigner aboard.")),
    dict(x=684, band=GREEN, kicker="PACIFIC",
         headline="Solomons bar foreign bases",
         body=("The Solomons signed a treaty naming Australia top security "
               "partner, barring foreign bases.")),
]
PY, PH, PW = 398, 176, 304
for p in panels_top:
    x = p["x"]
    card(x, PY, PW, PH, p["band"])
    kicker_pill(x + 18, PY + 12, p["kicker"], p["band"])
    hf = font(SERIF_B, 24)
    y = draw_wrapped(p["headline"], hf, x + 18, PY + 46, PW - 36, INK, 29)
    bf = font(SANS, 16)
    y2 = draw_wrapped(p["body"], bf, x + 18, y + 6, PW - 36, BODY, 21)
    print(p["kicker"], "panel text ends at y =", y2, "(panel bottom =", PY + PH, ")")

panels_mid = [
    dict(x=36, band=MAROON, kicker="CHINA",
         headline="Beijing probes a Politburo member",
         body=("Graft case against Shanghai chief Chen Jining, the fourth "
               "Politburo member probed since 2025.")),
    dict(x=532, band=OCHRE, kicker="INDONESIA",
         headline="Dozens trapped in Java gold mine",
         body=("Rescuers search for up to 30 miners trapped 100 metres down, "
               "after rain flooded a mine near Bogor.")),
]
PY2, PH2, PW2 = 586, 176, 456
for p in panels_mid:
    x = p["x"]
    card(x, PY2, PW2, PH2, p["band"])
    kicker_pill(x + 20, PY2 + 12, p["kicker"], p["band"])
    hf = font(SERIF_B, 27)
    y = draw_wrapped(p["headline"], hf, x + 20, PY2 + 46, PW2 - 40, INK, 32)
    bf = font(SANS, 16)
    y2 = draw_wrapped(p["body"], bf, x + 20, y + 6, PW2 - 40, BODY, 21)
    print(p["kicker"], "panel text ends at y =", y2, "(panel bottom =", PY2 + PH2, ")")

panels_bottom = [
    dict(x=36, band=VIOLET, kicker="AFRICA",
         headline="Sahel rebels take war to the skies",
         body=("Insurgents in Mali and the Sahel use cheap FPV drones to strip "
               "government forces of air superiority.")),
    dict(x=532, band=ORANGE, kicker="SPORT",
         headline="Real Madrid hit PSV for five",
         body=("Madrid beat PSV 5-1 in the Champions League; "
               "Arsenal and Man City were held to draws.")),
]
PY3, PH3, PW3 = 774, 176, 456
for p in panels_bottom:
    x = p["x"]
    card(x, PY3, PW3, PH3, p["band"])
    kicker_pill(x + 20, PY3 + 12, p["kicker"], p["band"])
    hf = font(SERIF_B, 27)
    y = draw_wrapped(p["headline"], hf, x + 20, PY3 + 46, PW3 - 40, INK, 32)
    bf = font(SANS, 16)
    y2 = draw_wrapped(p["body"], bf, x + 20, y + 6, PW3 - 40, BODY, 21)
    print(p["kicker"], "panel text ends at y =", y2, "(panel bottom =", PY3 + PH3, ")")

# ---------------- footer ----------------
d.line([36, 962, 988, 962], fill=BORDER, width=2)
ff = font(SANS, 17)
t = "Sources: Reuters \u00b7 CNN \u00b7 WSJ \u2014 25 November 2026"
tw = d.textlength(t, font=ff)
d.text(((W - tw) / 2, 972), t, font=ff, fill=GRAY)
diamond((W - tw) / 2 - 24, 980, 5, GOLD)
diamond((W + tw) / 2 + 24, 980, 5, GOLD)

img.save(OUT, optimize=True)
print("saved", OUT)
