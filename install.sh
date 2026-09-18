#!/usr/bin/env bash
set -Eeuo pipefail

PREFIX="${SUB_THEME_DIR:-/etc/3x-ui/sub_templates/modern}"
REPO_RAW="${SUB_THEME_RAW_BASE:-https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main}"
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
for name in index.html sub.html; do
  if [[ -f "$PREFIX/$name" ]]; then
    cp -a "$PREFIX/$name" "$PREFIX/$name.bak.$(date +%Y%m%d%H%M%S)"
  fi
  install -m 0644 "$TMP" "$PREFIX/$name"
done
chown -R root:root "$PREFIX"
chmod 0755 "$PREFIX"

echo
echo "تمپلت مدرن با موفقیت نصب شد: $PREFIX"
echo "اکنون دقیقاً همین مسیر را در پنل وارد کنید:"
echo "Settings → Subscription → Information → Sub Theme Directory"
echo "مسیر: $PREFIX"
echo
echo "اگر پنل از قبل باز بوده، تنظیمات را Save کنید و صفحه سابسکریپشن را با Ctrl+F5 بازخوانی کنید."
echo "برای مسیر دلخواه:"
echo "SUB_THEME_DIR=/srv/3x-ui-sub bash <(curl -fsSL $REPO_RAW/install.sh)"
