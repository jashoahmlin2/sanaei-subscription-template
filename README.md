# Sanaei Subscription Template

تمپلت مدرن، سبک و مستقل برای صفحهٔ سابسکریپشن **MHSanaei/3x-ui**. این پروژه با قرارداد رسمی Custom Subscription Templates سازگار است.

## قابلیت‌ها

- رابط RTL فارسی با طراحی شیشه‌ای و واکنش‌گرا
- مصرف، باقی‌مانده، سقف ترافیک، انقضا و آخرین اتصال
- وضعیت آنلاین/آفلاین و بروزرسانی زنده از `?format=info`
- لینک‌های چندگانه با کپی سریع
- Raw، JSON و Clash/Mihomo در صورت فعال بودن در پنل
- بدون CDN، فونت خارجی یا وابستگی JavaScript

## نصب سریع

روی همان سروری که 3x-ui نصب است اجرا کنید:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main/install.sh)
```

مسیر پیش‌فرض نصب:

```text
/etc/3x-ui/sub_templates/modern
```

نکتهٔ مهم: اجرای install به‌تنهایی تم را فعال نمی‌کند. در پنل 3x-ui به مسیر زیر بروید و **دقیقاً** همین مسیر را ذخیره کنید:

```text
Settings → Subscription → Information → Sub Theme Directory
```

```text
/etc/3x-ui/sub_templates/modern
```

نصب‌کننده برای سازگاری با نسخه‌های مختلف هر دو فایل `index.html` و `sub.html` را قرار می‌دهد. پس از Save، لینک صفحهٔ اشتراک را با `Ctrl+F5` باز کنید. اگر این فیلد خالی باشد یا مسیر اشتباه باشد، 3x-ui طبق طراحی به صفحهٔ پیش‌فرض برمی‌گردد.

برای مسیر دلخواه:

```bash
SUB_THEME_DIR=/srv/3x-ui-sub bash <(curl -fsSL https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main/install.sh)
```

## سازگاری

تمپلت از متغیرهای رسمی 3x-ui شامل `sId`، `enabled`، `isOnline`، مقادیر مصرف، timestampهای `expire` و `lastOnline`، URLهای اشتراک، `links`، `announce` و `subSupportUrl` استفاده می‌کند. `expire` برحسب ثانیه و `lastOnline` برحسب میلی‌ثانیه دریافت می‌شود.

## تست

```bash
./tests/validate.sh
```

اگر بعد از تنظیم مسیر هنوز صفحهٔ پیش‌فرض را دیدید، این سه مورد را بررسی کنید:

1. مسیر تنظیم‌شده باید **پوشه** باشد، نه مسیر فایل؛ یعنی در انتها `index.html` ننویسید.
2. کاربر سرویس 3x-ui باید دسترسی خواندن پوشه و فایل‌ها را داشته باشد.
3. پس از ذخیرهٔ تنظیمات، URL را با `Ctrl+F5` یا در پنجرهٔ ناشناس باز کنید.

## مجوز

MIT. این تمپلت مستقل است و جایگزین خود 3x-ui نیست.
