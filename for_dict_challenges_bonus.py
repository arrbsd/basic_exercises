"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]

    {
    'id': UUID('6a902ea1-a080-4f45-b722-a61c8a0e600d'),
    'sent_at': datetime.datetime(2024, 8, 26, 2, 48, 34, 696813),
    'sent_by': 7971,
    'reply_for': None,
    'seen_by': [4409, 2681, 4437],
    'text': 'Sit quaerat dolor dolorem tempora dolor sit magnam.'},
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime
from collections import Counter
from collections import defaultdict
import lorem
from pyexpat.errors import messages


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages

history = generate_chat_history()


# 1. Вывести айди пользователя, который написал больше всех сообщений.
# создаем словарь со всеми ID пользователей. которые отправили сообщения
def total_count(key_dict):
    list_keys = []
    for one_key in key_dict:
        list_keys.append(one_key['sent_by'])
    return list_keys


sender_counts = (Counter(total_count(history)))
max_sender = max(sender_counts, key=sender_counts.get)
max_count = sender_counts[max_sender]
#print(sender_counts)
print(f'Самое большое количество сообщений - {max_count}, написал пользователь с ID: {max_sender}')

# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
reply_for_counts = Counter(message['reply_for'] for message in history)
del reply_for_counts[None]
max_reply_for = max(reply_for_counts, key=reply_for_counts.get)
max_reply_count = reply_for_counts[max_reply_for]
#print(reply_for_counts)
for message in history:
    if message['id'] == max_reply_for:
        print(f'ID пользователя на сообщение которого, больше всего ответов - {message["sent_by"]}')

# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.

# 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов)
message_count = defaultdict(int)
for message in history:
    timestamp = message["sent_at"]
    hour = timestamp.hour

    if 0 <= hour < 12:
        message_count["Утром"] += 1
    elif 12 <= hour < 18:
        message_count["Днем"] += 1
    else:
        message_count["Вечером"] += 1

most_messages = max(message_count, key=message_count.get)
#print(message_count)
print(f'Больше всего сообщений было - {most_messages}')


# 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).
# Словарь для ответов на каждое сообщение
replies = {}

# Словарь длины цепочки для каждого сообщения
thread_len = {}

for message in history:
    message_id = message["id"]
    reply_to = message["reply_for"]

    if reply_to:
        if reply_to not in replies:
            replies[reply_to] = []
        replies[reply_to].append(message_id)

    thread_len[message_id] = 0

# Длина цепочки для сообщения
def count_thread_len(message_id):
    if message_id in replies:
        for reply_id in replies[message_id]:
            thread_len[message_id] = max(thread_len[message_id], count_thread_len(reply_id))
    return thread_len[message_id] + 1


# Вычислите длину цепочки для каждого сообщения
for message_id in thread_len:
    count_thread_len(message_id)

max_thread_len = max(thread_len.values())
long_threads = [message_id for message_id, length in thread_len.items() if length == max_thread_len]
#print(thread_len)
print(f"ID сообщений, которые стали началом самых больших тредов", long_threads)

# for sender_id in history:
#     print(sender_id['sent_by'])

#if __name__ == "__main__":
#    print(generate_chat_history())


