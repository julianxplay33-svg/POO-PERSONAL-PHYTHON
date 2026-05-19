class Persona(nombre: String) {

  def saludar(): Unit = {
    println("Hola, soy " + nombre)
  }
}

object Main {
  def main(args: Array[String]): Unit = {

    val p = new Persona("Julian")
    p.saludar()
  }
}
