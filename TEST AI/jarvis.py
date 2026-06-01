import openai

# Zde vlož svůj klíč (nikomu ho neukazuj!)
client = openai.OpenAI(api_key="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")

def jarvis_odpoved(dotaz):
    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Můžeš použít i "gpt-3.5-turbo" pro úsporu peněz
            messages=[
                {"role": "system", "content": "Jsi J.A.R.V.I.S., vysoce inteligentní a sarkastický asistent z Iron Mana. Odpovídej stručně a věcně."},
                {"role": "user", "content": dotaz}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Pane, došlo k chybě v systémech: {e}"

print("--- J.A.R.V.I.S. ONLINE ---")

while True:
    uzivatel = input("Ty: ")
    if uzivatel.lower() in ["konec", "exit", "vypnout"]:
        print("J.A.R.V.I.S.: Dobrou noc, pane.")
        break
        
    odpoved = jarvis_odpoved(uzivatel)
    print(f"J.A.R.V.I.S.: {odpoved}")