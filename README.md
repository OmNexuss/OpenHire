# 🚀 OpenHire | Intelligent Job-CV Matcher

**OpenHire**, iş ilanlarını CV'nizle analiz eden, teknik yetkinliklerinizi ilan gereksinimleriyle eşleştiren ve size bir uygunluk skoru sunan, **Playwright** tabanlı bir derin tarama (Deep Scraping) ve analiz motorudur.

---

## 🛠️ Mimari ve Teknik Stack

Proje, yüksek modülerlik ve "Clean Architecture" prensipleriyle yapılandırılmıştır:

- **Dil:** Python 3.x
- **Otomasyon Katmanı:** [Playwright](https://playwright.dev/) & `playwright-stealth` (Bot koruması baypası için)
- **Veri Ayrıştırma:** `PyPDF2` (CV içerik analizi)
- **Analiz Motoru:** Ağırlıklı anahtar kelime eşleştirme ve teknik yoğunluk algoritması.
- **Platform:** Windows/Linux/macOS uyumlu.

---

## 📋 Mevcut Özellikler (Current Capabilities)

- **Deep Content Extraction:** Google Jobs üzerindeki karmaşık DOM yapılarını ve Shadow-DOM bileşenlerini analiz ederek iş tanımlarını söküp alma.
- **Smart Tech-Stack Detection:** CV'deki uzmanlıkları (React, Next.js, FastAPI, Node.js vb.) sadece kelime bazlı değil, varyasyonlarıyla (örn: Nodejs/Node.js) eşleştirme.
- **Hybrid Operation:** Tam otomasyonun engellendiği noktalarda `Pause/Resume` mekanizmasıyla manuel müdahaleye izin veren hibrit çalışma modeli.
- **Instant Reporting:** Eşleşen teknolojiler üzerinden %0-%100 arası skorlama ve neden-sonuç raporu.

---

## 📊 Proje Durumu: "Virgül" (Paused)

> **"Başarı için nerede duracağınızı veya nerede virgül koyacağınızı iyi bilin."**

Proje şu an **v1.0-alpha** aşamasında "virgül" moduna alınmıştır. 
- **Tamamlananlar:** CV ayrıştırma motoru, teknik eşleşme algoritması, temel tarayıcı otomasyonu ve hibrit veri yakalama katmanı.
- **Bekleyenler:** Google'ın ileri düzey dinamik içerik korumalarını ve erişilebilirlik katmanlarını baypas edecek daha gelişmiş görsel tanıma veya API entegrasyonu.

---

## 🚀 Kurulum


# Depoyu klonlayın
git clone [https://github.com/OmNexuss/OpenHire.git](https://github.com/OmNexuss/OpenHire.git)

# Dizin içine girin
cd OpenHire

# Bağımlılıkları yükleyin
pip install playwright playwright-stealth PyPDF2

# Playwright tarayıcılarını kurun
playwright install chromium

---

## 💡 Kullanım


1. cv.pdf dosyanızı proje kök dizinine ekleyin.
2. Uygulamayı başlatın: python main.py
3. Tarayıcı açıldığında hedef ilana manuel olarak tıklayın.
4. Sağ panelde iş tanımı tam yüklendiğinde, terminalde bekleyen Playwright panelinden RESUME butonuna basın.
---
⚖️ Lisans
Bu proje kişisel gelişim ve Ar-Ge amaçlıdır. Tüm hakları saklıdır.
---
**© 2026 OmNexus. All Rights Reserved.**
