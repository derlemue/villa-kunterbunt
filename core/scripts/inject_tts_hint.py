import os
import re

css_pulse = """
        @keyframes pulse-gold {
            0% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0.4); }
            70% { box-shadow: 0 0 0 10px rgba(212, 175, 55, 0); }
            100% { box-shadow: 0 0 0 0 rgba(212, 175, 55, 0); }
        }

        .pulse-gold {
            animation: pulse-gold 1.5s infinite;
            border-color: var(--accent-gold) !important;
            background: rgba(212, 175, 55, 0.1) !important;
        }
"""

js_hint_func = """
        function triggerTTSHint(id) {
            const hintKey = 'tts_hint_shown';
            if (localStorage.getItem(hintKey)) return;

            const ttsBtn = id ? document.getElementById(`tts-btn-${id}`) : document.getElementById('tts-btn');
            const infoText = id ? document.getElementById(`info-text-${id}`) : document.getElementById('info-text');
            
            if (!ttsBtn || !infoText) return;

            setTimeout(() => {
                ttsBtn.classList.add('pulse-gold');
                setTimeout(() => {
                    infoText.classList.add('visible');
                    setTimeout(() => {
                        infoText.classList.remove('visible');
                        ttsBtn.classList.add('pulse-gold');
                        setTimeout(() => {
                            ttsBtn.classList.remove('pulse-gold');
                        }, 3000);
                    }, 4000);
                }, 1000);
            }, 500);

            localStorage.setItem(hintKey, 'true');
        }
"""

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Index files have multiple players, episode files have one
    is_index = "index.html" in filepath
    
    # 1. Inject CSS if not present
    if "pulse-gold" not in content:
        content = content.replace(".info-text {", css_pulse + "\n        .info-text {", 1)

    # 2. Inject JS function if not present
    if "function triggerTTSHint" not in content:
        # Inject before </script>
        content = content.replace("</script>", js_hint_func + "\n    </script>", 1)

    # 3. Add IDs to TTS buttons if not present
    if is_index:
        # In main/index.html, it's done dynamically or via loop? 
        # Actually our manual pages have them in HTML.
        # Main index.html has a loop in innerHTML or hardcoded?
        # Let's check main/index.html structure.
        pass
    else:
        content = content.replace('class="info-btn" onclick="toggleInfo()">TTS</button>', 'id="tts-btn" class="info-btn" onclick="toggleInfo()">TTS</button>')

    # 4. Inject call into play logic
    # For episodes:
    if not is_index and "triggerTTSHint();" not in content:
        # main/podcast episodes use playBtn.addEventListener('click', () => { if (audio.paused) { audio.play(); ... } })
        content = content.replace("audio.play();", "audio.play();\n                triggerTTSHint();")

    with open(filepath, 'w') as f:
        f.write(content)

# We'll handle index files more carefully
directories = [
    "core/data/main/podcast",
    "core/data/cowork/podcast",
    "core/data/meta/podcast"
]

for d in directories:
    if os.path.exists(d):
        for filename in os.listdir(d):
            if filename.endswith(".html") and "index" not in filename:
                update_file(os.path.join(d, filename))
