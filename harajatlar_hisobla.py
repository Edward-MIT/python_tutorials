import time

xarajatlar = []  # Har bir element: {"summa": float, "kategoriya": str, "izoh": str, "vaqt": str}


def add_expense():
    """Yangi xarajat qo'shish"""
    while True:
        summa_str = input("💰 Xarajat summasini kiriting (masalan: 12000): ").strip()
        try:
            summa = float(summa_str)
            if summa <= 0:
                print("❌ Summani 0 dan katta kiriting.")
                continue
        except ValueError:
            print("❌ Faqat son kiriting.")
            continue

        kategoriya = input("Kategoriya (ovqat, transport, o'yin-kulgi va h.k.): ").strip()
        if not kategoriya:
            kategoriya = "Noma'lum"

        izoh = input("Izoh (ixtiyoriy, bo'sh qoldirsa ham bo'ladi): ").strip()
        vaqt = time.strftime("%Y-%m-%d %H:%M")  # hozirgi vaqt

        xarajatlar.append({
            "summa": summa,
            "kategoriya": kategoriya,
            "izoh": izoh,
            "vaqt": vaqt
        })

        print(f"✅ {summa} so'm {kategoriya} uchun qo'shildi ({vaqt}).\n")
        break


def show_expenses():
    """Barcha xarajatlarni ko'rsatish"""
    if not xarajatlar:
        print("📭 Hozircha birorta ham xarajat kiritilmagan.\n")
        return

    print("\n📋 Xarajatlar ro'yxati:")
    for i, x in enumerate(xarajatlar, start=1):
        print(f"{i}. {x['vaqt']} | {x['summa']} so'm | {x['kategoriya']} | {x['izoh']}")
    print()


def show_summary():
    """Statistika: jami, o'rtacha, eng katta xarajat"""
    if not xarajatlar:
        print("📭 Statistika uchun ma'lumot yo'q. Avval xarajat qo'shing.\n")
        return

    summalar = [x["summa"] for x in xarajatlar]
    jami = sum(summalar)
    ortacha = jami / len(summalar)
    eng_katta = max(summalar)

    # Eng katta xarajatni topamiz (birinchi topilganini olamiz)
    for x in xarajatlar:
        if x["summa"] == eng_katta:
            eng_katta_item = x
            break

    print("\n📊 Statistika:")
    print(f"- Jami xarajat: {jami:.2f} so'm")
    print(f"- O'rtacha xarajat: {ortacha:.2f} so'm")
    print(f"- Eng katta xarajat: {eng_katta:.2f} so'm")
    print(f"  👉 {eng_katta_item['vaqt']} | {eng_katta_item['kategoriya']} | {eng_katta_item['izoh']}\n")


def filter_by_category():
    """Kategoriya bo'yicha filter qilish"""
    if not xarajatlar:
        print("📭 Hozircha ma'lumot yo'q.\n")
        return

    kat = input("Qaysi kategoriyani ko'rmoqchisiz? (masalan: ovqat): ").strip()
    if not kat:
        print("❌ Kategoriya kiritilmadi.\n")
        return

    tanlangan = [x for x in xarajatlar if x["kategoriya"].lower() == kat.lower()]

    if not tanlangan:
        print(f"🔍 '{kat}' kategoriyasida xarajat topilmadi.\n")
        return

    print(f"\n📂 '{kat}' kategoriyasidagi xarajatlar:")
    jami = 0
    for i, x in enumerate(tanlangan, start=1):
        print(f"{i}. {x['vaqt']} | {x['summa']} so'm | {x['izoh']}")
        jami += x["summa"]
    print(f"👉 Jami: {jami:.2f} so'm\n")


def remove_expense():
    """Xarajatni o'chirish"""
    if not xarajatlar:
        print("📭 O'chirish uchun hech qanday xarajat yo'q.\n")
        return

    show_expenses()
    try:
        idx = int(input("Qaysi raqamdagi xarajatni o'chirmoqchisiz? Raqam kiriting: "))
        if 1 <= idx <= len(xarajatlar):
            removed = xarajatlar.pop(idx - 1)
            print(f"🗑 O'chirildi: {removed['summa']} so'm | {removed['kategoriya']} | {removed['izoh']}\n")
        else:
            print("❌ Noto'g'ri raqam.\n")
    except ValueError:
        print("❌ Faqat raqam kiriting.\n")


def main():
    while True:
        print("========== EXPENSE TRACKER ==========")
        print("1. Xarajat qo'shish")
        print("2. Barcha xarajatlarni ko'rish")
        print("3. Statistika (jami, o'rtacha, eng katta)")
        print("4. Kategoriya bo'yicha ko'rish")
        print("5. Xarajatni o'chirish")
        print("6. Chiqish")
        choice = input("Tanlovingiz (1-6): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            remove_expense()
        elif choice == "6":
            print("Chiqildi. Xayr! 👋")
            break
        else:
            print("❌ Noto'g'ri tanlov, qayta urinib ko'ring.\n")


if __name__ == "__main__":
    main()
