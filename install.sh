#!/usr/bin/env bash
set -Eeuo pipefail

if [[ -n "${SUB_THEME_DIR:-}" ]]; then PREFIX="$SUB_THEME_DIR"
elif [[ -d /etc/3x-ui ]]; then PREFIX=/etc/3x-ui/sub_templates/modern
else PREFIX=/etc/x-ui/sub_templates/modern
fi
REPO_RAW="${SUB_THEME_RAW_BASE:-https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main}"
ASSET_RAW="${SUB_THEME_ASSET_BASE:-https://github.com/jashoahmlin2/sanaei-subscription-template/raw/refs/heads/main}"
TMP="$(mktemp)"; trap 'rm -f "$TMP" "$TMP.hero"' EXIT
if [[ "${EUID}" -eq 0 ]]; then SUDO=(); elif command -v sudo >/dev/null 2>&1; then SUDO=(sudo); else echo "خطا: نصب را با sudo اجرا کنید." >&2; exit 1; fi
command -v curl >/dev/null 2>&1 || { echo "خطا: curl نصب نیست." >&2; exit 1; }
if [[ -e "$PREFIX" && ! -d "$PREFIX" ]]; then echo "خطا: مقصد فایل است، پوشه نیست: $PREFIX" >&2; exit 1; fi
curl --fail --silent --show-error --location --retry 3 --connect-timeout 10 "$REPO_RAW/index.html" -o "$TMP"
curl --fail --silent --show-error --location --retry 3 --connect-timeout 10 "$ASSET_RAW/assets/pasargadae-hero.jpg" -o "$TMP.hero"
[[ -s "$TMP" && -s "$TMP.hero" ]] || { echo "خطا: دانلود قالب یا تصویر ناموفق بود." >&2; exit 1; }
"${SUDO[@]}" mkdir -p "$PREFIX/assets"
"${SUDO[@]}" install -m 0644 "$TMP.hero" "$PREFIX/assets/pasargadae-hero.jpg"
for name in index.html sub.html; do
  if [[ -f "$PREFIX/$name" ]]; then "${SUDO[@]}" cp -a "$PREFIX/$name" "$PREFIX/$name.bak.$(date +%Y%m%d%H%M%S)"; fi
  "${SUDO[@]}" install -m 0644 "$TMP" "$PREFIX/$name"
done
"${SUDO[@]}" chmod 0755 "$PREFIX" "$PREFIX/assets"
"${SUDO[@]}" test -s "$PREFIX/index.html" && "${SUDO[@]}" test -s "$PREFIX/sub.html" && "${SUDO[@]}" test -s "$PREFIX/assets/pasargadae-hero.jpg"
echo
echo "نصب موفق بود: $PREFIX"
echo "فایل‌ها: index.html، sub.html و assets/pasargadae-hero.jpg"
echo "همین مسیر را در Settings → Subscription → Information → Sub Theme Directory وارد کنید:"
echo "$PREFIX"
echo "اگر 3x-ui داخل Docker است، این مسیر باید داخل volume کانتینر هم mount شده باشد."
