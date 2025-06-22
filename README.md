# Processo Seletivo Metta Innovations | Detecção de Pessoas em Vídeo

Sistema de detecção de pessoas em vídeos utilizando rede neural YOLO pré-treinada, desenvolvido para o Processo Seletivo da Metta Innovations.

## Requisitos do Sistema

- Python 3.8 ou superior
- Pelo menos 4GB de RAM
- Espaço em disco: ~2GB (para modelo YOLO e dependências)

## Iniciar Ambiente de Desenvolvimento

### 1. Clone o repositório
```bash
git clone <https://github.com/LeonardoRdc/ProcessoSeletivoMetta.git>
cd processo-seletivo-metta
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Executar o projeto

Execute o processamento principal com os parâmetros obrigatórios:

```bash
python src/main.py --video_path ./sample/people-walking.mp4 --limiar_pessoas 5
```

**Parâmetros:**
- `--video_path`: Caminho para o vídeo de entrada (obrigatório)
- `--threshold`: Número mínimo de pessoas para gerar alerta (obrigatório)
- `--output_dir`: Diretório de saída (opcional, padrão: `./output_results`)

**Exemplo completo:**
```bash
python src/main.py --video_path ./sample/people-walking.mp4 --limiar_pessoas 2 --output_dir ./meus_resultados
```

### Interface Gráfica (GUI)

Após o processamento, visualize os resultados:

```bash
streamlit run src/interface.py
```

Acesse no navegador: http://localhost:8501

## Estrutura de Pastas

```
processo-seletivo-2025/
├── src/
│   ├── main.py           # Script principal
│   ├── detector.py       # Classe de detecção YOLO
│   ├── video_processor.py # Processamento de vídeo
│   └── interface.py           # Interface gráfica
├── sample/
│   └── people-walking.mp4 # Vídeo de exemplo
├── output_results/
│   ├── output_video.mp4  # Vídeo com detecções
│   ├── history.json      # Histórico por frame
│   └── alerts.json       # Alertas de limite
├── screenshots/
│   ├── grafico.png  # Print do gráfico
│   ├── video_processado.png     # Print do vídeo processado
├── yolov8n.pt           # Modelo YOLO
├── requirements.txt     # Dependências
├── README.md           # Este arquivo
└── ABOUT.md           # Documentação técnica
```

## 🎬 Outputs Gerados

O sistema gera automaticamente na pasta `output_results/`:

### 1. **output_video.mp4**
Vídeo processado com:
- Bounding boxes desenhadas ao redor das pessoas
- Labels "Person" identificando cada detecção

### 2. **history.json**
Histórico completo do processamento:
```json
[
  {"id": 0, "count": 2},
  {"id": 1, "count": 3},
  {"id": 2, "count": 1}
]
```

### 3. **alerts.json**
Alertas quando pessoas ≥ threshold:
```json
[
  {"id": 1, "count": 3},
  {"id": 5, "count": 4}
]
```

## Interface Gráfica (GUI)

O dashboard apresenta:
- **Vídeo processado** 
- **Gráfico Pessoas x Frame** 


## Solução de Problemas

### Erro: "Não foi possível abrir o vídeo"
- Verifique se o caminho do vídeo está correto
- Formatos suportados: mp4, avi, mov, mkv

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Dashboard não carrega
- Verifique se executou o processamento primeiro
- Confirme se os arquivos estão em `output_results/`

---

*Desenvolvido para o Processo Seletivo Metta Innovations 2025*