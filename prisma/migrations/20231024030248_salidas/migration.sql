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
    "comentario" VARCHAR(250) NOT NULL,
    "fecha_programada" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Salida_pkey" PRIMARY KEY ("id")
);

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
