import argparse
from detector import PersonDetector
from video_processor import VideoProcessor

def main():
    # Configurar parser de argumentos
    parser = argparse.ArgumentParser(description="Detecção de Pessoas em Vídeo com YOLO")
    parser.add_argument('--video_path', type=str, required=True,
                        help="Caminho para o vídeo de entrada")
    parser.add_argument('--output_dir', type=str, default='./output_results',
                        help="Diretório para salvar os resultados")
    parser.add_argument('--threshold', type=int, required=True,
                        help="Número mínimo de pessoas para gerar um alerta")

    args = parser.parse_args()

   
    detector = PersonDetector()

   
    processor = VideoProcessor(
        input_video_path=args.video_path,
        output_dir=args.output_dir,
        alert_threshold=args.threshold,
        detector=detector
    )


    processor.process_video()

if __name__ == "__main__":
    main()
