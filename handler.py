import base64
import runpod   # <--- dodane

def handler(event):
    """
    RunPod handler function.
    `event` zawiera dane wejściowe wysłane przez API.
    """
    # Pobierz parametry wejściowe
    input_data = event.get("input", {})
    preset = input_data.get("preset", "restore")

    # Na razie nie przetwarzamy obrazów – tylko testujemy przepływ
    result_text = f"✅ RunPod działa! Wybrany preset: {preset}"

    # Możesz tu później wstawić logikę: np. AI restore / colorize na obrazie
    return {
        "status": "ok",
        "result": result_text
    }

# 🔑 to jest najważniejsze — start serverlessa
runpod.serverless.start({"handler": handler})

# Ułatwia szybki test lokalny
if __name__ == "__main__":
    print(handler({"input": {"preset": "restore"}}))

