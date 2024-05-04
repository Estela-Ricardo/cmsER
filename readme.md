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



Estava a ver a escolha de estados (e pag.549)
Faz login e faz logout. O redirect para o profile ainda não funciona. 
5 de Maio:
    - preciso eliminar tudo o que tenha a ver com logins/logouts
    - preciso eliminar content
    - preciso corrigir e limpar css
    - Verificar viabilidade do signals.py pois imagens continuam na pasta



Funcionalidades:
 - Se o Mediador não for adicionado aquando da criação da propriedade, é automaticamente atribuido o user atual autenticado
 - ID da Propriedade/Cliente autogerados mas podem ser modificados

 