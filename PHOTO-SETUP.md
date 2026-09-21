# Add your photo

This is the same idea as Emmi's profile: the photo is part of the custom SVG hero.

1. Put a square portrait in `assets/`.
2. Name it `profile-photo.png` (JPG/JPEG also works).
3. Run:

```bash
python3 scripts/banner/generate.py
```

The script embeds the image into the SVG as base64, so the banner carries the photo with it.

Then:

```bash
git add .
git commit -m "feat: add profile photo"
git push
```

For the best result, use a clean portrait with your face centered and enough head/shoulder area for a circular crop.
