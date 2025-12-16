class Mascota:
    """Representa a un animal que asiste a la clínica."""
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.historial_medico = []

    def agregar_nota_medica(self, nota):
        self.historial_medico.append(nota)
        print(f"Nota añadida al historial de {self.nombre}.")

    def __str__(self):
        return f"{self.nombre} ({self.especie}), {self.edad} años."


class Veterinario:
    """Representa al profesional encargado de las consultas."""
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def realizar_consulta(self, mascota, diagnostico):
        """Demuestra la interacción entre el objeto Veterinario y Mascota."""
        print(f"El Dr. {self.nombre} está revisando a {mascota.nombre}...")
        nota = f"Consulta con Dr. {self.nombre}: {diagnostico}"
        mascota.agregar_nota_medica(nota)


# --- Bloque Principal (Simulación del Mundo Real) ---
if __name__ == "__main__":
    # 1. Instanciamos objetos
    mi_gato = Mascota("Azul", "Gato", 1)
    doctor_cristian = Veterinario("Cristian Perez", "Cirugía")

    # 2. Mostramos estado inicial
    print(f"Registro: {mi_gato}")

    # 3. Interacción: El veterinario atiende a la mascota
    doctor_cristian.realizar_consulta(mi_gato, "Vacunación anual completa.")

    # 4. Verificamos que los datos se guardaron en el objeto mascota
    print("\nHistorial de la mascota:")
    for entrada in mi_gato.historial_medico:
        print(f"- {entrada}")