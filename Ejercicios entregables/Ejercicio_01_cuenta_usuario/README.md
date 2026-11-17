# Práctica Integradora RA1 (Criterios a, b y c): Cuenta de Usuario

Este proyecto modela el funcionamiento básico de una cuenta de usuario para una plataforma de formación utilizando **Programación Orientada a Objetos (POO)** en Python.

---

## 1. Explicación del modelo

La clase `CuentaUsuario` encapsula el estado y el comportamiento de un usuario dentro de la plataforma:

* **Atributos de clase:**
  * `MAX_INTENTOS = 3`: Límite máximo de intentos fallidos de inicio de sesión permitidos antes de bloquear la cuenta.
  * `dominio = "formacion.local"`: Dominio corporativo al que deben pertenecer los correos electrónicos válidos.
* **Atributos de instancia:**
  * `nombre` (público): Nombre visible del usuario.
  * `_email` (protegido): Dirección de correo electrónico institucional.
  * `__password_hash` (privado): Representación simulada de la contraseña cifrada.
  * `_activa` (protegido): Estado booleano que indica si la cuenta está habilitada (`True`) o bloqueada (`False`).
  * `_intentos_fallidos` (protegido): Contador entero de fallos consecutivos de autenticación.

---

## 2. Ejemplos de ejecución

Para ejecutar las pruebas demostrativas incluidas en el bloque `main()`, lanza el script desde la terminal:

```bash
python cuenta_usuario.py
```

### Salida esperada en consola:

```text
Estado inicial cuenta_uno: {'nombre': 'Rebeca', '_email': 'rebeca@formacion.local', '_CuentaUsuario__password_hash': '1234', '_activa': True, '_intentos_fallidos': 2}
Estado inicial cuenta_dos: {'nombre': 'Miguel', '_email': 'miguel@formacion.local', '_CuentaUsuario__password_hash': '4321', '_activa': True, '_intentos_fallidos': 0}
¿Son el mismo objeto?: False
ID de cuenta_uno: 2145893214592
ID de cuenta_dos: 2145893214784
Perfil público: Usuario: Rebeca | Dominio: formacion.local
Nuevo email cuenta_uno: rebeca.nueva@formacion.local
¿Cuenta uno activa tras 3er fallo?: False
¿Puede iniciar sesión cuenta_uno?: False
¿Cuenta dos sigue activa?: True
Estado cuenta_dos intacto: {'nombre': 'Miguel', '_email': 'miguel@formacion.local', '_CuentaUsuario__password_hash': '4321', '_activa': True, '_intentos_fallidos': 0}
Error controlado al cambiar email: El email debe terminar en @formacion.local.
Dominio de la plataforma: formacion.local
Hash privado (name mangling): 1234
```

---

## 3. Diferencia entre atributos de instancia y de clase

* **Atributos de clase:** Se definen directamente en el cuerpo de la clase (fuera de `__init__`) y **pertenecen a la clase**, siendo compartidos por todas las instancias. Se utilizan para constantes o configuraciones globales del modelo (como `MAX_INTENTOS` y `dominio`).
* **Atributos de instancia:** Se definen dentro del constructor `__init__` ligados a `self` y **pertenecen a cada objeto concreto**. Cada cuenta almacena sus propios valores independientes (`nombre`, `_email`, etc.), de modo que modificar el estado de `cuenta_uno` no altera en absoluto el estado de `cuenta_dos`.

---

## 4. Diferencia entre método consultor y modificador

La separación entre consultas y comandos mantiene la integridad de los datos internos del objeto:

* **Métodos consultores (*getters*):** Devuelven información sobre el estado actual del objeto **sin producir efectos secundarios** ni alterar sus atributos. En esta clase son: `esta_activa()`, `puede_iniciar_sesion()`, `perfil_publico()` y `consultar_email()`.
* **Métodos modificadores (*setters / commands*):** Alteran el estado interno del objeto y son los responsables de **validar las reglas de negocio** antes de aplicar cambios. En esta clase son: `activar()`, `desactivar()`, `cambiar_email()`, `registrar_intento_fallido()` y `reiniciar_intentos()`.

---

## 5. Reflexión sobre la visibilidad por convención en Python

A diferencia de otros lenguajes como Java o C++, Python **no impone restricciones estrictas de acceso** a nivel de compilador o intérprete; la encapsulación se basa en convenciones de nomenclatura y disciplina de diseño:

1. **Público (`nombre`):** Forma parte de la interfaz pública de la clase y puede leerse o modificarse libremente desde el exterior.
2. **Protegido (`_atributo`):** Un guion bajo inicial advierte a otros programadores de que es un dato de uso interno y no debe manipularse directamente fuera de la clase (deben usarse los métodos consultores y modificadores). Sin embargo, Python no bloquea su acceso.
3. **Privado (`__atributo`):** El doble guion bajo activa el mecanismo conocido como ***name mangling***, mediante el cual Python renombra internamente el atributo a `_NombreClase__atributo` (por ejemplo, `_CuentaUsuario__password_hash`). Su objetivo real es evitar colisiones de nombres en futuras subclases (herencia), pero **no proporciona seguridad criptográfica ni ocultación real**, ya que cualquier código externo puede leer o modificar el valor conociendo su nombre interno.