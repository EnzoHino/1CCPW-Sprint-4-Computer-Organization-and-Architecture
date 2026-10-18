import machine
import time

# 1. Configuração dos LEDs
led_verde = machine.Pin(2, machine.Pin.OUT)
led_amarelo = machine.Pin(3, machine.Pin.OUT)
led_vermelho = machine.Pin(4, machine.Pin.OUT)

# 2. Dados dos Veículos
ev1_req = 2000
ev2_req = 2500
ev3_req = 3000
demanda_total = ev1_req + ev2_req + ev3_req
   

def gerenciar_energia(energia_disponivel):
    led_verde.value(0)
    led_amarelo.value(0)
    led_vermelho.value(0)

    print("\n" + "=" * 50)
    print(f"NOVO CICLO - ENERGIA NA REDE: {energia_disponivel} W")

    print(f"Valor Decimal:     {energia_disponivel} W")
    print(f"Valor Hexadecimal: {hex(energia_disponivel)}")
    print(f"Valor Binário:     {bin(energia_disponivel)}")

    print(f"\nDEMANDA TOTAL DOS 3 EVs:      {demanda_total} W")
    print("=" * 50)    
    
    # --- LÓGICA DE GERENCIAMENTO (O CÉREBRO DO SISTEMA) ---
    
    if energia_disponivel >= demanda_total: # Alta Disponibilidade
        print("STATUS: RECARGA ATIVA (Sobra de Energia)")
        led_verde.value(1)
        
        print(f"Fornecimento -> EV1: {ev1_req}W | EV2: {ev2_req}W | EV3: {ev3_req}W")
        print("Decisão: A rede suporta a demanda. 100% de potência para todos.")
        
    elif energia_disponivel >= 3000: # Disponibilidade Limitada
        print("STATUS: RECARGA CONTROLADA (Redução de Potência)")
        led_amarelo.value(1)
        
        # A energia disponível é rateada proporcionalmente ao solicitado por cada um dos veiculos
        fator_corte = energia_disponivel / demanda_total
        ev1_novo = int(ev1_req * fator_corte)
        ev2_novo = int(ev2_req * fator_corte)
        ev3_novo = int(ev3_req * fator_corte)
        
        print(f"Fornecimento -> EV1: {ev1_novo}W | EV2: {ev2_novo}W | EV3: {ev3_novo}W")
        print(f"Decisão: Demanda excedeu a rede. Redução proporcional de {int((1-fator_corte)*100)}% aplicada.")
        
    else: # Baixa disponiblidade
        print("STATUS: RECARGA LIMITADA (Veículos em Espera)")
        led_vermelho.value(1)
        
        print(f"Fornecimento -> EV1: {energia_disponivel}W | EV2: 0W (Bloqueado) | EV3: 0W (Bloqueado)")
        print("Decisão: Risco de queda geral. Sistema bloqueou EV2 e EV3 e direcionou o restante para o EV1.")

# 3. Loop Principal de Execução
while True:
    # Simula a Situação 1
    gerenciar_energia(8000)
    time.sleep(8)
    
    # Simula a Situação 2
    gerenciar_energia(5000)
    time.sleep(8)
    
    # Simula a Situação 3
    gerenciar_energia(2000)
    time.sleep(8)
