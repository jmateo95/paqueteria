-- CreateTable
CREATE TABLE "Tarifario" (
    "id" SERIAL NOT NULL,
    "fecha" TIMESTAMP(3) NOT NULL,
    "ganancia_lb" DOUBLE PRECISION NOT NULL,
    "costo_lb_km" DOUBLE PRECISION NOT NULL,
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
    "costokm" DOUBLE PRECISION NOT NULL,
    "tipovehiculo_id" INTEGER NOT NULL,
    "sucursal_id" INTEGER NOT NULL,

    CONSTRAINT "Vehiculo_pkey" PRIMARY KEY ("id")
);

-- AddForeignKey
ALTER TABLE "Tarifario" ADD CONSTRAINT "Tarifario_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Vehiculo" ADD CONSTRAINT "Vehiculo_tipovehiculo_id_fkey" FOREIGN KEY ("tipovehiculo_id") REFERENCES "TipoVehiculo"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Vehiculo" ADD CONSTRAINT "Vehiculo_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
