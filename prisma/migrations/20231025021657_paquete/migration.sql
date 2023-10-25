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

    CONSTRAINT "Paquete_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Tracking" (
    "id" SERIAL NOT NULL,
    "paquete_id" INTEGER NOT NULL,
    "sucursal_id" INTEGER NOT NULL,
    "estado_tracking_id" INTEGER NOT NULL,
    "salida_id" INTEGER NOT NULL,
    "fecha" TIMESTAMP(3) NOT NULL,
    "comentario" VARCHAR(250) NOT NULL,

    CONSTRAINT "Tracking_pkey" PRIMARY KEY ("id")
);

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
