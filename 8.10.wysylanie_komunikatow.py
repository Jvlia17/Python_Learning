# 8.10 Wysyłanie komunikatów. Pracę rozpocznij od kopii programu z ćwiczenia 8.9. Następnie utwórz funkcję o nazwie send_messages(), której zadaniem będzie wyświetlanie wszystkich komunikatów.

sent_messages = []

def send_messages(messages):
    """Wyświetla komunikaty i przenosi na nową listę."""
    while messages:
        sending_message = messages.pop()
        sent_messages.append(sending_message)

messages = ['pij dużo wody', 'chroń skórę przed słońcem', 'uważaj na dzikie zwierzęta']
send_messages(messages)

print(messages)
print(sent_messages)