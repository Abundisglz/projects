"""Pac-Man sencillo para jugar en la terminal."""

from collections import deque
import os

MAPA = [
	"###########",
	"#.........#",
	"#.###.###.#",
	"#.........#",
	"#.##...##.#",
	"#....#....#",
	"###..#..###",
	"#.........#",
	"#.##...##.#",
	"#.........#",
	"###########",
]
DIRECCIONES = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}


def jugar():
	paredes = {(x, y) for y, fila in enumerate(MAPA) for x, c in enumerate(fila) if c == "#"}
	jugador, inicio = (1, 1), (1, 1)
	inicios_fantasmas = [(9, 1), (1, 9), (9, 9)]
	fantasmas = inicios_fantasmas.copy()
	puntos = {(x, y) for y, fila in enumerate(MAPA) for x, c in enumerate(fila) if c != "#"}
	poderes = {(5, 1), (5, 9)}
	vidas, puntuacion, poder = 3, 0, 0

	def dibujar():
		os.system("cls" if os.name == "nt" else "clear")
		tablero = [list(fila) for fila in MAPA]
		for x, y in puntos:
			tablero[y][x] = "."
		for x, y in poderes:
			tablero[y][x] = "o"
		for x, y in fantasmas:
			tablero[y][x] = "👻" if poder else "👻"
		tablero[jugador[1]][jugador[0]] = "▲"
		print("\n".join(" ".join(fila) for fila in tablero))
		print(f"Puntuación: {puntuacion} | Vidas: {vidas} | Poder: {poder}")
		print("W/A/S/D para moverte, Q para salir.")

	def perseguir(posicion):
		cola = deque([(posicion, [])])
		visitadas = {posicion}
		while cola:
			actual, camino = cola.popleft()
			if actual == jugador:
				return camino[0] if camino else posicion
			for dx, dy in DIRECCIONES.values():
				siguiente = actual[0] + dx, actual[1] + dy
				if siguiente not in paredes and siguiente not in visitadas:
					visitadas.add(siguiente)
					cola.append((siguiente, camino + [siguiente]))
		return posicion

	while vidas and puntos:
		dibujar()
		tecla = input("Movimiento: ").strip().lower()[:1]
		if tecla == "q":
			return
		if tecla not in DIRECCIONES:
			print("Introduce W, A, S o D.")
			continue
		dx, dy = DIRECCIONES[tecla]
		destino = jugador[0] + dx, jugador[1] + dy
		if destino not in paredes:
			jugador = destino
		if jugador in puntos:
			puntos.remove(jugador)
			puntuacion += 10
		if jugador in poderes:
			poderes.remove(jugador)
			puntuacion += 50
			poder = 12

		fantasmas = [perseguir(f) for f in fantasmas]
		atrapado = [i for i, f in enumerate(fantasmas) if f == jugador]
		if atrapado and poder:
			puntuacion += 200 * len(atrapado)
			for i in atrapado:
				fantasmas[i] = inicios_fantasmas[i]
		elif atrapado:
			vidas -= 1
			jugador, fantasmas, poder = inicio, inicios_fantasmas.copy(), 0
			if vidas:
				input("¡Te atraparon! Pulsa Enter para continuar.")
		elif poder:
			poder -= 1

	dibujar()
	print(f"{'¡Ganaste!' if vidas else 'Fin del juego.'} Puntuación: {puntuacion}")


if __name__ == "__main__":
	try:
		jugar()
	except (EOFError, KeyboardInterrupt):
		print("\nJuego terminado.")
