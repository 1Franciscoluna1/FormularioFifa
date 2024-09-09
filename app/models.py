from sqlalchemy import Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Estado(Base):
    __tablename__ = 'estados'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Estado(id={self.id!r}, nombre={self.nombre!r})"

class Disciplina(Base):
    __tablename__ = 'disciplinas'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Disciplina(id={self.id!r}, descripcion={self.nombre!r})"

class Encuesta(Base):
    __tablename__ = 'encuestas'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Encuesta(id={self.id!r}, descripcion={self.descripcion!r})"

class Sexo(Base):
    __tablename__ = 'sexos'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    descripcion: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Sexo(id={self.id!r}, descripcion={self.descripcion!r})"

class Participante(Base):
    __tablename__ = "participantes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    firstname: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)
    sexo_id: Mapped[int] = mapped_column(Integer, nullable=False)
    estado_id: Mapped[int] = mapped_column(Integer, nullable=False)
    disciplina_id: Mapped[int] = mapped_column(Integer, nullable=False)
    encuesta_id: Mapped[int] = mapped_column(Integer, nullable=False)
    datestart: Mapped[str] = mapped_column(String, nullable=False)

    respuestas = relationship("Respuesta", back_populates="participante")

    def __repr__(self) -> str:
        return f"Participante(id={self.id!r}, firstname={self.firstname!r}, lastname={self.lastname!r}, sexo_id={self.sexo_id!r}, estado_id={self.estado_id!r}, disciplina_id={self.disciplina_id!r}, encuesta_id={self.encuesta_id!r}, datestart={self.datestart!r})"

class Pregunta(Base):
    __tablename__ = "preguntas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    texto: Mapped[str] = mapped_column(String, nullable=False)
    clase: Mapped[int] = mapped_column(Integer, nullable=False)

    opciones = relationship("Opcion", back_populates="pregunta", cascade="all, delete-orphan")
    respuestas = relationship("Respuesta", back_populates="pregunta")

    def __repr__(self) -> str:
        return f"Pregunta(id={self.id!r}, texto={self.texto!r}, clase={self.clase!r})"

class Opcion(Base):
    __tablename__ = "opciones"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pregunta_id: Mapped[int] = mapped_column(Integer, ForeignKey('preguntas.id'), nullable=True)
    peso: Mapped[int] = mapped_column(Integer, nullable=False)
    texto: Mapped[str] = mapped_column(String, nullable=False)

    pregunta = relationship("Pregunta", back_populates="opciones")

    def __repr__(self) -> str:
        return f"Opcion(id={self.id!r}, pregunta_id={self.pregunta_id!r}, peso={self.peso!r}, texto={self.texto!r})"
    
class Respuesta(Base):
    __tablename__ = "respuestas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    participante_id: Mapped[int] = mapped_column(Integer, ForeignKey('participantes.id'), nullable=False)
    pregunta_id: Mapped[int] = mapped_column(Integer, ForeignKey('preguntas.id'), nullable=False)
    opcion_id: Mapped[int] = mapped_column(Integer, ForeignKey('opciones.id'), nullable=False)

    participante = relationship("Participante", back_populates="respuestas")
    pregunta = relationship("Pregunta", back_populates="respuestas")
    opcion = relationship("Opcion")

    def __repr__(self) -> str:
        return f"Respuesta(id={self.id!r}, participante_id={self.participante_id!r}, pregunta_id={self.pregunta_id!r}, opcion_id={self.opcion_id!r})"