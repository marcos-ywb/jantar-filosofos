import threading
import datetime
import time
import random
import statistics
import matplotlib.pyplot as plt
import os

#===========================================================================================================#
#===[    CONFIGURAÇÕES    ]=================================================================================#
#===========================================================================================================#
NUM_FILOSOFOS = 5               # numero de filosofos
TEMPO_SIMULACAO = 15.0          # segundos que a simulação vai rodar
TAXA_PENSAR = 1.0               # taxa exponencial pra tempo de pensar
TAXA_COMER = 1.5                # taxa exponencial pra tempo de comer
INTERVALO_SALVAR = 0.5          # intervalo pra salvar frames (segundos)
ARQUIVO_LOG = "log.txt"         # arquivo de logs
PASTA_FRAMES = "frames"         # pasta salvamento das imagens

os.makedirs(PASTA_FRAMES, exist_ok=True)

subpasta = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
PASTA_FRAMES = os.path.join(PASTA_FRAMES, subpasta)
os.makedirs(PASTA_FRAMES, exist_ok=True)

#===========================================================================================================#
#===[    LOGS  ]============================================================================================#
#===========================================================================================================#
def get_datetime():
    data_hora = datetime.datetime.now()
    return data_hora.strftime("%d/%m/%Y - %H:%M")

def log_datetime(arquivo=ARQUIVO_LOG):
    linha = "#" + "="*84 + "#\n"
    titulo = f"#============================[    {get_datetime()}    ]============================#\n"
    with open(arquivo, 'a') as a:
        a.write(f"{linha}{titulo}{linha}\n")

def log(frame, stats, medias, arquivo=ARQUIVO_LOG):
    with open(arquivo, 'a') as a:
        a.write(f"Frame {frame:03d} salvo:\n")
        for i in range(NUM_FILOSOFOS):
            a.write(f"  Filósofo {i}: refeições={stats['refeicoes'][i]}, tempo médio de espera={medias[i]}s\n")
        a.write("\n#" + "="*84 + "#\n\n")

#===========================================================================================================#
#===[    FILÓSOFOS    ]=====================================================================================#
#===========================================================================================================#
def filosofar(id_filo, garfo_esq, garfo_dir, stats, parar):
    while not parar.is_set():
        time.sleep(random.expovariate(TAXA_PENSAR))

        hora_desejo = time.time()
        garfo_esq.acquire()
        pegou_dir = garfo_dir.acquire(timeout=1.0)
        if not pegou_dir:
            garfo_esq.release()
            continue

        hora_comeco = time.time()
        stats['tempos_espera'][id_filo].append(hora_comeco - hora_desejo)
        stats['refeicoes'][id_filo] += 1
        time.sleep(random.expovariate(TAXA_COMER))

        garfo_dir.release()
        garfo_esq.release()

#===========================================================================================================#
#===[    SIMULAÇÃO    ]=====================================================================================#
#===========================================================================================================#
def simular_e_salvar_frames():
    garfos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]
    parar = threading.Event()

    stats = {
        'tempos_espera': [[] for _ in range(NUM_FILOSOFOS)],
        'refeicoes': [0] * NUM_FILOSOFOS
    }

    threads = []
    for i in range(NUM_FILOSOFOS):
        esq = garfos[i]
        dir = garfos[(i + 1) % NUM_FILOSOFOS]
        t = threading.Thread(target=filosofar, args=(i, esq, dir, stats, parar))
        t.daemon = True
        threads.append(t)
        t.start()

    frame = 1
    inicio = time.time()
    log_datetime()
    while time.time() - inicio < TEMPO_SIMULACAO:
        plt.figure(figsize=(10,4))
        plt.bar(range(NUM_FILOSOFOS), stats['refeicoes'], color='teal')
        plt.xticks(range(NUM_FILOSOFOS), [f"Filósofo {i}" for i in range(NUM_FILOSOFOS)])
        plt.ylabel("Quantidade de refeições")
        plt.title(f"Simulação Jantar dos Filósofos - frame {frame:03d}")
        plt.tight_layout()

        arquivo = os.path.join(PASTA_FRAMES, f"{frame:03d}.png")
        plt.savefig(arquivo)
        plt.close()

        medias = [
            round(statistics.mean(w), 3) if len(w) > 0 else 0
            for w in stats['tempos_espera']
        ]
        print(f"Frame {frame:03d} salvo")
        for i in range(NUM_FILOSOFOS):
            print(f"  Filósofo {i}: refeições={stats['refeicoes'][i]}, tempo médio de espera={medias[i]}s")
        print("-"*40)

        log(frame, stats, medias)

        frame += 1
        time.sleep(INTERVALO_SALVAR)

    parar.set()
    for t in threads:
        t.join(timeout=0.5)

#===========================================================================================================#
#===[    RUN    ]===========================================================================================#
#===========================================================================================================#
if __name__ == "__main__":
    simular_e_salvar_frames()
