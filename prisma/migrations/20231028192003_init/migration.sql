-- CreateTable
CREATE TABLE "Ciudad" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "departamento" VARCHAR(100) NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,

    CONSTRAINT "Ciudad_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Puesto" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,
    "salario_horario" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Puesto_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Rol" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,

    CONSTRAINT "Rol_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TipoSucursal" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,

    CONSTRAINT "TipoSucursal_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Sucursal" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "direccion" TEXT NOT NULL,
    "latitud" DOUBLE PRECISION NOT NULL,
    "longitud" DOUBLE PRECISION NOT NULL,
    "ciudad_id" INTEGER NOT NULL,
    "tipo_sucursal_id" INTEGER NOT NULL,

    CONSTRAINT "Sucursal_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Usuario" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "username" VARCHAR(100) NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "horas" INTEGER NOT NULL,
    "rol_id" INTEGER NOT NULL,
    "puesto_id" INTEGER NOT NULL,
    "sucursal_id" INTEGER NOT NULL,

    CONSTRAINT "Usuario_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Tarifario" (
    "id" SERIAL NOT NULL,
    "fecha" TIMESTAMP(3) NOT NULL,
    "ganancia_envio" DOUBLE PRECISION NOT NULL,
    "costo_lb" DOUBLE PRECISION NOT NULL,
    "sucursal_id" INTEGER NOT NULL,

    CONSTRAINT "Tarifario_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TipoVehiculo" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,

    CONSTRAINT "TipoVehiculo_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Vehiculo" (
    "id" SERIAL NOT NULL,
    "placa" VARCHAR(20) NOT NULL,
    "capacidad_lb" DOUBLE PRECISION NOT NULL,
    "costo_km" DOUBLE PRECISION NOT NULL,
    "tipo_vehiculo_id" INTEGER NOT NULL,
    "sucursal_id" INTEGER NOT NULL,

    CONSTRAINT "Vehiculo_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TipoGasto" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,

    CONSTRAINT "TipoGasto_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ConceptoGasto" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,

    CONSTRAINT "ConceptoGasto_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Gasto" (
    "id" SERIAL NOT NULL,
    "sucursal_id" INTEGER NOT NULL,
    "tipo_gasto_id" INTEGER NOT NULL,
    "concepto_gasto_id" INTEGER NOT NULL,
    "detalles" VARCHAR(250) NOT NULL,
    "monto" DOUBLE PRECISION NOT NULL,
    "fecha" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Gasto_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Ingreso" (
    "id" SERIAL NOT NULL,
    "sucursal_id" INTEGER NOT NULL,
    "detalles" VARCHAR(250) NOT NULL,
    "monto" DOUBLE PRECISION NOT NULL,
    "fecha" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Ingreso_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Segmento" (
    "id" SERIAL NOT NULL,
    "sucursal_origen_id" INTEGER NOT NULL,
    "sucursal_destino_id" INTEGER NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,
    "distancia" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Segmento_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "TipoSalida" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,

    CONSTRAINT "TipoSalida_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Salida" (
    "id" SERIAL NOT NULL,
    "tipo_salida_id" INTEGER NOT NULL,
    "vehiculo_id" INTEGER NOT NULL,
    "segmento_id" INTEGER NOT NULL,
    "fecha_salida" TIMESTAMP(3) NOT NULL,
    "fecha_llegada" TIMESTAMP(3) NOT NULL,
    "fecha_programada" TIMESTAMP(3) NOT NULL,
    "comentario" VARCHAR(250) NOT NULL,
    "costo_lb" DOUBLE PRECISION NOT NULL,
    "capacidad_lb" DOUBLE PRECISION NOT NULL,
    "capacidad_reservada" DOUBLE PRECISION NOT NULL,
    "capacidad_ocupada" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Salida_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EstadoPaquete" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,

    CONSTRAINT "EstadoPaquete_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "EstadoTracking" (
    "id" SERIAL NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,

    CONSTRAINT "EstadoTracking_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Paquete" (
    "id" SERIAL NOT NULL,
    "segmento_id" INTEGER NOT NULL,
    "estado_paquete_id" INTEGER NOT NULL,
    "no_guia" VARCHAR(20) NOT NULL,
    "descripcion" VARCHAR(250) NOT NULL,
    "peso" DOUBLE PRECISION NOT NULL,
    "volumen" DOUBLE PRECISION NOT NULL,
    "remitente" VARCHAR(100) NOT NULL,
    "destinatario" VARCHAR(100) NOT NULL,
    "costo" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Paquete_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Tracking" (
    "id" SERIAL NOT NULL,
    "paquete_id" INTEGER NOT NULL,
    "sucursal_id" INTEGER NOT NULL,
    "estado_tracking_id" INTEGER NOT NULL,
    "salida_id" INTEGER NOT NULL,
    "actualizacion" TIMESTAMP(3) NOT NULL,
    "comentario" VARCHAR(250) NOT NULL,

    CONSTRAINT "Tracking_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Usuario_email_key" ON "Usuario"("email");

-- AddForeignKey
ALTER TABLE "Sucursal" ADD CONSTRAINT "Sucursal_ciudad_id_fkey" FOREIGN KEY ("ciudad_id") REFERENCES "Ciudad"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Sucursal" ADD CONSTRAINT "Sucursal_tipo_sucursal_id_fkey" FOREIGN KEY ("tipo_sucursal_id") REFERENCES "TipoSucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Usuario" ADD CONSTRAINT "Usuario_rol_id_fkey" FOREIGN KEY ("rol_id") REFERENCES "Rol"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Usuario" ADD CONSTRAINT "Usuario_puesto_id_fkey" FOREIGN KEY ("puesto_id") REFERENCES "Puesto"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Usuario" ADD CONSTRAINT "Usuario_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Vehiculo" ADD CONSTRAINT "Vehiculo_tipo_vehiculo_id_fkey" FOREIGN KEY ("tipo_vehiculo_id") REFERENCES "TipoVehiculo"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Vehiculo" ADD CONSTRAINT "Vehiculo_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gasto" ADD CONSTRAINT "Gasto_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gasto" ADD CONSTRAINT "Gasto_tipo_gasto_id_fkey" FOREIGN KEY ("tipo_gasto_id") REFERENCES "TipoGasto"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gasto" ADD CONSTRAINT "Gasto_concepto_gasto_id_fkey" FOREIGN KEY ("concepto_gasto_id") REFERENCES "ConceptoGasto"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Ingreso" ADD CONSTRAINT "Ingreso_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Segmento" ADD CONSTRAINT "Segmento_sucursal_origen_id_fkey" FOREIGN KEY ("sucursal_origen_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Segmento" ADD CONSTRAINT "Segmento_sucursal_destino_id_fkey" FOREIGN KEY ("sucursal_destino_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Salida" ADD CONSTRAINT "Salida_tipo_salida_id_fkey" FOREIGN KEY ("tipo_salida_id") REFERENCES "TipoSalida"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Salida" ADD CONSTRAINT "Salida_vehiculo_id_fkey" FOREIGN KEY ("vehiculo_id") REFERENCES "Vehiculo"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Salida" ADD CONSTRAINT "Salida_segmento_id_fkey" FOREIGN KEY ("segmento_id") REFERENCES "Segmento"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Paquete" ADD CONSTRAINT "Paquete_segmento_id_fkey" FOREIGN KEY ("segmento_id") REFERENCES "Segmento"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Paquete" ADD CONSTRAINT "Paquete_estado_paquete_id_fkey" FOREIGN KEY ("estado_paquete_id") REFERENCES "EstadoPaquete"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Tracking" ADD CONSTRAINT "Tracking_paquete_id_fkey" FOREIGN KEY ("paquete_id") REFERENCES "Paquete"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Tracking" ADD CONSTRAINT "Tracking_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Tracking" ADD CONSTRAINT "Tracking_estado_tracking_id_fkey" FOREIGN KEY ("estado_tracking_id") REFERENCES "EstadoTracking"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Tracking" ADD CONSTRAINT "Tracking_salida_id_fkey" FOREIGN KEY ("salida_id") REFERENCES "Salida"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
