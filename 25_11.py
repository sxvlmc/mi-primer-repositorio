class piedrapapeltijera:
    def __init__(self, juego, jugador1, jugador2) -> None:
        self.juego = juego
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.ganador = None
        self.perdedor = None
        self.empate = False
    def jugar(self, jugada_jug1, jugada_jug2):
        if jugada_jug1 == 'piedra' and jugada_jug2 == 'piedra':
            self.empate = True

        if jugada_jug1 == 'papel' and jugada_jug2 == 'papel':
            self.empate = True

        if jugada_jug1 == 'tijeras' and jugada_jug2 == ' tijeras':
            self.empate = True

        if jugada_jug1 == 'piedra' and jugada_jug2 == 'papel':
            self.ganador = self.jugador2
            self.perdedor = self.jugador1

        if jugada_jug1 == 'papel' and jugada_jug2 == 'piedra':
            self.ganador = self.jugador1
            self.perdedor = self.jugador2

        if jugada_jug1 == 'tijeras' and jugada_jug2 == 'papel':
            self.ganador = self.jugador1
            self.perdedor = self.jugador2

        if jugada_jug1 == 'papel' and jugada_jug2 == 'tijeras':
            self.ganador = self.jugador2
            self.perdedor = self.jugador1

        if jugada_jug1 == 'tijeras' and jugada_jug2 == 'piedra':
            self.ganador = self.jugador2
            self.perdedor = self.jugador1

        if jugada_jug1 == 'piedra' and jugada_jug2 == 'tijeras':
            self.ganador = self.jugador1
            self.perdedor = self.jugador2
    def resultado(self):
        print(f'el ganador es {self.ganador}')
        print(f'el perdedor es {self.perdedor}')
        print(f'es un {self.empate} empate')
    def reiniciar(self):
        self.ganador = None
        self.perdedor = None
        self.empate = False

ppt = piedrapapeltijera('piedra-papel-tijera', 'Baruc', 'Saul')
ppt.jugar('piedra', 'papel')
ppt.resultado()



