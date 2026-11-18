class SesionAula:
    centro = "CFGS Python"
    total_sesiones = 0

    def __init__(
    self,
    aula: str,
    profesor: str,
    alumnos: int = 0,
    log_path: str = "registro.txt",
    log: RegistroTemporal | None = None,
    cerrada: bool = False,

    
) -> None:

        if not isinstance(aula, str) or not aula.strip():
                raise ValueError("El aula no puede estar vacía")
        if not isinstance(profesor, str) or not profesor.strip():
                raise ValueError("El profesor no puede estar vacío")
        if not isinstance(alumnos, int) or isinstance(alumnos, bool) or alumnos < 0:
                raise ValueError("El número de alumnos no puede ser negativo")
        if not isinstance(log_path, str) or not log_path.strip():
                raise ValueError("No puede estar vacía")
        
        self.aula = aula.strip().upper(),
        self.profesor = profesor.strip().title(),
        self.alumnos = alumnos,
        self.log_path = log_path.strip(),
        self._log = log
        self._cerrada = cerrada

        SesionAula.total_sesiones += 1

def __enter__(self):
       self.log_path 
