#!/usr/bin/env bash
set -Eeuo pipefail

PREFIX="${SUB_THEME_DIR:-/etc/3x-ui/sub_templates/modern}"
REPO_RAW="${SUB_THEME_RAW_BASE:-https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main}"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

if [[ "${EUID}" -eq 0 ]]; then
  SUDO=()
elif command -v sudo >/dev/null 2>&1; then
  SUDO=(sudo)
else
  echo "خطا: برای نصب در $PREFIX باید root باشید یا sudo نصب باشد." >&2
  echo "دوباره با این دستور اجرا کنید: sudo bash <(curl -fsSL $REPO_RAW/install.sh)" >&2
  exit 1
fi

command -v curl >/dev/null 2>&1 || { echo "خطا: curl نصب نیست." >&2; exit 1; }
if [[ -e "$PREFIX" && ! -d "$PREFIX" ]]; then
  echo "خطا: مسیر مقصد وجود دارد اما پوشه نیست: $PREFIX" >&2
  exit 1
fi

curl --fail --silent --show-error --location --retry 3 --connect-timeout 10 "$REPO_RAW/index.html" -o "$TMP"
[[ -s "$TMP" ]] || { echo "خطا: دانلود تمپلت خالی است." >&2; exit 1; }

"${SUDO[@]}" mkdir -p "$PREFIX"
for name in index.html sub.html; do
  if [[ -f "$PREFIX/$name" ]]; then
    "${SUDO[@]}" cp -a "$PREFIX/$name" "$PREFIX/$name.bak.$(date +%Y%m%d%H%M%S)"
  fi
  "${SUDO[@]}" install -m 0644 "$TMP" "$PREFIX/$name"
done
"${SUDO[@]}" chmod 0755 "$PREFIX"

[[ -s "$PREFIX/index.html" && -s "$PREFIX/sub.html" ]] || { echo "خطا: بررسی نصب ناموفق بود." >&2; exit 1; }

echo
echo "تمپلت مدرن با موفقیت نصب شد: $PREFIX"
echo "فایل‌ها: $PREFIX/index.html و $PREFIX/sub.html"
echo
echo "در پنل 3x-ui این مسیر را ذخیره کنید:"
echo "Settings → Subscription → Information → Sub Theme Directory"
echo "مسیر: $PREFIX"
echo
echo "پس از Save، صفحه سابسکریپشن را با Ctrl+F5 بازخوانی کنید."
