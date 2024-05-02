Usar os related_names dos models:
    1. propriedades criadas por um determinado mediador:
    # Supondo que você tenha um objeto Mediador chamado 'mediador'
    propriedades_do_mediador = mediador.propriedade_criadas.all()

    2.  propostas feitas por um determinado cliente:
    # Supondo que você tenha um objeto Cliente chamado 'cliente'
    propostas_do_cliente = cliente.propostas_feitas.all()

    3. visitas feitas por um determinado cliente:
    # Supondo que você tenha um objeto Cliente chamado 'cliente'
    visitas_do_cliente = cliente.visitas_efetuadas.all()



Estava a ver a escolha de estados (e pag.520)



Funcionalidades:
 - Se o Mediador não for adicionado aquando da criação da propriedade, é automáticamente atribuido o user atual autenticado
 - ID da Propriedade/Cliente autogerados mas podem ser modificados

 