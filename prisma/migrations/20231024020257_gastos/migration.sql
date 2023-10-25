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

-- AddForeignKey
ALTER TABLE "Gasto" ADD CONSTRAINT "Gasto_sucursal_id_fkey" FOREIGN KEY ("sucursal_id") REFERENCES "Sucursal"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gasto" ADD CONSTRAINT "Gasto_tipo_gasto_id_fkey" FOREIGN KEY ("tipo_gasto_id") REFERENCES "TipoGasto"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Gasto" ADD CONSTRAINT "Gasto_concepto_gasto_id_fkey" FOREIGN KEY ("concepto_gasto_id") REFERENCES "ConceptoGasto"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
