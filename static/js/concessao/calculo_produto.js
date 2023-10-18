const valor_contratado = document.getElementById('id_valor_contratado');
const qtd_parcelas = document.getElementById('id_qtd_parcelas');
const data_primeiro_vencimento = document.getElementById('id_data_primeiro_vencimento');
const taxa_juros = document.getElementById('id_taxa_juros');
const valor_parcela = document.getElementById('id_valor_parcela');
const valor_total_pago = document.getElementById('id_valor_total_pago');
taxa_juros.value = 8;

function calcular(){
    const valor_contratado_value = valor_contratado.value;
    const qtd_parcelas_value = qtd_parcelas.value;
    const data_primeiro_vencimento_value = data_primeiro_vencimento.value;
    const taxa_juros_value = taxa_juros.value;
    if (qtd_parcelas_value > 12 && qtd_parcelas_value <= 36){
        taxa_juros.value = 10;
    }
    else if (qtd_parcelas_value > 36){
        taxa_juros.value = 12;
    }
    if (data_primeiro_vencimento_value == 45){
        taxa_juros.value = parseInt(taxa_juros_value) + 0.5;
    }
    else if (data_primeiro_vencimento_value == 60){
        taxa_juros.value = parseInt(taxa_juros_value) + 1;
    }

    const valor_juros = (valor_contratado_value * taxa_juros_value) / 100;
    const valor_total = parseFloat(valor_contratado_value) + parseFloat(valor_juros);
    const valor_parcela_calculado = valor_total / qtd_parcelas_value;
    valor_parcela.value = valor_parcela_calculado.toFixed(2);
    valor_total_pago.value = valor_total.toFixed(2);
}

calcular();
qtd_parcelas.addEventListener('change', calcular);
valor_contratado.addEventListener('change', calcular);
data_primeiro_vencimento.addEventListener('change', calcular);