# Sanaei Subscription Template

یک تمپلت مدرن، سبک و مستقل برای صفحهٔ سابسکریپشن **MHSanaei/3x-ui**. این پروژه با متغیرهای رسمی تمپلت‌های سفارشی 3x-ui سازگار است و برای نسخه‌های جدید شاخهٔ `main` طراحی شده است.

## قابلیت‌ها

- رابط کاربری RTL فارسی با طراحی شیشه‌ای و واکنش‌گرا
- نمایش مصرف، باقی‌مانده، سقف ترافیک، تاریخ انقضا و آخرین اتصال
- وضعیت آنلاین/آفلاین و بروزرسانی زنده از endpoint رسمی `?format=info`
- لینک‌های اتصال چندگانه با دکمهٔ کپی
- لینک‌های مستقیم Raw، JSON و Clash/Mihomo در صورت فعال بودن در پنل
- بدون CDN، فونت خارجی یا JavaScript dependency؛ مناسب سرورهای محدود
- نصب تکرارپذیر با پشتیبان‌گیری خودکار از نسخهٔ قبلی

## نصب سریع

دستور زیر را روی سرور 3x-ui اجرا کنید:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main/install.sh)
```

نصب‌کننده به‌صورت پیش‌فرض تمپلت را در `/opt/3x-ui-subscription-template` قرار می‌دهد. سپس در پنل به مسیر زیر بروید و همین مسیر را وارد کنید:

`Settings → Subscription → Information → Sub Theme Directory`

برای مسیر دلخواه:

```bash
SUB_THEME_DIR=/srv/3x-ui-sub bash <(curl -fsSL https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main/install.sh)
```

پس از ذخیرهٔ تنظیمات پنل، URL سابسکریپشن را بازخوانی کنید. برای بروزرسانی همین دستور نصب را دوباره اجرا کنید؛ فایل قبلی به‌صورت خودکار با پسوند `.bak.YYYYMMDDHHMMSS` نگهداری می‌شود.

## سازگاری

تمپلت از متغیرهای مستند رسمی 3x-ui شامل `sId`، `enabled`، `isOnline`، مقادیر مصرف، timestampهای `expire` و `lastOnline`، URLهای اشتراک، `links`، `announce` و `subSupportUrl` استفاده می‌کند. طبق قرارداد 3x-ui، `expire` برحسب ثانیه و `lastOnline` برحسب میلی‌ثانیه دریافت می‌شود.

آخرین نسخهٔ پایدار مشاهده‌شدهٔ 3x-ui در زمان ساخت این پروژه **v3.8.0** است. خود تمپلت به نسخهٔ خاصی از backend وابسته نیست و از قرارداد رسمی `custom-subscription-templates.md` استفاده می‌کند.

## تست و عیب‌یابی

برای بررسی syntax فایل HTML و تگ‌های Go template:

```bash
./tests/validate.sh
```

اگر صفحهٔ پیش‌فرض نمایش داده شد، مسیر **Sub Theme Directory** باید absolute و دقیقاً پوشه‌ای باشد که `index.html` داخل آن قرار دارد. اگر وضعیت زنده تغییر نکرد، endpoint سابسکریپشن باید از همان origin قابل دسترس باشد و کلاینت/پروکسی نباید `?format=info` را حذف کند.

## مجوز

MIT. این تمپلت یک پروژهٔ مستقل است و جایگزین خود 3x-ui نیست. استفاده از 3x-ui باید مطابق مجوز و هشدارهای پروژهٔ اصلی انجام شود.
