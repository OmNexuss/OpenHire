import asyncio
from parser import extract_text_from_pdf
from analyzer import OptiAnalyzer
from engine import scrape_google_jobs

async def start_process(pdf_path, job_title, mode="standard"):
    print("Süreç başlıyor...")
    
    # ÖNCE PDF'i oku ki cv_text değişkeni oluşsun
    try:
        from parser import extract_text_from_pdf # PDF okuyucu fonksiyonunuzun adı
        cv_text = extract_text_from_pdf(pdf_path)
    except Exception as e:
        print(f"Hata: PDF okunamadı! {e}")
        return

    # ŞİMDİ print edebiliriz
    print(f"DEBUG: CV'den okunan kelime sayısı: {len(cv_text.split())}")
    
    if len(cv_text.strip()) < 10:
        print("Efendim, CV içeriği boş veya okunamadı. Lütfen PDF'i kontrol edin.")
        return

    # Geri kalan işlemler...
    jobs = await scrape_google_jobs(job_title)
    # ...
    
    analyzer = OptiAnalyzer(mode=mode, api_key="YOUR_API_KEY")

    print(f"\n--- OptiHire Analiz Raporu ({len(jobs)} blok inceleniyor) ---")
    
    found_any = False
    for i, job in enumerate(jobs[:10]): # İlk 10 bloğa odaklanalım
        score, reason = analyzer.analyze(cv_text, job['description'])
        
        # Hata ayıklama için her bloğun ilk 50 karakterini görelim
        print(f"DEBUG: Blok {i+1} içeriği -> {job['description'][:50]}...")
        
        if score > 0: # Skoru geçici olarak 0'ın üstündeki her şeye açalım
            found_any = True
            print(f"[{i+1}] Şirket: {job['company']} | Skor: %{score}")
            print(f"Analiz: {reason}")
            print("-" * 30)
    
    if not found_any:
        print("Efendim, bloklar tarandı ancak CV'nizle (Next.js, FastAPI vb.) örtüşen anlamlı bir içerik bulunamadı.")
        print("İpucu: Resume demeden önce sağ taraftaki iş tanımının tam yüklendiğinden emin olun.")

if __name__ == "__main__":
    # Efendim, cv.pdf dosyanızın klasörde olduğundan emin olun
    asyncio.run(start_process("cv.pdf", "Python Developer Istanbul", mode="standard"))