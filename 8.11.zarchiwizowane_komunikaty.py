# 8.11 Zarchiwizowane komunikaty. Pracę rozpocznij od kodu utworzonego w ćwiczeniu 8.10. Wywołaj funkcję send_messages() wraz z kopią listy komunikatów.

sent_messages = []

def send_messages(messages):
    """Wyświetla komunikaty i przenosi na nową listę."""
    while messages:
        sending_message = messages.pop()
        sent_messages.append(sending_message)

messages = ['pij dużo wody', 'chroń skórę przed słońcem', 'uważaj na dzikie zwierzęta']
send_messages(messages[:])

print(messages)
print(sent_messages)