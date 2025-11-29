import time

alarms = []  # Har bir element: {"time": "HH:MM", "message": "Matn"}


def validate_time(time_str: str) -> bool:
    """Vaqt formatini tekshiradi: HH:MM"""
    if len(time_str) != 5 or time_str[2] != ":":
        return False
    h, m = time_str.split(":")
    if not (h.isdigit() and m.isdigit()):
        return False
    h, m = int(h), int(m)
    return 0 <= h <= 23 and 0 <= m <= 59


def add_alarm():
    while True:
        alarm_time = input("⏰ Vaqtni kiriting (HH:MM, masalan 07:30): ").strip()
        if not validate_time(alarm_time):
            print("❌ Noto‘g‘ri format! Qaytadan kiriting.")
            continue
        message = input("Eslatma matnini kiriting (masalan: Darsga bor!): ").strip()
        alarms.append({"time": alarm_time, "message": message})
        print(f"✅ Alarm qo‘shildi: {alarm_time} - {message}")
        break


def show_alarms():
    if not alarms:
        print("🚫 Hozircha birorta ham alarm yo‘q.")
        return
    print("\n📋 Alarmlar ro‘yxati:")
    for i, alarm in enumerate(alarms, start=1):
        print(f"{i}. {alarm['time']}  -  {alarm['message']}")
    print()


def remove_alarm():
    if not alarms:
        print("🚫 O‘chirish uchun alarm yo‘q.")
        return
    show_alarms()
    try:
        idx = int(input("Qaysi alarmni o‘chirmoqchisiz? Raqamini kiriting: "))
        if 1 <= idx <= len(alarms):
            removed = alarms.pop(idx - 1)
            print(f"🗑 O‘chirildi: {removed['time']} - {removed['message']}")
        else:
            print("❌ Noto‘g‘ri raqam.")
    except ValueError:
        print("❌ Raqam kiritishingiz kerak.")


def start_alarm_loop():
    if not alarms:
        print("🚫 Hech qanday alarm yo‘q. Avval qo‘shing.")
        return

    print("\n▶ Alarmlar ishga tushdi.")
    print("   To‘xtatish uchun: Ctrl + C\n")

    triggered = set()  # Bir marta ishlagan alarmlarni eslab qolamiz

    try:
        while True:
            now = time.strftime("%H:%M")
            for i, alarm in enumerate(alarms):
                if alarm["time"] == now and i not in triggered:
                    print("\n⏰⏰⏰ ALARM! ⏰⏰⏰")
                    print(f"Vaqt: {alarm['time']}")
                    print(f"Eslatma: {alarm['message']}")
                    print("\a")  # Terminalda beep ovozi (ba'zi joyda ishlamasligi mumkin)
                    triggered.add(i)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹ Alarmlar to‘xtatildi. Menyuga qaytdik.\n")


def main():
    while True:
        print("========== ALARM / REMINDER APP ==========")
        print("1. Alarm qo‘shish")
        print("2. Alarmlarni ko‘rish")
        print("3. Alarmni o‘chirish")
        print("4. Alarmlarni ishga tushirish")
        print("5. Chiqish")
        choice = input("Tanlovingiz (1-5): ").strip()

        if choice == "1":
            add_alarm()
        elif choice == "2":
            show_alarms()
        elif choice == "3":
            remove_alarm()
        elif choice == "4":
            start_alarm_loop()
        elif choice == "5":
            print("Chiqildi. Xayr! 👋")
            break
        else:
            print("❌ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring.\n")


if __name__ == "__main__":
    main()
