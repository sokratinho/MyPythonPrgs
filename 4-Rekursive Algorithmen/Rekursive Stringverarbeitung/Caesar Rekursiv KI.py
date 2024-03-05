#Caesar rekursiv KI-Lösung
def caesar_verschluesseln(wort, verschiebung):
  """
  Verschlüsselt ein Wort rekursiv mit der Caesar-Verschlüsselung.

  Args:
    wort: Das zu verschlüsselnde Wort.
    verschiebung: Die Anzahl der Stellen, um die die Buchstaben verschoben werden sollen.

  Returns:
    Das verschlüsselte Wort.
  """
  if not wort:
    return ""
  else:
    # ASCII-Wert des ersten Buchstabens ermitteln
    ascii_wert = ord(wort[0])

    # Kleinbuchstaben
    if ascii_wert >= 97 and ascii_wert <= 122:
      # Buchstabe um die Verschiebung verschieben
      neuer_ascii_wert = (ascii_wert + verschiebung - 97) % 26 + 97
    # Großbuchstaben
    elif ascii_wert >= 65 and ascii_wert <= 90:
      neuer_ascii_wert = (ascii_wert + verschiebung - 65) % 26 + 65
    # Sonderzeichen unverändert lassen
    else:
      neuer_ascii_wert = ascii_wert

    # Rekursion auf den Rest des Wortes
    return chr(neuer_ascii_wert) + caesar_verschluesseln(wort[1:], verschiebung)

# Beispiel
wort =input( "Geben Sie das Wort ein:")
verschiebung = int(input("Geben Sie die Verschiebung (1-20) ein:")
verschlüsseltes_wort = caesar_verschluesseln(wort, verschiebung)
print(f"Verschlüsseltes Wort: {verschlüsseltes_wort}")