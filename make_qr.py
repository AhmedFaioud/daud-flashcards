#!/usr/bin/env python3
"""Generates the QR code and wires the landing page to your hosting URLs.

Usage
-----
  python3 make_qr.py --site https://USER.github.io/daud-flashcards/ \
                     --deck https://github.com/USER/daud-flashcards/releases/download/v1/Daud-Language-PreA1.apkg

  # optional: also add an "Open in AnkiWeb" button
  python3 make_qr.py --site ... --deck ... --ankiweb https://ankiweb.net/shared/info/1234567890

Outputs (in this folder):
  qr.png   — 1200 px, for screens and for print
  qr.svg   — vector, for putting on a book page
  index.html — rewritten with your real links
"""
import argparse, pathlib, re, shutil

import qrcode
from qrcode.image.svg import SvgPathImage

HERE = pathlib.Path(__file__).parent
TPL = HERE / "index.template.html"
SITE = HERE / "index.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True, help="public URL of the landing page (what the QR points at)")
    ap.add_argument("--deck", required=True, help="direct download URL of the .apkg")
    ap.add_argument("--ankiweb", default="", help="optional AnkiWeb shared-deck URL")
    ap.add_argument("--out", default="qr", help="output basename")
    a = ap.parse_args()

    # keep an untouched template the first time we run
    if not TPL.exists():
        shutil.copy(SITE, TPL)

    html = TPL.read_text(encoding="utf-8")
    html = html.replace("__DECK_URL__", a.deck)
    if a.ankiweb:
        btn = ('<a class="btn ghost" href="%s">Open in AnkiWeb (no download)</a>' % a.ankiweb)
    else:
        btn = ""
    html = html.replace("__ANKIWEB_BUTTON__", btn)
    html = html.replace("__QR_IMG__", '<img src="%s.png" alt="QR code for the deck">' % a.out)
    SITE.write_text(html, encoding="utf-8")

    # QR -> landing page
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M,
                       box_size=20, border=4)
    qr.add_data(a.site)
    qr.make(fit=True)
    qr.make_image(fill_color="#153E69", back_color="white").save(HERE / f"{a.out}.png")

    qr2 = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M,
                        box_size=20, border=4, image_factory=SvgPathImage)
    qr2.add_data(a.site)
    qr2.make(fit=True)
    qr2.make_image().save(HERE / f"{a.out}.svg")

    print("QR points at :", a.site)
    print("deck link    :", a.deck)
    print("written      :", HERE / f"{a.out}.png", "|", HERE / f"{a.out}.svg", "| index.html")


if __name__ == "__main__":
    main()
