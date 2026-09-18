# Sanaei Subscription Template

تمپلت سابسکریپشن سبک و سازگار با **MHSanaei/3x-ui v3.8.5** و قرارداد رسمی Custom Subscription Templates.

## نصب

```bash
curl -fsSL https://raw.githubusercontent.com/jashoahmlin2/sanaei-subscription-template/main/install.sh | sudo bash
```

نصب‌کننده این مسیر را می‌سازد و دو فایل `index.html` و `sub.html` را قرار می‌دهد:

```text
/etc/3x-ui/sub_templates/modern
```

سپس در پنل 3x-ui مسیر زیر را دقیقاً روی همین پوشه قرار دهید و Save کنید:

```text
Settings → Subscription → Information → Sub Theme Directory
```

بعد لینک سابسکریپشن را با `Ctrl+F5` باز کنید.

## ویژگی‌های نسخهٔ v3

این نسخه عمداً بدون `grid`، `backdrop-filter`، CDN و وابستگی خارجی ساخته شده است تا با renderer فعلی 3x-ui و مرورگرهای موبایل سازگار باشد. از layout سادهٔ block/inline-block، `viewport` استاندارد، شکستن لینک‌های طولانی، کارت‌های تک‌ستونه در عرض کمتر از 600px، fallback کپی لینک و endpoint رسمی `?format=info` استفاده می‌کند.

## متغیرهای رسمی استفاده‌شده

`subTitle`, `sId`, `enabled`, `isOnline`, `used`, `remained`, `total`, `expire`, `lastOnline`, `downloadByte`, `uploadByte`, `totalByte`, `subUrl`, `subJsonUrl`, `subClashUrl`, `links`, `announce` و `subSupportUrl`.

## تست

```bash
./tests/validate.sh
```

اگر صفحهٔ پیش‌فرض نمایش داده شد، مقدار **Sub Theme Directory** خالی یا اشتباه است. اگر صفحه فشرده و عریض نمایش داده شد، نسخهٔ قدیمی cache شده است؛ نصب را دوباره اجرا کنید و صفحه را در Incognito/Private با Ctrl+F5 باز کنید.

## مجوز

MIT. این پروژه مستقل از خود 3x-ui است.
