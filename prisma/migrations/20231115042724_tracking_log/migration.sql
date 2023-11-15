-- CreateTable
CREATE TABLE "TrackingLog" (
    "id" SERIAL NOT NULL,
    "paquete_id" INTEGER NOT NULL,
    "sucursal_id" INTEGER NOT NULL,
    "estado_tracking_id" INTEGER NOT NULL,
    "salida_id" INTEGER NOT NULL,
    "actualizacion" TIMESTAMP(3),
    "comentario" VARCHAR(250) NOT NULL,

    CONSTRAINT "TrackingLog_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "TrackingLog" ADD CONSTRAINT "TrackingLog_paquete_id_fkey" FOREIGN KEY ("paquete_id") REFERENCES "Paquete"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TrackingLog" ADD CONSTRAINT "TrackingLog_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TrackingLog" ADD CONSTRAINT "TrackingLog_estado_tracking_id_fkey" FOREIGN KEY ("estado_tracking_id") REFERENCES "EstadoTracking"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "TrackingLog" ADD CONSTRAINT "TrackingLog_salida_id_fkey" FOREIGN KEY ("salida_id") REFERENCES "Salida"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
