-- AlterTable
ALTER TABLE "Ciudad" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "ConceptoGasto" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "EstadoPaquete" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "EstadoTracking" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "Puesto" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "Rol" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "Sucursal" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "TipoGasto" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "TipoSalida" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "TipoSucursal" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "TipoVehiculo" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;

-- AlterTable
ALTER TABLE "Usuario" ADD COLUMN     "estatico" BOOLEAN NOT NULL DEFAULT false;
