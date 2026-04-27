import asyncio
import os
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

async def scrape_google_jobs(search_query):
    async with async_playwright() as p:
        user_data_dir = os.path.join(os.getcwd(), "user_data")
        context = await p.chromium.launch_persistent_context(
            user_data_dir, headless=False, args=["--disable-blink-features=AutomationControlled"]
        )
        page = context.pages[0] if context.pages else await context.new_page()
        await Stealth().apply_stealth_async(page)

        try:
            url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}&ibp=htl;jobs"
            await page.goto(url)
            print("\n[KRİTİK TALİMAT]")
            print("1. Sol listeden bir ilana TIKLAYIN.")
            print("2. Sağda 'İş Hakkında' metni göründüğünde sayfayı 2-3 saniye bekleyin.")
            print("3. Sonra RESUME'ye basın.")
            await page.pause() 

            # Veriyi çekmeden önce 'sahte' bir kullanıcı hareketi yapalım
            await page.mouse.wheel(0, 500)
            await asyncio.sleep(2)

            jobs_data = await page.evaluate("""() => {
                const results = [];
                
                // 1. ADIM: Navigasyon ve Erişilebilirlik gürültüsünü temizle
                const noiseSelectors = ['header', 'nav', '.S679S', '#gb'];
                noiseSelectors.forEach(s => {
                    const el = document.querySelector(s);
                    if(el) el.remove(); // Gürültüyü geçici olarak DOM'dan sil
                });

                // 2. ADIM: İş tanımının saklanabileceği spesifik kutuları tara
                // Google Jobs'ta iş tanımı genellikle 'yB79cc' veya 'HBvzbc' içindedir.
                const targetSelectors = ['.yB79cc', '.HBvzbc', '.tl-det', '[role="main"]'];
                let bestText = "";

                for (const selector of targetSelectors) {
                    const element = document.querySelector(selector);
                    if (element && element.innerText.length > 200) {
                        bestText = element.innerText;
                        break; 
                    }
                }

                // 3. ADIM: Eğer hala boşsa, 'Aranan Nitelikler' içeren en uzun bloğu bul
                if (!bestText) {
                    const allDivs = Array.from(document.querySelectorAll('div'));
                    const jobDivs = allDivs.filter(d => 
                        (d.innerText.includes('nitelik') || d.innerText.includes('tecrübe') || d.innerText.includes('Requirements')) 
                        && d.innerText.length > 300
                    );
                    if (jobDivs.length > 0) {
                        bestText = jobDivs.reduce((a, b) => a.innerText.length > b.innerText.length ? a : b).innerText;
                    }
                }

                if (bestText) {
                    results.push({
                        company: "Nitelikli İş Tanımı",
                        description: bestText
                    });
                }
                return results;
            }""")

            print(f"[SİSTEM] {len(jobs_data)} adet NİTELİKLİ veri bloğu yakalandı.")
            await context.close()
            return jobs_data

        except Exception as e:
            print(f"Hata: {e}")
            return []