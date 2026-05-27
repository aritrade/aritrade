# Profile assets

## `avatar.png`

The current avatar is a generated **"AD" monogram** (480×480, dark-emerald
gradient with an accent ring). It exists so the profile README ships polished
even before a real photo is uploaded.

### Swap in a real photo

Pick **one** of these — both work, no README edit required:

1. **Easiest** — drop a square photo here:
   ```sh
   cp ~/Downloads/your-linkedin-photo.jpg assets/avatar.png
   git add assets/avatar.png && git commit -m "Update profile avatar" && git push
   ```
2. **Best long-term** — update your **GitHub profile picture** in
   [Settings → Profile](https://github.com/settings/profile). It will appear
   on this README, on every commit, on every PR, and across the GitHub UI.
   Then optionally delete `assets/avatar.png` and point the README `<img>`
   at `https://github.com/aritrade.png` instead.

### Regenerate the monogram

If you want to tweak colours, initials, or the ring:

```sh
python3 assets/generate_avatar.py
```

Requires `Pillow` (`pip3 install --user Pillow`).
