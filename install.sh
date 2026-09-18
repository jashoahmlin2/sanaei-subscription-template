#!/usr/bin/env bash
set -Eeuo pipefail

PREFIX="${SUB_THEME_DIR:-/opt/3x-ui-subscription-template}"
REPO_RAW="${SUB_THEME_RAW_BASE:-https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main}"
TARGET="$PREFIX/index.html"
TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

if [[ "${EUID}" -ne 0 ]]; then
  echo "خطا: این نصب‌کننده باید با root اجرا شود. مثال: sudo bash install.sh" >&2
  exit 1
fi

command -v curl >/dev/null 2>&1 || { echo "خطا: curl نصب نیست." >&2; exit 1; }
mkdir -p "$PREFIX"
curl --fail --silent --show-error --location --retry 3 --connect-timeout 10 "$REPO_RAW/index.html" -o "$TMP"
[[ -s "$TMP" ]] || { echo "خطا: فایل تمپلت خالی است." >&2; exit 1; }
if [[ -f "$TARGET" ]]; then
  cp -a "$TARGET" "$TARGET.bak.$(date +%Y%m%d%H%M%S)"
fi
install -m 0644 "$TMP" "$TARGET"
chown -R root:root "$PREFIX"
chmod 0755 "$PREFIX"

echo
printf 'تمپلت با موفقیت نصب شد: %s\n' "$TARGET"
echo 'در پنل 3x-ui مسیر زیر را تنظیم کنید:'
echo 'Settings → Subscription → Information → Sub Theme Directory'
echo "مقدار مسیر: $PREFIX"
echo
 echo 'برای نصب با مسیر دلخواه:'
echo "SUB_THEME_DIR=/srv/3x-ui-sub bash <(curl -fsSL $REPO_RAW/install.sh)"
