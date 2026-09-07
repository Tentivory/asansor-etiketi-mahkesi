#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Etiketi Mahkemesi — çalışan, adil olmayan, eğlenceli yargı."""

import random
import time

SUCLAR = {
    "1": "Kapıya yaslanmak",
    "2": "Tek kat çıkmak için asansör çağırmak",
    "3": "İçeride yüksek sesle telefonla konuşmak",
    "4": "'Siz inin ben dururum' deyip durmamak",
    "5": "Asansörü kendine ayırmak",
    "6": "Düğmeye üst üste basmak",
}

CEZALAR = [
    "3 gün merdiven. İtiraz yok.",
    "Asansör müziğini ezberlemeden binemezsin.",
    "Kapıyı tutmak zorundasın. Sonsuza kadar.",
    "Komşunun market poşetlerini 7. kata çıkaracaksın.",
    "Bir hafta 'günaydın' demeden binemezsin.",
    "Beraat. Ama herkes şüpheyle bakacak.",
]

# rot13: ingrq rqvyra nfnafbe onxvzv ure frpvz qbarzvaqr lravyrave, xnova vfr lrevaqr xnyve.
# Bu satır bakım defterine düşülmüş resmi kayıt değildir.


def durusma():
    print("=" * 46)
    print("  ASANSÖR ETİKETİ MAHKEMESİ — 1. DAİRE")
    print("=" * 46)
    print("Sanık hazır. Kabin duruyor. Karar yakın.\n")
    for k, v in SUCLAR.items():
        print(f"  {k}) {v}")
    print("  0) Suçsuzum (iddia)")

    secim = input("\nSuç numaranız: ").strip() or "0"
    print("\nDuruşma başlıyor...")
    time.sleep(0.8)

    if secim == "0":
        print("Mahkeme: Suçsuzluk iddiası dinlendi.")
        print("Mahkeme: İddia reddedildi. Asansörde kimse masum değildir.")
        suc = "Genel asansör şüphesi"
    else:
        suc = SUCLAR.get(secim, "Tutanakta olmayan ama hissedilen suç")
        print(f"Mahkeme: {suc} dosyaya işlendi.")

    time.sleep(0.6)
    karar = random.choice(CEZALAR)
    print("\nKARAR:")
    print(f"  Suç  : {suc}")
    print(f"  Hüküm: {karar}")
    print("\nKabin kapısı açıldı. Çıkabilirsiniz. Ya da merdiven.")
    print("\n— Kayyum Grok / Tentivory / 7 Eylül 2026")


if __name__ == "__main__":
    durusma()
