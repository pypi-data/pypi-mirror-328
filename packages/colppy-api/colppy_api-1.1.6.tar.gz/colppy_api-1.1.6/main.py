import asyncio
from colppy.operations.main import ColppyAPIClient
from groovindb import GroovinDB
from db_types import GeneratedClient
from colppy.helpers.formatters import sql_bulk

async def main():
    db: GeneratedClient  = GroovinDB().client
    colppy = ColppyAPIClient()
    await colppy.get_token()
    await db.dev.execute('TRUNCATE TABLE norm_colppy.empresas RESTART IDENTITY;')
    empresas = await colppy.get_empresas()
    # query_empresas = sql_bulk(empresas, 'norm_colppy', 'empresas')
    # print(query_empresas)
    for e in empresas:
        query = e.to_query(schema_db='norm_colppy', table_name='empresas')
        print(query)
        await db.dev.execute(query)
    # await db.dev.execute('TRUNCATE TABLE norm_colppy.empresas RESTART IDENTITY;')
    # await db.dev.execute(query_empresas)

    # clientes = await colppy.get_all_clientes()
    # query_clientes = sql_bulk(clientes, 'norm_colppy', 'clientes')
    # # print(query_clientes)
    # await db.dev.execute('TRUNCATE TABLE norm_colppy.clientes RESTART IDENTITY;')
    # await db.dev.execute(query_clientes)

    # proveedores = await colppy.get_all_proveedores()
    # query_proveedores = sql_bulk(proveedores, 'norm_colppy', 'proveedores')
    # # print(query_proveedores)
    # await db.dev.execute('TRUNCATE TABLE norm_colppy.proveedores RESTART IDENTITY;')
    # await db.dev.execute(query_proveedores)

    # print(empresas)
    # print(clientes)
    # print(proveedores)
    # print(comprobantes_venta)
    # print(comprobantes_compra)
    # print(comprobantes_compra_detail)
    # print(comprobantes_venta_detail)
    # print(cobro_factura)
    # print(movimientos)
    await colppy.logout()

if __name__ == "__main__":
    asyncio.run(main())
