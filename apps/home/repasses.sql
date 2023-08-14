SELECT
	pev.id as COD,
    cp.contratos_id as id_contrato,
    case when not isnull(pev.nome) then pev.nome else 'boleto avulso' end as vendedor,
    case when not isnull(pec.nome) then pec.nome else peb.nome end as comprador,
    cp.nu_parcela as nu_parcela,
    cp.vl_parcela as vl_parcela,
    cp.vl_pagto,
    cp.dt_vencimento as dt_vencimento,
    cp.dt_credito as dt_credito,
    cp.dt_processo_pagto as dt_processamento,
    case when cp.contratos_id > 12460 or isnull(cp.contratos_id) then 'UNICRED' else 'BRADESCO' end as banco,
    co.parcela_primeiro_pagto as parcela_primeiro_pagto,
    co.nu_parcelas as tt_parcelas,
    (select count(*) from contrato_parcelas cpx where cpx.contratos_id = cp.contratos_id and (not isnull(dt_pagto) and not dt_pagto = '0000-00-00') ) as tt_quitadas,
    ev.nome as evento,
    co.descricao as produto
FROM contrato_parcelas cp
LEFT JOIN contratos co on co.id = cp.contratos_id
LEFT JOIN boletos_avulso bo on bo.id = cp.boletos_avulso_id
LEFT JOIN pessoas pec on pec.id = co.comprador_id
LEFT JOIN pessoas pev on pev.id = co.vendedor_id
LEFT JOIN pessoas peb on peb.id = bo.pessoas_id
LEFT JOIN eventos ev on ev.id = co.eventos_id
where date(cp.dt_credito) = '2022-02-01'
order by banco desc, cp.contratos_id asc