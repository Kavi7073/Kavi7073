# KAVI KANDA_ GitHub Profile

## 1. Create the profile repository

Create a **public** GitHub repository named exactly:

`Kavi7073`

It must belong to `Kavi7073`.

## 2. Copy the files from this package into it

Keep:

```text
README.md
assets/
data/
scripts/
.github/workflows/
```

## 3. Add your photo

Put it at:

`assets/profile-photo.png`

Then run:

```bash
python3 scripts/banner/generate.py
```

## 4. Generate live GitHub stats

```bash
python3 scripts/cards.py
```

## 5. Push

```bash
git add .
git commit -m "feat: build custom GitHub profile"
git push
```

## 6. Automatic stats updates

The included workflow runs daily and can also be triggered manually from GitHub Actions. It uses the repository's built-in `GITHUB_TOKEN`.

## Customize

- `data/profile.json` → identity
- `data/skills.json` → engineering radar
- `data/aimix.json` → AI/product radar
- `scripts/banner/generate.py` → hero design
- `README.md` → text, links and sections
