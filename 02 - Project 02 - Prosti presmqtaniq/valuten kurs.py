pari = float(input())
valuta_in = input()
valuta_out = input()

if valuta_in == valuta_out:
    print(pari)

if valuta_in =="BGN" and valuta_out =="EUR":
    bgn_euro = pari / 1.95583
    print("%.2f" % bgn_euro + " " +  valuta_out)
if valuta_in =="BGN" and valuta_out =="GBP":
    bgn_gbp = pari / 2.53405
    print("%.2f" % bgn_gbp + " " +  valuta_out)
if valuta_in == "BGN" and valuta_out == "USD":
    bgn_usd = pari / 1.79549
    print("%.2f" % bgn_usd + " " +  valuta_out)

if valuta_in =="EUR" and valuta_out =="BGN":
    euro_bgn = pari*1.95583
    print("%.2f" % euro_bgn + " " +  valuta_out)
if valuta_in =="EUR" and valuta_out =="GBP":
    euro_gbp = pari*1.95583/2.53405
    print("%.2f" % euro_gbp + " " +  valuta_out)
if valuta_in == "EUR" and valuta_out == "USD":
    euro_usd = pari*1.95583/1.79549
    print("%.2f" % euro_usd + " " +  valuta_out)

if valuta_in =="USD" and valuta_out =="BGN":
    usd_bgn = pari*1.79549
    print("%.2f" % usd_bgn + " " +  valuta_out)
if valuta_in =="USD" and valuta_out =="GBP":
    usd_gbp = pari*1.79549/2.53405
    print("%.2f" % usd_gbp + " " +  valuta_out)
if valuta_in == "USD" and valuta_out == "EUR":
    usd_euro = pari*1.79549/1.95583
    print("%.2f" % usd_euro + " " +  valuta_out)

if valuta_in =="GBP" and valuta_out =="BGN":
    gbp_bgn = pari*2.53405
    print("%.2f" % gbp_bgn +  " " + valuta_out)
if valuta_in =="GBP" and valuta_out == "EURO":
    gbp_euro = pari*2.53405/1.95583
    print("%.2f" % gbp_euro + " " +  valuta_out)
if valuta_in == "GBP" and valuta_out == "USD":
    gbp_usd = pari*2.53405/1.79549
    print("%.2f" % gbp_usd + " " + valuta_out)