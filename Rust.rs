struct Persona {
    nombre: String,
}

impl Persona {

    fn saludar(&self) {
        println!("Hola, soy {}", self.nombre);
    }
}

fn main() {

    let p = Persona {
        nombre: String::from("Julian"),
    };

    p.saludar();
}
