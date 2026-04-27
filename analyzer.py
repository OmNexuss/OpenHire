import openai
import json

class OptiAnalyzer:
    def __init__(self, mode="standard", api_key=None):
        self.mode = mode
        self.api_key = api_key

    def analyze(self, cv_text, raw_page_text):
        # Sayfadaki gürültüyü temizle ve sadece anlamlı blokları al
        cleaned_text = self._clean_raw_text(raw_page_text)
        
        if self.mode == "ai" and self.api_key:
            return self._ai_matching(cv_text, cleaned_text)
        else:
            return self._keyword_matching(cv_text, cleaned_text)

    def _clean_raw_text(self, text):
        # Google navigasyon ve footer gürültülerini filtrele
        noise = ["gizlilik", "şartlar", "tümü", "ayarlar", "bildirim", "hakkında", "paylaş"]
        lines = text.split('\n')
        # Sadece yeterli uzunluktaki ve gürültü içermeyen satırları birleştir
        filtered = [l.strip() for l in lines if len(l) > 15 and not any(n in l.lower() for n in noise)]
        return " ".join(filtered)

    # analyzer.py içindeki _keyword_matching metodunu tamamen bununla değiştirin:
    def _keyword_matching(self, cv_text, job_description):
        # Sizin CV'nizdeki (Ali Rıza Fatih Bakırcı) kritik uzmanlıklar
        # analyzer.py içindeki target_techs listesini genişletelim:
        target_techs = {
            "python": ["python"],
            "javascript": ["javascript", "js", "typescript", "ts"],
            "react": ["react", "react.js", "reactjs"],
            "next.js": ["next.js", "nextjs"],
            "fastapi": ["fastapi"],
            "node.js": ["node.js", "nodejs", "node"],
            "sql": ["sql", "postgresql", "mysql", "mongodb", "database"],
            "docker": ["docker", "container"],
            "git": ["git", "github", "gitlab"],
            "rest api": ["rest", "api", "backend"]
        }
        
        job_lower = job_description.lower()
        matches = []
        for tech, keywords in target_techs.items():
            if any(kw in job_lower for kw in keywords):
                matches.append(tech)
        
        job_lower = job_description.lower()
        # Kelime kelime değil, metin içinde var mı diye kontrol ediyoruz
        matches = [tech for tech in target_techs if tech in job_lower]
        
        # Ağırlıklı skorlama (Sizin uzmanlıklarınızın iş tanımındaki yoğunluğu)
        score = (len(matches) / len(target_techs)) * 100
        
        return round(score, 2), f"Eşleşen Teknolojiler: {', '.join(matches)}"