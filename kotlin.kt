class Persona(private val nombre: String) {

    fun saludar() {
        println("Hola, soy $nombre")
    }
}

fun main() {

    val p = Persona("Julian")
    p.saludar()
}
