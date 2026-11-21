from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.tyhjenna()

    def tavaroita_korissa(self):
        return self._tavaroita

    def hinta(self):
        return self._hinta

    def lisaa_tuote(self, lisattava: Tuote):
        self._tavaroita += 1
        self._hinta += lisattava.hinta()
        ostos = self._etsi_ostos(lisattava)
        if ostos is None:
            self._ostokset.append(Ostos(lisattava))
        else:
            ostos.muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        self._tavaroita -= 1
        self._hinta -= poistettava.hinta()
        ostos = self._etsi_ostos(poistettava)
        if ostos is None:
            return
        ostos.muuta_lukumaaraa(-1)
        if ostos.lukumaara() == 0:
            self._ostokset.remove(ostos)

    def tyhjenna(self):
        self._tavaroita = 0
        self._hinta = 0
        self._ostokset = []

    def ostokset(self):
        return self._ostokset

    def _etsi_ostos(self, tuote: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == tuote.nimi():
                return ostos
        return None
